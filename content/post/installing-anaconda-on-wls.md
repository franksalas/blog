---
title: Installing Anaconda on  WLS
date: 2016-04-12
draft: false
keywords: []
description: ""
tags: ['conda','python']
categories: ['anacoda','python','WSL']
slug: installing-anaconda-on-wls
comment: false
toc: false
autoCollapseToc: false
postMetaInFooter: false
hiddenFromHomePage: false
reward: false
mathjax: false
mathjaxEnableSingleDollar: false
mathjaxEnableAutoNumber: false
---



![alt text][img1]

# Difference between conda and Anaconda
conda is the package manager. Anaconda is a set of about a hundred packages including conda, numpy, scipy, ipython notebook, and so on.

You installed Miniconda, which is a smaller alternative to Anaconda that is just conda and its dependencies (as opposed to Anaconda, which is conda and a bunch of other packages like numpy, scipy, ipython notebook, etc.). Once you have Miniconda, you can easily install Anaconda into it with conda install anaconda.
<!--more-->

- Navigator
    - GUI included in Anaconda that allows you to launch applications and easily manage conda packages, environments and channels without using a command prompt or terminal program. Navigator is automatically installed when you install Anaconda.

- Anaconda
    - free enterprise-ready python distribution w/150+ popular python packages.Used mostly for science, math , engineering & data analysis.
    - Comes with `conda` to manage librareis & enviroments.
    - another $250$ packages can be installed with the `conda install` command.
    - A full distrubution of the central sofwae in the Pydata ecosystem including Python itself anong with binaries for several hundred thrie-party open souce projects.
- Miniconda:
    - lighter alternative to Anaconda.
    - comes just with Python and `conda`
    - ideal for user who want to star witha  minimal linstallation and be able to manage their own set of packages.
    - installer for an empty conda enviroment containing ony `conda` and its dependencies, so you can install from scratch.

- pip
    - **P**ip **I**nstalls **P**ackages is a python's officialy-sanctioned package manager, and ist most commonly used to isntall packages published on the ***Python Package Index (PyPI)**.
    - general purpose manger for Python packages
    - pip installs *python* packages with  *any* enviroment.
    - `conda` installs `any` package within `conda` enviroment

- virtualenv
    - utility that allows user to crate isolated Python envirometns that work with `pip`

- conda v pip
    - both are package managers they are different.
    - `pip` is psecifi for python packages
    - `conda` is language-agnostic, it maintains packages form any language.
    - `pip` compiles from souce 
    - `conda` installs binaries, so no compilation.
    - `conda` craetes language-agnostic enviroments natively
    - `pip` relies on *virtualenv* to manage only python enviroments.

- conda
    - general-purposepackage management system designed to build ns manage softawe of any type from any language
    - its not a fundamentally a python package.
    - its designed to manage packages and dependencies with *any* sofwatre stack.
    - Its less like `pip` andmore like a cross-platform version of `apt` or `yum`
---

## Misconceptions
Conda is a package manager, Anaconda is a distribution.




## Install Miniconda on Windows Linux Subsystem

Open your terminal and type

```$
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

After its done downloading type

```$
$ ls
Miniconda3-latest-Linux-x86_64.sh
```
Make the file executable

```$
$ chmod +x Miniconda3-latest-Linux-x86_64.sh 
```


Run the file 


```$
$ ls
Miniconda3-latest-Linux-x86_64.sh*
```


```$
$ ./Miniconda3-latest-Linux-x86_64.sh 


In order to continue the installation process, please review the license
agreement.
Please, press ENTER to continue


===================================
Anaconda End User License Agreement
===================================

Copyright 2016, Continuum Analytics, Inc.

All rights reserved under the 3-clause BSD License:

...
..
.


Do you approve the license terms? [yes|no]
>>> yes

Miniconda3 will now be installed into this location:
/home/ubuntu/miniconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/frank/miniconda3] >>> 
PREFIX=/home/frank/miniconda3
installing: python-3.6.1-2 ...
installing: asn1crypto-0.22.0-py36_0 ...
installing: cffi-1.10.0-py36_0 ...
installing: conda-env-2.6.0-0 ...
installing: cryptography-1.8.1-py36_0 ...
installing: idna-2.5-py36_0 ...
installing: libffi-3.2.1-1 ...
installing: openssl-1.0.2l-0 ...
installing: packaging-16.8-py36_0 ...
installing: pycosat-0.6.2-py36_0 ...
installing: pycparser-2.17-py36_0 ...
installing: pyopenssl-17.0.0-py36_0 ...
installing: pyparsing-2.1.4-py36_0 ...
installing: readline-6.2-2 ...
installing: requests-2.14.2-py36_0 ...
installing: ruamel_yaml-0.11.14-py36_1 ...
installing: setuptools-27.2.0-py36_0 ...
installing: six-1.10.0-py36_0 ...
installing: sqlite-3.13.0-0 ...
installing: tk-8.5.18-0 ...
installing: xz-5.2.2-1 ...
installing: yaml-0.1.6-0 ...
installing: zlib-1.2.8-3 ...
installing: conda-4.3.21-py36_0 ...
installing: pip-9.0.1-py36_1 ...
installing: wheel-0.29.0-py36_0 ...
Python 3.6.1 :: Continuum Analytics, Inc.
creating default environment...
installation finished.
Do you wish the installer to prepend the Miniconda3 install location
to PATH in your /home/ubuntu/.bashrc ? [yes|no]
[no] >>> yes

Prepending PATH=/home/ubuntu/miniconda3/bin to PATH in /home/ubuntu/.bashrc
A backup will be made to: /home/ubuntu/.bashrc-miniconda3.bak


For this change to become active, you have to open a new terminal.

Thank you for installing Miniconda3!

Share your notebooks and packages on Anaconda Cloud!
Sign up for free: https://anaconda.org
```





## References



1. https://conda.io/miniconda.html










[img1]: /images/installing-anaconda-on-wls/anaconda_horizontal.png