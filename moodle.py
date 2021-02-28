from selenium import webdriver
from selenium.webdriver.common.keys import Keys
uname = input("Enter the username:")
pword = input("Enter the password:")
driver = webdriver.Chrome(r"C:\WebDriver\bin\chromedriver.exe")
driver.get("https://moodle.iitd.ac.in/login/index.php")
uinput = driver.find_element_by_id('username')
pinput = driver.find_element_by_id('password')
cinput = driver.find_element_by_id('valuepkg3')
captcha=driver.find_element_by_id('login').text
s=captcha.split('\n')
captcha=s[3].split()
l=['first','second','add','subtract']
for i in captcha:
    if i in l:
        if i=='first':
            cans=captcha[-4]
        elif i=='second':
            cans=captcha[-2]
        elif i=='add':
            cans=str(int(captcha[-2])+int(captcha[-4]))
        else:
            cans=str(int(captcha[-4])-int(captcha[-2]))
uinput.clear()
pinput.clear()
cinput.clear()
uinput.send_keys(uname)
pinput.send_keys(pword)
cinput.send_keys(cans)
cinput.send_keys(Keys.RETURN)