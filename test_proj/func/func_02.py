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


# User kiválasztása -> a bejegyzés szerzője szerinti szűrés
# lapozás nincs -> az első oldalon szerepelnie kell a kiválasztott blogírónak
def select_user(brow, username):
    wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div')
    time.sleep(2)
    users = brow.find_elements_by_class_name('info')
    #print(users)
    for user in users:
        user_link = user.find_element_by_tag_name('a')
        user_name = user_link.text
        if user_name == username:
            user_link.click()
            break
        elif user_name != username and user != users[-1]:
            continue
        else:
            print("A megadott felhasználónév nem jó.")
    wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]')
    brow.refresh()
    time.sleep(3)
    user_blog_num = len(brow.find_elements_by_class_name('article-preview'))
    print(user_blog_num, "blogbejegyzés")
    return user_blog_num


def user_read(brow, rn):
    blogs_text = []
    for i in range(rn):
        blogs = brow.find_elements_by_class_name('article-preview')
        time.sleep(1)
        blogs[i].find_element_by_tag_name('h1').click()
        time.sleep(2)
        blog_text = []
        blog_title = brow.find_element_by_xpath('//div[@id="app"]/div/div[1]/div/h1').text
        blog_p = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[1]/div/div[1]/p').text
        time.sleep(1)
        blog_text.append(blog_title)
        blog_text.append(blog_p)
        blogs_text.append(blog_text)
        brow.back()
        time.sleep(1)
    click_menu(brow, 1)
    time.sleep(1)
    brow.refresh()
    print(blogs_text)
    return blogs_text


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


# komment írás
def user_comment(brow, rn, blog, comment):
    time.sleep(1)
    brow.refresh()
    time.sleep(1)
    data_blogs = []
    for i in range(rn):
        time.sleep(2)
        data_blog = []
        blog_cur = blog[i][0]
        comm_cur = comment[i]
        blogs = brow.find_elements_by_class_name('article-preview')
        users = brow.find_elements_by_class_name('info')
        blog_num = len(blogs)
        if blog_cur > blog_num:
            print("A megadott sorszám túl nagy!")
        else:
            time.sleep(2)
            blog_selected = blogs[blog_cur-1].find_element_by_tag_name('h1')
            blog_title = blog_selected.text
            username = users[blog_cur-1].find_element_by_tag_name('a').text
            #print(blog_title)
            #print(username)
            data_blog.append(username)
            data_blog.append(blog_title)
            data_blogs.append(data_blog)
            blog_selected.click()
            time.sleep(2)
            write_input = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[2]/div/div/form/div[1]/textarea')
            post_button = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[2]/div/div[1]/form/div[2]/button')
            write_input.clear()
            write_input.send_keys(comm_cur)
            time.sleep(1)
            post_button.click()
            time.sleep(1)
            click_menu(brow, 1)
            time.sleep(1)
    click_menu(brow, 1)
    time.sleep(2)
    #print(data_blogs)
    return data_blogs



# komment funkció ellenőrzése
# belépés egy másik felhasználóval -> ellenőrzés, hogy a user_comment() függvénnyel előzőleg létrehozott hozzászólások látszanak-e
def user_comment_control(brow, rn, blog, comment):
    time.sleep(1)
    brow.refresh()
    time.sleep(1)
    data_blogs_cont = []
    for i in range(rn):
        time.sleep(2)
        data_blog_cont = []
        blog_cur = blog[i][0]
        comm_cur = comment[i]
        blogs = brow.find_elements_by_class_name('article-preview')
        blog_num = len(blogs)
        if blog_cur > blog_num:
            print("A megadott sorszám túl nagy!")
        else:
            time.sleep(2)
            blog_selected = blogs[blog_cur-1].find_element_by_tag_name('h1')
            blog_selected.click()
            time.sleep(2)
            user = brow.find_element_by_class_name('info')
            username_cont = user.find_element_by_tag_name('a').text
            title = brow.find_element_by_class_name('banner')
            title_cont = title.find_element_by_tag_name('h1').text
            #print(username_cont)
            #print(title_cont)
            data_blog_cont.append(username_cont)
            data_blog_cont.append(title_cont)
            cards = brow.find_elements_by_class_name('card')
            card_text = cards[1].find_element_by_tag_name('p').text
            time.sleep(1)
            if card_text == comm_cur:
                #print(card_text)
                data_blog_cont.append(card_text)
            else:
                card_text2 = cards[-1].find_element_by_tag_name('p').text
                #print(card_text2)
                data_blog_cont.append(card_text2)
            data_blog_cont.append(card_text)
            data_blogs_cont.append(data_blog_cont)
            time.sleep(1)
            click_menu(brow, 1)
            time.sleep(1)
    click_menu(brow, 1)
    time.sleep(2)
    return data_blogs_cont



# komment törlése (az utoljára létrehozott kommentet töröljük)
def user_comment_del(brow, rn, blog, comment):
    time.sleep(1)
    brow.refresh()
    time.sleep(1)
    data_blogs_del = []
    for i in range(rn):
        time.sleep(2)
        data_blog_del = []
        blog_cur = blog[i][0]
        comm_cur = comment[i]
        blogs = brow.find_elements_by_class_name('article-preview')
        blog_num = len(blogs)
        if blog_cur > blog_num:
            print("A megadott sorszám túl nagy!")
        else:
            time.sleep(2)
            blog_selected = blogs[blog_cur-1].find_element_by_tag_name('h1')
            blog_selected.click()
            time.sleep(2)
            user = brow.find_element_by_class_name('info')
            username_del = user.find_element_by_tag_name('a').text
            title = brow.find_element_by_class_name('banner')
            title_del = title.find_element_by_tag_name('h1').text
            #print(username_del)
            #print(title_del)
            data_blog_del.append(username_del)
            data_blog_del.append(title_del)
            cards = brow.find_elements_by_class_name('card')
            elements1 = len(cards)
            card_text = cards[1].find_element_by_tag_name('p').text
            if card_text == comm_cur:
                button_del = cards[1].find_element_by_class_name('ion-trash-a')
                button_del.click()
            else:
                button_del2 = cards[-1].find_element_by_class_name('ion-trash-a')
                button_del2.click()
            time.sleep(2)
            cards2 = brow.find_elements_by_class_name('card')
            elements2 = len(cards2)
            try:
                assert elements1 > elements2
            except:
                print("A bejegyzés törlése sikertelen!")
            data_blogs_del.append(data_blog_del)
            time.sleep(1)
            click_menu(brow, 1)
            time.sleep(1)
    click_menu(brow, 1)
    time.sleep(2)
    return data_blogs_del


