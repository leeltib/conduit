from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time


# várakozás a betöltésre
def wait(brow, by, attr):
    try:
        WebDriverWait(brow, 30).until(EC.presence_of_element_located((by, attr)))
    except TimeoutException:
        print("Loading took too much time!-Try again")


# menüpont kiválasztása
def click_menu(brow, i):
    menu_full = brow.find_elements_by_class_name('nav-item')
    menu_full[i-1].click()


# My Articles -> bejegyzés kiválasztása
def click_my_blog(brow, i):
    my_blogs = brow.find_elements_by_class_name('article-preview')
    my_blog = my_blogs[i].find_element_by_tag_name('h1')
    my_blog.click()


# My Articles -> bejegyzés h1 elemének szövege
def text_my_blog(brow, i, tagname):
    my_blogs = brow.find_elements_by_class_name('article-preview')
    my_bl_text = my_blogs[i].find_element_by_tag_name(tagname).text
    return my_bl_text


# New Article -> új bejegyzés beviteli mezői
def new_art_inp(brow, i, tagname):
    art_inputs = brow.find_elements_by_class_name('form-group')
    art_inp = art_inputs[i].find_element_by_tag_name(tagname)
    return art_inp


# Sign up -> regisztrálás: regisztrációs űrlap kitöltése (username, email, password), belépés
def sign_up(brow, uname, mail, passw):
    try:
        brow.find_element_by_xpath('//div[@id="cookie-policy-panel"]/div/div[2]/button[1]/div').click()
    except:
        print("Nincs cookie.")
    brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[3]/a').click()
    wait(brow, By.XPATH, '//div[@id="app"]/div/div/div/div/form/fieldset[1]/input')
    time.sleep(1)
    username = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset[1]/input')
    email = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset[2]/input')
    password = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset[3]/input')
    sign_up_button = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/button')
    username.send_keys(uname)
    email.send_keys(mail)
    password.send_keys(passw)
    sign_up_button.click()
    time.sleep(1)


# Regisztráció belépés utáni fázisai: welcome OK, username megjelenésének ellenőrzése
def registr_check(brow):
    wait(brow, By.XPATH, "/html/body/div[2]/div/div[4]/div/button")
    time.sleep(1)
    try:
        welcome_button = brow.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
        welcome_button.click()
        wait(brow, By.XPATH, '//div[@id="app"]/nav/div/ul/li[4]/a')
        time.sleep(1)
        usern_text = brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[4]/a').text
        print(usern_text)
        wait(brow, By.XPATH, '//div[@id="app"]/nav/div/ul/li[5]/a')
        time.sleep(2)
        brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[5]/a').click()
        return usern_text
    except:
        print("Ez a felhasználó már létezik.")


# sign_in -> belépés email és jelszó megadásával
def sign_in(brow, mail, passw):
    try:
        brow.find_element_by_xpath('//div[@id="cookie-policy-panel"]/div/div[2]/button[1]/div').click()
    except:
        print("Nincs cookie.")
    click_menu(brow, 2)
    wait(brow, By.XPATH, '//div[@id="app"]/div/div/div/div/form/fieldset[1]/input')
    email = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset[1]/input')
    password = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset[2]/input')
    sign_in_button = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/button')
    email.send_keys(mail)
    password.send_keys(passw)
    sign_in_button.click()


# username (megjelenésének) ellenőrzése
# induló és záró állapot: belépve, "Home" menü aktív
def login_check(brow):
    wait(brow, By.XPATH, '//div[@id="app"]/nav/div/ul/li[4]/a')
    time.sleep(1)
    try:
        usern_text = brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[4]/a').text
        time.sleep(1)
        print(usern_text)
        return usern_text
    except:
        print("Hibás belépési adatok, nincs ilyen felhasználó.")


# ------------------------------------------------------------------------------------------
# blog írás, ellenőrzés (hogy létrejött-e az új bejegyzés)
# induló és záró állapot: belépve, "Home" menü aktív

# Bejegyzés létrejöttének és tartalmának ellenőrzése
def control_blog_write_edit(brow, da):
    brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/button').click()
    wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div[1]/div/div[1]/p')
    time.sleep(2)
    write_cont = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[1]/div/div[1]/p').text
    print(write_cont)
    tags = brow.find_elements_by_xpath('//div[@class="tag-list"]//a')
    tags_text = []
    for tag in tags:
        tag_cont = tag.text
        print(tag_cont)
        tags_text.append(tag_cont)
    try:
        assert tags_text == da.tags
    except:
        print('A "tags" paraméter nem egyezik.')
    click_menu(brow, 4)
    wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/h1')
    time.sleep(2)
    my_art_title = text_my_blog(brow, -1, 'h1')
    print(my_art_title)
    try:
        assert my_art_title == da.title
    except:
        print('A "title" paraméter nem egyezik.')
    my_art_what = text_my_blog(brow, -1, 'p')
    print(my_art_what)
    try:
        assert my_art_what == da.what
    except:
        print('A "what" paraméter nem egyezik.')
    return write_cont


