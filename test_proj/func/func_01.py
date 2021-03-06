from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time


# Wait for loading
def wait(brow, by, attr, sleep_s):
    try:
        WebDriverWait(brow, 30).until(EC.presence_of_element_located((by, attr)))
        if sleep_s > 0:
            time.sleep(sleep_s)
    except TimeoutException:
        print("Loading took too much time!-Try again")


# create menu
def menu_create(brow):
    return brow.find_elements_by_class_name('nav-item')


# list articles on current page
def article_list_create(brow):
    return brow.find_elements_by_class_name('article-preview')


# handling Cookies:
def cookie_ok(brow):
    try:
        brow.find_element_by_xpath('//div[@id="cookie-policy-panel"]/div/div[2]/button[1]/div').click()
    except:
        pass


# sign up, sign in entry fields:
def sel_up_input(brow, i):
    up_inputs = brow.find_elements_by_class_name('form-group')
    up_button = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/button')
    up_inputs.append(up_button)
    if i < len(up_inputs):
        up_input = up_inputs[i-1].find_element_by_tag_name('input')
    else:
        up_input = up_inputs[i-1]
    return up_input


# accept Welcome window on succesful registration
def welcome_ok(brow):
    welcome_text = brow.find_element_by_xpath('/html/body/div[2]/div/div[2]').text
    assert welcome_text == "Welcome!"
    welcome_button = brow.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
    welcome_button.click()
    wait(brow, By.XPATH, '//div[@id="app"]/nav/div/ul/li[4]/a', 1)


# accept Registration failed window on failed registration
def reg_failed(brow):
    failed_text = brow.find_element_by_xpath('/html/body/div[2]/div/div[2]').text
    assert failed_text == "Registration failed!"
    failed_button = brow.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
    failed_button.click()
    wait(brow, By.XPATH, '//div[@id="app"]/div/div/div/div/h1', 1)


# wait for the loading of...
wait_sign_up_in = '//div[@id="app"]/div/div/div/div/form/fieldset[1]/input'     # ... login form
wait_registr_check1 = '/html/body/div[2]/div/div[4]/div/button'                 # ... Welcome OK button
wait_registr_check2 = '//div[@id="app"]/nav/div/ul/li[5]/a'                     # ... Log out button
wait_login_check = '//div[@id="app"]/nav/div/ul/li[4]/a'                        # ... user name (menu) 

wait_blog_write1 = '//div[@id="app"]/nav/div/ul/li[2]/a'                                  # ... New Article button
wait_blog_write2 = '//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'     # ... blog edit form 
wait_blog_write3 = '//div[@id="app"]/div/div[2]/div/div[1]/div[1]/ul/li[2]/a'             # ... Home menu

wait_control_blog_write_edit1 = '//div[@id="app"]/div/div[2]/div[1]/div/div[1]/p'                    # ... edit-delete-comment page
wait_control_blog_write_edit2 = '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/h1'        # ... user menu 

wait_blog_edit1_del14 = '//div[@id="app"]/nav/div/ul/li[4]/a'                                  # ... user menu 
wait_blog_edit2_del2 = '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/span'      # ... My Articles 
wait_blog_edit3_del3 = '//div[@id="app"]/div/div[1]/div/div/span/a/span'                       # ... selected item at edit-delet-comment page
wait_blog_edit4 = '//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'           # ... edit form

wait_tags_list12 = '//div[@class="tag-list"]'                                  # ... Popular Tags
wait_tags_list3 = '//div[@class="article-preview"]'                            # ... tagged articles

wait_return_home = '//div[@id="app"]/div/div[2]/div/div[1]/div[1]/ul/li[2]/a'             # ... Home menu
wait_select_user = '//div[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]'


# New Article -> Fields and buttton of new article 
def new_art_inp(brow, i, tagname):
    art_inputs = brow.find_elements_by_class_name('form-group')
    art_button = brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/button')
    art_inputs.append(art_button)
    if i < len(art_inputs):
        art_inp = art_inputs[i - 1].find_element_by_tag_name(tagname)
    else:
        art_inp = art_inputs[i - 1]
    return art_inp


