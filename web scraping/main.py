# projet controle du web
#https://selenium-python.readthedocs.io/index.html

from selenium import webdriver
from time import sleep
#permet ouvrir une page sur le navigateur firefox
driver =webdriver.Firefox(executable_path="ff.exe")
driver.get("https://www.youtube.com/")

#on donne un temp de repos pour que la page ce charge 
sleep(5)
#en general on a les conditions a accepter donc le but ici et de trouver id du button 
#cependant il y en a plusieur dans le code de la page donc on prend le dernier bouton 
#car le bouton accepter et le dernier de la page puis on clique dessus 
searchbutton = driver.find_elements_by_xpath('//*[@id="button"]') 
n=len(searchbutton)
searchbutton[n-1].click()

sleep(2)
#on cherche id de la barre de recherche 
searchbox = driver.find_element_by_xpath('//input[@id="search"]')
#on saisie du texte
searchbox.send_keys("université toulon")
sleep(2)
#on cherche le button entrée et on clique dessus 
searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]') 
searchbutton.click()
sleep(2)
driver.back()
sleep(2)
driver.forward()


