import requests
from bs4 import BeautifulSoup

def ehyun():
    meal = requests.get("https://www.wahschool.com/school/meal/view.htm?seq=772&menu=3&id=661072")
    meal.text

    meal1 = BeautifulSoup(meal.content, "html.parser")
    meal2 = meal1.find_all("td")[-5].text

    return meal2

# ----------------------------------------------------------------------------------------------------------------
print(ehyun())