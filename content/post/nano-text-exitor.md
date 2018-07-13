---
title: Nano text exitor
date: 2016-07-12
draft: true
keywords: []
description: ""
tags: []
categories: []
slug: nano-text-exitor
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


## intro

> The need to format a file quickly ...

Every time I wanted to edit a file throught the command line somehow I end up rebooting my laptop because I ended up stuck in vim.


{{< tweet 435555976687923200 >}}

<!--more-->

Nano is a text-editor  that uses a command-line interface. Unlike Vim or Emacs that have steep learning curve nano is super easy to get started.



## installation
First lets check if its installed

```$
nano --version
```
The output should be something similar to this:

```$
GNU nano version 2.2.6 (compiled 14:12:08, Oct  1 2012)
 (C) 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
 2008, 2009 Free Software Foundation, Inc.
 Email: nano@nano-editor.org    Web: http://www.nano-editor.org/
 Compiled options: --disable-wrapping-as-root --enable-color --enable-extra --enable-multibuffer --enable-nanorc --enable-utf8

```
If somehow you dont have nano installed, just follow the instructions on the [official site](https://www.nano-editor.org/download.php)

## commands

### Create a new file

```$
$ nano new_file.py
```

### Open file

```$
nano old_file.py
```


### Open file as read only

```$
nano -v myfile
```


## tips


![alt text][img1]


[img1]: /images/nano-text-exitor/