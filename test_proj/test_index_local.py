# Tesztek listája, futtatása localhoston, pytest keretrendszerben
# (venv) C:\ukautom\t360\kurzus\pycharm\conduit\test_proj>
# pytest test_index_local.py --alluredir=./out
# allure serve ./out

import time


def time_sl():
    time.sleep(5)


# tcA001_run = A001 test case - New user registration with user name, email and password
tcA001_run = True
# tcA002_run = A002 test case - Login in with new user data - exit
tcA002_run = True
# tcA003_run = A003 test case - New blog post  - exit
tcA003_run = True
# tcA004_run = A004 test case - Modifying existing blogpost - exit
tcA004_run = True
# tcA005_run = A005 test case - Deleting own blogpost - exit
tcA005_run = True
# tcA006_run = A006 test case - Testing Tags function (by listing)
tcA006_run = True
# tcA007_run = A007 test case - User select function -> write selected user's posts to text file
tcA007_run = True
# tcA008_run = A008 test case - Comment function -> commenting, checking and deleting of seleced posts
tcA008_run = True
# tcA009_run = A009 test case - Scrolling function -> displaying 10 blogs simultaneously 
tcA009_run = True
# tcA010_run = A010 test case - Validating registration form fields
tcA010_run = True
# tcA011_run = A011 test case - Testing Cookie function
tcA011_run = True


print("RUN TEST CASES:")
not_run = []

if tcA001_run == True:
    print("  A001 test case - New user registration with user name, email and password")
    time_sl()

    def test_t_case001():
        import test_tcA001 as tc01
        assert tc01.list_username == tc01.user_menu_text
else:
    not_run.append("  A001 test case - New user registration with user name, email and password")


if tcA002_run == True:
    print("  A002 test case - Login in with new user data.")
    time_sl()

    def test_t_case002():
        import test_tcA002 as tc02
        import data.data_tcA002 as da02
        assert da02.name == tc02.username_text
else:
    not_run.append("  A002 test case - Login in with new user data.")


if tcA003_run == True:
    print("  A003 test case - New blog post.")
    time_sl()

    def test_t_case003():
        import test_tcA003 as tc03
        import data.data_tcA003 as da03
        assert da03.write == tc03.write_add_text
else:
    not_run.append("  A003 test case - New blog post.")


if tcA004_run == True:
    print("  A004 test case - Modifying existing blogpost.")
    time_sl()

    def test_t_case004():
        import test_tcA004 as tc04
        import data.data_tcA004 as da04
        assert da04.write == tc04.write_edit_text
else:
    not_run.append("  A004 test case - Modifying existing blogpost.")


if tcA005_run == True:
    print("  A005 test case - Deleting own blogpost.")
    time_sl()

    def test_t_case005():
        import test_tcA005 as tc05
        assert tc05.what_text[0] != tc05.what_text[1]
else:
    not_run.append("  A005 test case - Deleting own blogpost.")


if tcA006_run == True:
    print("  A006 test case - Testing Tags function (by listing)")
    time_sl()

    def test_t_case006():
        import test_tcA006 as tc06
        assert tc06.tags_basis == tc06.tags_del
        assert tc06.tags_basis != tc06.tags_add
else:
    not_run.append("  A006 test case - Testing Tags function (by listing)")


if tcA007_run == True:
    print("  A007 test case - User select function -> write selected user's posts to text file")
    time_sl()

    def test_t_case007():
        import test_tcA007 as tc07
        user_blog_num2 = tc07.test_A007_write()
        assert tc07.user_blog_num1 == user_blog_num2
else:
    not_run.append("  A007 test case - User select function -> write selected user's posts to text file")


if tcA008_run == True:
    print("  A008 test case - Comment function -> commenting, checking and deleting of selected posts")
    time_sl()

    def test_t_case008():
        import test_tcA008 as tc08
        assert tc08.comments_text_set == tc08.control_text_list_set
        assert tc08.comments_user_title_list == tc08.del_user_title_list
else:
    not_run.append("  A008 test case - Comment function -> commenting, checking and deleting of selected posts")


if tcA009_run == True:
    print("  A009 test case - Scrolling function -> displaying 10 blogs simultaneously")
    time_sl()

    def test_t_case009():
        import test_tcA009 as tc09
        assert tc09.pages_blog_num == 10
else:
    not_run.append("  A009 test case - Scrolling function -> displaying 10 blogs simultaneously")


if tcA010_run == True:
    print("  A010 test case - Validating registration form fields.")
    time_sl()

    def test_t_case010():
        import test_tcA010 as tc10
        assert tc10.expect_valid == tc10.sign_up_valid_list
else:
    not_run.append("  A010 test case - Validating registration form fields.")


if tcA011_run == True:
    print("  A011 test case - Testing Cookie function.")
    time_sl()

    def test_t_case011():
        import test_tcA011 as tc11
        assert tc11.cookie_valid_dec == tc11.expect_valid_dec
        assert tc11.cookie_valid_acc == tc11.expect_valid_acc
else:
    not_run.append("  A011 test case - Testing Cookie function.")


# -------------------------------------------------------------------------------

print('-' * 80)
print("TEST CASES NOT RUN:")
for test_case in not_run:
    print(test_case)



