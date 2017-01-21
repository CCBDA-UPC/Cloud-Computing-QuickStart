# Markdown syntax

Markdown is a way to style text on the web very popular between computer science engineers. Monstly, Markdown is just regular text with a few non-alphabetic characters thorwn in, like \# or \*. Github uses its own version of the Markdown syntax tjat provides an additional set of useful features. This is a subset of Github-flavored Markdown syntax that I'm using.

# Markdown codes for "Headers"
We have 6 levels:
```
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6

Alternatively, for Header 1 and Header 2, an underline-ish style:
```
Header 1
========

Header 2
--------
```

Header 1
========

Header 2
--------


# Markdown codes for "Emphasis"
We have italics, bold, italic+bold and strikethrough:

```
Italics, with *asterisks* or _underscores_.

Bold, with **asterisks** or __underscores__.

Italic+Bold with **asterisks and _underscores_**.

Strikethrough with two tildes. ~~Scratch this.~~
```

Italics, with *asterisks* or _underscores_.

Bold, with **asterisks** or __underscores__.

Italic+Bold with **asterisks and _underscores_**.

Strikethrough with two tildes. ~~Scratch this.~~

# Markdown codes for "Ordered Lists"
Actual numbers don't matter in an ordered list, just that it's a number. Could content a unordered or ordered list. A text box can be aligned with the above item as shown in the example (keep a :
```
1. List Item 1
1. List Item 2
  1. Ordered sub-list Item 1
  3. Ordered sub-list Item 2
5. List Item 3
  * Unordered sub-list item 1
  * Unordered sub-list item 2
  
    Some text that should be aligned with the above item.
   
    Another text that should be aligned with the above item.  
   
7. List Item 4

   Some text that should be aligned with the above item.
   
   Another text that should be aligned with the above item.
```

1. List Item 1
1. List Item 2
  1. Ordered sub-list Item 1
  3. Ordered sub-list Item 2
5. List Item 3
  * Unordered sub-list item 1
  * Unordered sub-list item 2
   
    Some text that should be aligned with the above item.
   
    Another text that should be aligned with the above item.  
    
7. List Item 4
   
   Some text that should be aligned with the above item.
   
   Another text that should be aligned with the above item.
 
# Markdown codes for "Unordered Lists"
Unordered list can use asterisks, or minuses, or pluses.

```
* List Item 1
* List Item 2
  1. Ordered sub-list Item 1
  3. Ordered sub-list Item 2
+ List Item 3
  * Unordered sub-list item 1
  * Unordered sub-list item 2
  
- List Item 4
   
   Some text that should be aligned with the above item.
   
   Another text that should be aligned with the above item.

