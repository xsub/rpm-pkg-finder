#!/usr/bin/env python3
# RPM package finder
# 2023 psuchanecki@almalinux.org
# github.com/xsub/rpm-pkg-finder
import glob
import re
import subprocess
import sqlite3

class Package:
    def __init__(self, name, version, repo_name):
        self.name = name
        self.version = version
        self.repo_name = repo_name

def grep_repos_names(pattern, path):
    repo_files = glob.glob(path)

    for file in repo_files:
        with open(file, 'r') as f:
            for line in f:
                match = re.search(pattern, line)
                if match:
                    yield match.group(0).strip("[]")

def parse_dnf_output(output):
    lines = output.strip().split('\n')
    packages = []

    for line in lines:
        parts = line.split()
        if len(parts) >= 3:
            package_name = parts[0]
            version = parts[1]
            repo_name = ' '.join(parts[2:])
            packages.append((package_name, version, repo_name))

    return packages

# Recreate the fresh database
def recreate_database(conn):
    conn.execute("DROP TABLE IF EXISTS packages")
    conn.execute("CREATE TABLE packages (name TEXT UNIQUE, version TEXT, repo_name TEXT)")

def query_repo(repo_name, conn):
    command = ['sudo', 'dnf', '--enablerepo=' + repo_name, 'list']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        packages = parse_dnf_output(result.stdout)
        for package in packages:
            package_name = package[0]
            version = package[1]
            repo_name = package[2]
            conn.execute("INSERT OR IGNORE INTO packages (name, version, repo_name) VALUES (?, ?, ?)", (package_name, version, repo_name))
        conn.commit()
    else:
        print(result.stderr)

# Example usage
pattern = r'\[.*\]'
path = '/etc/yum.repos.d/*.repo'

# Count the number of repo files
attern = r'\[.*\]'
path = '/etc/yum.repos.d/*.repo'

repo_files = glob.glob(path)

# Complicate `grep '\[.*\]' /etc/yum.repos.d/*.repo`
num_repo_files = 0
for file in repo_files:
    with open(file, 'r') as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                num_repo_files += 1

# Open the SQLite in-memory connection and create the table
conn = sqlite3.connect(':memory:')
recreate_database(conn)

try:
    # Iterate over the generator and query each repository
    for index, repo_name in enumerate(grep_repos_names(pattern, path), start=1):
        print(f"repo id: {index}/{num_repo_files} -- name: {repo_name}")
        query_repo(repo_name, conn)

finally:
    # Save the in-memory database to a SQLite file
    conn.execute("PRAGMA foreign_keys = OFF")
    conn.commit()

    # Open a connection to the file-based SQLite database
    file_conn = sqlite3.connect("package_db.sqlite")

    # Backup the in-memory database to the file-based database
    conn.backup(file_conn)

    # Close the connections
    file_conn.close()
    conn.close()
