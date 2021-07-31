# A008 - comment function
# Blog author and blog can be set 
# Comment text is read from external file

import data.data_tcA008 as da08
import func.func_01 as fu01

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("http://localhost:1667")

# Wait for loading
fu01.wait(driver, By.ID, "app", 2)

# *** TC-A008 **************************************


def test_comment_text():
    comm_full_list = []
    for element in da08.comment_full:
        el1 = element.strip()
        el2 = el1.replace("\n", " ")
        comm_full_list.append(el2)
    return comm_full_list


comments_text = test_comment_text()
comments_text_set = set(comments_text)


def test_A008_comment():
    fu01.cookie_ok(driver)
    fu01.sign_in(driver, da08.mail, da08.passw)
    co_da_li = fu01.user_comment(driver, da08.com_list_num, da08.com_list, comments_text)
    fu01.out_user(driver)
    return co_da_li


comments_user_title_list = test_A008_comment()


def test_A008_control():
    fu01.cookie_ok(driver)
    fu01.sign_in(driver, da08.mail_cont, da08.passw_cont)
    cont_da_li = fu01.user_comment_control(driver, da08.com_list_num, da08.com_list, comments_text)
    fu01.out_user(driver)
    return cont_da_li


control_user_title_text_list = test_A008_control()
control_text_list = []
for comment_text in control_user_title_text_list:
    control_text_list.append(comment_text[2])

control_text_list_set = set(control_text_list)


def test_A008_del():
    fu01.cookie_ok(driver)
    fu01.sign_in(driver, da08.mail, da08.passw)
    del_da_li = fu01.user_comment_del(driver, da08.com_list_num, da08.com_list, comments_text)
    fu01.out_close_driver(driver)
    return del_da_li


del_user_title_list = test_A008_del()



# ***************************************************

# Normal, automatic run
if __name__ == "__main__":
    print(comments_text)
    print(comments_text_set)
    print(comments_user_title_list)
    print(control_user_title_text_list)
    print(control_text_list)
    print(control_text_list_set)
    print(del_user_title_list)
    try:
        assert comments_text_set == control_text_list_set
        assert comments_user_title_list == del_user_title_list
    except:
        print("Hiba, az ellenőrző feltételek nem a várt eredményt mutatják.")



