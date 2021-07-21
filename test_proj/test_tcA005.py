# A005 test case - Saját, meglévő blogbejegyzés törlése - kilépés.

import data.data_tcA005 as da05
import func.func_01 as fu01

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("http://localhost:1667")

# Várakozás a betöltésre
fu01.wait(driver, By.ID, "app")
time.sleep(2)

# *** TC-A005 **************************************


def test_A005():
    fu01.sign_in(driver, da05.mail, da05.passw)
    what_text_l = fu01.blog_del(driver)
    fu01.out_close_driver(driver)
    return what_text_l


what_text = test_A005()


# ***************************************************

# normál futtatáshoz:
if __name__ == "__main__":
    print(what_text[0], what_text[1],)
    try:
        assert what_text[0] != what_text[1]
    except:
        print("Hiba, az ellenőrző feltételnél nincs eltérés.")

