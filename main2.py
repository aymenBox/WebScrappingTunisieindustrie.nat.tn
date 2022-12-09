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
@animation.wait('bar', color='red')
def extract_data(tab):
    print(".................extrating data from table.................")
    data={'Dénomination':"",'Raison Sociale':"",'Responsable':"",'Activités':"",
    'Produits':"",'Adresse':"",'Gouvernorat':"",'Délégation':"",'Téléphone':"",'Fax':""
    ,'E-mail':"",'URL':"",'Régime':"",'Pays du Participant Etranger':"",'Entrée en production':"",'Capital en DT':"",'Emploi':""}
    data["Dénomination"]=tab[0].replace('Dénomination','')
    data["Raison Sociale"]=tab[1].replace('Raison Sociale','')
    data["Responsable"]=tab[2].replace('Responsable','')
    data["Activités"]=tab[3].replace('Activités','')
    data["Produits"]=tab[4].replace('Produits','')
    data["Adresse"]=tab[5].replace('Adresse','')
    data["Gouvernorat"]=tab[6].replace('Gouvernorat','')
    data["Délégation"]=tab[7].replace('Délégation','')
    data["Téléphone"]=tab[8].replace('Téléphone siège/usine','')
    data["Fax"]=tab[9].replace('Fax siège/usine','')
    data["E-mail"]=tab[10].replace('E-mail','')
    data["URL"]=tab[11].replace('URL','')
    data["Régime"]=tab[12].replace('Régime','')
    data["Pays du Participant Etranger"]=tab[13].replace('Pays du Participant Etranger','')
    data["Entrée en production"]=tab[14].replace('Entrée en production','')
    data["Capital en DT"]=tab[15].replace('Capital en DT','')
    data["Emploi"]=tab[16].replace('Emploi','')
    return data

if __name__=="__main__":
    print("..........script started.........")
    #create a dataframe with name specialite tel tel1 adresse 
    data = pd.DataFrame(columns=['Dénomination','Raison Sociale','Responsable','Activités',
    'Produits','Adresse','Gouvernorat','Délégation','Téléphone','Fax'
    ,'E-mail','URL','Régime','Pays du Participant Etranger','Entrée en production','Capital en DT','Emploi'])
    #4873 data entry has been found while scanning this website
    page= 2873
    driver = webdriver.Chrome()
    #the ident param points to the number of publicly registred companys 
    driver.get("http://www.tunisieindustrie.nat.tn/fr/dbi.asp?action=result&ident=1")
    loading(4)
    while(page<3873):
        try:
            driver.get("http://www.tunisieindustrie.nat.tn/fr/dbi.asp?action=result&ident="+str(page))
            tab = driver.find_element(By.CLASS_NAME,"table-wrap")
            loading(2)
            data_table=tab.text.split("\n")     
            data=data.append(extract_data(data_table),ignore_index=True)
            print(data.tail(1))
            page+=1
        except:
            print("error while getting page")
            print("saving data before continuing...")
            data.to_excel("backup2.xlsx")
            print("page number: "+str(page))
            print("skip to next page")
            continue       
        pass
    pass
    #save data to excel
    data.to_excel("final_data2.xlsx")
    driver.quit()
    print("..........script ended.........")

