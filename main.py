from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def main():
    headless_browser()
    # images_directory()
    # chrome_driver()

    quiting()

def headless_browser():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    driver.get("https://google.com")
    
    print("Headless browser access", "\n")

def images_directory():
    import os
    path = os.getcwd() + "\Images"

    isExist = os.path.exists(path)
    print("Searching for", path, "\n", "Located?", isExist, "\n")

    if not isExist:
        os.makedirs(path)
        print("Directory is created:")
        print("Directory |", os.listdir())

def chrome_driver():
    import os
    path = os.getcwd() + "\chromedriver.exe"
    
    isExist = os.path.exists(path)
    print("Searching for", path, "\n", "Located?", isExist)

    if not isExist:
        # os.makedirs(path)
        print("   ----------")
        print("   1. Navitate to following page and grab google version:     chrome://version")
        print("   2. Download corresponding driver found here:               https://sites.google.com/chromium.org/driver/")
        print("   3. Save or move the 'chromedriver.exe' file in:           ", path)
        print("   ----------", "\n")

def quiting():
    from sys import exit
    sleep( 5 )
    print("Exiting in:")
    sleep( 1 )
    print("3")
    sleep( 1 )
    print("2")
    sleep( 1 )
    print("1")
    sleep( 1 )
    exit()

if __name__ == "__main__":
    main()
    quit()