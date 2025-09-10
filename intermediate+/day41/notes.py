"""
Websites - HTML, CSS and JavaScript

HTML = Structure
CSS = Sytle
JavaScript = Functionaility/Behaviour


🔧 1. Basic HTML Structure Tags
Tag 	Description 	Example
<html> 	Root of the HTML document 	<html> ... </html>
<head> 	Metadata container 	<head> ... </head>
<body> 	Main document content 	<body> ... </body>
<title> 	Page title (in browser tab) 	<title>My Page</title>
<!DOCTYPE> 	Declares document type 	<!DOCTYPE html>

📝 2. Text Formatting Tags
Tag 	Description 	Example
<p> 	Paragraph 	<p>This is a paragraph.</p>
<br> 	Line break 	Hello<br>World
<hr> 	Horizontal line 	<hr>
<h1> to <h6> 	Headings 	<h1>Heading 1</h1>
<strong> 	Bold (semantic) 	<strong>Important</strong>
<b> 	Bold (visual only) 	<b>Bold Text</b>
<i> 	Italic (visual only) 	<i>Italic Text</i>
<em> 	Emphasis (semantic italic) 	<em>Emphasized</em>
<mark> 	Highlighted text 	<mark>Highlight</mark>
<small> 	Smaller text 	<small>Note</small>
<sub> 	Subscript 	H<sub>2</sub>O
<sup> 	Superscript 	E = mc<sup>2</sup>
<u> 	Underline 	<u>Underlined</u>
<del> 	Deleted text 	<del>Old</del>
<ins> 	Inserted text 	<ins>New</ins>

🔗 3. Links & Anchors
Tag 	Description 	Example
<a> 	Hyperlink 	<a href="https://example.com">Visit</a>
<link> 	External resources (e.g., CSS) 	<link rel="stylesheet" href="style.css">
<nav> 	Navigation block 	<nav><a href="#home">Home</a></nav>

🖼️ 4. Media Tags
Tag 	Description 	Example
<img> 	Image 	<img src="img.jpg" alt="Image">
<video> 	Video 	<video controls><source src="video.mp4"></video>
<audio> 	Audio 	<audio controls><source src="audio.mp3"></audio>
<source> 	Media source 	<source src="movie.mp4" type="video/mp4">
<track> 	Captions/subtitles 	<track src="subs.vtt" kind="subtitles">
<embed> 	External resource (e.g., PDF) 	<embed src="file.pdf">

📋 5. Lists
Tag 	Description 	Example
<ul> 	Unordered list 	<ul><li>Item</li></ul>
<ol> 	Ordered list 	<ol><li>First</li></ol>
<li> 	List item 	<li>Element</li>
<dl> 	Description list 	<dl><dt>HTML</dt><dd>Markup</dd></dl>
<dt> 	Term in <dl> 	<dt>Term</dt>
<dd> 	Description in <dl> 	<dd>Definition</dd>

📦 6. Table Tags
Tag 	Description 	Example
<table> 	Table container 	<table> ... </table>
<tr> 	Table row 	<tr> ... </tr>
<td> 	Table data cell 	<td>Data</td>
<th> 	Table header cell 	<th>Header</th>
<thead> 	Table header section 	<thead><tr><th>Col</th></tr></thead>
<tbody> 	Table body section 	<tbody><tr><td>Row</td></tr></tbody>
<tfoot> 	Table footer section 	<tfoot><tr><td>Foot</td></tr></tfoot>
<caption> 	Table caption/title 	<caption>Sales Data</caption>
<col> 	Column formatting 	<col span="2">
<colgroup> 	Group of columns 	<colgroup><col></colgroup>

🧩 7. Form & Input Tags
Tag 	Description 	Example
<form> 	Form container 	<form> ... </form>
<input> 	User input 	<input type="text">
<textarea> 	Multi-line input 	<textarea></textarea>
<label> 	Form label 	<label for="name">Name</label>
<select> 	Dropdown 	<select><option>One</option></select>
<option> 	Dropdown item 	<option value="1">One</option>
<button> 	Button 	<button>Click</button>
<fieldset> 	Group form fields 	<fieldset><legend>Info</legend></fieldset>
<legend> 	Caption for <fieldset> 	<legend>User Info</legend>
<datalist> 	Predefined input list 	<datalist id="browsers"><option>Chrome</option></datalist>
<output> 	Output result 	<output>Result</output>

📁 8. Semantic Layout Tags
Tag 	Description 	Example
<header> 	Page or section header 	<header> ... </header>
<footer> 	Page or section footer 	<footer> ... </footer>
<section> 	Generic section 	<section> ... </section>
<article> 	Independent content 	<article> ... </article>
<aside> 	Sidebar content 	<aside> ... </aside>
<main> 	Main content 	<main> ... </main>
<div> 	Generic container 	<div> ... </div>
<span> 	Inline container 	<span> ... </span>

🧠 9. Scripting & Meta Tags
Tag 	Description 	Example
<script> 	JavaScript code 	<script>alert('Hi')</script>
<noscript> 	Shown if JS disabled 	<noscript>No JS</noscript>
<meta> 	Metadata 	<meta charset="UTF-8">
<style> 	Internal CSS 	<style>p{color:red}</style>

🔎 10. Interactive Tags
Tag 	Description 	Example
<details> 	Toggle details 	<details><summary>Click</summary>Info</details>
<summary> 	Visible heading in <details> 	<summary>More</summary>
<dialog> 	Dialog box 	<dialog open>Hi</dialog>

🔄 11. Deprecated/Obsolete Tags (for reference only)
Tag 	Description 	Example
<center> 	Center align 	<center>Centered</center>
<font> 	Font formatting 	<font color="red">Text</font>
<marquee> 	Scrolling text 	<marquee>Scroll</marquee>

✅ 12. Miscellaneous Tags
Tag 	Description 	Example
<iframe> 	Inline frame (embed) 	<iframe src="page.html"></iframe>
<base> 	Base URL for links 	<base href="https://example.com/">
<time> 	Time value 	<time datetime="2025-07-30">Today</time>
<code> 	Code snippet 	<code>print()</code>
<kbd> 	Keyboard input 	<kbd>Ctrl</kbd>
<samp> 	Sample output 	<samp>Hello</samp>
<var> 	Variable name 	<var>x</var>
<bdi> 	Isolate bidirectional text 	<bdi>abc</bdi>
<bdo> 	Override text direction 	<bdo dir="rtl">Text</bdo>

"""

