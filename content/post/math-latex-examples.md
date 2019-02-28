---
title: Math Latex Examples

date: 2016-02-09
draft: false
keywords: []
description: ""
tags: ['LaTeX']
categories: ['math','laTex']
slug: math-latex-examples
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


## $\LaTeX$

LaTeX is a high-quality typesetting system; it includes features designed for the production of technical and scientific documentation. LaTeX is the de facto standard for the communication and publication of scientific documents.

For now,  we will focus just on writing math equations inside of a Markdown file or a jupyter notebook cell.

In most Markdown editors, you write a math equation inside two single dollar signs `$eqt$`, or double dollar signs
```latex
$$
eqt
$$
```


<!--more-->




## Operators

```
\cos (2\theta) = \cos^2 \theta - \sin^2 \theta
```

$$
\cos (2\theta) = \cos^2 \theta - \sin^2 \theta
$$

## limits

```latex
\lim_{x \to \infty} \exp(-x) = 0
```

$$
\lim_{x \to \infty} \exp(-x) = 0
$$


## Powers and indices

```latex
n^{22}
```


$n^{22}$


```latex
f(n) = n^5 + 4n^2 + 2 |_{n=17}
```

$$
f(n) = n^5 + 4n^2 + 2 |_{n=17}
$$

## Fractions and Binomials


```latex
\frac{n!}{k!(n-k)!} = \binom{n}{k}
```

$$
\frac{n!}{k!(n-k)!} = \binom{n}{k}
$$


```latex
\frac{\frac{1}{x}+\frac{1}{y}}{y-z}
```

$$
\frac{\frac{1}{x}+\frac{1}{y}}{y-z}
$$

## Sums and integrals

```latex
\sum_{i=1}^{10} t_i
```

$$
\sum_{i=1}^{10} t_i
$$

```latex
\displaystyle\sum_{i=1}^{10} t_i
```


$$
\displaystyle\sum_{i=1}^{10} t_i
$$


```latex
\int_0^\infty \mathrm{e}^{-x}\,\mathrm{d}x
```

$$
\int_0^\infty \mathrm{e}^{-x}\,\mathrm{d}x
$$

```latex
\sum_{\substack{
   0<i<m \\
   0<j<n
  }} 
 P(i,j)
 ```


$$
\sum_{\substack{
   0<i<m \\
   0<j<n
  }} 
 P(i,j)
 $$

 ---

## Brackets, braces and delimiters

```latex
( a ), [ b ], \{ c \}, | d |, \| e \|,
\langle f \rangle, \lfloor g \rfloor,
\lceil h \rceil, \ulcorner i \urcorner
```

$$
( a ), [ b ], \{ c \}, | d |, \| e \|,
\langle f \rangle, \lfloor g \rfloor,
\lceil h \rceil, \ulcorner i \urcorner
$$

## Manual sizing

```latex
( \big( \Big( \bigg( \Bigg( word \Bigg)  \bigg) \Big) \big) )
```

$$ 
( \big( \Big( \bigg( \Bigg( word \Bigg) \bigg) \Big) \big) )
$$


```latex
\frac{\mathrm d}{\mathrm d x} \left( k g(x) \right)
```

$$
\frac{\mathrm d}{\mathrm d x} \left( k g(x) \right)
$$



## Color

```latex
k = {\color{red}x} \mathbin{\color{blue}-} 2
```

$$
k = {\color{red}x} \mathbin{\color{blue}-} 2
$$



## Manually Specifying Formula Style

```latex
\begin{equation}
   C^i_j = {\textstyle \sum_k} A^i_k B^k_j
\end{equation}
```


$$
\begin{equation}
   C^i_j = {\textstyle \sum_k} A^i_k B^k_j
\end{equation}
$$


```latex
\newcommand{\tsum}[1]{{\textstyle \sum_{#1}}}
```

