from bs4 import BeautifulSoup
import requests
from win10toast import ToastNotifier

source = requests.get("https://www.worldometers.info/coronavirus/country/india/").text

soup = BeautifulSoup(source, "lxml")


date = soup.find("div", class_="news_date")

cases = soup.find("li", class_="news_li")
new_case = cases.strong.text.split()[0]
# print(f"new_case : {new_case}")

deaths = list(cases.strong.next_siblings)[1].text.split()[0]
# print(f"deaths: {deaths}")

notifier = ToastNotifier()
message = f"New Cases: {new_case} \n New Deaths: {deaths}"
notifier.show_toast(title="Covid-19 Update", msg=message, duration=5)

