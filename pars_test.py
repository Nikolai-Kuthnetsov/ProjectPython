import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent

user = fake_useragent.UserAgent().random
header = {"user-agent": user}
urls = "https://browser-info.ru/"

res = requests.get(urls, headers=header).text
bs = BeautifulSoup(res, "lxml")

status_js = bs.find("div", id="javascript_check").find_all("span")[1].text
res_js = f"JavaScript: {status_js}"

status_flash = bs.find("div", id="flash_version").find_all("span")[1].text
res_flash = f"Flash: {status_flash}"

user_agent = bs.find("div", id="user_agent").text

print(res_js, res_flash, user_agent, sep="\n")
with open("f1.html", "w", encoding="utf-8") as file:
    file.write(res)