# Write (modify) blog post, fill input fields
def blog_write_input(brow, da, inp_num):
    if inp_num == 1:
        input1 = new_art_inp(brow, 1, 'input')
        input1.clear()
        input1.send_keys(da.title)
    elif inp_num == 2:
        input2 = new_art_inp(brow, 2, 'input')
        input2.clear()
        input2.send_keys(da.what)
    elif inp_num == 3:
        input3 = new_art_inp(brow, 3, 'textarea')
        input3.clear()
        input3.send_keys(da.write)
    else:
        print("A beviteli mez?? azonos??t??sa sikertelen.")


# write blog post, fill tag field
def tag_write(brow, da):
    for i in range(da.ta_nu):
        input4 = brow.find_element_by_xpath(f'//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[{i + 1}]/input')
        input4.send_keys(da.tags[i])
        input4.send_keys(Keys.ENTER)
        time.sleep(1)


# modify blog post, change tags
def tag_edit(brow, da):
    tags_num = int(len(brow.find_elements_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li')))
    for i in range(tags_num - 1):
        brow.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[1]/div[2]/i[2]').click()
        time.sleep(2)
    for i in range(da.ta_nu):
        input4 = brow.find_element_by_xpath(f'//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[{i + 1}]/input')
        input4.send_keys(da.tags[i])
        input4.send_keys(Keys.ENTER)
        time.sleep(1)


# fields of modify-edit-delete-comment page:
# choose Edit Article - Delete Article buttons
def edit_delete_button_sel(brow, i):
    buttons = []
    button_edit = brow.find_element_by_xpath('//div[@id="app"]/div/div[1]/div/div/span/a')
    button_delete = brow.find_element_by_xpath('//div[@id="app"]/div/div[1]/div/div/span/button')
    buttons.append(button_edit)
    buttons.append(button_delete)
    buttons_sel = buttons[i-1]
    return buttons_sel


# choose Write - Tags fields
def edit_write_tags_sel(brow, i):
    wri_tag = []
    write_sel = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[1]/div/div[1]/p')
    tags_sel = brow.find_elements_by_xpath('//div[@class="tag-list"]//a')
    wri_tag.append(write_sel)
    wri_tag.append(tags_sel)
    wri_tag_sel = wri_tag[i-1]
    return wri_tag_sel


# choose Write comment field and Post Comment button
def edit_write_com_postbut_sel(brow, i):
    wcom_postb = []
    wcom_sel = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[2]/div/div/form/div[1]/textarea')
    postb_sel = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[2]/div/div/form/div[2]/button')
    wcom_postb.append(wcom_sel)
    wcom_postb.append(postb_sel)
    wcom_postb_sel = wcom_postb[i-1]
    return wcom_postb_sel


# number of tags, number of tagged posts (list) 
def tags_list(brow):
    wait(brow, By.XPATH, wait_tags_list12, 2)
    tags_bas = brow.find_elements_by_xpath('//div[@id="app"]/div/div[2]/div/div[2]/div/div//a')
    tb_num = len(tags_bas)
    print(f'{tb_num} tag van az alkalmaz??sban.')
    tb_list = []
    for i in range(tb_num):
        wait(brow, By.XPATH, wait_tags_list12, 1)
        tb_list_el = []
        tb_list_el.append(tags_bas[i].text)
        tags_bas[i].click()
        wait(brow, By.XPATH, wait_tags_list3, 1)
        tb_list_el.append(len(brow.find_elements_by_class_name('article-preview')))
        tb_list.append(tb_list_el)
        click_menu(brow, 1)
        time.sleep(1)
    return tb_list


# choose Users-links from Global Fedd list
def select_users_links(brow):
    wait(brow, By.XPATH, '//div[@id="app"]/div/div[2]/div/div[1]/div[1]/ul/li[2]/a', 2)
    users = brow.find_elements_by_class_name('info')
    users_link = []
    for user in users:
        users_link.append(user.find_element_by_tag_name('a'))
    return users_link


# az aktu??lis oldalon tal??lhat?? blogbejegyz??sek h1 elem??nek (kattint??sra) list??ba gy??jt??se
def create_article_link_list(brow):
    article_list = article_list_create(brow)
    article_link_list = []
    for article in article_list:
        article_link_list.append(article.find_element_by_tag_name('h1'))
    return article_link_list


# az aktu??lis oldalon tal??lhat?? blogbejegyz??sek user-linkjeinek list??ba gy??jt??se
def create_article_user_link_list(brow):
    article_user_list = brow.find_elements_by_class_name('info')
    article_user_link_list = []
    for article_user in article_user_list:
        article_user_link_list.append(article_user.find_element_by_tag_name('a'))
    return article_user_link_list


# a Comment lap f?? mez??inek list??ba gy??jt??se:
def blog_commnent_ele_sel(brow, i):
    elements = []
    title_sel = brow.find_element_by_xpath('//div[@id="app"]/div/div[1]/div/h1')
    follow_button = brow.find_element_by_xpath('//div[@id="app"]/div/div[1]/div/div/span/button[1]')
    favorite_button = brow.find_element_by_xpath('//div[@id="app"]/div/div[1]/div/div/span/button[2]')
    write_sel = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[1]/div/div[1]/p')
    write_comm_sel = brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[2]/div/div[1]/form/div[1]/textarea')
    post_button_sel =  brow.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[2]/div/div[1]/form/div[2]/button')
    username_sel = brow.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/a')
    elements.append(title_sel)                # i = 1 -> title sz??veg
    elements.append(follow_button)            # i = 2 -> + Follow ... gomb
    elements.append(favorite_button)          # i = 3 -> Favorite Article gomb
    elements.append(write_sel)                # i = 4 -> blog sz??vege
    elements.append(write_comm_sel)           # i = 5 -> comment sz??veg mez??
    elements.append(post_button_sel)          # i = 6 -> Push Comment gomb
    elements.append(username_sel)             # i = 7 -> Username
    element_sel = elements[i-1]
    return element_sel


# egy megnyitott bloghoz tartoz?? kommentek sz??vegmez??inek list??ja
def comment_p_list(brow):
    cards_list = brow.find_elements_by_class_name('card-text')
    return cards_list


# komment t??rl?? ikonok list??ja
def del_comm_button(brow):
    del_buttons = brow.find_elements_by_class_name('ion-trash-a')
    return del_buttons


# username (megjelen??s??nek) ellen??rz??se
def login_check(brow):
    wait(brow, By.XPATH, wait_login_check, 1)
    try:
        login_failed_text = brow.find_element_by_xpath('/html/body/div[2]/div/div[2]').text
        assert login_failed_text == "Login failed!"
        login_failed_button = brow.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
        login_failed_button.click()
        wait(brow, By.XPATH, '//div[@id="app"]/div/div/div/div/h1', 1)
        print("Hib??s bel??p??si adatok, nincs ilyen felhaszn??l??.")
    except:
        usern_text = sel_menu(brow, 4).text
        time.sleep(1)
        print(usern_text)
        return usern_text


# Cookie kezel??s tesztel??se - decline:
def cookie_valid_decline(brow):
    try:
        brow.find_element_by_xpath('//div[@id="cookie-policy-panel"]/div/div[2]/button[1]/div').click()
        print('"I decline!" click')
        return '"I decline!" click'
    except:
        print("No cookies")
        return "No cookies"


# Cookie kezel??s tesztel??se - accept:
def cookie_valid_accept(brow):
    try:
        brow.find_element_by_xpath('//div[@id="cookie-policy-panel"]/div/div[2]/button[2]/div').click()
        print('"I accept!" click')
        return '"I accept!" click'
    except:
        print("No cookies")
        return "No cookies"


# ****************************************************************************************
# ****************************** "TISZTA" F??GGV??NYEK *************************************


# klikkel??s kiv??lasztott men??pontra
def click_menu(brow, i):
    menu_full = menu_create(brow)
    menu_full[i-1].click()


# men??pont kiv??laszt??sa
def sel_menu(brow, i):
    menu_full = menu_create(brow)
    return menu_full[i-1]


# My Articles -> bejegyz??s kiv??laszt??sa
def click_my_blog(brow, i):
    my_blogs = article_list_create(brow)
    my_blog = my_blogs[i].find_element_by_tag_name('h1')
    my_blog.click()


# My Articles -> kiv??lasztott bejegyz??s elem??nek sz??vege
def text_my_blog(brow, i, tagname):
    my_blogs = article_list_create(brow)
    my_bl_text = my_blogs[i].find_element_by_tag_name(tagname).text
    return my_bl_text


# regisztr??ci??
def sign_up(brow, uname, mail, passw):
    click_menu(brow, 3)
    wait(brow, By.XPATH, wait_sign_up_in, 2)
    sel_up_input(brow, 1).send_keys(uname)
    sel_up_input(brow, 2).send_keys(mail)
    sel_up_input(brow, 3).send_keys(passw)
    sel_up_input(brow, 4).click()
    time.sleep(1)


# Regisztr??ci?? bel??p??s ut??ni f??zisai: welcome OK, username megjelen??s??nek ellen??rz??se
def registr_check(brow):
    wait(brow, By.XPATH, wait_registr_check1, 2)
    try:
        welcome_ok(brow)
        usern_text = sel_menu(brow, 4).text
        print(usern_text)
        wait(brow, By.XPATH, wait_registr_check2, 2)
        click_menu(brow, 5)
        return usern_text
    except:
        reg_failed(brow)
        print("Sikertelen regisztr??ci??.")


# sign_in -> bel??p??s email ??s jelsz?? megad??s??val
def sign_in(brow, mail, passw):
    click_menu(brow, 2)
    wait(brow, By.XPATH, wait_sign_up_in, 1)
    sel_up_input(brow, 1).send_keys(mail)
    sel_up_input(brow, 2).send_keys(passw)
    sel_up_input(brow, 3).click()


# navig??l??s a home menure, friss??t??s, ??jrat??lt??s
def return_home(brow, menu_n=1):
    click_menu(brow, menu_n)
    wait(brow, By.XPATH, wait_blog_write3, 1)
    brow.refresh()
    time.sleep(2)


# kil??p??s
def out_user(brow):
    brow.refresh()
    time.sleep(2)
    click_menu(brow, 5)
    time.sleep(1)


# kil??p??s ??s driver bez??r??s
def out_close_driver(brow):
    time.sleep(2)
    click_menu(brow, 5)
    time.sleep(1)
    brow.close()


# driver bez??r??s
def close_driver(brow):
    time.sleep(2)
    brow.close()


# Bejegyz??s l??trej??tt??nek ??s tartalm??nak ellen??rz??se
def control_blog_write_edit(brow, da):
    new_art_inp(brow, 5, 'button').click()
    wait(brow, By.XPATH, wait_control_blog_write_edit1, 2)
    write_cont = edit_write_tags_sel(brow, 1).text
    print(write_cont)
    tags = edit_write_tags_sel(brow, 2)
    tags_text = []
    for tag in tags:
        tag_cont = tag.text
        print(tag_cont)
        tags_text.append(tag_cont)
    try:
        assert tags_text == da.tags
    except:
        print('A "tags" param??ter nem egyezik.')
    click_menu(brow, 4)
    wait(brow, By.XPATH, wait_control_blog_write_edit2, 2)
    my_art_title = text_my_blog(brow, -1, 'h1')
    print(my_art_title)
    try:
        assert my_art_title == da.title
    except:
        print('A "title" param??ter nem egyezik.')
    my_art_what = text_my_blog(brow, -1, 'p')
    print(my_art_what)
    try:
        assert my_art_what == da.what
    except:
        print('A "what" param??ter nem egyezik.')
    return write_cont


# ??j bejegyz??s l??trehoz??sa / indul?? ??s z??r?? ??llapot: bel??pve, "Home" men?? akt??v
def blog_write(brow, da):
    wait(brow, By.XPATH, wait_blog_write1, 2)
    click_menu(brow, 2)
    wait(brow, By.XPATH, wait_blog_write2, 2)
    blog_write_input(brow, da, 1)
    blog_write_input(brow, da, 2)
    blog_write_input(brow, da, 3)
    tag_write(brow, da)
    # ellen??rz??s, lez??r??s
    wri_contr = control_blog_write_edit(brow, da)
    return_home(brow)
    return wri_contr


# megl??v?? blog bejegyz??s m??dos??t??sa, ellen??rz??s (megv??ltozott-e az eredeti bejegyz??s)
def blog_edit(brow, da):
    wait(brow, By.XPATH, wait_blog_edit1_del14, 2)
    click_menu(brow, 4)
    wait(brow, By.XPATH, wait_blog_edit2_del2, 4)
    try:
        click_my_blog(brow, -1)
        wait(brow, By.XPATH, wait_blog_edit3_del3, 1)
        edit_delete_button_sel(brow, 1).click()
        wait(brow, By.XPATH, wait_blog_edit4, 1)
        blog_write_input(brow, da, 1)
        blog_write_input(brow, da, 2)
        blog_write_input(brow, da, 3)
        time.sleep(1)
        tag_edit(brow, da)
        # ellen??rz??s, lez??r??s
        wri_con = control_blog_write_edit(brow, da)
        return_home(brow)
        return wri_con
    except:
        print("Nincs m??dos??that?? bejegyz??s.")


# ------------------------------------------------------------------------------------------
# bejegyz??s t??rl??se -> indul?? ??s z??r?? ??llapot: bel??pve, "Home" men?? akt??v
# az utols?? bejegyz??st t??rli, ellen??rzi, hogy val??ban t??rl??dik a bejegyz??s

def blog_del(brow):
    del_list = []
    wait(brow, By.XPATH, wait_blog_edit1_del14, 2)
    click_menu(brow, 4)
    wait(brow, By.XPATH, wait_blog_edit2_del2, 4)
    try:
        blog_del_what = text_my_blog(brow, -1, 'p')
        print(blog_del_what)
        del_list.append(blog_del_what)
        click_my_blog(brow, -1)
        wait(brow, By.XPATH, wait_blog_edit3_del3, 1)
        edit_delete_button_sel(brow, 2).click()
        wait(brow, By.XPATH, wait_blog_edit1_del14, 1)
        # ellen??rz??s, lez??r??s
        click_menu(brow, 4)
        wait(brow, By.XPATH, wait_blog_edit2_del2, 3)
        try:
            blog_stay_what = text_my_blog(brow, -1, 'p')
            print(blog_stay_what)
            del_list.append(blog_stay_what)
            try:
                assert blog_del_what != blog_stay_what
            except:
                print("Hiba a t??rl??sn??l, a bejegyz??s megmaradt.")
        except:
            del_list.append('None')
            print("Nincs t??bb bejegyz??s a My Articles mapp??ban.")
        return_home(brow)
        return del_list
    except:
        print("Nincs t??r??lhet?? bejegyz??s.")


# User kiv??laszt??sa -> a bejegyz??s szerz??je szerinti sz??r??s (lapoz??s egyel??re nincs -> az els?? oldalon szerepelnie kell a kiv??lasztott blog??r??nak)
def select_user(brow, username):
    users_link_list = select_users_links(brow)
    for user_link in users_link_list:
        user_name = user_link.text
        if user_name == username:
            user_link.click()
            break
        elif user_name != username and user_link != users_link_list[-1]:
            continue
        else:
            print("A megadott felhaszn??l??n??v nem j??.")
    wait(brow, By.XPATH, wait_select_user, 1)
    brow.refresh()
    time.sleep(3)
    user_blog_num = len(article_list_create(brow))
    print(user_blog_num, "blogbejegyz??s")
    return user_blog_num


def user_read(brow, rn):
    blogs_text = []
    for i in range(rn):
        art_link_list = create_article_link_list(brow)
        time.sleep(1)
        art_link_list[i].click()
        time.sleep(2)
        blog_text = []
        blog_title = blog_commnent_ele_sel(brow, 1).text
        blog_p = blog_commnent_ele_sel(brow, 4).text
        time.sleep(1)
        blog_text.append(blog_title)
        blog_text.append(blog_p)
        blogs_text.append(blog_text)
        brow.back()
        time.sleep(1)
    return_home(brow)
    print(blogs_text)
    return blogs_text


# komment ??r??s
def user_comment(brow, rn, blog, comment):
    time.sleep(1)
    brow.refresh()
    time.sleep(1)
    data_blogs = []
    for i in range(rn):
        time.sleep(2)
        data_blog = []
        blog_cur = blog[i][0]
        k = blog[i][1]
        comm_cur = comment[k-1]
        blogs = create_article_link_list(brow)
        users = create_article_user_link_list(brow)
        blog_num = len(blogs)
        if blog_cur > blog_num:
            print("A megadott sorsz??m t??l nagy!")
        else:
            time.sleep(2)
            blog_title = blogs[blog_cur-1].text
            username = users[blog_cur-1].text
            data_blog.append(username)
            data_blog.append(blog_title)
            data_blogs.append(data_blog)
            blogs[blog_cur - 1].click()
            time.sleep(2)
            write_input = blog_commnent_ele_sel(brow, 5)
            post_button = blog_commnent_ele_sel(brow, 6)
            write_input.clear()
            write_input.send_keys(comm_cur)
            time.sleep(1)
            post_button.click()
            time.sleep(1)
            click_menu(brow, 1)
            time.sleep(1)
    click_menu(brow, 1)
    time.sleep(2)
    return data_blogs


# komment funkci?? ellen??rz??se
# bel??p??s egy m??sik felhaszn??l??val -> ellen??rz??s, hogy a user_comment() f??ggv??nnyel el??z??leg l??trehozott hozz??sz??l??sok l??tszanak-e
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
            print("A megadott sorsz??m t??l nagy!")
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
                print("Nincs komment ehhez a bejegyz??shez.")
    click_menu(brow, 1)
    time.sleep(2)
    return data_blogs_cont


# komment t??rl??se (az utolj??ra l??trehozott kommentet t??r??lj??k)
def user_comment_del(brow, rn, blog, comment):
    time.sleep(1)
    brow.refresh()
    time.sleep(1)
    data_blogs_del = []
    for i in range(rn):
        time.sleep(2)
        data_blog_del = []
        blog_cur = blog[i][0]
        k = blog[i][1]
        comm_cur = comment[k - 1]
        blogs = create_article_link_list(brow)
        blog_num = len(blogs)
        if blog_cur > blog_num:
            print("A megadott sorsz??m t??l nagy!")
        else:
            time.sleep(2)
            blogs[blog_cur-1].click()
            time.sleep(2)
            try:
                username_del = blog_commnent_ele_sel(brow, 7).text
                title_del = blog_commnent_ele_sel(brow, 1).text
                data_blog_del.append(username_del)
                data_blog_del.append(title_del)
                cards = comment_p_list(brow)
                elements1 = len(cards)
                card_text = comment_p_list(brow)[0].text
                if card_text == comm_cur:
                    del_comm_button(brow)[0].click()
                else:
                    del_comm_button(brow)[-1].click()
                time.sleep(2)
                cards2 = comment_p_list(brow)
                elements2 = len(cards2)
                try:
                    assert elements1 > elements2
                except:
                    print("A bejegyz??s t??rl??se sikertelen!")
                data_blogs_del.append(data_blog_del)
                time.sleep(1)
                click_menu(brow, 1)
                time.sleep(1)
            except:
                print("Nincs t??r??lhet?? komment ehhez a bejegyz??shez.")
    click_menu(brow, 1)
    time.sleep(2)
    return data_blogs_del


# Regisztr??ci?? bel??p??s ut??ni f??zisai: welcome OK, username megjelen??s??nek ellen??rz??se
# A009 tesztesethez -> nincs kil??p??s, blogbejegyz??s k??vetkezik
def registr_check_a009(brow):
    wait(brow, By.XPATH, wait_registr_check1, 2)
    try:
        welcome_ok(brow)
        usern_text = sel_menu(brow, 4).text
        wait(brow, By.XPATH, wait_registr_check2, 2)
        click_menu(brow, 1)
        return usern_text
    except:
        reg_failed(brow)
        print("Sikertelen regisztr??ci??.")


# ??j bejegyz??s l??trehoz??sa az A009 teszthez
def blog_write_a009(brow, da):
    wait(brow, By.XPATH, wait_blog_write1, 1)
    click_menu(brow, 2)
    wait(brow, By.XPATH, wait_blog_write2, 1)
    blog_write_input(brow, da, 1)
    new_art_inp(brow, 5, 'button').click()
    wait(brow, By.XPATH, '//div[@id="app"]/nav/div/ul/li[5]/a', 2)
    click_menu(brow, 1)
    time.sleep(1)
    click_menu(brow, 5)
    time.sleep(2)


def blog_num_check(brow):
    wait(brow, By.XPATH, wait_login_check, 1)
    try:
        login_failed_text = brow.find_element_by_xpath('/html/body/div[2]/div/div[2]').text
        assert login_failed_text == "Login failed!"
        login_failed_button = brow.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
        login_failed_button.click()
        wait(brow, By.XPATH, '//div[@id="app"]/div/div/div/div/h1', 1)
        print("Hib??s bel??p??si adatok, nincs ilyen felhaszn??l??.")
    except:
        usern_text = sel_menu(brow, 4).text
        time.sleep(1)
        print(usern_text)
        click_menu(brow, 1)
        time.sleep(2)
        blogs = article_list_create(brow)
        time.sleep(1)
        click_menu(brow, 5)
        time.sleep(2)
        return len(blogs)


def registr_check_a010(brow):
    wait(brow, By.XPATH, wait_registr_check1, 2)
    try:
        welcome_ok(brow)
        time.sleep(1)
        click_menu(brow, 1)
        time.sleep(1)
        click_menu(brow, 5)
        time.sleep(2)
        return "OK"
    except:
        reg_failed(brow)
        return "FAIL"

