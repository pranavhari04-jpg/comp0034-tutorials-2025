# 1. Introduction: HTML and CSS

### HTML basics

The basic tag structure for HTML is `<start_tag> some content </end_tag>`. This set of opening tag +
content + closing tag is referred to as an **HTML element**.

A small number of elements only have an opening tag e.g. `<img>`, `<br>`, `<hr>`. There is a list of
these [void elements here](https://developer.mozilla.org/en-US/docs/Glossary/Void_element).

Elements can also have attributes that give additional information. In this course you will mostly
use id e.g. `id="some-name"` and class e.g. `class="some-class"`. `id` is used to locate an element
on a webpage; `class` is used in adding styles to elements.

HTML documents start with a document type declaration `<!DOCTYPE html>`. This is required at the
start of the document.

The HTML document itself begins with `<html>` and ends with `</html>`

The part that is mostly not visible in the final webpage is between `<head>` and `</head>`. This is
typically metadata, i.e. info about the page.

The part of the HTML document that is visible in the browser is between `<body>` and `</body>`.

A minimal page structure looks like the following:

```html
<!DOCTYPE html>
<!-- This is an HTML comment, you won't see it on the page -->
<!-- Head section -->
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>COMP0034 Introduction to HTML - Basic page structure</title>
</head>
<!-- Body section -->
<body>
<h1>Here is a heading</h1>
<p>Here is some text on a page.</p>
</body>
</html>
```

Use references for HTML elements and their options,
e.g. [W3Schools](https://www.w3schools.com/TAGS/default.asp)
or [Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference)

## CSS basics

CSS stands for Cascading Style Sheets. It provides styles for HTML elements.

Web browsers apply CSS rules to a document. A CSS **rule** consist of:

- A **selector**, which selects the element(s) you want to style

- A declaration which is a set of **properties** with values

The following CSS rule selects the paragraph tag `p` and makes the font colour red and the text
centre-aligned.

```css
p {
    color: red;
    text-align: center;
}
```

A set of these CSS rules is called a **stylesheet**.

CSS can be added to HTML elements in these ways:

- **Inline**: using the style attribute in HTML elements
- **Internal**: using a `<style>` element in the `<head>` section
- **External**: using an external CSS file e.g. `my_css.css`.

An **Inline style** affects one element only and is defined in the `style'=""` attribute of that
HTML element e.g. `<h1 style="color: blue; background-color: yellow;">Hello World! </h1>`. Avoid 
using this method as it is much harder to maintain.

An **internal stylesheet** places CSS inside a `<style>` element contained inside the HTML `<head>`
section.

An **external CSS file** is usually the preferred method and is used in most COMP0034 example code.
CSS is written in a separate file with a `.css` extension.
The stylesheet `.css` file is referenced in the `<head>` section of the HTML using an HTML `<link>`
element.

There are CSS references, though for the course you will use an open source CSS which will have its
own documentation that you will use.

[Next activity](2-determine-layout.md)
