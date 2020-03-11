from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class InstaBot:
    def __init__(self,username,password):
        self.username=username
        self.driver=webdriver.Chrome("C:/Users/KIIT/Downloads/chromedriver.exe")
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        
    def get_followers(self):
        driver=self.driver
        driver.get("https://www.instagram.com/explore/people/suggested/")
        sleep(2)
        for i in range(1,2):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            sleep(2)
        hrefs=driver.find_elements_by_tag_name('a')
        pic_hrefs=[elem.get_attribute('href')for elem in hrefs]
        
             
        print(len(pic_hrefs))
        print(pic_hrefs)
           
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            
            try:
                driver.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()
                sleep(18)
                    
            except Exception as e:
                sleep(2)
    def follow_users(self):
        driver=self.driver
        sugs=driver.get("https://www.instagram.com/explore/people/suggested/")
        sleep(2)
        driver.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()
        sleep(2)
        
    def unfollow_users(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format('pycode123')).click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Following')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
        sleep(2)
        
    def like_photo(self,hashtags):
        driver=self.driver    
                #print(done)
            except Exception as e:
                print('bye')
                sleep(2)
            
        
mybot=InstaBot("6371098564","11012000")
n=0
while(n<2):
    mybot.follow_users()
    n=n+1  
#mybot.get_followers()
    
#mybot.unfollow_users()
#mybot.like_photo('newyork')
