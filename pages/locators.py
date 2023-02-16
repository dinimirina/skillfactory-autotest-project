from selenium.webdriver.common.by import By


class BasePageLocators():
	''' Локаторы Базовой страницы'''
	pass


class AuthPageLocators():
	'''Локаторы страницы авторизации'''

	AUTH_URL = "https://b2c.passport.rt.ru"

	AUTH_HEADER = (By.XPATH, "/html/body/div[1]/header/div")

	AUTH_TITLE_FORM = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/h1")

	AUTH_MENU = (By.XPATH, "/html/body/div[1]/main/section[2]/div")

	AUTH_SLOGAN = (By.XPATH, "/html/body/div[1]/main/section[1]/div/div[2]/p")

	AUTH_TAB = (By.CSS_SELECTOR, ".rt-tab.rt-tab")

	AUTH_TAB_SPAN = (By.CSS_SELECTOR, ".rt-tab.rt-tab > span")

	AUTH_DEFAULT_ACTIVE_TAB = (By.CSS_SELECTOR, "#t-btn-tab-phone.rt-tab--active")

	AUTH_INPUT_U = (By.XPATH, '//*[@id="username"]')

	AUTH_INPUT_P = (By.XPATH, '//*[@id="password"]')

	AUTH_ACTIVE_TAB_EMAIL = (By.CSS_SELECTOR, "#t-btn-tab-mail.rt-tab--active")

	AUTH_ACTIVE_TAB_PHONE = AUTH_DEFAULT_ACTIVE_TAB

	AUTH_ACTIVE_TAB_LOGIN = (By.CSS_SELECTOR, "#t-btn-tab-login.rt-tab--active")

	AUTH_ACTIVE_TAB_LS = (By.CSS_SELECTOR, "#t-btn-tab-ls.rt-tab--active")

	AUTH_ACTIVE_TAB_INPUT_TEXT = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/span[2]")

	AUTH_ACTIVE_TAB_EMAIL = (By.CSS_SELECTOR, "#t-btn-tab-mail")

	AUTH_ACTIVE_TAB_PHONE = (By.CSS_SELECTOR, "#t-btn-tab-phone")

	AUTH_ACTIVE_TAB_LOGIN = (By.CSS_SELECTOR, "#t-btn-tab-login")

	AUTH_ACTIVE_TAB_LS = (By.CSS_SELECTOR, "#t-btn-tab-ls")

	AUTH_SIGN_IN_BUTTON = (By.XPATH, '//*[@id="kc-login"]')

	AUTH_SIGN_UP_BUTTON = (By.XPATH, '//*[@id="kc-register"]')

	AUTH_PAGE_SIGN_IN_LK = (By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/h3")

	AUTH_ERROR_AUTH_MSG = (By.XPATH, '//*[@id="form-error-message"]')



class RegPageLocators():

	REG_TITTLE = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/h1")

	REG_FORM = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form")

	REG_SLOGAN = (By.XPATH, "/html/body/div[1]/main/section[1]/div/div[2]/p")

	REG_INPUT_BOX_FIRST_NAME = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div/input")

	REG_INPUT_BOX_LAST_NAME = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/div/input")

	REG_INPUT_DROPDOWN_REGIN = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/div/input")

	REG_INPUT_BOX_EMAIL_OR_PHONE = (By.XPATH, '//*[@id="address"]')

	REG_INPUT_BOX_PASSWORD = (By.XPATH, '//*[@id="password"]')

	REG_INPUT_BOX_PASSWORD_CONFIRM = (By.XPATH, '//*[@id="password-confirm"]')

	REG_CONTINUE_BUTTON = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/button")

	REG_FIRST_NAME_VALIDATION_MESSAGE = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/span")

	REG_LAST_NAME_VALIDATION_MESSAGE = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/span")

	REG_EMAIL_OR_PHONE_VALIDATION_MESSAGE = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/span")

	REG_PASSWORD_VALIDATION_MESSAGE = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/span")

	REG_PASSWORD_CONFIRM_VALIDATION_MESSAGE = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[2]/span")

	REG_EMAIL_CONFIRM_TITLE = (By.XPATH, "/html/body/div[1]/main/section[2]/div/div/h1")


	REG_INPUT_BOX_CONFIRM_CODE = (By.XPATH, '//*[@id="rt-code-0"]')



