---
title: Markdown Language Overview
date: 2016-05-02
draft: false
keywords: []
description: ""
tags: []
categories: ['markdown']
slug: markdown-language
comment: false
toc: false
autoCollapseToc: false
postMetaInFooter: false
hiddenFromHomePage: false
mathjax: false
mathjaxEnableSingleDollar: false
mathjaxEnableAutoNumber: false
---


# What is markdown?

Markdown is a text to HTML conversion tool for anyone wanting to document on the web. It allowes you to write plain text format that then is converted it to valid HTML.

It was created in 2004 by Jhon Gruber with collaboration with others including Aaron Swartz. Its syntax is influnec by previous text-to-HTML filters including *Setext*, *atx*, *Textile*, *reStructuredText*, *Grutatext*, and *EtText*.

The main difference is that markdown's syntax is comprised entirely of punctuation characters as to look like what they mean.

Markdown is a lightweight super eazy[^1] to use markup language that is widely used today.

<!--more-->



# Syntax Comparison
Lets compare the syntax between writing raw HTML and writing markdown.


## Headers

The `<h1>` to `<h6>`tags are used to define HTML headings.

`<h1>` defines the most important heading. `<h6>` defines the least important heading.

### HTML

```html
<h1>Header 1</h1>
<h2>Header 2</h2>
<h3>Header 3</h3>
..
<h6>Header 6</h6>
```

### Markdown

```markdown
# Header1
## Header 2
### Header 3
..
###### Header 6
```
### Output

# Header1
## Header 2
### Header 3
..
###### Header 6

---

## Paragraphs
The `<p>` tag defines a paragraph.


### HTML

```html
<p> Quisque nisi nisi, pellentesque sit 
    amet arcu quis, ultricies commodo lorem.
    Vestibulum laoreet viverra nisl et feugiat.
    Vestibulum in lacinia nisl, a elementum risus.</p>
```

### Markdown

```markdown
Quisque nisi nisi, pellentesque sit 
amet arcu quis, ultricies commodo lorem.
Vestibulum laoreet viverra nisl et feugiat.
Vestibulum in lacinia nisl, a elementum 
```

### Output

Quisque nisi nisi, pellentesque sit 
amet arcu quis, ultricies commodo lorem.
Vestibulum laoreet viverra nisl et feugiat.
Vestibulum in lacinia nisl, a elementum 

---
## Emphasis

The `<em>` tag is a phrase tag. It renders as emphasized text.
The `<strong>` tag is a phrase tag. It defines important text.


### HTML
```html
<em>This text will be italic</em>
<strong>This text will be bold.</strong>
```

### Markdown
```markdown
*This text will be italic*
**This text will be bold**

_this can also be italic_
__this can also be bold__
```

### Output

*This text will be italic*
**This text will be bold**

_this can also be italic_
__this can also be bold__


---




## Lists
The `<li>` tag defines a list item, its also used in:

- ordered lists `<ol>`
- unordered lists `<ul>`
- menu lists `<menu>`

### Unorder list

### HTML
```html
<ul>
    <li>apples</li>
    <li>oranges</li>
    <li>bananas</li>
</ul>
```

### Markdown
```md
- apples
- oranges
- bananas
```

### Output
- apples
- oranges
- bananas

### Order list

#### HTML
```html
<ol>
    <li>apples</li>
    <li>oranges</li>
    <li>bananas</li>
</ol>
```

### Markdown
```md
1. apples
2. oranges
3. bananas
```

### Output
1. apples
2. oranges
3. bananas

---


## BlockQuotes
The `<blockquote>` tag specifies a section that is quoted from another source.

Browsers usually indent `<blockquote>` elements.

### HTML
```html
<blockquote>
    That's what she said
</blockquote>
```

### Markdown
```md
> That's what she said.
```

### Output
> That's what she said.

---

## Images
The `<img>` tag defines an image in an HTML page.

The `<img>` tag has two required attributes: src and alt.

Note: Images are not technically inserted into an HTML page, images are linked to HTML pages. The `<img>` tag creates a holding space for the referenced image.

> Tip: To link an image to another document, simply nest the `<img>` tag inside `<a>` tags.

### HTML
```html
<img src="images/logo.png">
<img src="https://www.example.com/images/logo.png">
```

### Markdown
```md
![alt text] (/images/logo.png)

![alt text](https://www.example.com/images/logo.png)
```

### Output

<img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png">

---

![image alt](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png "title")
---

## Links
The `<a>` tag defines a hyperlink, which is used to link from one page to another.

The most important attribute of the `<a>` element is the *href* attribute, which indicates the link's destination.

By default, links will appear as follows in all browsers:

- An unvisited link is underlined and blue
- A visited link is underlined and purple
- An active link is underlined and red


### HTML
```html
<a href="https://www.google.com">google</a>
```

### Markdown
```markdown
[google](https://www.google.com/)
```

### Output

[google](https://www.google.com/)

---


## Code blocks

The `<pre>` tag defines preformatted text.

Text in a `<pre>` element is displayed in a fixed-width font (usually Courier), and it preserves both spaces and line breaks.

The `<code>` tag is a phrase tag. It defines a piece of computer code.


<p>This is a python <code>function</code></p>

<pre><code>def square(value):
    result = value*value
    return result
</code></pre>


### HTML
```html
<p>This is a python <code>function</code></p>

<pre><code>def square(value):
    result = value*value
    return result
</code></pre>
```


### Markdown

{{< highlight md >}}
```python
    def square(value):
        result = value*value
        return result
```
{{< /highlight >}}



### Output
```python
def square(value):
    result = value*value
    return result
```

---

## Tables
The `<table>` tag defines an HTML table.

An HTML table consists of the `<table>` element and one or more `<tr>`, `<th>`, and `<td>` elements.

The `<tr>` element defines a table row, the `<th>` element defines a table header, and the `<td>` element defines a table cell.

A more complex HTML table may also include `<caption>`, `<col>`, `<colgroup>`, `<thead>`, `<tfoot>`, and `<tbody>` elements.



### HTML
```html
<table>
  <tr>
    <td>Ham</td>
    <td>yes</td>
  </tr>
  <tr>
    <td>Spam</td>
    <td>no</td>
  </tr>
</table>
```

### Markdown
```markdown
| Ham | Spam |
| ----| ---  |
| Yes | No   | 
```

### Output

| Ham |Spam |
| ----|--- |
| Yes | No |



# References

1. [markdown tutorial](https://www.markdowntutorial.com/)
2. [dillinger.io](http://dillinger.io/)
3. [stackedit.io](https://stackedit.io/)
4. [editor.md](https://pandao.github.io/editor.md/index.html)


[^1]: my opinion
