from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import animation
import pandas as pd

@animation.wait('bar', color='blue')
def loading(sec):
    time.sleep(sec)
    pass

if __name__=="__main__":
    print("..........script started.........")
    #create a dataframe with name specialite tel tel1 adresse 
    data = pd.DataFrame(columns=['Denomination','Activités','Tél. siège/usine','Gouvernorat','google_map'])
    driver = webdriver.Chrome()
    #the ident param points to the number of publicly registred companys 
    driver.get("http://www.tunisieindustrie.nat.tn/fr/dbi.asp?action=result&ident=1")
    loading(2)
    elem = driver.find_element(By.CLASS_NAME,"table-wrap")
    print(elem.text)
    
    pass

