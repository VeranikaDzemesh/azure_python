import allure
import pytest
from allure_commons.types import AttachmentType


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'setup' and rep.failed:
        print(f"Set up has failed: {rep.nodeid}")
    if rep.when == 'call' and rep.failed:
        allure.attach(rep.capstderr, name='Stderr', attachment_type=AttachmentType.TEXT)
        allure.attach(rep.capstdout, name='Stdout', attachment_type=AttachmentType.TEXT)
        print(f"Test failed: {rep.nodeid}")