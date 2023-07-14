from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@given('Open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()

