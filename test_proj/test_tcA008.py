# A008 - comment function
# Kiválasztható a blogszerző, és a konkrét blog
# A komment szövegét külső fájlból olvassuk be

import data.data_tcA008 as da08
import func.func_02 as fu02

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("http://localhost:1667")

# Várakozás a betöltésre
fu02.wait(driver, By.ID, "app")
time.sleep(2)

# *** TC-A008 **************************************


def test_comment_text():
    comm_full_list = []
    for element in da08.comment_full:
        el1 = element.strip()
        el2 = el1.replace("\n", " ")
        comm_full_list.append(el2)
    return comm_full_list


comments_text = test_comment_text()


def test_A008_comment():
    fu02.sign_in(driver, da08.mail, da08.passw)
    co_da_li = fu02.user_comment(driver, da08.com_list_num, da08.com_list, comments_text)
    fu02.out_user(driver)
    return co_da_li


comments_user_title_list = test_A008_comment()


def test_A008_control():
    fu02.sign_in(driver, da08.mail_cont, da08.passw_cont)
    cont_da_li = fu02.user_comment_control(driver, da08.com_list_num, da08.com_list, comments_text)
    fu02.out_user(driver)
    return cont_da_li


control_user_title_text_list = test_A008_control()
control_text_list = []
for comment_text in control_user_title_text_list:
    control_text_list.append(comment_text[2])


def test_A008_del():
    fu02.sign_in(driver, da08.mail, da08.passw)
    del_da_li = fu02.user_comment_del(driver, da08.com_list_num, da08.com_list, comments_text)
    fu02.out_close_driver(driver)
    return del_da_li


del_user_title_list = test_A008_del()



# ***************************************************

# normál, önálló futtatáshoz:
if __name__ == "__main__":
    print(comments_text)
    print(comments_user_title_list)
    print(control_user_title_text_list)
    print(control_text_list)
    print(del_user_title_list)
    try:
        assert set(comments_text) == set(control_text_list)
        assert comments_user_title_list == del_user_title_list
    except:
        print("Hiba, az ellenőrző feltételek nem a várt eredményt mutatják.")

