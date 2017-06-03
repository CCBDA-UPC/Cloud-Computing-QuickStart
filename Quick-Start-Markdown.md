# Markdown syntax

Markdown is a way to style text on the web. It is very popular among computer science engineers because it is intended to be as easy-to-read and easy-to-write as is feasible. Mostly, Markdown is just regular text with a few non-alphabetic characters thrown in, such as \# or \*. Github uses its own version of the Markdown syntax which provides an additional set of useful features. This is a subset of Github-flavored Markdown syntax that I'm using.


# Markdown code for "Headers"
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


# Markdown code for "Emphasis"
We have italics, bold, italic+bold and strikethrough:

```
Italics, use *asterisks* or _underscores_.

Bold, use **asterisks** or __underscores__.

Italic+Bold use **asterisks and _underscores_**.

Strikethrough use two tildes. ~~Scratch this.~~
```

Italics, use *asterisks* or _underscores_.

Bold, use **asterisks** or __underscores__.

Italic+Bold use **asterisks and _underscores_**.

Strikethrough use two tildes. ~~Scratch this.~~


Highlighting code inline isn't part of the Markdown spec, however Github supports it, using `backticks around` the specific code: 

```no-highlight
Inline `code` has `backticks around` it.
```

Inline `code` has `backticks around` it.


# Markdown code for "Ordered Lists"
Actual numbers don't matter in an ordered list, it only matters that there's a number. Lists can be ordered or unordered. A text box can be aligned with the item above as shown in the example (use three spaces to indent):
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
   
     Some text that should be aligned with the item above .
   
     Another text that should be aligned with the item above.  
    
7. List Item 4
   
   Some text that should be aligned with the item above.
   
   Another text that should be aligned with the item above.
 
# Markdown code for "Unordered Lists"
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
   Some text that should be aligned with the item above.
   Another text that should be aligned with the item above.
```
* List Item 1
* List Item 2
   1. Ordered sub-list Item 1
   3. Ordered sub-list Item 2
+ List Item 3
   * Unordered sub-list item 1
   * Unordered sub-list item 2
- List Item 4
   Some text that should be aligned with the item above.
   Another text that should be aligned with the item above.

# Markdown code for "Links"
We have 3 ways to create links:
```
[This is an inline-style link to my web page](http://www.angeltoribio.com)

URLs will automatically get turned into links: http://www.angeltoribio.com

```

[This is an inline-style link to my web page](http://www.angeltoribio.com)

```
URLs will automatically become links: http://www.angeltoribio.com
```

URLs will automatically become links: http://www.angeltoribio.com

You can also use numbers or text for reference-style a link:
```
[This is a reference-style link to my web page][text_or_number]

[text_or_number]: http://www.angeltoribio.com
```
[This is a reference-style link to my web page][text_or_number]

[text_or_number]: http://www.angeltoribio.com

Finally, despite it isn't part of the Markdown spec, if you want to link to a specific position in the same page `.md` you can create a label as:

```
<a name="code"/>
```
above the text to want to have a link to and to create a link to that position use
```
[Code](#code)  
```
<a name="code"/>
[Code](#code)  

# Markdown code for "Images"
We can insert images by using either an inline-style or a reference-style:
```
![UPC Barcelona Tech](./img/UPClogo.png "UPC logo")

![UPC Barcelona Tech][UPC-logo]

[UPC-logo]: ./img/UPClogo.png "UPC logo"

```
![UPC Barcelona Tech](./img/UPClogo.png "UPC logo")


![UPC Barcelona Tech][UPC-logo]

[UPC-logo]: ./img/UPClogo.png  "UPC logo"




# Markdown code for "Bloc code"

Blocks of code are either fenced by lines with three backticks <code>```</code>, or are indented using four spaces. I only recommend using the fenced code blocks -- they're easier to spot and they support syntax highlighting.

<pre lang="no-highlight"><code>
```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```
 
```
No language indicated, therefore no syntax highlighting. 
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
No language indicated, therefore no syntax highlighting in Markdown Here (varies on Github). 
But let's throw in a <b>tag</b>.
```

# Markdown code for "Tables"
You can add tables using colons to align column content: 

```no-highlight

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

```

| Tables        | Are           | Cool |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

```
Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3
```

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

# Markdown code for "Blockquotes"


```no-highlight
> This is a quote.
> This line is part of the same quote.
```

> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

```
> This is a very long line that will still be quoted properly when it wraps. This is a very long line that will still be quoted properly when it wraps. This is a very long line that will still be quoted properly when it wraps.
```

> This is a very long line that will still be quoted properly when it wraps. This is a very long line that will still be quoted properly when it wraps. This is a very long line that will still be quoted properly when it wraps.

# Markdown code for "inline HTML"

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



# Markdown code for "Horizontal Rule"


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




# Youtube videos

They can't be added directly but you can add an image with a link to the video like this:

```no-highlight
<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
```


# Backslash escapes
Markdown allows you to use backslash escapes to generate literal characters which would otherwise have special meaning in Markdown’s formatting syntax. 
Markdown provides backslash escapes for the following characters:

Character | Code | Description
--- | --- | ---
 **\\**   | `\\` | back slash
 **\`**   | ```\` ``` | backtick
 \*    | `\*` | asterisk
 **\_**   | `\_` | underscore
 **\{\}**  | `\{\}` | curly braces
 **\[\]**  | `\[\]` | square brackets
 **\(\)**  | `\(\)` | parentheses
 **\#**   | `\#` | hash mark
 **\+**   | `\+` | plus sign
 **\-**   | `\-` | minus sign (hyphen)
 **\.**   | `\.` | dot
 **\!**   | `\!` | exclamation mark

---
*Part of this Quick Start tutorial is based on https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet*

