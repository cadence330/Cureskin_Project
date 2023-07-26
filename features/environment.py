from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.chrome.options import Options


def browser_init(context):
    """
    :param context: Behave context
    """
    service = Service(executable_path=r'C:\Users\domon\OneDrive\Desktop\Cureskin Project\chromedriver.exe')

    # Headless Mode
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode without a GUI
    # chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional)

    # Drivers
    context.driver = webdriver.Chrome(service=service, options=None)
    # context.driver = webdriver.Firefox(executable_path=r'C:\Users\domon\OneDrive\Desktop\Cureskin Project\
    # geckodriver.exe')

    context.driver.maximize_window()

    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
