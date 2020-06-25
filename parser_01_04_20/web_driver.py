from selenium import webdriver


def get_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path="/home/mukola/Documents/courses/chromedriver", options=options)
    return driver


driver = get_web_driver()
