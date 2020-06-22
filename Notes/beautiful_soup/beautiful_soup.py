from bs4 import BeautifulSoup
import requests


# we are opening the html file "sample.html" which is in the same directory as this
# lxml is a parser we are using to parse the html file
with open("sample.html") as html_file:
    soup = BeautifulSoup(html_file, "lxml")

# *************************************************************************************************
# prettify make the html look good for better understatnding
# print(soup.prettify())

# *************************************************************************************************
# easiest way to grab information from a "tag" is to just access it like a attribute
# grabbibg the title

# match = soup.title
# print(match)

# *************************************************************************************************
# to only get the text inside the "title" use "text" at the end
# match = soup.title.text
# print(match)

# *************************************************************************************************
# if there are multiple tags and if we access them as attribute then it will return the first tag
# returns the first "div"
# match = soup.div
# print(match)
# print("*" * 50)

# *************************************************************************************************
# to get access to perticular div we will use "find()"
# the reason we use underscore after class is because class is a keyword in python
# match = soup.find("div", class_="footer")
# print(match)

# *************************************************************************************************
# now we want to parse the html and get all the article headline and summaries from the page anytime we want multiple things from the page
# the good way is to get one of whatever it is you wanted to parse
# now i want the headline and snippet from each article from page then let's first grab the information of first article and once we have that
# working we will apply it to all the article
# for grabbing something make use of the "inspect element"
# article = soup.find("div", class_="article")
# print(article)

# *************************************************************************************************
# now we can access the child tag of that div as an attribute
# so let's select heading of that article
# headline = article.h2.a.text
# print(headline)

# summary = article.p.text
# print(summary)

# *************************************************************************************************
# so we have the information of one article so let's now use this to grab the information of all the article
# to grab all the article we just need to use "find_all()" instead of "find()"
# "find_all()" will return the list of all that matches the argument so we can loop over it

for article in soup.find_all("div", class_="article"):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print("-" * 60)

