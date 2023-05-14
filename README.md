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
repo id: 1/39 -- name: appstream
repo id: 2/39 -- name: appstream-debug
repo id: 3/39 -- name: appstream-source
repo id: 4/39 -- name: baseos
repo id: 5/39 -- name: baseos-debug
repo id: 6/39 -- name: baseos-source
repo id: 7/39 -- name: crb
repo id: 8/39 -- name: crb-debug
repo id: 9/39 -- name: crb-source
repo id: 10/39 -- name: extras
repo id: 11/39 -- name: extras-debug
repo id: 12/39 -- name: extras-source
repo id: 13/39 -- name: highavailability
repo id: 14/39 -- name: highavailability-debug
repo id: 15/39 -- name: highavailability-source
repo id: 16/39 -- name: nfv
repo id: 17/39 -- name: nfv-debug
repo id: 18/39 -- name: nfv-source
repo id: 19/39 -- name: plus
repo id: 20/39 -- name: plus-debug
repo id: 21/39 -- name: plus-source
repo id: 22/39 -- name: resilientstorage
repo id: 23/39 -- name: resilientstorage-debug
repo id: 24/39 -- name: resilientstorage-source
repo id: 25/39 -- name: rt
repo id: 26/39 -- name: rt-debug
repo id: 27/39 -- name: rt-source
repo id: 28/39 -- name: sap
repo id: 29/39 -- name: sap-debug
repo id: 30/39 -- name: sap-source
repo id: 31/39 -- name: saphana
repo id: 32/39 -- name: saphana-debug
repo id: 33/39 -- name: saphana-source
repo id: 34/39 -- name: epel-testing
repo id: 35/39 -- name: epel-testing-debuginfo
repo id: 36/39 -- name: epel-testing-source
repo id: 37/39 -- name: epel
repo id: 38/39 -- name: epel-debuginfo
repo id: 39/39 -- name: epel-source

real	1m36.491s
user	1m28.366s
sys	0m6.713s
```

[Go AlmaLinux!](https://almalinux.org)
