#!/usr/bin/env python3
# RPM package finder
# 2023 psuchanecki@almalinux.org
# github.com/xsub/rpm-pkg-finder
import argparse
import glob
import os
import re
import subprocess
import sqlite3
from tqdm import tqdm

class Package:
    def __init__(self, name, version, repo_name, description=None):
        self.name = name
        self.version = version
        self.repo_name = repo_name
        self.description = description

def grep_repos_names(pattern, path):
    repo_files = glob.glob(path)
    for file in repo_files:
        with open(file, 'r') as f:
            for line in f:
                match = re.search(pattern, line)
                if match:
                    yield [os.path.basename(file), match.group(0).strip("[]")]

def parse_dnf_output(output_as_lines):
    packages = []
    packages.clear()
    for line in output_as_lines:
        parts = line.split()
        if len(parts) >= 3:
            package_name = parts[0]
            version = parts[1]
            repo_name = ' '.join(parts[2:])
            packages.append((package_name, version, repo_name))
    return packages

def recreate_database(conn):
    conn.execute("DROP TABLE IF EXISTS packages")
    conn.execute("CREATE TABLE packages (name TEXT UNIQUE, version TEXT, repo_name TEXT)")

def query_repo_build_db(repo_name, conn):
    command = ['sudo', 'dnf', '--disablerepo=*', '--enablerepo=' + repo_name, 'list']
    result = subprocess.run(command, capture_output=True, text=True)
    packages = []
    if result.returncode == 0:
        lines = result.stdout.split('\n')
        filtered_lines = [line for line in lines if re.match('^[a-z]', line) and '@' not in line]
        packages = parse_dnf_output(filtered_lines)
        for package in packages:
            package_name = package[0]
            version = package[1]
            repo_name = package[2]
            conn.execute("INSERT OR IGNORE INTO packages (name, version, repo_name) VALUES (?, ?, ?)", (package_name, version, repo_name))
        conn.commit()
        print("➡️ indexed " + str(len(packages)) + " packages.")
    else:
        print(result.stderr)
    return(len(packages))

def parse_dnf_info_output(output):
    description_lines = output.split("\n")[10:]
    description = " ".join(description_lines).replace("Description  : ", "").strip()
    return description

def add_description_to_package(package_name, conn_desc):
    command = ['sudo', 'dnf', 'info', package_name]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        description = parse_dnf_info_output(result.stdout)
        conn_desc.execute("INSERT OR IGNORE INTO packages_desc (name, description) VALUES (?, ?)", (package_name, description))
        conn_desc.commit()

def recreate_description_database(conn_desc):
    conn_desc.execute("DROP TABLE IF EXISTS packages_desc")
    conn_desc.execute("CREATE TABLE packages_desc (name TEXT UNIQUE, description TEXT)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build the package database.")
    parser.add_argument("--generate-descriptions", action="store_true", help="Generate descriptions for packages")
    args = parser.parse_args()

    pattern = r'\[.*\]'
    path = '/etc/yum.repos.d/*.repo'
    repo_files = glob.glob(path)
    num_repo_files = 0

    for file in repo_files:
        with open(file, 'r') as f:
            for line in f:
                match = re.search(pattern, line)
                if match:
                    num_repo_files += 1

    conn = sqlite3.connect(':memory:')
    recreate_database(conn)

    conn_desc = sqlite3.connect(':memory:')
    recreate_description_database(conn_desc)

    try:
        total_pkgs = 0
        for index, (file, repo_name) in enumerate(grep_repos_names(pattern, path), start=1):
            print(f"repo id: {index}/{num_repo_files} | file: {file} | name: {repo_name}", end=" ", flush=True)
            indexed_pkgs = query_repo_build_db(repo_name, conn)
            total_pkgs += indexed_pkgs
        print(f"Total packages: {total_pkgs}.")


        if args.generate_descriptions:
            print("Generating package descriptions...")
            cursor = conn.execute("SELECT * FROM packages ORDER BY name")
            rows = cursor.fetchall()
            for row in tqdm(rows, desc="Processing descriptions"):
                package_name = row[0]
                add_description_to_package(package_name, conn_desc)

    finally:
        conn.execute("PRAGMA foreign_keys = OFF")
        conn.commit()

        file_conn = sqlite3.connect("package_db.sqlite")
        conn.backup(file_conn)

        conn_desc.execute("PRAGMA foreign_keys = OFF")
        conn_desc.commit()

        file_conn_desc = sqlite3.connect("package_db_desc.sqlite")
        conn_desc.backup(file_conn_desc)

        file_conn.close()
        file_conn_desc.close()
        conn.close()
        conn_desc.close()