```

* List Item 1
* List Item 2
  1. Ordered sub-list Item 1
  3. Ordered sub-list Item 2
+ List Item 3
  * Unordered sub-list item 1
  * Unordered sub-list item 2
  
- List Item 4
   
   Some text that should be aligned with the above item.
   
   Another text that should be aligned with the above item.

# Markdown codes for "Links"
We have 3 ways to create links:
```
[This is an inline-style link](http://www.JordiTorres.Barcelona)

URLs will automatically get turned into links: http://www.JordiTorres.Barcelona

```

[This is an inline-style link to my web page](http://www.JordiTorres.Barcelona)

```
URLs will automatically get turned into links: http://www.JordiTorres.Barcelona
```

URLs will automatically get turned into links: http://www.JordiTorres.Barcelona

You can also use numbers or text for reference-style a link:
```
[This is a reference-style link to my web page][text_or_number]

[text_or_number]: http://www.JordiTorres.Barcelona
```
[This is a reference-style link to my web page][text_or_number]

[text_or_number]: http://www.JordiTorres.Barcelona

# Markdown codes for "Images"
We can do it either in inline-style or reference-style:
```
![UPC Barcelona Tech](https://github.com/jorditorresBCN/Quick-Start/blob/master/img/UPClogo.png "UPC logo")

![UPC Barcelona Tech][UPC-logo]

[UPC-logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "UPC logo"

```
![UPC Barcelona Tech](https://github.com/jorditorresBCN/Quick-Start/blob/master/img/UPClogo.png "UPC logo")


![UPC Barcelona Tech][UPC-logo]

[UPC-logo]: https://github.com/jorditorresBCN/Quick-Start/blob/master/img/UPClogo.png  "UPC logo"





# VAIG PER AQUI


<a name="code"/>
## Code and Syntax Highlighting

Code blocks are part of the Markdown spec, but syntax highlighting isn't. However, many renderers -- like Github's and *Markdown Here* -- support syntax highlighting. Which languages are supported and how those language names should be written will vary from renderer to renderer. *Markdown Here* supports highlighting for dozens of languages (and not-really-languages, like diffs and HTTP headers); to see the complete list, and how to write the language names, see the [highlight.js demo page](http://softwaremaniacs.org/media/soft/highlight/test.html).

```no-highlight
Inline `code` has `back-ticks around` it.
```

Inline `code` has `back-ticks around` it.

Blocks of code are either fenced by lines with three back-ticks <code>```</code>, or are indented with four spaces. I recommend only using the fenced code blocks -- they're easier and only they support syntax highlighting.

<pre lang="no-highlight"><code>```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```
 
```
No language indicated, so no syntax highlighting. 
But let's throw in a &lt;b&gt;tag&lt;/b&gt;.
```
</code></pre>



```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
```

```
No language indicated, so no syntax highlighting in Markdown Here (varies on Github). 
But let's throw in a <b>tag</b>.
```


<a name="tables"/>
## Tables

Tables aren't part of the core Markdown spec, but they are part of GFM and *Markdown Here* supports them. They are an easy way of adding tables to your email -- a task that would otherwise require copy-pasting from another application.

```no-highlight
Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3
```

Colons can be used to align columns.

| Tables        | Are           | Cool |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell. The outer pipes (|) are optional, and you don't need to make the raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

<a name="blockquotes"/>
## Blockquotes

```no-highlight
> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote. 
```

> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote. 

<a name="html"/>
## Inline HTML

You can also use raw HTML in your Markdown, and it'll mostly work pretty well. 

```no-highlight
<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>
```

<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>

<a name="hr"/>
## Horizontal Rule

```
Three or more...

---

Hyphens

***

Asterisks

___

Underscores
```

Three or more...

---

Hyphens

***

Asterisks

___

Underscores

<a name="lines"/>
## Line Breaks

My basic recommendation for learning how line breaks work is to experiment and discover -- hit &lt;Enter&gt; once (i.e., insert one newline), then hit it twice (i.e., insert two newlines), see what happens. You'll soon learn to get what you want. "Markdown Toggle" is your friend. 

Here are some things to try out:

```
Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

This line is also a separate paragraph, but...
This line is only separated by a single newline, so it's a separate line in the *same paragraph*.
```

Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

This line is also begins a separate paragraph, but...  
This line is only separated by a single newline, so it's a separate line in the *same paragraph*.

(Technical note: *Markdown Here* uses GFM line breaks, so there's no need to use MD's two-space line breaks.)

<a name="videos"/>
## Youtube videos

They can't be added directly but you can add an image with a link to the video like this:

```no-highlight
<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
```

Or, in pure Markdown, but losing the image sizing and border:

```no-highlight
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
```



# BACKSLASH ESCAPES
Markdown allows you to use backslash escapes to generate literal characters which would otherwise have special meaning in Markdown’s formatting syntax. 
Markdown provides backslash escapes for the following characters:

| **\\**   | backslash| 
| **\`**   | backtick| 
| \*    | asterisk| 
| **\_**   | underscore| 
| **\{\}**  | curly braces| 
| **\[\]**  | square brackets| 
| **\(\)**  | parentheses| 
| **\#**   | hash mark| 
| **\+**   | plus sign| 
| **\-**   | minus sign (hyphen)| 
| **\.**   | dot| 
| **\!**   | exclamation mark| 

