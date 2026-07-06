import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from config import config


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    if config.HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    service = ChromeService(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)

    yield drv

    drv.quit()


@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(request, driver=None):
    
    yield
    if request.node.rep_call.failed if hasattr(request.node, "rep_call") else False:
        try:
            import allure
            drv = request.node.funcargs.get("driver")
            if drv:
                allure.attach(
                    drv.get_screenshot_as_png(),
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )
        except Exception:
            pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
