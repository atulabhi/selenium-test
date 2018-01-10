import time
from selenium import webdriver
browser = webdriver.Firefox()
home_page = "http://openebs.io"
'''global is_link_element_displayed
is_link_element_displayed = 'none'''
def check_page_broken_links(self, url):

    try:
        failed = []
        self.implicitly_wait(15)
        #self.manage().timeouts().implicitly_wait(10, TimeUnit.SECONDS); 

        self.get(url)
        #number_of_links = len(self.find_elements_by_tag_name('a'))
        number_of_links = len(self.find_elements_by_xpath("//a[@href]"))
        print number_of_links
        #print self.find_elements_by_tag_name('a')
        for i in range(number_of_links):
            initial_window = self.current_window_handle 
            #print "initial_window_handle:      ", initial_window

            link = self.find_elements_by_xpath("//a[@href]")[i]
            #print link 
            #print i
            link_address = link.get_attribute("href")
            #print link_address
            link_name = link.text
            print "link checked: ",i,": ",link_name,": ",link_address

            if ((link_address is not None) 
                and ("google" not in link_address) 
                and ("mailto" not in link_address) #is True):
                and link.is_displayed() is True):
                  #time.sleep(15)
                  link.click()
                  time.sleep(120)
                  open_windows = self.window_handles
                 # print "window_handles:      ", open_windows

                  self.switch_to_window(open_windows[-1])
                  ## print "current_window_handle:"
                  #print self.current_window_handle
                  time.sleep(15)
                  print "defined: ",link_address
                  print "current: ", self.current_url
                  time.sleep(15)

                  if (link_address[-1] == "#" 
                       and self.current_url in 
                        [link_address, link_address[:-1],
                                      link_address[:-2],link_address+'/']):
                          # A "#" at the end means user 
                          # will stay on the same page.(Valid scenario) 
                          pass  
                  elif (self.current_url not in 
                        [link_address,
                         home_page + link_address[1:]]): 
                        
                        if link_name:
                          failed.append(link_name)
                        else:
                          failed.append(link_address)

                  if len(self.window_handles) > 1:  
                          # close newly opened window
                          self.close()

                  # Switch to main browser window
                  self.switch_to_window(open_windows[0]) 

            self.get(url)
    except Exception, e: 
           return ['Exception occurred while checking',e]
    return failed

print check_page_broken_links(browser,"http://openebs.io/")
#print check_page_broken_links(browser,"http://www.carwale.com/")
