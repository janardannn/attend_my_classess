from scripts import student_info  # importing student_info for student's login credentials
from scripts import class_info   # importing class_info for url of google classrooms and class timings
from scripts.time_and_date import time_now # use time_now module to get current time as par IST time-zone
from scripts.time_and_date import today_date
from selenium.common.exceptions import NoSuchElementException as NoSuchElementException   # to deal with NoSuchElementException error
from selenium import webdriver     # using selenium module for automation
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
#from win10toast import ToastNotifier
import time                      # to time.sleep as some page(s) load much slower and selenium may raise NoSuchElementException error

#NoSuchElementException = selenium.common.exceptions.NoSuchElementException

class Firelord_Azula:

    def __init__(self):

        print('''

                    ___       _____      __  __   __       ___ 
                   /   |     /__  /     / / / /  / /      /   |
                  / /| |       / /     / / / /  / /      / /| |
                 / ___ |      / /__   / /_/ /  / /___   / ___ |
                /_/  |_|     /____/   \____/  /_____/  /_/  |_|
                                   v 1.1            
                                    
                                     is
                                 starting''',end="")
        
        for j in range(5):
            print('.',end="",flush=True)
            time.sleep(0.7)
        print('\n')


        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        self.driver = webdriver.Chrome(options=chrome_options)
        print('-----------------------------------------------------------------',end='\n')
    
        # using webdriver to initiate our Browser  
	
	self.driver = webdriver.Browser('/path_to_webdriver')        
        # set attendance today to 0 at start, and checks if it is 0, if not then the object calls the attendance function for the particular subject else pass

        self.xyz_attendance_today = 0
        
        self.abc_attendance_today = 0
        
        # to send notifications (windows 10 only)
        ##self.notifier = ToastNotifier()
        
        # log file to log each and everything from initiation to end.
        self.log_file = open("/attend_my_classes.log",'a+')
        self.log_file.write('initiated {} {} \n'.format(time_now(),today_date()))


    def login(self):

        # logging in into google classroom dashboard
        self.driver.get(class_info.google_classroom_login)

        # finding gmail input box, clicking it and entering gmail
        email = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email.click() 
        email.send_keys(student_info.email)

        # finding next button and clicking it after entering gmail
        next_button = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
        next_button.click()

        self.driver.implicitly_wait(25)
        # time.sleep, so as the next page loads otherwise selenium may raise NoSuchElementException error

        # finding password entry, clicking it and entering password
        password = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password.click()
        password.send_keys(student_info.password)

        # finding next button and clicking it after entering password
        next_button2 = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
        next_button2.click()

        self.log_file.write('login {} {} \n'.format(time_now(),today_date()))

        print('Logged in      -- {} -- {}'.format(time_now(),today_date()),end="\n")

        #time.sleep as it takes some time to load classroom page (even on fast connection :P)
        time.sleep(7)



########################################################################################
    #                          Code block for                                    #
    #                 attending live google meet classess                        #
    #                 embedded in google classroom banner                        #
