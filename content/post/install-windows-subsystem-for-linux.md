---
title: Linux on Windows
date: 2016-03-12
draft: false
keywords: []
description: ""
tags: ['linux']
categories: []
slug: install-windows-subsystem-for-linux
comment: false
toc: false
autoCollapseToc: false
postMetaInFooter: false
hiddenFromHomePage: false
fancybox : false
mathjax: false
mathjaxEnableSingleDollar: false
mathjaxEnableAutoNumber: false
---


![alt text][img0]

For those who want to run Linux without dual booting your machine or  sharing resources by using a virtual machine, Windows Subsytem for Linux is the best option.

The Windows Subsystem for Linux lets us run Linux environments like popular command-line tools, utilities and applications *inside* windows.
Windows Subsytem for Linux or (WLS) its a layer fo running Linux binary files natively on Windows 10 and its awesome.  It provides a Linux-compatible kernel interface develop by Microsoft that then can run a GNU userland on top of it, like Ubuntu.

### What can we do with WLS?

> short answer: Bash on windows!



Having bash on Windows is a great tool for developers comming from a Linux/Unix enviroment that want/need to work with a Windows 10 machine.



<!--more-->

## Enable Feature
Before we install anything, we need to enable it.

- Open Powershell as an admin and run

```PowerShell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```


![alt text][img1]

- Restart when propted.


## Install Linux Distro

Open the Microsoft Store and choose Ubuntu distribution.. or something else Im not your boss..

- From the distro's page, select `Get`


![alt text][img3]


- Once the download has completed, select `lauch`
This will open a console window. Wait for installation to complete then you will be prompted to create your LINUX user account and password

![alt text][img4]

## Update & Upgrade

After its done, type: `sudo apt-get update`

This It will download the package list from the repositories and `updates` them to gather information on the newest version of packages and its dependencies.

![alt text][img5]

After its done, type: `sudo apt-get upgrade`
this will fetch new version of those updated packages in your machine

![alt text][img6]





## References



1. https://docs.microsoft.com/en-us/windows/wsl/install-win10
2. https://askubuntu.com/questions/222348/what-does-sudo-apt-get-update-do


[img0]: /images/install-windows-subsystem-for-linux/bashonwindows0.png
[img1]: /images/install-windows-subsystem-for-linux/bashonwindows1.png
[img2]: /images/install-windows-subsystem-for-linux/bashonwindows2.png
[img3]: /images/install-windows-subsystem-for-linux/bashonwindows3.png
[img4]: /images/install-windows-subsystem-for-linux/bashonwindows4.png
[img5]: /images/install-windows-subsystem-for-linux/bashonwindows5.png
[img6]: /images/install-windows-subsystem-for-linux/bashonwindows6.png