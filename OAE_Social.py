from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import random
import time
import requests
import datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

hub_url = "http://hub_ip:4444/wd/hub"

# Define the desired capabilities for the browser you want to test on
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['platform'] = 'LINUX'

# Create a remote webdriver instance
driver = webdriver.Remote(command_executor=hub_url, desired_capabilities=capabilities)

# Navigate to a website
# driver.get("https://www.example.com")

# Perform your tests here

# # Close the webdriver
# driver.quit()


# Get the current date and time
current_datetime = datetime.datetime.now()

# Access various components of the date and time
current_year = current_datetime.year
current_month = current_datetime.month
current_day = current_datetime.day
current_hour = current_datetime.hour
current_minute = current_datetime.minute
current_second = current_datetime.second

# Create a specific date and time
specific_datetime = datetime.datetime(2023, 11, 4, 15, 30, 0)  # November 4, 2023, 15:30:00

# Formatting the date and time as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d")



#กำหนด array 
error_cases = {}
count = 1
#กำหนด ตัวแปร error ให้เป็นค่าว่าง
error_msg = ""
# รับค่า API จาก line noti
url = 'https://notify-api.line.me/api/notify'
# กำหนด token
token = 'NVHEr0sFNZBrkIHHYDYWupQHgd3mKYbovnU05fEJzyR'
# API FROM INE NOTI
header = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

username = "admin@gmail.com"
password = "P@ssw0rd"

username1 = "admin"
password2 = "1234"
driver = webdriver.Edge()



######## OAE-SOCIAL #######
# driver.get('https://oae-social-listening.demotoday.net/sign-in/signin')
driver.get('https://social.oae.go.th/sign-in/signin')
driver.maximize_window()
try:
    use2 = driver.find_element(By.XPATH, '//*[@id="username"]') 
    pwd2 = driver.find_element(By.XPATH, '//*[@id="password"]')
    use2.send_keys("admin@gmail.com")
    pwd2.send_keys("P@ssw0rd")
    login = driver.find_element(By.XPATH, '/html/body/app-root/app-guest/app-auth-signin/div[2]/div/div/div/div/form/div/div/button')
    login.click()
    time.sleep(5)
except Exception as e:
    error_msg += f"{count}. Error: Login\n"
    count += 1
# #dashboard
try:
    top = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/div/div/div/div/div/div/app-dashboard/app-slm-dashboard/div[2]/div/div[1]/div/div[1]/div[2]/img')
    top.click()
    time.sleep(5)
except Exception as e:
    error_msg += f"{count}. Error: Top Mentions\n"
    count += 1
try:
    datetop = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/div/div/div/div/div/div/app-dashboard/app-slm-dashboard/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/input')
    datetop.click()
    time.sleep(3)
except Exception as e:
    error_msg += f"{count}. Error: Select a time range to view data \n"
    count += 1

try:
    selectdatetop = driver.find_element(By.XPATH, '/html/body/bs-daterangepicker-container/div/div/div/div/bs-days-calendar-view[1]/bs-calendar-layout/div[2]/table/tbody/tr[2]/td[3]/span')
    selectdatetop.click()
    time.sleep(3)
except Exception as e:
    error_msg += f"{count}. Error: Select a time range to view data start\n"
    count += 1


try:
    selectdatetop1 = driver.find_element(By.XPATH, '/html/body/bs-daterangepicker-container/div/div/div/div/bs-days-calendar-view[2]/bs-calendar-layout/div[2]/table/tbody/tr[4]/td[7]/span')
    selectdatetop1.click()
    time.sleep(3)
except Exception as e:
    error_msg += f"{count}. Error: Select a time range to view data end\n"
    count += 1



# try:
#     topfacbook = driver.find_element(By.XPATH, '/html/body/app-root/app-admin/div/div/div/div/div/div/app-dashboard/app-slm-dashboard/div[2]/div/div[1]/div/div[2]/div/div[1]/div[2]/div/button[2]/span')
#     topfacbook.click()
#     time.sleep(2)
# except Exception as e:
#     print("error Top Mentions Facebook")   

# try:
#     data = driver.find_element(By.XPATH,'//*[@id="highcharts-ia44vp7-4711"]/svg/g[5]/g[1]/text[1]')
#     driver.execute_script("arguments[0].scrollIntoView();", data)
#     data.click()
#     time.sleep(2)
# except Exception as e:
#     error_msg += f"{count}. Error: word\n"
#     count += 1

# try:
#     toptwitter = driver.find_element(By.XPATH, '/html/body/app-root/app-admin/div/div/div/div/div/div/app-dashboard/app-slm-dashboard/div[2]/div/div[1]/div/div[2]/div/div[1]/div[2]/div/button[3]/span')
#     toptwitter.click()
#     time.sleep(3)
# except Exception as e:
#     print("error Top Mentions Twitter")

try:
    droptop = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/div/div/div/div/div/div/app-dashboard/app-slm-dashboard/div[2]/div/div[1]/div/div[1]/div[2]/img')
    droptop.click()
    time.sleep(3)
except Exception as e:
    error_msg += f"{count}. Error: Top mantions up\n"
    count += 1

try:
    datekeyword = driver.find_element(By.XPATH, '/html/body/app-root/app-admin/div/div/div/div/div/div/app-dashboard/app-slm-dashboard/div[2]/div/div[2]/div[1]/div[1]/input')
    datekeyword.click()
    time.sleep(3)
except Exception as e:
    error_msg += f"{count}. Error: Select a time range to view data keyword\n"
    count += 1     

