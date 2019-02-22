---
title: Install Hugo on WSL
date: 2019-02-08
draft: false
keywords: []
description: ""
tags: ['hugo','go','WSL']
categories: []
slug: install-hugo-on-wsl
comment: false
mathjax: false
mathjaxEnableSingleDollar: false
mathjaxEnableAutoNumber: false
toc: false
---


![alt text][img1]

Static websites have become popular over the years for its speed, simplicity, and low to no cost hosting.
<!--more-->


## Elevator pitch on Static vs. Dynamic

![fig](https://media.giphy.com/media/obh9JV6JSCby8/giphy.gif)


When you go online and check your Gmail ***(or if you are my dad, your Hotmail)*** account, the site is generated **dynamically** for you, that means it changes depending on day/time or in this case the user. Its usually controlled by an application server and some database.

{{% figure  src="https://upload.wikimedia.org/wikipedia/commons/4/4f/Scheme_dynamic_page_en.svg" title="Dynamic site" alt="img" %}}


On the other hand a static site (like this one :smile:)  it is delivered to the user exactly as it is stored, it displays the same information for all users. It usually contains some `HTML`,`CSS` & `JS` files


{{% figure  src="https://upload.wikimedia.org/wikipedia/commons/5/57/Scheme_static_page_en.svg" title="Static site" alt="img" %}}


In this tutorial, we will install a popular static website generator called Hugo. Hugo is a static site generator written in go, and it is fantastic. 


## Requirements
- Windows Linux Subsystem, with Ubuntu as distribution ( vanilla Ubuntu will work)
-  Golang installed, preferably `1.11` or higher.

## Download package

To get the latest package, we need to go to https://github.com/gohugoio/hugo/releases/ and select a compatible version. Since we are on an Unbutu/Debian distribution we will choose `hugo_0.54.0_Linux-64bit.deb`, to save on typing a long link address, right click and copy link address.

![alt text][img2]



Open your terminal and type `wget` and paste the link
```$
wget https://github.com/gohugoio/hugo/releases/download/v0.54.0/hugo_0.54.0_Linux-64bit.deb
```
> `wget` stands for "web get". It is a command-line utility which downloads files over a network.


## Extract package

Now we will extract the package, make sure you type `sudo`.

```bash
$ sudo dpkg -i hugo_0.54.0_Linux-64bit.deb
[sudo] password for salas:

Selecting previously unselected package hugo.
(Reading database ... 28572 files and directories currently installed.)
Preparing to unpack hugo_0.54.0_Linux-64bit.deb ...
Unpacking hugo (0.54.0) ...
Setting up hugo (0.54.0) ...
```

> The Debian package `dpkg` provides the dpkg program, is used to install, remove, and provide information about .deb packages.
> 
> flag: `-i` : install

## Verify

Now let's check if it is installed correctly.

```bash
$ hugo  version

Hugo Static Site Generator v0.54.0-B1A82C61 linux/amd64 BuildDate: 2019-02-01T09:40:34Z
```

![](https://media.giphy.com/media/3otPoS81loriI9sO8o/giphy.gif)

{{% admonition type="info" title="References" details="true" %}}
- https://gohugo.io/
- https://itrendbuzz.com/install-hugo-on-ubuntu/
- https://en.wikipedia.org/wiki/Dpkg
- https://www.computerhope.com/unix/wget.htm
{{% /admonition %}}




[img1]: /images/install-hugo-on-wsl/hugo_WLS.png
[img2]: /images/install-hugo-on-wsl/Inkedshow_dist_LI.jpg