# A007 select user - Szűrés blogszerző szerint, a kiválasztott blogszerző bejegyzéseinek kiírása text fájlba

import data.data_tcA007 as da07
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

# *** TC-A007 **************************************


def test_A007_select():
    fu01.cookie_ok(driver)
    fu01.sign_in(driver, da07.mail, da07.passw)
    return fu01.select_user(driver, da07.username)


user_blog_num1 = test_A007_select()


def test_A007_read():
    blog_read = fu01.user_read(driver, user_blog_num1)
    fu01.out_close_driver(driver)
    return blog_read


blog_read_full = test_A007_read()


def test_A007_write():
#    filename = f"data_out/a007_{da07.username}_blogs"
    filename = f"a007_{da07.username}_blogs.txt"
    with open(filename, "w", encoding='utf-8') as f:
        f.write(f"{da07.username} bejegyzései:\n")
        r_num = len(blog_read_full)
        for i in range(r_num):
            b_tit = str(blog_read_full[i][0])
            b_tit_upper = b_tit.upper()
            f.write(f"\n{b_tit_upper}\n")
            b_tex = str(blog_read_full[i][1]).replace('. ', '.\n')
            f.write(f"{b_tex}\n")
    return r_num


#user_blog_num2 = test_A007_write()


# ***************************************************

# Normal, automatic run
if __name__ == "__main__":
    user_blog_num2 = test_A007_write()
    print(f"\n{da07.username} bejegyzései:")
    r_n = len(blog_read_full)
    for i in range(r_n):
        b_title = str(blog_read_full[i][0])
        b_title_upper = b_title.upper()
        print(f"\n{b_title_upper}")
        b_text = str(blog_read_full[i][1]).replace('. ', '.\n')
        print(b_text)
    try:
        assert user_blog_num1 == user_blog_num2
    except:
        print("Hiba, az ellenőrző feltételek nem a várt eredményt mutatják.")

