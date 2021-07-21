# A001 test case -  Új felhasználó regisztrációja felhasználó név, email cím és jelszó megadásával.
# A tesztekhez használt felhasználók adatait a data/users.csv fájlban kell megadni (tetszőleges számú lehet)

import func.func_01 as fu01

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

#driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
#driver = webdriver.Chrome(ChromeDriverManager().install())                              # normál mód

driver.get("http://localhost:1667")

# Várakozás a betöltésre
fu01.wait(driver, By.ID, "app")
time.sleep(2)

# *** TC-A001 **************************************


def test_A001_users():
#    filename = "users.csv"
    with open("users.csv", "r", encoding='utf-8') as csvfile:
        reader = list(csv.reader(csvfile, delimiter=','))
        print(reader)
        list_us = reader[1:]
        print(list_us)
        return list_us


list_user = test_A001_users()
list_username = []
for user in list_user:
    list_username.append(user[0])

print(list_username)


def test_A001(users):
    usern_text = []
    for user in users:
        fu01.sign_up(driver, user[0], user[1], user[2])
        usn_text = fu01.registr_check(driver)
        usern_text.append(usn_text)
    fu01.close_driver(driver)
    return usern_text


user_menu_text = test_A001(list_user)


# ***************************************************

# normál futtatáshoz:
if __name__ == "__main__":
    print(user_menu_text)
    try:
        assert list_username == user_menu_text
    except:
        print("Hiba, az ellenőrző feltételnél nincs egyezés.")




