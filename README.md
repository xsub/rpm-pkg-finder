
# Simple utility to identify by package RPM package name all RPM repos which offer the package.


Featuring:
* KISS, primtive design
* Actual functionality
* Python3, sqlite, dnf (for rpm-pkg-db-builder.py)


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

