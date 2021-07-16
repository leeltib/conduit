# A006 test case - Tags funkció tesztelése (listázás)

import data.data_tcA006 as da06
import func.func_01 as fu01

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
#driver = webdriver.Chrome(ChromeDriverManager().install())                              # normál mód

driver.get("http://localhost:1667")

# Várakozás a betöltésre
fu01.wait(driver, By.ID, "app")
time.sleep(2)

# *** TC-A006 **************************************

def test_A006_basis():
    fu01.sign_in(driver, da06.mail, da06.passw)
    ta_bas = fu01.tags_list(driver)
    return ta_bas

tags_basis = test_A006_basis()

def test_A006_add():
    fu01.blog_write(driver, da06)
    ta_add = fu01.tags_list(driver)
    return ta_add

tags_add = test_A006_add()

def test_A006_del():
    fu01.blog_del(driver)
    ta_del = fu01.tags_list(driver)
    fu01.out_close_driver(driver)
    return ta_del

tags_del = test_A006_del()

# ***************************************************

# normál futtatáshoz:
if __name__ == "__main__":
    print(tags_basis)
    print(tags_add)
    print(tags_del)
    try:
        assert tags_basis == tags_del
        assert tags_basis != tags_add

    except:
        print("Hiba, az ellenőrző feltételek nem a várt eredményt mutatják.")


