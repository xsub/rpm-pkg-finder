# `rpm-pkg-finder`  :mag_right:
## A Python tool to identify the parent repository for a known package (name).
### Discover the source repository for RPM packages with ease. :sparkles:

**Featuring:**
* :muscle: KISS, primitive design
* :gear: Actual functionality: CLI tool with local database
* :snake: Python3, SQLite; DNF (for `rpm-pkg-db-builder.py`)
* :file_folder: `/etc/yum.repos.d/*.repo` files (for `rpm-pkg-db-builder.py`)


#### Example (using):

```
➜  rpm-pkg-finder ./rpm-pkg-finder.py -1 htop      
epel-debuginfo       - 3.2.2-1.el9                              - htop-debuginfo.x86_64
epel-debuginfo       - 3.2.2-1.el9                              - htop-debugsource.x86_64
epel-source          - 3.2.2-1.el9                              - htop.src
@epel                - 3.2.2-1.el9                              - htop.x86_64

➜  rpm-pkg-finder ./rpm-pkg-finder.py -i htop
sudo dnf --enablerepo=epel-debuginfo info htop-debuginfo.x86_64
sudo dnf --enablerepo=epel-debuginfo info htop-debugsource.x86_64
sudo dnf --enablerepo=epel-source info htop.src
sudo dnf info htop.x86_64

➜  rpm-pkg-finder ./rpm-pkg-finder.py -I htop
sudo dnf --enablerepo=epel-debuginfo install htop-debuginfo.x86_64
sudo dnf --enablerepo=epel-debuginfo install htop-debugsource.x86_64
sudo dnf --enablerepo=epel-source install htop.src
sudo dnf install htop.x86_64

# --exact-match or -e: match exact token (no substring matching)
➜  rpm-pkg-finder git:(main) ./rpm-pkg-finder.py -e mc    
Package Name: mc-debuginfo.x86_64
Version: 1:4.8.26-5.el9
Repository Name: appstream-debug

Package Name: mc-debugsource.x86_64
Version: 1:4.8.26-5.el9
Repository Name: appstream-debug

Package Name: mc.src
Version: 1:4.8.26-5.el9
Repository Name: appstream-source

Package Name: mc.x86_64
Version: 1:4.8.26-5.el9
Repository Name: appstream
```

#### Example (database building):

```
➜  rpm-pkg-finder time ./rpm-pkg-db-builder.py
repo id: 1/39 | file: almalinux-appstream.repo | name: appstream ➡️ indexed 22014 packages.
repo id: 2/39 | file: almalinux-appstream.repo | name: appstream-debug ➡️ indexed 26759 packages.
repo id: 3/39 | file: almalinux-appstream.repo | name: appstream-source ➡️ indexed 23700 packages.
repo id: 4/39 | file: almalinux-baseos.repo | name: baseos ➡️ indexed 22014 packages.
repo id: 5/39 | file: almalinux-baseos.repo | name: baseos-debug ➡️ indexed 23862 packages.
repo id: 6/39 | file: almalinux-baseos.repo | name: baseos-source ➡️ indexed 22429 packages.
repo id: 7/39 | file: almalinux-crb.repo | name: crb ➡️ indexed 23632 packages.
repo id: 8/39 | file: almalinux-crb.repo | name: crb-debug ➡️ indexed 22519 packages.
repo id: 9/39 | file: almalinux-crb.repo | name: crb-source ➡️ indexed 22323 packages.
repo id: 10/39 | file: almalinux-extras.repo | name: extras ➡️ indexed 22014 packages.
repo id: 11/39 | file: almalinux-extras.repo | name: extras-debug ➡️ indexed 22014 packages.
repo id: 12/39 | file: almalinux-extras.repo | name: extras-source ➡️ indexed 22032 packages.
repo id: 13/39 | file: almalinux-highavailability.repo | name: highavailability ➡️ indexed 22089 packages.
repo id: 14/39 | file: almalinux-highavailability.repo | name: highavailability-debug ➡️ indexed 22064 packages.
repo id: 15/39 | file: almalinux-highavailability.repo | name: highavailability-source ➡️ indexed 22023 packages.
repo id: 16/39 | file: almalinux-nfv.repo | name: nfv ➡️ indexed 22035 packages.
repo id: 17/39 | file: almalinux-nfv.repo | name: nfv-debug ➡️ indexed 22019 packages.
repo id: 18/39 | file: almalinux-nfv.repo | name: nfv-source ➡️ indexed 22018 packages.
repo id: 19/39 | file: almalinux-plus.repo | name: plus ➡️ indexed 22015 packages.
repo id: 20/39 | file: almalinux-plus.repo | name: plus-debug ➡️ indexed 22017 packages.
repo id: 21/39 | file: almalinux-plus.repo | name: plus-source ➡️ indexed 22015 packages.
repo id: 22/39 | file: almalinux-resilientstorage.repo | name: resilientstorage ➡️ indexed 22092 packages.
repo id: 23/39 | file: almalinux-resilientstorage.repo | name: resilientstorage-debug ➡️ indexed 22066 packages.
repo id: 24/39 | file: almalinux-resilientstorage.repo | name: resilientstorage-source ➡️ indexed 22024 packages.
repo id: 25/39 | file: almalinux-rt.repo | name: rt ➡️ indexed 22030 packages.
repo id: 26/39 | file: almalinux-rt.repo | name: rt-debug ➡️ indexed 22019 packages.
repo id: 27/39 | file: almalinux-rt.repo | name: rt-source ➡️ indexed 22018 packages.
repo id: 28/39 | file: almalinux-sap.repo | name: sap ➡️ indexed 22023 packages.
repo id: 29/39 | file: almalinux-sap.repo | name: sap-debug ➡️ indexed 22024 packages.
repo id: 30/39 | file: almalinux-sap.repo | name: sap-source ➡️ indexed 22019 packages.
repo id: 31/39 | file: almalinux-saphana.repo | name: saphana ➡️ indexed 22022 packages.
repo id: 32/39 | file: almalinux-saphana.repo | name: saphana-debug ➡️ indexed 22022 packages.
repo id: 33/39 | file: almalinux-saphana.repo | name: saphana-source ➡️ indexed 22019 packages.
repo id: 34/39 | file: epel-testing.repo | name: epel-testing ➡️ indexed 22123 packages.
repo id: 35/39 | file: epel-testing.repo | name: epel-testing-debuginfo ➡️ indexed 23142 packages.
repo id: 36/39 | file: epel-testing.repo | name: epel-testing-source ➡️ indexed 22486 packages.
repo id: 37/39 | file: epel.repo | name: epel ➡️ indexed 22014 packages.
repo id: 38/39 | file: epel.repo | name: epel-debuginfo ➡️ indexed 28296 packages.
repo id: 39/39 | file: epel.repo | name: epel-source ➡️ indexed 27548 packages.
Total packages: 883594.

real	1m36.491s
user	1m28.366s
sys	0m6.713s
```

-----
Warning: Linux Evangelism Ahead⚠️
-----

[Go AlmaLinux!](https://almalinux.org) <br>
![AlmaLinuxPin](https://github.com/xsub/rpm-pkg-finder/assets/426035/d36feb1d-86f8-4308-9149-9fdb76cc4f9c)





