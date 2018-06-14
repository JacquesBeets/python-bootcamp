from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
d = soup.select("[data-example]") #css selecter select attribute (always returns a list back)
d = soup.select("#first") #css selecter (always returns a list back)
d = soup.select(".special") #css selecter (always returns a list back)
d1 = soup.find(id="first")
d2 = soup.find_all(class_="special")
d3 = soup.find_all(attrs={"data-example": "yes"})
#print(soup.body.div) # will give the first div
#print(soup.body.div.text) # will give the first div and give all the text in it
#print(d)
#print(d1)
#print(d2)
#print(d3[1])

