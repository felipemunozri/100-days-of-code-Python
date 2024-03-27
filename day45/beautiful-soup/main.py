from bs4 import BeautifulSoup

# First we read the file that we want to scrap
# WARNING: we MUST pass the encoding used on the file to avoid errors while passing on the file to BeautifulSoup later
# (in this case the emoji character causes an error, so we must specify the utf-8 encoding)
with open(file="website.html", encoding="utf-8") as file:
    contents = file.read()

# To parse a document we pass it into the BeautifulSoup constructor. We can pass in a string or an open filehandle. Then
# we select the parser. The parser is the part that helps BeautifulSoup to 'understand' the content of the file.
# Depending on the type of file we can use a html or xml parser. The html.parser comes built in with python.
# Alternatively, we can use the lxml parser, but this one must be installed first
soup = BeautifulSoup(contents, "html.parser")

# The document is converted to Unicode and HTML entities are converted to Unicode characters. We can see it by printing
# it
# print(soup)
# print(soup.prettify())  # prettify() indents the text as if it were a html doc

# Once parsed, we can access specific sections of the original document by tapping on its elements, for example:

# print the <title> of the document
print(soup.title)

# we can get deeper into the elements by tapping into their properties
print(soup.title.name)
print(soup.title.string)

# we also can get the first appearance of an element
print(soup.li)

# or all the <li> elements on the document by using the find_all() function
for li in soup.find_all("li"):
    print(li)

# we can also get all the texts or all the href of the <a> elements in the document (aka. all the links to external
# pages) by using the .getText() and .get() functions respectively
for a in soup.find_all("a"):
    print(a.getText())
    print(a.get("href"))

# we can search specifics elements by using their ids as query. We do this by using the .find() function and passing the
# element and its id value
print(soup.find(name="h1", id="name"))

# when searching specifics elements by their class we must use the 'class_' keyword instead of 'class', since class is a
# reserved keyword in python used for creating classes
print(soup.find(name="h3", class_="heading"))

# when searching for a particular element who doesn't have a unique identifier we can use selectors in a similar way
# that we use them with css. In this example we use the .select_one() function which returns the first coincidence with
# the search term which is the selector 'p a', meaning an 'a' element inside a 'p' element
company_url = soup.select_one(selector="p a")
print(company_url)

# for selectors, we can use both ids and class names too
name_id = soup.select_one(selector="#name")
print(name_id)
all_headings = soup.select(selector=".heading")  # the .select() functions returns a list with all the coincidences
print(all_headings)
