---
title: Install Golang on WSL
date: 2019-02-01
draft: false
keywords: []
description: ""
tags: ['go','WSL']
categories: []
slug: install-golan-on-wsl
comment: false
toc: false
autoCollapseToc: false
postMetaInFooter: false
hiddenFromHomePage: false
reward: false
mathjax: true
mathjaxEnableSingleDollar: true
mathjaxEnableAutoNumber: false
---


![alt text][img1]

Go is a modern programming language developed at Google at around 2007 to improve programming productivity. 
It is increasingly popular for its many applications like Docker, Kubernetes and popular static site generator like Hugo.

In this tutorial, we will install Go on our Windows Linux Subsystem environment.

First, we will install it using Ubuntu's package manager, and then we will install it using the binary distribution.


<!--more-->

## Check version

Before we do anything lets check what version of Linux we have installed.

```#
$ lsb_release -a

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.1 LTS
Release:        18.04
Codename:       bionic
```

Our current version is 18.04, and the LTS means Long Term Support

From the beginning, Ubuntu has its packages, and we can install go within the `apt-get` utility

## Easy way

Open the terminal  and lets update & upgrade our APT package utility  and install go
```$
$ sudo apt-get update
$ sudo apt-get upgrade


$ sudo apt-get install golang-go
```
### Check

Let us check if it installed correctly
```$
$ go version

// go version go1.10.4 linux/amd64
```

{{% center %}}
![gif](https://media.giphy.com/media/12NUbkX6p4xOO4/giphy.gif)
{{% /center %}}


##  Install Binary Distribution
Let's say we wanted to get the latest version, we would have to install the official binary distribution.

We first go to https://golang.org/dl/ and select a compatible release according to our OS

- `go1.11.5.linux-amd64.tar.gz`

Let us open our terminal download our file and extract it in our current directory.
```bash
wget https://dl.google.com/go/go1.11.5.linux-amd64.tar.gz

$ sudo tar -xvf go1.11.5.linux-amd64.tar.gz
```

- `tar` : stores/extracts files from the archive
- `x`  : extracts the file from target
- `v`  : verbosly list files process
- `f`  :  use archive file

Now we have a folder `/go` on our current directory. Let us move it to `/usr/local/`

```$
sudo mv go /usr/local
```

### Set Enviroments

Our last step is to add our global variables on our `.bahsrc` or `.profile` file.

```$
sudo nano ~/.bashrc
```
scroll down and add these to your `.bashrc` profile

```$

# Go Global variables

export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
```
To save it  `Ctrl + o`, and to exit nano `Ctrl + x`

update current session

```$
source ~/.bashrc
```

## Check 

```$
go version

// go version go1.11.5 linux/amd64
```

{{% center %}}
![](https://media.giphy.com/media/3o7TKP9ln2Dr6ze6f6/giphy.gif)

{{% /center %}}

{{% admonition type="info" title="References" details="true" %}}
1. https://github.com/golang/go/wiki/Ubuntu
2. https://link.medium.com/n5s7IUg47T
3. https://golang.org/dl/
4. https://www.techonthenet.com/linux/commands/tar.php
{{% /admonition %}}

[img1]: /images/installing-golan-on-wsl/golang_WLS.png