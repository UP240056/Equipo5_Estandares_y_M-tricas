import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    """Fixture de pytest encargada del ciclo de vida del WebDriver bajo aislamiento estricto."""
    chrome_options = Options()
    
    # Comenta la siguiente linea poniendole un '#' al inicio si quieres ver el navegador abrirse en tu pantalla:
    chrome_options.add_argument("--headless") 
    
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(0)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()