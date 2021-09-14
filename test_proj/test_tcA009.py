# test case A009 - test of scrolling functino
# 2 users are randomly generated with one post each
# If the number of posts is too small new users number can be set to a higher one at the start of the test in data_tcA009.py


import data.data_tcA009 as da09
import func.func_01 as fu01

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("http://localhost:1667")

# Wait for loading
fu01.wait(driver, By.ID, "app", 1)


# *** TC-A009 **************************************


def test_A009_users_add(users):
    users_in_data = []
    for user in users:
        user_in = []
        fu01.sign_up(driver, user[0], user[1], user[2])
        fu01.registr_check_a009(driver)
        user_in.append(user[1])
        user_in.append(user[2])
        users_in_data.append(user_in)
        fu01.blog_write_a009(driver, da09)
    return users_in_data


users_in_data_list = test_A009_users_add(da09.users)
print(users_in_data_list)
login_user = users_in_data_list[0]

def test_A009_blog_num():
    fu01.cookie_ok(driver)
    fu01.sign_in(driver, login_user[0], login_user[1])
    return fu01.blog_num_check(driver)

pages_blog_num = test_A009_blog_num()
print(pages_blog_num)

try:
    assert pages_blog_num == 10
    print("10 db blogbejegyzés van egy oldalon, további tesztekkel vizsgálhatjuk az oldalak léptetését.")
except:
    print("Hibás lapozó funkció, 10-nél több elem jelenik meg egy oldalon.")
    fu01.close_driver(driver)


# ***************************************************


# Normal run
if __name__ == "__main__":
    print(pages_blog_num)
    try:
        assert pages_blog_num == 10
    except:
        print("Hiba, egy lapon 10-nél több bejegyzés van.")