# új bejegyzés létrehozása
def blog_write(brow, da):
    wait(brow, By.XPATH, '//div[@id="app"]/nav/div/ul/li[2]/a')
    time.sleep(2)
    click_menu(brow, 2)
    wait(brow, By.XPATH, '//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
    time.sleep(2)
    input1 = new_art_inp(brow, 0, 'input')
    input1.send_keys(da.title)
    input2 = new_art_inp(brow, 1, 'input')
    input2.send_keys(da.what)
    input3 = new_art_inp(brow, 2, 'textarea')
    input3.send_keys(da.write)
    for i in range(da.ta_nu):
        input4 = brow.find_element_by_xpath(f'//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[{i + 1}]/input')
        input4.send_keys(da.tags[i])
        input4.send_keys(Keys.ENTER)
        time.sleep(1)
    # ellenórzés, lezárás
    wri_contr = control_blog_write_edit(brow, da)
    click_menu(brow, 1)
    wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/p')
    brow.refresh()
    time.sleep(2)
    return wri_contr


# ------------------------------------------------------------------------------------------
# meglévő blog módosítása, ellenőrzés  (hogy változott-e az eredeti bejegyzés)
# induló és záró állapot: belépve, "Home" menü aktív

def blog_edit(brow, da):
    wait(brow, By.XPATH, '//div[@id="app"]/nav/div/ul/li[4]/a')
    time.sleep(2)
    click_menu(brow, 4)
    wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/span')
    time.sleep(4)
    try:
        click_my_blog(brow, -1)
        wait(brow, By.XPATH, '//div[@id="app"]/div/div[1]/div/div/span/a/span')
        time.sleep(1)
        brow.find_element_by_xpath('//div[@id="app"]/div/div[1]/div/div/span/a/span').click()
        wait(brow, By.XPATH, '//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
        time.sleep(1)
        input1 = new_art_inp(brow, 0, 'input')
        input1.clear()
        input1.send_keys(da.title)
        input2 = new_art_inp(brow, 1, 'input')
        input2.clear()
        input2.send_keys(da.what)
        input3 = new_art_inp(brow, 2, 'textarea')
        input3.clear()
        input3.send_keys(da.write)
        time.sleep(1)
        tags_num = int(len(brow.find_elements_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li')))
        for i in range(tags_num-1):
            brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[1]/div[2]/i[2]').click()
            time.sleep(2)
        for i in range(da.ta_nu):
            input4 = brow.find_element_by_xpath(f'//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[{i + 1}]/input')
            input4.send_keys(da.tags[i])
            input4.send_keys(Keys.ENTER)
            time.sleep(1)
        # ellenórzés, lezárás
        wri_con = control_blog_write_edit(brow, da)
        click_menu(brow, 1)
        wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/p')
        brow.refresh()
        time.sleep(2)
        return wri_con
    except:
        print("Nincs módosítható bejegyzés.")


# ------------------------------------------------------------------------------------------
# bejegyzés törlése -> induló és záró állapot: belépve, "Home" menü aktív
# a legfelső bejegyzést törli, ellenőrzi, hogy valóban törlődik a bejegyzés

def blog_del(brow):
    del_list = []
    wait(brow, By.XPATH, '//div[@id="app"]/nav/div/ul/li[4]/a')
    time.sleep(2)
    click_menu(brow, 4)
    wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/p')
    time.sleep(4)
    try:
        blog_del_what = text_my_blog(brow, -1, 'p')
        print(blog_del_what)
        del_list.append(blog_del_what)
        click_my_blog(brow, -1)
        wait(brow, By.XPATH, '//div[@id="app"]/div/div[1]/div/div/span/button/span')
        time.sleep(1)
        brow.find_element_by_xpath('//div[@id="app"]/div/div[1]/div/div/span/button/span').click()
        wait(brow, By.XPATH, '//div[@id="app"]/nav/div/ul/li[4]/a')
        time.sleep(1)
        # ellenórzés, lezárás
        click_menu(brow, 4)
        wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/p')
        brow.refresh()
        time.sleep(3)
        try:
            blog_stay_what = text_my_blog(brow, -1, 'p')
            print(blog_stay_what)
            del_list.append(blog_stay_what)
            try:
                assert blog_del_what != blog_stay_what
            except:
                print("Hiba a törlésnél, a bejegyzés megmaradt.")
        except:
            del_list.append('None')
            print("Nincs több bejegyzés a My Articles mappában.")
        click_menu(brow, 1)
        wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/p')
        brow.refresh()
        time.sleep(2)
        return del_list
    except:
        print("Nincs módosítható bejegyzés.")


# ------------------------------------------------------------------------------------------

# kilépés
def out_user(brow):
    brow.refresh()
    time.sleep(2)
    click_menu(brow, 5)
    time.sleep(1)


# kilépés és driver bezárás
def out_close_driver(brow):
    brow.refresh()
    time.sleep(2)
    click_menu(brow, 5)
    time.sleep(1)
    brow.close()


# driver bezárás
def close_driver(brow):
    time.sleep(2)
    brow.close()


# tag elemek száma, az egyes tag-ekhez tartozó bejegyzések száma (listázás)
def tags_list(brow):
    wait(brow, By.XPATH, '//div[@class="tag-list"]')
    time.sleep(2)
    tags_bas = brow.find_elements_by_xpath('//div[@id="app"]/div/div[2]/div/div[2]/div/div//a')
    tb_num = len(tags_bas)
    print(f'{tb_num} tag van az alkalmazásban.')
    tb_list = []
    for i in range(tb_num):
        wait(brow, By.XPATH, '//div[@class="tag-list"]')
        time.sleep(1)
        tb_list_el = []
        tb_list_el.append(tags_bas[i].text)
        tags_bas[i].click()
        wait(brow, By.XPATH, '//div[@class="article-preview"]')
        time.sleep(1)
        tb_list_el.append(len(brow.find_elements_by_class_name('article-preview')))
        tb_list.append(tb_list_el)
        click_menu(brow, 1)
        time.sleep(1)
    return tb_list



