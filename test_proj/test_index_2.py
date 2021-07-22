# Tesztek listája, futtatása pytest keretrendszerben
# (venv) C:\ukautom\t360\kurzus\pycharm\conduit\test_proj>
# pytest test_index_2.py --alluredir=./out
# allure serve ./out

import time
time.sleep(10)

# tcA001_run = A001 test case -  Új felhasználó regisztrációja felhasználó név, email cím és jelszó megadásával.
tcA001_run = True
# tcA002_run = A002 test case - Belépés a regisztráció során megadott adatokkal - kilépés.
tcA002_run = False
# tcA003_run = A003 test case - Új blogbejegyzés készítése - kilépés.
tcA003_run = False
# tcA004_run = A004 test case - Saját, meglévő blogbejegyzés módosítása - kilépés.
tcA004_run = False
# tcA005_run = A005 test case - Saját, meglévő blogbejegyzés törlése - kilépés.
tcA005_run = False
# tcA006_run = A006 test case - Tags funkció tesztelése (listázással)
tcA006_run = True
# tcA007_run = A007 test case - User select funkció -> a kiválasztott user bejegyzéseinek kiírása egy text fájlba
tcA007_run = False
# tcA008_run = A008 test case - Comment funkció -> kiválasztható bejegyzések kommentelése, ellenörzés, törlés
tcA008_run = False


if tcA001_run == True:
    def test_t_case001():
        import test_tcA001 as tc01
        assert tc01.list_username == tc01.user_menu_text
else:
    print("Az A001 teszteset vizsgálata ki van kapcsolva!")

if tcA002_run == True:
    time.sleep(5)
    def test_t_case002():
        import test_tcA002 as tc02
        import data.data_tcA002 as da02
        assert da02.name == tc02.username_text
else:
    print("Az A002 teszteset vizsgálata ki van kapcsolva!")

if tcA003_run == True:
    def test_t_case003():
        time.sleep(5)
        import test_tcA003 as tc03
        import data.data_tcA003 as da03
        assert da03.write == tc03.write_add_text
else:
    print("Az A003 teszteset vizsgálata ki van kapcsolva!")

if tcA004_run == True:
    def test_t_case004():
        time.sleep(5)
        import test_tcA004 as tc04
        import data.data_tcA004 as da04
        assert da04.write == tc04.write_edit_text
else:
    print("Az A004 teszteset vizsgálata ki van kapcsolva!")

if tcA005_run == True:
    def test_t_case005():
        time.sleep(5)
        import test_tcA005 as tc05
        assert tc05.what_text[0] != tc05.what_text[1]
else:
    print("Az A005 teszteset vizsgálata ki van kapcsolva!")

if tcA006_run == True:
    def test_t_case006():
        time.sleep(5)
        import test_tcA006 as tc06
        assert tc06.tags_basis == tc06.tags_del
        assert tc06.tags_basis != tc06.tags_add
else:
    print("Az A006 teszteset vizsgálata ki van kapcsolva!")

if tcA007_run == True:
    def test_t_case007():
        time.sleep(5)
        import test_tcA007 as tc07
        assert tc07.user_blog_num1 == tc07.user_blog_num2
else:
    print("Az A007 teszteset vizsgálata ki van kapcsolva!")

if tcA008_run == True:
    def test_t_case008():
        time.sleep(5)
        import test_tcA008 as tc08
        assert tc08.comments_text == tc08.control_text_list
        assert tc08.comments_user_title_list == tc08.del_user_title_list
else:
    print("Az A008 teszteset vizsgálata ki van kapcsolva!")
