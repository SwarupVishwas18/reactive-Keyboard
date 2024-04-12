from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def get_data(item: str) -> list:
    driver = webdriver.Firefox()
    item.replace(" ", "+")
    driver.get(f"https://www.google.com/maps/search/{item}+near+me/")
    assert "Google" in driver.title

    data = []

    element = driver.find_elements(By.CLASS_NAME, "fontHeadlineSmall")

    stars = driver.find_elements(By.CLASS_NAME, "MW4etd")
    addresses = driver.find_elements(By.CLASS_NAME, "W4Efsd")
    links = driver.find_elements(By.CLASS_NAME, "hfpxzc")
    img_divs = driver.find_elements(By.CLASS_NAME, "p0Hhde")

    imgs = []

    for img_div in img_divs:
        # imgs.append(img_div.find_element(By.TAG_NAME, "img").get_dom_attribute("src"))
        data.append(
            {"img": img_div.find_element(By.TAG_NAME, "img").get_dom_attribute("src")}
        )

    print(imgs)
    i = 0
    for el in element:
        data[i]["text"] = el.text
        i += 1
        print(el.text)

    i = 0
    for star in stars:
        data[i]["rating"] = star.text
        i += 1
        print(star.text)

    i = 0
    for address in addresses:
        text = address.text
        # print(text.split("."))
        if ("\n" in text) or ("₹" in text):
            continue
        print(i)
        if "·" in text:
            print(text.split("·"))
        elif "⋅" in text:
            print(text.split("⋅"))
        i += 1

    i = 0
    for l in links:
        print(l.get_dom_attribute("href"))
        data[i]["link"] = l.get_dom_attribute("href")
        i += 1
    assert "No results found." not in driver.page_source

    # print(element.text)
    print(driver.current_url)
    driver.close()

    print(data)
    return data


get_data("donut")

# from bs4 import BeautifulSoup
# import requests


# url = "https://www.google.com/maps/search/donuts+near+me/"
# fp = requests.get(url).text

# # print(fp)

# soup = BeautifulSoup(fp, "html.parser")

# print(soup.body.a)

# # obj = soup.find_all(attrs={"class": "hfpxzc"})
# # print(obj)
