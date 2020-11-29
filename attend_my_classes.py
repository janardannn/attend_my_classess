from scripts import student_info  # importing student_info for student's login credentials
from scripts import class_info   # importing class_info for url of google classrooms and class timings
from scripts.time_now import current_indian_time as time_now    # use time_now module to get current time as par IST time-zone
import selenium                     # to deal with NoSuchElementException error
from selenium import webdriver     # using selenium module for automation
import time                       # to time.sleep as some page(s) load much slower and selenium may raise NoSuchElementException error


class attend_my_class:
    def __init__(self):
        self.driver = webdriver.Edge(r'')    # path to webdriver executable # use webdriver.YourBrowser(r'path/to/webdriver_executable')
        # using webdriver to initiate our Browser
    def login(self):
        google_classroom = 'https://classroom.google.com/h'
        # logging in to google classroom dashboard
        self.driver.get(google_classroom)

        # finding gmail entry, clicking it and entering gmail
        email = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email.click() 
        email.send_keys(student_info.email)

        # finding next button and clicking it after entering gmail
        next_button = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
        next_button.click()

        time.sleep(7)
        # time.sleep, so as the next page loads otherwise selenium may raise NoSuchElementException error

        # finding password entry, clicking it and entering password
        password = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password.click()
        password.send_keys(student_info.password)

        # finding next button and clicking it after entering password
        next_button2 = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
        next_button2.click()

        #time.sleep as it takes some time to load classroom page (even on fast connection :P)
        time.sleep(11)

    def attend_chemistry_class(self):
        
        # object's method to attend chemistry class

        self.driver.get(class_info.chemistry_class_url) # opening chemistry classroom
        time.sleep(5) 
        
        chemistry_live = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[1]/div[1]/div[2]/div[2]/span/a/div')
        # finds the google meet link/icon 
        chemistry_live.click() # clicks it

        time.sleep(5)

        # google meet prompts mic and webcam usage permission
        # clicks dismiss button if available 
        # else: pass
        try:
            dismiss_button = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
            dismiss_button.click()
        except selenium.common.exceptions.NoSuchElementException:
            pass

        # finds the mic button and click on it
        mic = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div')
        mic.click()

        # //  __code__here__
        # //  for disabling
        # //  __webcam__

        # finds join now button and clicks it
        join_class = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]/span/span')
        join_class.click()



attend = attend_my_class() #creating an instance