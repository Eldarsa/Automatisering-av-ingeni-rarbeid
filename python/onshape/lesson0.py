from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome import webdriver
driver = webdriver.WebDriver(ChromeDriverManager().install())

driver.get("https://cad.onshape.com/documents/134ceaa9538ff7ed8226dd9c/w/f54cb266b299aaff0f3c9681/e/3c7b41e5709f97c5b437ffb6?configuration=List_W3iASF43O2szfb%3DDefault%3Bdiameter%3D0.854%2Bmeter%3Bheight%3D0.127%2Bmeter")