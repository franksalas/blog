# sal.as
## What is this?
Static site buid on Hugo, a static site  framework written in go,  deploid on Netlify.
## Why is this?
I wanted a place where I could write intresting things I've learned where I or anyone could go back to.

## Who is this?
![who](https://media.giphy.com/media/3tHXbjKLm2tkfMMgA0/giphy.gif)


- Just someone who likes :pizza: & :bread:
- [Me work  history](https://www.linkedin.com/in/frank-salas/)

- [Buy me Coffee?](https://ko-fi.com/K3K4QVF2)

---
## Requirements
- go 1.11
- Hugo 0.54
- Theme is heavily modified version of [hugo-theme-even
](https://github.com/olOwOlo/hugo-theme-even)
- python

## Build
Clone repo

```bash
git clone https://github.com/franksalas/blog.git

cd blog
```
## Run
```bash
hugo server
```

## Create a blog post

On your terminal type

```$
python blog_post.py "Name of Blog post"
```
It will create:
- markdown file under `/content/post/` with the name of your blog post
- creates a folder under`/content/images/` with the name of the blog post

If any file or directory were created previously, it will skip the steps.


```
content/
    images/
        name-of-blog-post/  // <- place images here
    post/
        name-of-blog-post.md // blog post
```

## Thats it
![go home](https://media.giphy.com/media/1vWzzLEcMhl4Y/giphy.gif)