try:
    datekeyword1 = driver.find_element(By.XPATH,'/html/body/bs-daterangepicker-container/div/div/div/div/bs-days-calendar-view[1]/bs-calendar-layout/div[2]/table/tbody/tr[2]/td[2]/span')
    datekeyword1.click()
    time.sleep(3)
except Exception as e:
    error_msg += f"{count}. Error: Select a time range to view data start keyword\n"
    count += 1    

try:
    datekeyword2 = driver.find_element(By.XPATH,'/html/body/bs-daterangepicker-container/div/div/div/div/bs-days-calendar-view[1]/bs-calendar-layout/div[2]/table/tbody/tr[4]/td[2]/span')
    datekeyword2.click()
    time.sleep(3)
except Exception as e:
    error_msg += f"{count}. Error: Select a time range to view data end keyword\n"
    count += 1  

try:
    searchkeyword = driver.find_element(By.XPATH, '/html/body/app-root/app-admin/div/div/div/div/div/div/app-dashboard/app-slm-dashboard/div[2]/div/div[2]/div[2]/div[2]/app-button[1]/button')
    searchkeyword.click() 
    time.sleep(3)
except Exception as e:
    error_msg += f"{count}. Error: Search Keyword\n"
    count += 1  

# Project

try:
    # wait = WebDriverWait(driver, 2)
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    project = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/app-navigation/nav/div/app-nav-content/ng-scrollbar/div/div/div/div/div/ul/app-nav-item[2]/li/a/span[2]')
    project.click()
    time.sleep(10)
except Exception as e:
    error_msg += f"{count}. Error: Project\n"
    count += 1  





# try:
#     editepro = driver.find_element(By.XPATH, '//*[@id="menu-wrap"]/input') 
#     editepro.click()
#     time.sleep(2)
#     editepro2 = driver.find_element(By.XPATH,'//*[@id="menu-wrap"]/div[2]/div/ul/li[1]/a')
#     editepro2.click()
#     time.sleep(2)
# except Exception as e:
#    print("error: Edite Project")

# try:
#     namepro = driver.find_element(By.XPATH, '//*[@id="mat-input-9"]')
#     namepro.send_keys(nameproject)
#     time.sleep(2)
# except Exception as e:
#    print("error: Name Project")

#CATAGORY

try:
    manageso = driver.find_element(By.XPATH, '/html/body/app-root/app-admin/app-navigation/nav/div/app-nav-content/ng-scrollbar/div/div/div/div/div/ul/app-nav-group/app-nav-collapse/li/a/span[2]')
    manageso.click()
    time.sleep(2)
except Exception as e:
    error_msg += f"{count}. Error: Data management\n"
    count += 1  

try:
    cat = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/app-navigation/nav/div/app-nav-content/ng-scrollbar/div/div/div/div/div/ul/app-nav-group/app-nav-collapse/li/ul/app-nav-item[1]/li/a')
    cat.click()
    time.sleep(2)
except Exception as e:
    error_msg += f"{count}. Error: Category\n"
    count += 1  



try:
    ware = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/app-navigation/nav/div/app-nav-content/ng-scrollbar/div/div/div/div/div/ul/app-nav-group/app-nav-collapse/li/ul/app-nav-item[2]/li/a')
    ware.click()
    time.sleep(2)
except Exception as e:
    error_msg += f"{count}. Error: Data repository\n"
    count += 1 

try:
    word = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/app-navigation/nav/div/app-nav-content/ng-scrollbar/div/div/div/div/div/ul/app-nav-group/app-nav-collapse/li/ul/app-nav-item[3]/li/a')
    word.click()
    time.sleep(2)
except Exception as e:
    error_msg += f"{count}. Error: Agricultural terminology\n"
    count += 1



try:
    timema= driver.find_element(By.XPATH,'/html/body/app-root/app-admin/app-navigation/nav/div/app-nav-content/ng-scrollbar/div/div/div/div/div/ul/app-nav-item[3]/li/a/span[2]')
    timema.click()
    time.sleep(2)
except Exception as e:
    error_msg += f"{count}. Error: Schedule time\n"
    count += 1


try:
    manaper = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/app-navigation/nav/div/app-nav-content/ng-scrollbar/div/div/div/div/div/ul/app-nav-item[4]/li/a/span[2]')
    manaper.click()
    time.sleep(2)
except Exception as e:
    error_msg += f"{count}. Error: Manage user permissions\n"
    count += 1



try:
    history = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/app-navigation/nav/div/app-nav-content/ng-scrollbar/div/div/div/div/div/ul/app-nav-item[5]/li/a/span[2]')
    history.click()
    time.sleep(2)
except Exception as e:
    error_msg += f"{count}. Error: Access history\n"
    count += 1



try:
    logout = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/app-navigation/nav/div/app-nav-content/ng-scrollbar/div/div/div/div/div/ul/app-nav-item[6]/li/a/span[2]')
    logout.click()
    time.sleep(2)
except Exception as e:
    error_msg += f"{count}. Error: logout\n"
    count += 1

for key, error_status in (error_cases.items()):
    if (error_status is True):
        error_msg += (str(count) + ". " + str(key) + "\n")
        count += 1
    
if (error_msg == ""):
    req = requests.post(url, headers=header, data= {'message':formatted_datetime+"\n 1.ระบบสามารถเข้าใช้งานได้ตามปกติ"})
    # req = requests.post(url, headers=header, data= {'message': "\nSuccess"})
else:
    req = requests.post(url, headers=header, data= {'message':formatted_datetime +"\n"+"พบข้อผิดพลาด"+"\n"+"ระบบ OAE-Social:"+"\n"+error_msg})