#############################
# Tags vs Element
#############################

# The Element is the entire thing
# Tags and Content

# <h1>content</>
# opening tag -- content -- closing tag

# Example
# <h1>Book</h1>
#   <h2>Chapter 1</h2>
#     <h3>Section 1</h3>
#     <h3>Section 2</h3>
#   <h2>Chapter 2</h2>
#     <h3>Section 1</h3>
#       <h4>Diagram 1</h4>
#   <h2>Chapter 3</h2>
#     <h3>Section 1</h3>
#     <h3>Section 2</h3>

#############################
# Paragraph
#############################

# <p>paragraph of text</p>

#############################
# Void Elements
#############################

# Horizontal Rule
# <hr />

# Break Rule (new line in Poem or address)
# <br /> 

#############################
# Challenge
#############################

# <!DOCTYPE html>
# <h1>James' Top TV Shows</h1>
# <h2>In no particular order - 5 of my favourite TV series!</h2>
# <hr />
# <h3>Bron ||| Broen</h3>
# <p>
#     When a body is found on the bridge between Denmark and Sweden, right on the border, Danish inspector Martin Rohde and
#     Swedish Saga Norén have to share jurisdiction and work together to find the killer.
# </p>
# <h3>Ted Lasso</h2>
# <p>
#     American college football coach Ted Lasso heads to London to manage AFC Richmond, a struggling English Premier League
#     soccer team.
# </p>
# <h3>The Sorpanos</h3>
# <p>
#     New Jersey mob boss Tony Soprano deals with personal and professional issues in his home and business life that affect
#     his mental state, leading him to seek professional psychiatric counseling.
# </p>
# <h3>Breaking Bad</h3>
# <p>
#     A chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine with a
#     former student to secure his family's future.
# </p>
# <h3>Taskmaster</h3>
# <p>
#     Five comedians are set tasks challenging their creativity and wit. The tasks are supervised by Alex Horne but the
#     Taskmaster, Greg Davies, always has the final word.
# </p>