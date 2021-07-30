# A010 test case -  regisztrációs űrlap mezőinek validálása
# A teszthez random generálással készülnek a tesztadatok (data_tcA010.py)

import data.data_tcA010 as da10
import func.func_01 as fu01

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("http://localhost:1667")

# Várakozás a betöltésre
fu01.wait(driver, By.ID, "app", 1)


# *** TC-A010 **************************************


def test_A010_sign_up_valid(users):
    valid_data = []
    for user in users:
        time.sleep(1)
        fu01.cookie_ok(driver)
        fu01.sign_up(driver, user[0], user[1], user[2])
        result_test = fu01.registr_check_a010(driver)
        valid_data.append(result_test)
    fu01.close_driver(driver)
    return valid_data


expect_valid = ['OK', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL']

sign_up_valid_list = test_A010_sign_up_valid(da10.users)


def test_comment_text_list(val):
    comm_ok_full_list = []
    elements = val.split('//')
    for element in elements:
        list_elem = element.replace("\n", "")
        comm_ok_full_list.append(list_elem)
    return comm_ok_full_list


print_ok = test_comment_text_list(da10.comment_ok)
print_error = test_comment_text_list(da10.comment_error)

try:
    assert len(expect_valid) == len(sign_up_valid_list)
    rn = len(sign_up_valid_list)
    for i in range(rn):
        if expect_valid[i] == sign_up_valid_list[i]:
            print(print_ok[i])
        else:
            print(print_error[i])
except:
    print('Error. Az "expect_valid" és a "sign_up_valid_list" listák elemszáma nem azonos!')


# ***************************************************
# normál futtatáshoz:
if __name__ == "__main__":
    print(expect_valid)
    print(sign_up_valid_list)
    try:
        assert expect_valid == sign_up_valid_list
    except:
        print("A beviteli mezők validálása közben nem kaptuk mindenhol az elvárt eredményt.")

