from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://localhost/home.html")

start_time = time.time() # pt contor

sleep5 = 5
sleep3 = 3

# testare login invalid
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, '//*[@id="login-container"]//button')

username_input.send_keys("wronguser")
password_input.send_keys("wrongpass")
login_button.click()

# test daca se vede msj err
error_msg = driver.find_element(By.ID, "error-msg")
# assert error_msg.is_displayed(), "se afiseaza corect mesajul de login invalid"
if error_msg.is_displayed():
    print("[t1] pass - se afiseaza incorrect login cand trebuie")
else:
    print("[t1] fail - nu se afiseaza incorrect login cand trebuie")
    assert False, "nu se afiseaza corect mesajul de login invalid"


time.sleep(sleep5)

# test login corect
username_input.clear()
password_input.clear()

username_input.send_keys("test123")
password_input.send_keys("test123")
login_button.click()

# test daca se vede dashboardul
dashboard = driver.find_element(By.ID, "dashboard-container")
if dashboard.is_displayed():
    print("[t2] pass - se vede dashboard post-login")
else:
    print("[t2] fail - se vede dashboard post-login")
    assert False, "nu se vede dashboard post-login"


user_name_display = driver.find_element(By.ID, "user-name")
if "test123" in user_name_display.text:
    print("[t3] pass - se vede username-ul in dashboard")
else:
    print("[t3] fail - se vede username-ul in dashboard")
    assert False, "nu se vede username-ul in dashboard"


time.sleep(sleep3)

# test pt feedback form
feedback_input = driver.find_element(By.ID, "feedback")
feedback_button = driver.find_element(By.XPATH, "//button[contains(text(),'Trimitere Feedback')]")

feedback_input.send_keys("Selenium test feedback")
feedback_button.click()

feedback_msg = driver.find_element(By.ID, "feedback-msg")
if feedback_msg.is_displayed():
    print("[t4] pass - msj feedback e vizibil post-submit")
else:
    print("[t4] fail - msj feedback e vizibil post-submit")
    assert False, "msj feedback nu e vizibil post-submit"

time.sleep(sleep3)

# test logout si return la login form
logout_button = driver.find_element(By.XPATH, "//button[contains(text(),'Logout')]")
logout_button.click()

# test daca se vede login container
login_container = driver.find_element(By.ID, "login-container")
if login_container.is_displayed():
    print("[t5] pass - login form vizibil post-logout")
else:
    print("[t5] fail - login form vizibil post-logout")
    assert False, "login form nu e vizibil post-logout"

time.sleep(sleep5)

end_time = time.time()
# folosim sleep5 si sleep3 de 2 ori fiecare -> 16 sec artificial adaugate

print(f"timp delta executie fara wait/sleep: {end_time - start_time - 16:.2f} sec")

driver.quit()