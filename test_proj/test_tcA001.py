# A001 test case -  Új felhasználó regisztrációja felhasználó név, email cím és jelszó megadásával.
# A tesztekhez használt felhasználók adatait a data/users.txt fájlban kell megadni (tetszőleges számú lehet)

import data.data_tcA001 as da01
import func.func_01 as fu01

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("http://localhost:1667")

# Várakozás a betöltésre
fu01.wait(driver, By.ID, "app")
time.sleep(2)

# *** TC-A001 **************************************


def test_A001(users):
    usern_text = []
    for user in users:
        fu01.sign_up(driver, user[0], user[1], user[2])
        usn_text = fu01.registr_check(driver)
        usern_text.append(usn_text)
    fu01.close_driver(driver)
    return usern_text


user_menu_text = test_A001(da01.users)

list_username = []
for user in da01.users:
    list_username.append(user[0])

print(list_username)

# ***************************************************

# normál futtatáshoz:
if __name__ == "__main__":
    print(user_menu_text)
    try:
        assert list_username == user_menu_text
    except:
        print("Hiba, az ellenőrző feltételnél nincs egyezés.")




