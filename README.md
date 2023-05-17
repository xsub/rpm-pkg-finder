# `rpm-pkg-finder`  :mag_right:
## A Python tool to identify the parent repository for a known package (name).
### Discover the source repository for RPM packages with ease. :sparkles:

**Featuring:**
* :muscle: KISS, primitive design
* :gear: Actual functionality: CLI tool with local database
* :snake: Python3, SQLite; DNF (`rpm-pkg-db-builder.py`)
* :file_folder: Consume `/etc/yum.repos.d/*.repo` files (`rpm-pkg-db-builder.py`)


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
repo id: 1/40 | file: almalinux-appstream.repo | name: appstream ➡️ indexed 5344 packages.
repo id: 2/40 | file: almalinux-appstream.repo | name: appstream-debug ➡️ indexed 4690 packages.
repo id: 3/40 | file: almalinux-appstream.repo | name: appstream-source ➡️ indexed 1675 packages.
repo id: 4/40 | file: almalinux-baseos.repo | name: baseos ➡️ indexed 930 packages.
repo id: 5/40 | file: almalinux-baseos.repo | name: baseos-debug ➡️ indexed 1817 packages.
repo id: 6/40 | file: almalinux-baseos.repo | name: baseos-source ➡️ indexed 412 packages.
repo id: 7/40 | file: almalinux-crb.repo | name: crb ➡️ indexed 1608 packages.
repo id: 8/40 | file: almalinux-crb.repo | name: crb-debug ➡️ indexed 504 packages.
repo id: 9/40 | file: almalinux-crb.repo | name: crb-source ➡️ indexed 308 packages.
repo id: 10/40 | file: almalinux-extras.repo | name: extras ➡️ indexed 24 packages.
repo id: 11/40 | file: almalinux-extras.repo | name: extras-debug ➡️ indexed 0 packages.
repo id: 12/40 | file: almalinux-extras.repo | name: extras-source ➡️ indexed 18 packages.
repo id: 13/40 | file: almalinux-highavailability.repo | name: highavailability ➡️ indexed 90 packages.
repo id: 14/40 | file: almalinux-highavailability.repo | name: highavailability-debug ➡️ indexed 50 packages.
repo id: 15/40 | file: almalinux-highavailability.repo | name: highavailability-source ➡️ indexed 9 packages.
repo id: 16/40 | file: almalinux-nfv.repo | name: nfv ➡️ indexed 21 packages.
repo id: 17/40 | file: almalinux-nfv.repo | name: nfv-debug ➡️ indexed 4 packages.
repo id: 18/40 | file: almalinux-nfv.repo | name: nfv-source ➡️ indexed 4 packages.
repo id: 19/40 | file: almalinux-plus.repo | name: plus ➡️ indexed 2 packages.
repo id: 20/40 | file: almalinux-plus.repo | name: plus-debug ➡️ indexed 2 packages.
repo id: 21/40 | file: almalinux-plus.repo | name: plus-source ➡️ indexed 1 packages.
repo id: 22/40 | file: almalinux-resilientstorage.repo | name: resilientstorage ➡️ indexed 93 packages.
repo id: 23/40 | file: almalinux-resilientstorage.repo | name: resilientstorage-debug ➡️ indexed 52 packages.
repo id: 24/40 | file: almalinux-resilientstorage.repo | name: resilientstorage-source ➡️ indexed 10 packages.
repo id: 25/40 | file: almalinux-rt.repo | name: rt ➡️ indexed 16 packages.
repo id: 26/40 | file: almalinux-rt.repo | name: rt-debug ➡️ indexed 4 packages.
repo id: 27/40 | file: almalinux-rt.repo | name: rt-source ➡️ indexed 4 packages.
repo id: 28/40 | file: almalinux-sap.repo | name: sap ➡️ indexed 9 packages.
repo id: 29/40 | file: almalinux-sap.repo | name: sap-debug ➡️ indexed 10 packages.
repo id: 30/40 | file: almalinux-sap.repo | name: sap-source ➡️ indexed 5 packages.
repo id: 31/40 | file: almalinux-saphana.repo | name: saphana ➡️ indexed 7 packages.
repo id: 32/40 | file: almalinux-saphana.repo | name: saphana-debug ➡️ indexed 8 packages.
repo id: 33/40 | file: almalinux-saphana.repo | name: saphana-source ➡️ indexed 5 packages.
repo id: 34/40 | file: epel-testing.repo | name: epel-testing ➡️ indexed 1163 packages.
repo id: 35/40 | file: epel-testing.repo | name: epel-testing-debuginfo ➡️ indexed 343 packages.
repo id: 36/40 | file: epel-testing.repo | name: epel-testing-source ➡️ indexed 220 packages.
repo id: 37/40 | file: epel.repo | name: epel ➡️ indexed 14932 packages.
repo id: 38/40 | file: epel.repo | name: epel-debuginfo ➡️ indexed 6181 packages.
repo id: 39/40 | file: epel.repo | name: epel-source ➡️ indexed 5486 packages.
repo id: 40/40 | file: google-chrome.repo | name: google-chrome ➡️ indexed 3 packages.
Total packages: 46064.

real	0m42.953s
user	0m36.364s
sys	0m5.698s
```

-----
Warning: Linux Evangelism Ahead ⚠️
-----

[Go AlmaLinux!](https://almalinux.org) <br>
![AlmaLinuxPin](https://github.com/xsub/rpm-pkg-finder/assets/426035/d36feb1d-86f8-4308-9149-9fdb76cc4f9c)





