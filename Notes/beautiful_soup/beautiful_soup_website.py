from bs4 import BeautifulSoup
import requests
import csv

# getting the source code from the website
# .get will return the response object
# to get the source code from the request object we can  use ".text"
source = requests.get("http://coreyms.com").text

soup = BeautifulSoup(source, "lxml")

article = soup.find("article")
# print(article.prettify())
# headline = article.h2.a.text
# print(headline)

# summary = article.find("div", class_="entry-content").p.text
# print(summary)


# to get the link to video is not easy
# src is pointing to youtube so we will select the id of that youtube video
# vid_src = article.find("iframe", class_="youtube-player")
# print(vid_src)


# now we don't want the text of the iframe what we really want is the value of that src attribute from that tag
#  to do this we can access it like a dictionary
# vid_src = article.find("iframe", class_="youtube-player")["src"]
# print(vid_src)

# now we have to grab the id of that video
# id comes after '/' so let's split on '/'

# vid_id = vid_src.split("/")
# print(vid_id)


# now id is in index 4 so let's grab index 4
# vid_id = vid_src.split("/")[4]
# print(vid_id)

# now the video id is before "?" so now let's do another split on "?" to get the id
# vid_id = vid_src.split("/")[4]
# vid_id = vid_id.split("?")[0]
# print(vid_id)

# now we can create our own youtube like using this video id
# if i use this yt_link then this will take me to exact youtube video
# yt_link = f"https://youtube.com/watch?v={vid_id}"
# print(yt_link)

# now we got the information of one article so loop over and find the information for all the article
# i used try-catch by myself because it was givving error due to "update" article present in website

# for article in soup.find_all("article"):
#     headline = article.h2.a.text
#     print(headline)

#     summary = article.find("div", class_="entry-content").p.text
#     print(summary)

#     try:
#         vid_src = article.find("iframe", class_="youtube-player")["src"]
#         vid_id = vid_src.split("/")[4]
#         vid_id = vid_id.split("?")[0]
#         yt_link = f"https://youtube.com/watch?v={vid_id}"
#     except Exception as e:
#         yt_link = None

#     print(yt_link)
#     print()

# let save the scrapped output in csv file
csv_file = open("cms_scrape.csv", "w")

csv_writter = csv.writer(csv_file)
csv_writter.writerow(["headline", "summary", "video link"])

for article in soup.find_all("article"):
    headline = article.h2.a.text
    print(headline)

    summary = article.find("div", class_="entry-content").p.text
    print(summary)

    try:
        vid_src = article.find("iframe", class_="youtube-player")["src"]
        vid_id = vid_src.split("/")[4]
        vid_id = vid_id.split("?")[0]
        yt_link = f"https://youtube.com/watch?v={vid_id}"
    except Exception as e:
        yt_link = None

    print(yt_link)
    print()

    csv_writter.writerow([headline, summary, yt_link])

csv_file.close()
