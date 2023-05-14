#!/usr/bin/env python3
# RPM package finder
# github.com/xsub/rpm-pkg-finder
# 2023 psuchanecki@almalinux.org
import argparse
import os
import re
import sqlite3
import sys

# Function to query the package database by package name
def query_package(package_name, conn, exact_match):
    matched_packages = []
    if exact_match:
        pattern = re.compile(r'\b{}\b'.format(package_name))
    else:
        pattern = re.compile('.*{}.*'.format(package_name))

    cursor = conn.execute("SELECT * FROM packages ORDER BY name")
    for row in cursor.fetchall():
        if re.match(pattern, row[0]):
            matched_packages.append((row[0], row[1], row[2]))

    return matched_packages

# Function to print the results in the specified format
def print_results(results, format_option):
    for package in results:
        if format_option == "-1":
            formatted_string = "{:<{width}} - {:<{width2}} - {}".format(package[2], package[1], package[0], width=20, width2=40)
            print(formatted_string)
        elif format_option == "-I" or format_option == "-i":
            repo_name = package[2]
            cmd="install"
            if format_option == "-i":
                cmd="info"
            if repo_name.startswith('@'):
                print(f'sudo dnf {cmd} {package[0]}')
            else:
                print(f'sudo dnf --enablerepo={package[2]} {cmd} {package[0]}')
        else:
            print("Package Name:", package[0])
            print("Version:", package[1])
            print("Repository Name:", package[2])
            print()

# Example usage: python3 query_package.py PATTERN
if __name__ == "__main__":
    # Args args args!
    parser = argparse.ArgumentParser(description="Query package database.")
    parser.add_argument("pattern", help="Pattern to match against package names")
    parser.add_argument("-1", dest="format_option", action="store_const", const="-1", help="Format output as one record per line")
    parser.add_argument("-I", dest="format_option", action="store_const", const="-I", help="Format output as dnf install command")
    parser.add_argument("-i", dest="format_option", action="store_const", const="-i", help="Format output as dnf info command")
    parser.add_argument("-e", "--exact-match", action="store_true", help="Perform an exact match without wildcards")
    args = parser.parse_args()
    pattern = args.pattern
    format_option = args.format_option
    exact_match = args.exact_match

    # Check if package_db.sqlite exists
    if not os.path.exists("package_db.sqlite"):
        print("Package database does not exist. Please run rpm-pkg-db-builder.py first.")
        sys.exit(1)

    # Open the SQLite connection
    conn = sqlite3.connect('package_db.sqlite')

    try:
        # Query the package database by pattern
        results = query_package(pattern, conn, exact_match)

        # Print the results in the specified format
        print_results(results, format_option)
    finally:
        # Close the SQLite connection
        conn.close()

