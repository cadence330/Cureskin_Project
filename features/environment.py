from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.chrome.options import Options
from support.logger import logger
import allure
from allure_commons.types import AttachmentType


# Allure command:
# python3 -m behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/main_page_tests.feature


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
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

    #### BROWSERSTACK ####
    desired_cap = {
        'browser': 'Chrome',
        'os_version': '11',
        'os': 'Windows',
        'name': test_name
    }
    bs_user = 'domonicdavis_fPl95A'
    bs_key = 'yBJZyz2qsiTg7xotNiuh'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

    context.driver.implicitly_wait(5)


def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # Documentation: https://www.browserstack.com/docs/automate/selenium/view-test-results/mark-tests-as-pass-fail
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": '
        #     '{"status":"failed", "reason": "Step failed"}}'
        # )

        # Attach a screenshot to Allure report in case the step fails:
        # allure.attach(
        #     context.driver.get_screenshot_as_png(),
        #     name=f'{step.name}.png',
        #     attachment_type=AttachmentType.PNG
        # )


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