########################################################################################



    def attend_class(self,subject,class_url,class_timing,class_ending):
        
        # object's method to attend xyz class

        class_name = subject

        self.driver.get(class_url) # opening xyz classroom
        
        
        
        try:
            self.driver.implicitly_wait(25)
            class_live = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[1]/div/div[2]/div[2]/div/span/a/div').text
            self.driver.get(class_live) # clicks it

        # finds the mic button and click on it
            try:
                # ----- code for mic here ----- #
                
                #self.driver.implicitly_wait(25)
                #mic = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div/div[1]')
                #self.driver.execute_script("arguments[0].click()",mic)

        # //  __code__here__
        # //  for disabling
        # //   __webcam__

        # finds join now button and clicks it
                time.sleep(10)
                self.driver.implicitly_wait(25)
                join_class = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
                join_class.click()

                print('Attending {} Class...      -- {} -- {}'.format(subject,time_now(),today_date()))
                self.log_file.write('{} class {} {} \n'.format(subject,time_now(),today_date()))

                while True:
                    if time_now() > class_ending:

                        try:
                            no_of_people = self.driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]')
                            if no_of_people.text != '':
                                people = int(no_of_people.text)
                                print(people)
                                if people < 10:
                                    print('{} class is over      -- {} -- {}'.format(subject,time_now(),today_date()),end='\n')
                                    self.driver.get(class_info.google_classroom)
                                    # notification when a class ends
                                    ##self.notifier.show_toast('English Class Ended','English class ended just now',duration=15)
                                    self.log_file.write('{} class ended {} {} \n'.format(subject,time_now(),today_date()))
                                    break

                                else:
                                    time.sleep(1.2)
                                    continue

                            else:
                                pass
                           

                        except NoSuchElementException:
                            print('no such element : no_of_people')
                        
                    time.sleep(5)


            except NoSuchElementException:
                try:
                    self.driver.implicitly_wait(25)
                    no_class = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[1]').text
                    if no_class == 'You can\'t create a meeting yourself. Contact your system administrator for more information.':
                        time.sleep(300)
                except NoSuchElementException:
                    pass
      #  time.sleep(25000)
       # the_end = self.driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[9]/div[2]/div[2]/div/span/span/svg')
        # finds the google meet link/icon 
        except NoSuchElementException:
            for k in range(2):
                # sample notification 
                ##self.notifier.show_toast('No English Class','there is no google meet link for english, try heading to classroom',duration=50)
                time.sleep(300)
            print('\n')



########################################################################################
    #                          Code block for                                    #
    #                            attendance                                      #
    #                    in posts in google classroom                            #
########################################################################################



    def attendance(self,subject):

        if subject == 'xyz':
            # this is to ensure that the bot only comments in specific posts which are meant for attendance
            check_1 = 'any consistent word in attendance post'
            check_2 = 'any other consistent word in attendance post'

            class_link = class_info.xyz_class_url
            teacher = class_info.xyz_teacher
            attendance_line = 'Present Sir/Ma\'am'

        elif subject == 'abc':
            check_1 = 'give your presence here'      
            check_2 = ' '

            class_link = class_info.abc_class_url
            teacher = class_info.abc_teacher
            attendance_line = 'Present Sir/Ma\'am'

        if True:
            self.driver.get(class_link)

            for k in range(1,5):
                for code_id in ['37','38','39']:
                    try:
                        teacher_name = self.driver.find_element_by_xpath('//*[@id="ow{}"]/div[2]/div[{}]/div[1]/div[1]/div[1]/div/div/span'.format(code_id,k)).text
                    except NoSuchElementException:
                        continue
                    if teacher_name == teacher:
                        try:
                            time_of_post = self.driver.find_element_by_xpath('//*[@id="ow{}"]/div[2]/div[{}]/div[1]/div[1]/div[1]/span/span[2]'.format(code_id,k)).text.upper()
                            
                            if "AM" in time_of_post or "PM" in time_of_post:
                                post_content = self.driver.find_element_by_xpath('//*[@id="ow{}"]/div[2]/div[{}]/div[1]/div[2]/div[1]/html-blob/span'.format(code_id,k)).text.lower()

                        
                                if check_1 in post_content and check_2 in post_content:
                                
                                    comment_box = self.driver.find_element_by_xpath('//*[@id="ow{}"]/div[2]/div[{}]/div[2]/div/div[3]/div/div[2]/div[1]'.format(code_id,k))
                                    time.sleep(1.5)

                                    ActionChains(self.driver).move_to_element(comment_box).click(comment_box).send_keys(attendance_line).perform()
                                    time.sleep(1.5)
                                
                                    send_key = self.driver.find_element_by_xpath('//*[@id="ow{}"]/div[2]/div[{}]/div[2]/div/div[3]/div/div[2]/div[2]/div/span'.format(code_id,k))
                                    time.sleep(2.5)
                                    send_key.click()
                                    
                                    if subject == 'xyz':
                                        self.xyz_attendance_today+=1       

                                        if self.xyz_attendance_today == 1:

                                            print('xyz Attendance marked present      -- {} -- {}'.format(time_now(),today_date()),end='\n')

                                            self.log_file.write('xyz attendance {} {} \n'.format(time_now(),today_date()))

                                    elif subject == 'abc':
                                        self.abc_attendance_today+=1       

                                        if self.abc_attendance_today == 1:
                                           

                                            print('abc Attendance marked present      -- {} -- {}'.format(time_now(),today_date()),end='\n')

                                            self.log_file.write('abc attendance {} {} \n'.format(time_now(),today_date()))


                        except  NoSuchElementException:
                            continue


