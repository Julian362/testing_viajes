import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="driver\chromedriver.exe")

driver.get("https://www.viajesexito.com/")
time.sleep(2)
paquetes = driver.find_element(by=By.XPATH,value="/html/body/form/header/div[2]/div/div/nav/div[2]/a/span")
paquetes.click()



time.sleep(2)
entrada_vuelo = driver.find_element(by=By.XPATH,value="/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div/div/input")
time.sleep(2)



salida_vuelo = driver.find_element(by=By.XPATH,value="/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div/div/input")
salida_vuelo.send_keys("Punta Cana, Republica Dominicana (PUJ)")
time.sleep(2)

input_fechas_click = driver.find_element(by=By.XPATH,value="/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/input")
input_fechas_click.click()
time.sleep(1)
fecha1_vuelo_click = driver.find_element(by=By.XPATH,value="/html/body/div[21]/div[1]/table/tbody/tr[3]/td[3]")
time.sleep(1)
fecha1_vuelo_click.click()
fecha2_vuelo_click = driver.find_element(by=By.XPATH,value="/html/body/div[21]/div[1]/table/tbody/tr[4]/td[4]")
time.sleep(1)
fecha2_vuelo_click.click()
time.sleep(1)
habitaciones_click = driver.find_element(by=By.XPATH,value="/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div")
habitaciones_click.click()
time.sleep(1)
habitaciones_mas_click = driver.find_element(by=By.XPATH,value="/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div/span[2]")
habitaciones_mas_click.click()
time.sleep(1)
boton_habitaciones__click = driver.find_element(by=By.XPATH,value="/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/button")
boton_habitaciones__click.click()
time.sleep(1)
buscar_click = driver.find_element(by=By.XPATH,value="/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[4]/a")
buscar_click.click()
time.sleep(15)
print("-----------------------------------------------")
for i in range(1,11):
    precio= driver.find_element(by=By.XPATH,value="/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div["+str(i)+"]/div/div/div[2]/div/div[1]/div/p[1]/span[2]")
    print(precio.text)

time.sleep(3)
aerolinea_click = driver.find_element(by=By.XPATH,value="/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input")
aerolinea_click.send_keys("Avianca (AV)")
time.sleep(1)
bsucar_aerolinea_click = driver.find_element(by=By.XPATH,value="/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input")
bsucar_aerolinea_click.click()
time.sleep(15)
driver.quit()
driver.close()