import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import json
import os

data = None


def before_scenario(context, scenario):
    global data
    folder = os.getcwd()
    f = open(folder + '\\resources\\config.json', 'rt')
    data = json.load(f)

    if data["testConfig"]["execute"] == "Ui":
        if data["testConfig"]["browser"] == "chrome":
            chrome_options = Options()
            if data["testConfig"]["headlessMode"] == "Yes":
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--start-maximized")
            context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                              chrome_options=chrome_options)
        elif data["testConfig"]["browser"] == "firefox":
            context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif data["testConfig"]["browser"] == "ie":
            context.driver = webdriver.Ie(service=Service(IEDriverManager().install()))
        else:
            print('Browser not yet implemented - ' + data["testConfig"]["browser"])
            raise Exception('Browser not yet implemented - ' + data["testConfig"]["browser"])
        context.driver.get(data["appConfig"]["webBaseURL"])


def after_step(context, step):
    if data["testConfig"]["execute"] == "Ui":
        if step.status == "failed":
            allure.attach(context.driver.get_screenshot_as_png(),
                          name=step.name, attachment_type=allure.attachment_type.PNG)


def after_scenario(context, scenario):
    if data["testConfig"]["execute"] == "Ui":
        context.driver.quit()
