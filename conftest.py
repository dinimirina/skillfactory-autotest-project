import os 

os.chdir('\\'.join(__file__.split("\\")[:-1]))


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
# pytest -s -v test_items.py по умолчанию запустится как:
# pytest -s -v --browser_name=firefox --language=es test_items.py


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
	'''
	Данная функция помогает сохранить статус прохождения теста
	'''

	outcome = yield
	rep = outcome.get_result()
	setattr(item, "rep_" + rep.when, rep)
	return rep


@pytest.fixture(scope="function")
def browser(request):
	path = r"C:\СОФТ\geckodriver-v0.32.2-win64"
	options = Options()
	options.binary_location = "C:\\Program Files\\LibreWolf\\librewolf.exe"
	print("\nstart firefox browser for test..")
	# FirefoxProfile = webdriver.FirefoxProfile()
	# options.set_preference("intl.accept_languages", browser_lang)
	browser = webdriver.Firefox(path, options = options) 
	yield browser
	print("\nquit browser..")
	browser.quit()


def get_test_case_docstring(item):
	"""Данная функция получает docstring из тест-кейса
	   и форматирует для того, чтобы отборажать ее вместо названия функции тест-кейса.
	"""

	full_name = ''

	if item._obj.__doc__:
		# Remove extra whitespaces from the doc string:
		name = str(item._obj.__doc__.split('.')[0]).strip()
		full_name = ' '.join(name.split())

		# Generate the list of parameters for parametrized test cases:
		if hasattr(item, 'callspec'):
			params = item.callspec.params

			res_keys = sorted([k for k in params])
			# Create List based on Dict:
			res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
			# Add dict with all parameters to the name of test case:
			full_name += ' Parameters ' + str(', '.join(res))
			full_name = full_name.replace(':', '')

	return full_name


def pytest_itemcollected(item):
	"""Данная функция меняте название тест-кейсов "on the fly"
		во время их выполнения.
	"""

	if item._obj.__doc__:
		item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
	""" This function modified names of test cases "on the fly"
		when we are using --collect-only parameter for pytest
		(to get the full list of all existing test cases).
	"""

	if session.config.option.collectonly is True:
		for item in session.items:
			# If test case has a doc string we need to modify it's name to
			# it's doc string to show human-readable reports and to
			# automatically import test cases to test management system.
			if item._obj.__doc__:
				full_name = get_test_case_docstring(item)
				print(full_name)

		pytest.exit('Done!')