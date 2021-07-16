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

# sign_in -> belépés email és jelszó megadásával
def sign_in(brow, mail, passw):
    try:
        brow.find_element_by_xpath('//div[@id="cookie-policy-panel"]/div/div[2]/button[1]/div').click()
    except:
        print("Nincs cookie.")
    brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[2]/a').click()
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

# blog írás, ellenőrzés (hogy létrejött-e az új bejegyzés)
# induló és záró állapot: belépve, "Home" menü aktív
def blog_write(brow, da):
    wait(brow, By.XPATH, '//div[@id="app"]/nav/div/ul/li[2]/a')
    time.sleep(2)
    brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[2]/a').click()
    wait(brow, By.XPATH, '//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
    time.sleep(2)
    input1 = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
    input1.send_keys(da.title)
    input2 = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
    input2.send_keys(da.what)
    input3 = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
    input3.send_keys(da.write)
    for i in range(da.ta_nu):
        input4 = brow.find_element_by_xpath(f'//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[{i + 1}]/input')
        input4.send_keys(da.tags[i])
        input4.send_keys(Keys.ENTER)
        time.sleep(1)
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
    brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[4]/a').click()
    wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/h1')
    brow.refresh()
    time.sleep(2)
    my_art_title = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/h1').text
    print(my_art_title)
    try:
        assert my_art_title == da.title
    except:
        print('A "title" paraméter nem egyezik.')
    my_art_what = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/p').text
    print(my_art_what)
    try:
        assert my_art_what == da.what
    except:
        print('A "what" paraméter nem egyezik.')
    brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[1]/a').click()
    wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/p')
    time.sleep(2)
    brow.refresh()
    return write_cont

# meglévő blog módosítása, ellenőrzés  (hogy változott-e az eredeti bejegyzés)
# induló és záró állapot: belépve, "Home" menü aktív
def blog_edit(brow, da):
    wait(brow, By.XPATH, '//div[@id="app"]/nav/div/ul/li[4]/a')
    time.sleep(2)
    brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[4]/a').click()
    wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/span')
    brow.refresh()
    time.sleep(5)
    try:
        brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/h1').click()
        wait(brow, By.XPATH, '//div[@id="app"]/div/div[1]/div/div/span/a/span')
        time.sleep(1)
        brow.find_element_by_xpath('//div[@id="app"]/div/div[1]/div/div/span/a/span').click()
        wait(brow, By.XPATH, '//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
        time.sleep(1)
        input1 = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
        input1.clear()
        input1.send_keys(da.title)
        input2 = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
        input2.clear()
        input2.send_keys(da.what)
        input3 = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
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
        brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/button').click()
        wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div[1]/div/div[1]/p')
        time.sleep(3)
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
        brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[4]/a').click()
        wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/h1')
        brow.refresh()
        time.sleep(2)
        my_art_title = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/h1').text
        print(my_art_title)
        my_art_what = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/p').text
        print(my_art_what)
        time.sleep(1)
        try:
            assert my_art_title == da.title
            assert my_art_what == da.what
        except:
            print('A "title" vagy a "what" paraméter nem egyezik.')
        brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[1]/a').click()
        wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/p')
        time.sleep(2)
        brow.refresh()
        return write_cont
    except:
        print("Nincs módosítható bejegyzés.")

# bejegyzés törlése -> induló és záró állapot: belépve, "Home" menü aktív
# a legfelső bejegyzést törli, ellenőrzi, hogy valóban törlődik a bejegyzés
def blog_del(brow):
    del_list = []
    wait(brow, By.XPATH, '//div[@id="app"]/nav/div/ul/li[4]/a')
    time.sleep(2)
    brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[4]/a').click()
    wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/p')
    time.sleep(4)
    try:
        blog_del_what = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/p').text
        print(blog_del_what)
        del_list.append(blog_del_what)
        brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/h1').click()
        wait(brow, By.XPATH, '//div[@id="app"]/div/div[1]/div/div/span/button/span')
        time.sleep(1)
        brow.find_element_by_xpath('//div[@id="app"]/div/div[1]/div/div/span/button/span').click()
        wait(brow, By.XPATH, '//div[@id="app"]/nav/div/ul/li[4]/a')
        time.sleep(1)
        brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[4]/a').click()
        wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/p')
        brow.refresh()
        time.sleep(3)
        try:
            blog_stay_what = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/p').text
            print(blog_stay_what)
            del_list.append(blog_stay_what)
            try:
                assert blog_del_what != blog_stay_what
            except:
                print("Hiba a törlésnél, a bejegyzés megmaradt.")
        except:
            del_list.append('None')
            print("Nincs több bejegyzés a My Articles mappában.")
        brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[1]/a').click()
        wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div[2]/div/p')
        time.sleep(2)
        brow.refresh()
        return del_list
    except:
        print("Nincs módosítható bejegyzés.")

# kilépés
def out_user(brow):
    brow.refresh()
    time.sleep(2)
    brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[5]/a').click()
    time.sleep(1)

# kilépés és driver bezárás
def out_close_driver(brow):
    brow.refresh()
    time.sleep(2)
    brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[5]/a').click()
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
        #print(tb_list_el)
        tb_list.append(tb_list_el)
        brow.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[1]/a').click()
        time.sleep(2)
    print(tb_list)
    return tb_list

