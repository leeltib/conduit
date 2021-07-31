# Test data of test case A004 

name = 'testuser01'
mail = 'tuser01@gmail.com'
passw = 'TestUser01'
title = 'User01-1.1'
what = 'User01 articel-1.1'
write = 'Ez User01 első bejegyzésének módosítása.'
tags = ['birs', "szőlő", 'mandula']
ta_nu = int(len(tags))




def user_comment_control(brow, rn, blog, comment):
    time.sleep(1)
    brow.refresh()
    time.sleep(1)
    data_blogs_cont = []
    for i in range(rn):
        time.sleep(2)
        data_blog_cont = []
        blog_cur = blog[i][0]
        k = blog[i][1]
        comm_cur = comment[k - 1]
        blogs = create_article_link_list(brow)
        blog_num = len(blogs)
        if blog_cur > blog_num:
            print("A megadott sorszám túl nagy!")
        else:
            time.sleep(2)
            blogs[blog_cur - 1].click()
            time.sleep(2)
            try:
                username_cont = blog_commnent_ele_sel(brow, 7).text
                title_cont = blog_commnent_ele_sel(brow, 1).text
                data_blog_cont.append(username_cont)
                data_blog_cont.append(title_cont)
                card_text = comment_p_list(brow)[0].text
                time.sleep(1)
                if card_text == comm_cur:
                    data_blog_cont.append(card_text)
                else:
                    card_text2 = comment_p_list(brow)[-1].text
                    data_blog_cont.append(card_text2)
                data_blogs_cont.append(data_blog_cont)
                time.sleep(1)
                click_menu(brow, 1)
                time.sleep(1)
            except:
                print("Nincs komment ehhez a bejegyzéshez.")
    click_menu(brow, 1)
    time.sleep(2)
    return data_blogs_cont
