# ==================================================
# Objectives
# ==================================================

# Define what web scraping is and the issues surrounding it
# Use the requests and BeautifulSoup modules to parse HTML
# Explain some common problems with web scraping
# Explore other tools that can interact with web pages

# ==================================================
# BEAUTIFULL SOUP
# ==================================================

# To extract data from HTML, we'll use Beautiful Soup
# Install it with pip
# Beautiful Soup lets us navigate through HTML with Python



# ==================================================
# Parsing and Navigating HTML
# ==================================================


# BeautifulSoup(html_string, "html.parser") - parse HTML
# Once parsed, There are several ways to navigate:
#   By Tag Name
#   Using find - returns one matching tag
#   Using find_all - returns a list of matching tags



# ==================================================
# Navigating with CSS Selectors
# ==================================================

# select - returns a list of elements matching a CSS selector

# Selector Cheatsheet

    # Select by id of foo: #foo
    # Select by class of bar: .bar
    # Select children: div > p
    # Select descendents: div p

# # find an element with an id of foo
# soup.find(id="foo")
# soup.select("#foo")[0]

# # find all elements with a class of bar
# # careful! "class" is a reserved word in Python
# soup.find_all(class_="bar")
# soup.select(".bar")

# # find all elements with a data
# # attribute of "baz"
# # using the general attrs kwarg
# soup.find_all(attrs={"data-baz": True})
# soup.select("[data-baz]")



# ==================================================
# Accessing Data in Elements
# ==================================================

# get_text - access the inner text in an element
# name - tag name
# attrs - dictionary of attributes
# You can also access attribute values using brackets!



# ==================================================
# Navigating with CSS Selectors
# ==================================================

# Via Tags

#     parent / parents
#     contents
#     next_sibling / next_siblings
#     previous_sibling / previous_siblings

# Via Searching

#     find_parent / find_parents
#     find_next_sibling / find_next_siblings
#     find_previous_sibling / find_previous_siblings