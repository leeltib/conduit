# TC002 test case - Belépés a regisztráció során megadott adatokkal - kilépés.

import data.data_tcA002 as da02
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
fu01.wait(driver, By.ID, "app", 2)

# *** TC-A002 **************************************


def test_A002():
    fu01.cookie_ok(driver)
    fu01.sign_in(driver, da02.mail, da02.passw)
    usern_text = fu01.login_check(driver)
    fu01.out_close_driver(driver)
    return usern_text


username_text = test_A002()


# ***************************************************

# normál futtatáshoz:
if __name__ == "__main__":
    print(username_text)
    try:
        assert da02.name == username_text
    except:
        print("Hiba, az ellenőrző feltételnél nincs egyezés.")