########################################################################################
    #                          Code block for                                    #
    #                         testing purposes                                   #
    #                                                                            #
########################################################################################

# function to test new features

    def attend_test_class(self):

        inp_link = str(input('Google meet code: ')).strip()
        inp_link = 'https://meet.google.com/' + inp_link + '/'
        self.driver.get(inp_link)


        self.driver.implicitly_wait(25)
        mic = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div/div[1]')
      #  self.driver.execute_script("arguments[0].click()",mic)

        # //  __code__here__
        # //  for disabling
        # //   __webcam__

        # finds join now button and clicks it
        time.sleep(10)
        self.driver.implicitly_wait(25)
        join_class = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]/span/span')
        join_class.click()
        

        print('Attending Test Class...      -- {} -- {}'.format(time_now(),today_date()))

        self.driver.implicitly_wait(25)

        while True:
            if time_now() > '14:27:55':
                no_of_people = self.driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[7]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]')

                people = int(no_of_people.text)
                print(people)
                print(type(people))

                if people<5:
                    print('Test class is over      -- {} -- {}'.format(time_now(),today_date()),end='\n')
                    self.driver.get(class_info.google_classroom)
              #  self.driver.execute_script("arguments[0].click()",end_button)
                    break
                else:
                    continue
            time.sleep(5)

                

    def __str__(self):

        return('''
        HELPS YOU to attend online classes,

        AND helps you with attendance,
        
        ENJOY!

        v 1.1
        ''')



Azula = Firelord_Azula()
Azula.login()
time.sleep(3)

def run():
    while True:

        # xyz attendance and class

        if time_now() > "08:05:00" and time_now() < class_info.xyz_class_timing:
            if Azula.xyz_attendance_today == 0:
                Azula.attendance('xyz')

        elif time_now() > class_info.xyz_class_timing and time_now() < class_info.xyz_class_ending:
            Azula.attend_class("xyz",class_info.xyz_class_url,class_info.xyz_class_timing,class_info.xyz_class_ending)

        # abc attendance and class

        elif time_now() > "12:50:25" and time_now() < class_info.abc_class_timing:
            if Azula.abc_attendance_today == 0:
                Azula.attendance('abc')

        elif time_now() > class_info.abc_class_timing and time_now() < class_info.abc_class_ending:
            Azula.attend_class("abc",class_info.abc_class_url,class_info.abc_class_timing,class_info.xyz_class_ending)

        # to exit forever loop
        elif time_now() > '14:05:05':
            break

        # time.sleep(x) to keep the cpu usage low if forever is running
        time.sleep(10)


def end():

    Azula.driver.close()
    Azula.log_file.close()
    print('-----------------------------------------------------------------',end='\n')
    time.sleep(1.1)
    print('''
                    ___       _____      __  __   __       ___ 
                   /   |     /__  /     / / / /  / /      /   |
                  / /| |       / /     / / / /  / /      / /| |
                 / ___ |      / /__   / /_/ /  / /___   / ___ |
                /_/  |_|     /____/   \____/  /_____/  /_/  |_|
                                               
                                    
                                     is
                               shutting down''',end="")

    for k in range(5):
        print(".",end="",flush=True)
        time.sleep(0.5)
    print("!",end="\n")    

if __name__ == '__main__':
    
    run()
    k = 1
    #Azula.attend_test_class()

    end()
    quit()
