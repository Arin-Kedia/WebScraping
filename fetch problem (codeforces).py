from selenium import webdriver
import os
a=input("Enter the problem no. : ")
driver = webdriver.Chrome(r"C:\WebDriver\bin\chromedriver.exe")
l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
bpath = "https://codeforces.com/problemset/problem/"+a+'/'
i=0
directorymain = ('/' + a)
os.mkdir(directorymain)
k='1'
while (i<26):
    driver.get(bpath+l[i])
    if ((a+l[i]) in driver.title and k == '1'):
        k=''
    if (a+l[i]+k) not in driver.title:
        driver.get(bpath+l[i]+k)
        if (a+l[i]+k) not in driver.title:
            break
    dirpath = directorymain + '/' + l[i] + k
    os.mkdir(dirpath)
    driver.save_screenshot(dirpath+'\problem.png')
    inputdata = driver.find_elements_by_class_name("input")
    j=0
    while (j<len(inputdata)):
        f=open(dirpath + '\input' + str(j+1) + '.txt','w')
        inputtext = inputdata[j].text
        inputd = inputtext.split('\n')
        inputd = inputd[2:]
        for line in inputd:
            f.write(line+'\n')
        f.close()
        j+=1
    outputdata = driver.find_elements_by_class_name("output")
    j=0
    while (j<len(outputdata)):
        f=open(dirpath + '\output' + str(j+1) + '.txt','w')
        outputtext = outputdata[j].text
        outputd = outputtext.split('\n')
        outputd = outputd[2:]
        for line in outputd:
            f.write(line+'\n')
        f.close()
        j+=1
    if k == '':
        i+=1
        k='1'
    else:
        if k=='1':
            k='2'
        else:
            i+=1
            k='1'
driver.quit()
