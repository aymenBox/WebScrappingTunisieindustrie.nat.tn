from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import animation
import pandas as pd

@animation.wait('bar', color='blue')
def fucntion():
    time.sleep(5)
    pass

if __name__=="__main__":
    wait = animation.Wait('bar', color='blue')
    print("..........script started.........")
    #create a dataframe with name specialite tel tel1 adresse 
    data = pd.DataFrame(columns=['Denomination','Activités','Tél. siège/usine','Gouvernorat','google_map'])
    driver = webdriver.Chrome()
    driver.get("http://www.tunisieindustrie.nat.tn/fr/dbi.asp?action=result&ident=1")
    time.sleep(5)
    pass