$$
\newcommand{\tsum}[1]{{\textstyle \sum_{#1}}}
$$



$$
\begin{equation}
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{equation}
$$

```latex
\begin{equation}
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{equation}
```








# List of mathematical symbols







## Trigonometric Functions

|Symbol	|Script   	|Symbol   	|Script   	|Symbol   	|Script   	|Symbol   	|Script|
|---	|---	|---	|---	|---	|---	|---	|---	|
|$\sin$   	|`\sin`   	|$\arcsin$   	|`\arcsin`   	|$\sinh$   	|`\sinh`   	|$\sec$   	|`\sec`   	|
|$\cos$   	|`\cos`   	|$\arccos$   	|`\arccos`   	|$\cosh$   	|`\cosh`   	|$\csc$   	|`\csc`   	|
|$\tan$   	|`\tan`   	|$\arctan$  	|`\arctan`   	|$\tanh$   	|`\tanh`   	|$\cot$  	| `\cot`  	|


## Other Symbols

|Symbol   	|Script   	|Symbol   	|Script   	|Symbol   	|Script   	|Symbol   	|Script   	|Symbol   	|Script   	|
|---	|---	|---	|---	|---	|---	|---	|---	|---	|---	|
|$\partial$   	|`\partial`     |$\imath$   	|`\imath`   	|$\Re$   	|`\Re`   	|$\nabla$   	|`\nabla`   	|$\aleph$   	|`\aleph`  |
|$\eth$   	|`\eth`     |$jmath$   	|`\jmath`   	|$\Im$   	|`\Im`   	|$\Box$   	|`\Box`   	|$\beth$   	|`\beth`  |
|$\hbar$   	|`\hbar`     |$\ell$   	|`\ell`   	|$\wp$   	|`\wp`   	|$\infty$   	|`\infty`   	|$\gimel$   	|`\gimel`  |


## Greek Letters







|Symbol       |Script   	    |Symbol   	|Script    	|
|-------	    |------	        |--------	  |-------    |
|A and $\alpha$|A and `\alpha`|N and $\nu$|N and `\nu`|
|B and $\beta$|B and `\beta`|$\Xi$ and $\xi$|`\Xi` and `\xi`|
|$\Gamma$ and $\gamma$ |`\Gamma` and `\gamma`|O and o|`O` and `o`|
|$\Delta$ and $\delta$|`\Delta` and `\delta`|$\Pi$, $\pi$, and $\varpi$|`\Pi`, `\pi` and `\varpig`|
|E,  $\epsilon$, and $\varepsilon$|E, `\epsilon`, and `\varepsilon`|P, $\rho$ and $\varrho$|P, `\rho` and `\varrho`|
|Z and $\zeta$|Z and `\zeta`|$\Sigma$, $\sigma$ and $\varsigma$|`\Sigma`, `\sigma` and `\varsigma`|
|H and $\eta$|H and `\eta`|T and $\tau$|T and `\tau`|
|$\Theta$, $\theta$ and $\vartheta$|`\Theta`, `\theta` and `\vartheta`|$\Upsilon$ and $\upsilon$|`\Upsilon` ,`\upsilon`|
|I and $\iota$|I and `\iota`|$\Phi$, $\phi$ and $\varphi$|`\Phi`, `\phi` and `\varphi`|
|K, $\kappa$, $\varkappa$|K, `\kappa`, `\varkappa`|X, $\chi$|X, `\chi`|
|$\Lambda$, $\lambda$|`\Lambda`, `\lambda`|$\Psi$, $\psi$|`\Psi`, `\psi`|
|M, $\mu$|M, `\mu`|$\Omega$, $\omega$|`\Omega`, `\omega`|


## Delimeters

|Symbol |Script|Symbol|Script|Symbol |Script|
|-------|------|------|------|-------|------|
|$\uparrow$|`\uparrow`|$\{$|`\{`| $\}$|`\}`|
|$\downarrow$ |`\downarrow`|$\Uparrow$|`\Uparrow`|$\Downarrow$|`\Downarrow`|







## Relation Symbols

|Symbol |Script|Symbol|Script|Symbol |Script|Symbol|Script|Symbol|Script|
|-------|------|------|------|-------|------|------|------|------|------|
|$<$|`<`|$>$|`>`|$=$|`=`|$\parallel$|`\parallel`|$\nparallel$|`\nparallel`|
|$\leq$|`\leq`|$\geq$|`\geq`|$\doteq$|`\doteq`|$\asymp$|`\asymp`|$\bowtie$|`\bowtie`|
|$\ll$|`\ll`|$\gg$|`\gg`|$\equiv$|`\equiv`|$\vdash$|`\vdash`|$\dashv$|`\dashv`|
|$\subset$|`\subset`|$\supset$|`\supset`|$\approx$|`\approx`|$\in$|`\in`|$\ni$|`\ni`|
|$\sqsubset$|`\sqsubset`|$\sqsupset$|`\sqsupset`|$\sim$|`\sim`|$\perp$|`\perp`|$\mid$|`\mid`|
|$\sqsubseteq$|`\sqsubseteq`|$\sqsupseteq$|`\sqsupseteq`|$\propto$|`\propto`|$\prec$|`\prec`|$\succ$|`\succ`|
|$\preceq$|`\preceq`|$\succeq$|`\succeq`|$\neq$|`\neq`|$\sphericalangle$|`\sphericalangle`|$\measuredangle$|`\measuredangle`|





## Binary Operations

|Symbol |Script|Symbol|Script|Symbol |Script|Symbol|Script|
|-------|------|------|------|-------|------|------|------|
|$\pm$|`\pm`|$\cap$|`\cap`|$\diamond$|`\diamond`|$\oplus$|`\oplus`|
|$\mp$|`\mp`|$\cup$|`\cup`|$\bigtriangleup$|`\bigtriangleup`|$\ominus$|`\ominus`|
|$\times$|`\times`|$\uplus$|`\uplus`|$\triangleleft$|`\triangleleft`|$\otimes$|`\otimes`|
|$\ast$|`\ast`|$\sqcap$|`\sqcap`|$\triangledown$|`\triangledown`|$\odot$|`\dot`|
|$\star$|`\star`|$\vee$|`\vee`|$\bigcirc$|`\bigcirc`|$\circ$|`\circ`|
|$\dagger$|`\dagger`|$\wedge$|`\wedge`|$\bullet$|`\bullet`|$\setminus$|`\setminus`|
|$\ddagger$|`\ddagger`|$\cdot$|`\cdot`|$\wr$|`\wr`|$\amalg$|`\amalg`|





## References



1. https://en.wikibooks.org/wiki/LaTeX/Mathematics
2. https://en.wikibooks.org/wiki/LaTeX/Introduction
