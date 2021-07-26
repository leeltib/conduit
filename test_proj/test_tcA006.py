# A006 test case - Tags funkció tesztelése (listázás)

import data.data_tcA006 as da06
import func.func_01 as fu01

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("http://localhost:1667")

# Várakozás a betöltésre
fu01.wait(driver, By.ID, "app", 2)

# *** TC-A006 **************************************


def test_A006_basis():
    fu01.sign_in(driver, da06.mail, da06.passw)
    return fu01.tags_list(driver)


tags_basis = test_A006_basis()


def test_A006_add():
    fu01.blog_write(driver, da06)
    return fu01.tags_list(driver)


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
    rn = len(tags_add)
    add_num = len(tags_add) - len(tags_basis)
    ta_ba = tags_basis
    for i in range(add_num):
        ta_ba.append([0, 0])
    ta_de = tags_del
    for i in range(add_num):
        ta_de.append([0, 0])
    for i in range(rn):
        print(f"{tags_add[i][0]}: bas={ta_ba[i][1]}, add={tags_add[i][1]}, del={ta_de[i][1]}")
    try:
        assert tags_basis == tags_del
        assert tags_basis != tags_add
    except:
        print("Hiba, az ellenőrző feltételek nem a várt eredményt mutatják.")


