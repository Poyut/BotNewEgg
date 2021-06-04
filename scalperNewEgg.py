import time
from fake_useragent.utils import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

EMAIL = ""
PASSWORD = ""
PATH = "/Users/poiuy/Desktop/BotRTX/chromedriver"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
ua = UserAgent()
userAgent = ua.random
chrome_options.add_argument(f'user-agent={userAgent}')

driver = webdriver.Chrome(PATH,options=chrome_options)

# URL de l'item désiré
#driver.get("https://www.newegg.ca/tp-link-archer-tx50e-pci-express/p/0E6-002W-005Y8?Item=0E6-002W-005Y8&cm_sp=Homepage_dailydeals-_-P2_0E6-002W-005Y8-_-06042021")
driver.get("https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308teagle-12gd/p/N82E16814932439?Description=3080ti&cm_re=3080ti-_-14-932-439-_-Product")

buyButton = False

while not buyButton:

    try:
        #Cherche le bouton add to cart
        addToCartBtn = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-primary"))
        )
        addToCartBtn.click()
        print("Added to cart !")
        time.sleep(1)
        #Ouvre la page du panier
        driver.get("https://secure.newegg.ca/shop/cart")
        buyButton = True
        # À partir d'ici, si le bot crash l'utilisateur peut conitnuer à entrer les infos manuellement

        # Cherche le bouton paypal checkout et click dessus
        checkoutBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"paypal-button"))
        )
        checkoutBtn.click()
        driver.switch_to.window(driver.window_handles[1])

        emailField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"login_email"))
        )
        emailField.click()
        emailField.send_keys(EMAIL)
        print("write email")
        time.sleep(1)

        nextBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID,"btnNext"))
        )
        nextBtn.click()
        time.sleep(2)
        passwordField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"login_password"))
        )
        print("write password")
        passwordField.send_keys(PASSWORD)

        print("test")
        btnLogin = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID,"btnLogin"))
        )
        btnLogin.click()

        # --------- LA FUNCTION CI-DESSOUS VALIDE LE PAIEMENT -------------

        btnPayment = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID,"payment-submit-btn"))
        )
        btnPayment.click()

    except:
        # Refresh page after a delay
        if(buyButton == False):
            time.sleep(1)
            print("sold out...")
            driver.refresh()
