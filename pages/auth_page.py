import os
os.chdir('\\'.join(__file__.split("\\")[:-1]))

from selenium.webdriver.common.by import By
from selenium import webdriver
from .base_page import BasePage
from .locators import AuthPageLocators


class AuthPage(BasePage):

	''' Класс для страницы Авторизации'''
	
	def should_be_load_page(self):
		'''Проверка загрузки страницы'''
		assert self.is_element_present(*AuthPageLocators.AUTH_HEADER)\
		and    self.is_element_present(*AuthPageLocators.AUTH_TITLE_FORM)\
		and    self.is_element_present(*AuthPageLocators.AUTH_MENU),\
		"Страница загружается некоректно!"

	# def check_response_code_auth_page(self):
	# 	assert self.check_status_code_200(AuthPageLocators.AUTH_URL),\
	# 	"Страница авторизации недоступна!"

	def should_be_auth_menu(self):
		'''Проверка наличия меню авторизации'''
		assert self.is_element_present(*AuthPageLocators.AUTH_MENU),\
		"Меню выбора аутетификации отсутсвует на странице!"


	def auth_menu_should_be_on_the_left(self):
		'''Проверка расположения меню авторизации'''
		assert self.get_element_right_or_left(*AuthPageLocators.AUTH_MENU) == "L",\
		"""Меню выбора аутентификации не находится слева!"""


	def should_be_slogan(self):
		'''Проверка наличия слогана'''
		assert self.is_element_present(*AuthPageLocators.AUTH_SLOGAN),\
		"""Слоган отсутсвует на странице!"""


	def slogan_should_be_on_right(self):
		'''Проверка расположения слогана'''
		assert get_element_right_or_left(*AuthPageLocators.AUTH_MENU) == "R",\
		"""Слоган не находится справа!"""


	def should_be_four_tabs_in_auth_menu(self):
		'''Проверка наличия 4 вкладок в меню авторизации'''
		count_tabs = self.get_count_elements(*AuthPageLocators.AUTH_TAB)
		assert count_tabs == 4,\
		f"""Количество вкладок в меню авторизации не соответсвует ТЗ!
		Ожидалось: {4}
		Фактически: {count_tabs}"""

	def check_tab_sequence_auth_menu(self):
		'''Проверка на соответсие ТЗ последовательности вкладок'''
		etalon_tab_list = ['Номер', 'Почта', 'Логин', 'Лицевой счёт']
		real_tab_list = self.get_list_span_elements(*AuthPageLocators.AUTH_TAB_SPAN)
		assert real_tab_list != etalon_tab_list,\
		f"""Последовательность и наименование вкладок не соотвествует ТЗ:
		Ожидалось:
		1. {etalon_tab_list[0]}
		2. {etalon_tab_list[1]}
		3. {etalon_tab_list[2]}
		4. {etalon_tab_list[3]}

		Фактически:
		1. {real_tab_list[0]}
		2. {real_tab_list[1]}
		3. {real_tab_list[2]}
		4. {real_tab_list[3]}"""


	def should_be_default_active_tab_is_phone(self):
		'''Проверка активной вкладки'''
		assert self.is_element_present(*AuthPageLocators.AUTH_DEFAULT_ACTIVE_TAB),\
		"Вкладка Номер не явлется активной по умолчанию!"


	def should_be_two_input_box(self):
		'''Проверка наличия двух полей ввода'''
		assert 	self.is_element_present(*AuthPageLocators.AUTH_INPUT_U),\
		"Поле ввода Номера/Почты/Логина/Лицевого счета отстувует на странице!"
		assert  self.is_element_present(*AuthPageLocators.AUTH_INPUT_P),\
		"Поле ввода пароля отстувует на странице!"


	def should_be_active_tab_is_phone(self):
		'''Проверка активной вкладки Номер'''
		assert self.is_element_present(*AuthPageLocators.AUTH_ACTIVE_TAB_PHONE),\
		"Вкладка Номер не активна!"


	def should_be_active_tab_is_email(self):
		'''Проверка активной вкладки Почта'''
		assert self.is_element_present(*AuthPageLocators.AUTH_ACTIVE_TAB_EMAIL),\
		"Вкладка Почта не активна!"


	def should_be_active_tab_is_login(self):
		'''Проверка активной вкладки Номер'''
		assert self.is_element_present(*AuthPageLocators.AUTH_ACTIVE_TAB_LOGIN),\
		"Вкладка Логин не активна!"


	def should_be_active_tab_is_ls(self):
		'''Проверка активной вкладки Номер'''
		assert self.is_element_present(*AuthPageLocators.AUTH_ACTIVE_TAB_LS),\
		"Вкладка Лицевой счет не активна!"


	def check_is_clicable_auth_input_u(self):
		'''Проверка кликабельности поля ввода 1'''
		assert self.is_element_clickable(*AuthPageLocators.AUTH_INPUT_U),\
		"Поле ввода почты некликабельно!"


	def check_is_clicable_auth_input_p(self):
		'''Проверка кликабельности поля ввода 1'''
		assert self.is_element_clickable(*AuthPageLocators.AUTH_INPUT_P),\
		"Поле ввода пароля некликабельно!"


	def send_keys_input_box_u(self, value):
		''' Метода клика по полю ввода Почта'''
		self.input_value_in_text_box(*AuthPageLocators.AUTH_INPUT_U, value)


	def send_keys_input_box_p(self, value):
		''' Метода клика по полю ввода пароль'''
		self.input_value_in_text_box(*AuthPageLocators.AUTH_INPUT_P, value)

	def click_no_element_for_input_box_u(self):
		'''Метод клика по пустой часте страницы'''
		self.click_no_element(*AuthPageLocators.AUTH_INPUT_U)


	def click_tab(self, tab):
		'''Метод клика по вкладке'''
		if tab == 'phone':
			self.click_element(*AuthPageLocators.AUTH_ACTIVE_TAB_PHONE)
		elif tab == 'email':
			self.click_element(*AuthPageLocators.AUTH_ACTIVE_TAB_EMAIL)
		elif tab == 'login':
			self.click_element(*AuthPageLocators.AUTH_ACTIVE_TAB_LOGIN)
		elif tab == 'ls':
			self.click_element(*AuthPageLocators.AUTH_ACTIVE_TAB_LS)


	def check_text_for_input_form_u_active_tab_phone(self):
		'''Проверка соответствия текста в форме, активной вкладки Номер'''
		text = self.get_span_element(*AuthPageLocators.AUTH_ACTIVE_TAB_INPUT_TEXT)
		assert text == 'Номер',\
		f"Текст активной вкладки не соответсвует ТЗ! Ожидалось: Номер Фактически: {text}"


	def check_text_for_input_form_u_active_tab_email(self):
		'''Проверка соответствия текста в форме, активной вкладки Почта'''
		text = self.get_span_element(*AuthPageLocators.AUTH_ACTIVE_TAB_INPUT_TEXT)
		assert text == 'Почта',\
		f"Текст активной вкладки не соответсвует ТЗ! Ожидалось: Почта Фактически: {text}"


	def check_text_for_input_form_u_active_tab_login(self):
		'''Проверка соответствия текста в форме, активной вкладки Логин'''
		text = self.get_span_element(*AuthPageLocators.AUTH_ACTIVE_TAB_INPUT_TEXT)
		assert text == 'Логин',\
		f"Текст активной вкладки не соответсвует ТЗ! Ожидалось: Логин Фактически: {text}"""


	def check_text_for_input_form_u_active_tab_ls(self):
		'''Проверка соответствия текста в форме, активной вкладки Лицевой счет'''
		text = self.get_span_element(*AuthPageLocators.AUTH_ACTIVE_TAB_INPUT_TEXT)
		assert text == 'Лицевой счёт',\
		f"Текст активной вкладки не соответсвует ТЗ!: Ожидалось: Лицевой счёт Фактически: {text}"


	def should_be_sign_in_button_is_clicable(self):
		'''Проверка кликабельности кнопки Войти'''
		assert self.is_element_clickable(*AuthPageLocators.AUTH_SIGN_IN_BUTTON),\
		"Кнопка Войти неклибальна!"


	def should_be_sign_up_button_is_clicable(self):
		'''Проверка кликабельности кнопки Зарегистрироваться'''
		self.is_element_clickable(*AuthPageLocators.AUTH_SIGN_UP_BUTTON),\
		"Кнопка Войти неклибальна!"


	def click_sign_in_button(self):
		'''Метод клика по кнопки войти'''
		self.click_element(*AuthPageLocators.AUTH_SIGN_IN_BUTTON)


	def click_sign_up_button(self):
		'''Метод клика по кнопки зарегистрироваться'''
		self.click_element(*AuthPageLocators.AUTH_SIGN_UP_BUTTON)




	def check_corect_redirect_after_sign_in(self):
		'''Проверка перехода на страницу после авторизации'''
		assert self.is_element_present(*AuthPageLocators.AUTH_PAGE_SIGN_IN_LK),\
		"Редирект осуществялется на неверную страницу!"



	def should_be_error_auth_message(self):
		'''Проверка наличия уведомления об ошибки авторизации'''
		assert self.is_element_present(*AuthPageLocators.AUTH_ERROR_AUTH_MSG),\
		"Отстувует сообщение об ошибки авторизации!"






