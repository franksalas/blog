---
title: Create Alias for Windows App
date: 2019-02-19
draft: false
keywords: []
description: ""
tags: []
categories: []
slug: create-alias-for-windows-app
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

According to [Larry Wall](https://en.wikipedia.org/wiki/Larry_Wall), the original author of the Perl programming language, there are three great virtues of a programmer:

- Laziness
- Impatience 
- Hubris

As a person who aligns himself with the first two virtues and is too dumb to know what the third one means, I find myself creating ways to reduce time wastage and increase productivity that is sometimes resulting in the inverse of it.


In this tutorial, we will create an alias of a windows app to open within our bash terminal.
<!--more-->

![questions](https://media.giphy.com/media/cI320yRBJZcyc/giphy.gif)

## What is an alias?
A bash alias is a command which enables a replacement of a word by another string, that's just $fancy\ talk$ for abbreviating a compact system command from a long one.

They are defined on our `.bash_profile` or `.bashrc` file under our home `~`  directory with this structure
```bash
alias short_code_name='path_or_command'
```
## Example

Let us say that we have a folder on our windows directory whose full path is 
```
C:Users\{username}\Documents\linux_dev
```
 if we want to access this folder quickly under our bash terminal by typing `linux_dev`, our alias command looks something like this:

```bash
# at the bottom of our .bashrc or .bash_profile
alias linux_dev='cd /mnt/c/Users/{username}/Documents/linux_dev'
```
- Here, our shortcode name is `linux_dev`, but we could've called it anything (preferably not a global variable). 

- The command changes the directory `cd` followed by the path of our folder according to the Linux directory structure.


{{% admonition type="tip" title="tip" details="false" %}}

to see a list of global variable type `printenv` on your terminal

{{% /admonition %}}


Now that we know how alias work, let us create one for VS Code.

## VS Code

Visual Studio Code is a  great text editor developed by Microsoft, its based on Electron, a desktop GUI framework maintained by Github based on Node.js that all the cool kids are on now.

The reason I choose VS Code instead of other lightweight text editors like sublime text or Github's Atom is that:

1. It has a fantastic IntelliSense with built-in Extension market place, and over the last three years, VS Code has matured immensely and makes it easy for nubies to experience developers to get coding the second after you install it.
2. You are not the boss of me[^1]




## Find origin location

![write_down](https://media.giphy.com/media/4wuzE31HC6Lba/giphy.gif)

Now that we decided what app to use we need to find the origin where the application is installed.

According to Microsoft own documents, VS Code is installed under

```shell
C:\users\{username}\AppData\Local\Programs\Microsoft VS Code\Code.exe
```


### Where Your Windows System Drive Appears in Linux

The Windows Linux subsystem gives us to access to the Windows system drives; however, our bash environment doesn't know (or care?), so it places your Windows system drives under the `/mnt/` directory.

### Example
If we wanted to access our `C:` drive under bash terminal, we would type
```bash
$ cd  /mnt/c

$ pwd
#/mnt/c
```

## Finally Create an alias for Windows App

Open your `.bashrc` or `.bash_profile` under the home directory with `nano` text editor, make sure you open it as a superuser  

```bash
$ cd 
#go home

$ sudo nano .bashrc
```
Scroll to the bottom of the file and append  our new alias code

```bash
# at the bootom of our .bashrc file
alias vscode='/mnt/c/Users/{username}/AppData/Local/Programs/Microsoft\ VS\ Code/Code.exe'
```
type `Ctrl-o` to save our edits & `Ctrl-x` to exit

- Our bash shortcode keyword is `vscode`
- the path is `/mnt/c/Users/{username}/AppData/Local/Programs/Microsoft\ VS\ Code/Code.exe'`

The reason the path looks odd especially under the folder name `\Microsoft VS Code` is that shell translates empty spaces.

Let us reload our `/bashrc` file by typing
```bash
source ~/.bashrc
```

## Test it

```bash
$ vscode .
# opens app within the current directory
```



![thanks](https://media.giphy.com/media/1U41ujsx7HDkk/giphy.gif)


{{% admonition type="info" title="References" details="true" %}}
- https://blogs.msdn.microsoft.com/commandline/2016/11/17/do-not-change-linux-files-using-windows-apps-and-tools/
- https://code.visualstudio.com/docs/setup/windows
- http://www.linfo.org/mnt.html
- https://en.wikipedia.org/wiki/Alias_(command)
- http://tldp.org/LDP/abs/html/aliases.html
{{% /admonition %}}




[img1]: /images/create-alias-for-windows-app/alias_logo.png
[^1]: subjective
