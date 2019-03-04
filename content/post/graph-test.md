---
title: graph test
date: 2019-02-27
draft: true
keywords: []
description: ""
tags: []
categories: []
slug: graph-test
comment: false
toc: false
autoCollapseToc: false
postMetaInFooter: false
hiddenFromHomePage: false
mathjax: false
mathjaxEnableSingleDollar: false
mathjaxEnableAutoNumber: false
---

## Testing graph display
![alt text][img1]


<!--more-->

## readfile 

{{< readfile file="/content/graphs/testing.txt" >}}


## allow markdown

{{< readfile file="/content/graphs/testing.txt" markdown="true" >}}

---

# how about html
{{% center %}}
{{< readfile file="/content/graphs/graph01.html" >}}

{{% /center %}}



---

# graph 2
{{< readfile file="/content/graphs/graph02.txt" >}}


# graph 3 on images dir

{{< readfile file="/images/graph-test/graph03.txt" >}}

---
# graph 4 no responsive

{{< readfile file="/content/graphs/graph04.txt" >}}


[img1]: /images/graph-test/colormap.html