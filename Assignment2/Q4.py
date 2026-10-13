#-------------------------------------------------------------------------
# AUTHOR: Jeannette Ruiz
# FILENAME: Q4.py
# FOR: CS 4250 - Assignment #2, Question 4
#-------------------------------------------------------------------------

# Importing Python libraries
import re
from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>My first web page</title>
</head>
<body>
<h1>My first web page</h1>
<h2>What this is tutorial</h2>
<p>A simple page put together using HTML. <em>I said a simple page.</em>.</p>
<ul>
<li>To learn HTML</li>
<li>
To show off
<ol>
<li>To my boss</li>
<li>To my friends</li>
<li>To my cat</li>
<li>To the little talking duck in my brain</li>
</ol>
</li>
<li>Because I have fallen in love with my computer.</li>
</ul>
<h3>Where to find the tutorial</h3>
<p><a href="http://www.aaa.com"><img src=http://www.aaa.com/badge1.gif></a></p>
<h4>Some random table</h4>
<table>
<tr class="tutorial1">
<td>Row 1, cell 1</td>
<td>Row 1, cell 2<img src=http://www.bbb.com/badge2.gif></td>
<td>Row 1, cell 3</td>
</tr>
<tr class="tutorial2">
<td>Row 2, cell 1</td>
<td>Row 2, cell 2</td>
<td>Row 2, cell 3<img src=http://www.ccc.com/badge3.gif></td>
</tr>
</table>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print()

# [a] Print the text of the <title> element by navigating the HTML tags

print(soup.html.head.title.text)

print()


# [B] Print the text of the second <li> element inside the <ol> below "To show off" by navigating the HTML tags.

print(soup.html.body.ul.find_all("li", recursive=False)[1].ol.find_all("li")[1].text)

print()


# [C] Print all <td> elements in the first <tr> row of the table by navigating the HTML tags.

for td in soup.html.body.table.tr.find_all("td"):
    print(td)

print()


# [D] Print the text of the <h2> element that contains the word "tutorial" by navigating the HTML tags and using a RegEx.

print(soup.html.body.find("h2", string=re.compile("tutorial")).text)

print()


# [E] Print all text nodes that contain the word "HTML" by using a RegEx.

for text in soup.html.body.find_all(string=re.compile("HTML")):
    print(text)

print()


# [F] Print all <td> elements in the second <tr> row of the table by navigating the HTML tags.

for td in soup.html.body.table.find_all("tr")[1].find_all("td"):
    print(td)

print()


# [G] Print all <img> tags contained within the <table> element by navigating the HTML tags.

for img in soup.html.body.table.find_all("img"):
    print(img)