import os
os.chdir('\\'.join(__file__.split("\\")[:-1]))

from selenium.webdriver.common.by import By
from selenium import webdriver
from .base_page import BasePage
from .auth_page import AuthPage
from .locators import RegPageLocators, AuthPageLocators


class RegPage(AuthPage):

	''' Класс для страницы регистрации'''


	def check_correct_load_page(self):
		'''Проверка корректной загрузки страницы'''
		assert self.is_element_present(*RegPageLocators.REG_TITTLE),\
		"Страница загружается некорректно!"


	def should_be_reg_form(self):
		'''Проверка наличия формы регистрации'''
		assert self.is_element_present(*RegPageLocators.REG_FORM),\
		"Форма регистрации отсутсвует на странице!"


	def should_be_reg_form_on_right(self):
		'''Проверка расположения формы авторизации'''
		assert self.get_element_right_or_left(*RegPageLocators.REG_FORM) == "R",\
		"Форма регистрации не находится справа!"


	def should_be_slogan(self):
		'''Проверка наличия слогана'''
		assert self.is_element_present(*RegPageLocators.REG_SLOGAN),\
		"""Слоган отсутсвует на странице!"""


	def should_be_slogan_on_left(self):
		'''Проверка расположения слогана'''
		assert get_elemet_right_or_left(*AuthPageLocators.AUTH_MENU) == "L",\
		"""Слоган не находится слева!"""


	def should_be_reg_form_input_boxs(self):
		'''Проверка наличия полей регистрации'''
		assert self.is_element_present(*RegPageLocators.REG_INPUT_BOX_FIRST_NAME),\
		"Поле ввода имени отсутствует на странице!"
		assert self.is_element_present(*RegPageLocators.REG_INPUT_BOX_LAST_NAME),\
		"Поле ввода фамилии отсутствует на странице!"
		assert self.is_element_present(*RegPageLocators.REG_INPUT_DROPDOWN_REGIN),\
		"Поле выбора региона отсутствует на странице!"
		assert self.is_element_present(*RegPageLocators.REG_INPUT_BOX_EMAIL_OR_PHONE),\
		"Поле ввода Email или телефона отсутствует на странице!"
		assert self.is_element_present(*RegPageLocators.REG_INPUT_BOX_PASSWORD),\
		"Поле ввода пароля отсутствует на странице!"
		assert self.is_element_present(*RegPageLocators.REG_INPUT_BOX_PASSWORD_CONFIRM),\
		"Поле ввода подтверждения пароля отсутствует на странице!"


	def should_be_continue_button(self):
		'''Проверка наличия кнопки Продолжить'''
		assert self.is_element_present(*RegPageLocators.REG_CONTINUE_BUTTON),\
		"Кнопка Продолжить регистрацию отсутствует на странице!"


	def should_be_confirm_email_title(self):
		'''Проверка редиректа на подверждение почты'''
		assert self.is_element_present(*RegPageLocators.REG_EMAIL_CONFIRM_TITLE),\
		"Редирект на подверждение почты не производится!"


	def check_name_continue_button(self):
		'''Проверка наименования кнопки Продолжить'''
		text_button = self.get_span_element(*RegPageLocators.REG_CONTINUE_BUTTON)
		assert text_button  == "Продолжить",\
		"Наименование кнопки продолжения регистрации не соотвествует ТЗ! Ожидалось: Продолжить Фактичиски: {text_button}"


	def check_is_clicable_reg_input_first_name(self):
		'''Проверка кликабельности поля ввода имени'''
		assert self.is_element_clickable(*RegPageLocators.REG_INPUT_BOX_FIRST_NAME),\
		"Поле ввода имени некликабельно!"

	def check_is_clicable_reg_input_last_name(self):
		'''Проверка кликабельности поля ввода фамилии'''
		assert self.is_element_clickable(*RegPageLocators.REG_INPUT_BOX_LAST_NAME),\
		"Поле ввода фамилии некликабельно!"


	def check_is_clicable_reg_dropdown_region(self):
		'''Проверка кликабельности поля ввода фамилии'''
		assert self.is_element_clickable(*RegPageLocators.REG_INPUT_DROPDOWN_REGIN),\
		"Поле ввода фамилии некликабельно!"


	def check_is_clicable_click_continiue_registration_button(self):
		assert self.is_element_clickable(*RegPageLocators.REG_CONTINUE_BUTTON),\
		"Кнопка продолжить регистрацию некликабельна!"



	def should_be_first_name_validation_msg(self):
		'''Проверка наличия валидационного сообщения на Имя'''
		assert self.is_element_present(*RegPageLocators.REG_FIRST_NAME_VALIDATION_MESSAGE),\
		"Валидация по полю Имя пройдена!"


	def should_be_last_name_validation_msg(self):
		'''Проверка наличия валидационного сообщения на Фамилия'''
		assert self.is_element_present(*RegPageLocators.REG_LAST_NAME_VALIDATION_MESSAGE),\
		"Валидация по полю Фамилия пройдена!"


	def should_be_email_or_phone_validation_msg(self):
		'''Проверка наличия валидационного сообщения на Почта'''
		assert self.is_element_present(*RegPageLocators.REG_EMAIL_OR_PHONE_VALIDATION_MESSAGE),\
		"Валидация по полю Почта пройдена!"


	def should_be_password_validation_msg(self):
		'''Проверка наличия валидационного сообщения на Пароль'''
		assert self.is_element_present(*RegPageLocators.REG_PASSWORD_VALIDATION_MESSAGE),\
		"Валидация по полю Пароль пройдена!"


	def should_be_password_confirm_validation_msg(self):
		'''Проверка наличия валидационного сообщения на подтвердить пароль'''
		assert self.is_element_present(*RegPageLocators.REG_PASSWORD_CONFIRM_VALIDATION_MESSAGE),\
		"Валидация по полю потдерждения пароля пройдена!"


	def should_not_be_first_name_validation_msg(self):
		'''Проверка отсутсвия валидационного сообщения на Имя'''
		assert self.is_not_element_present(*RegPageLocators.REG_FIRST_NAME_VALIDATION_MESSAGE),\
		"Валидация по полю Имя не пройдена!"


	def should_not_be_last_name_validation_msg(self):
		'''Проверка отсутсвия валидационного сообщения на Фамилия'''
		assert self.is_not_element_present(*RegPageLocators.REG_LAST_NAME_VALIDATION_MESSAGE),\
		"Валидация по полю Фамилия не пройдена!"


	def should_not_be_email_or_phone_validation_msg(self):
		'''Проверка отсутсвия валидационного сообщения на Почта'''
		assert self.is_not_element_present(*RegPageLocators.REG_EMAIL_OR_PHONE_VALIDATION_MESSAGE),\
		"Валидация по полю Почта не пройдена!"


	def should_not_be_password_validation_msg(self):
		'''Проверка отсутсвия валидационного сообщения на Пароль'''
		assert self.is_not_element_present(*RegPageLocators.REG_EMAIL_OR_PHONE_VALIDATION_MESSAGE),\
		"Валидация по полю Пароль не пройдена!"


	def should_not_be_password_confirm_validation_msg(self):
		'''Проверка отсутсвия валидационного сообщения на подтвердить пароль'''
		assert self.is_not_element_present(*RegPageLocators.REG_PASSWORD_CONFIRM_VALIDATION_MESSAGE),\
		"Валидация по полю потдерждения пароля пройдена!"



	


	def send_keys_input_box_first_name(self, value):
		'''Метод ввода знаений в поля имя'''
		self.input_value_in_text_box(*RegPageLocators.REG_INPUT_BOX_FIRST_NAME, value)


	def send_keys_input_box_last_name(self, value):
		'''Метод ввода знаений в поля фамилия'''
		self.input_value_in_text_box(*RegPageLocators.REG_INPUT_BOX_LAST_NAME, value)

	def send_keys_input_box_password(self, value):
		'''Метод ввода знаений в поля пароль'''
		self.input_value_in_text_box(*RegPageLocators.REG_INPUT_BOX_PASSWORD, value)

	def send_keys_input_box_for_email_or_phone_reg(self, value):
		'''Метод заполнения поля почта или номер'''
		self.input_value_in_text_box(*RegPageLocators.REG_INPUT_BOX_EMAIL_OR_PHONE, value)


	def send_keys_input_box_password_confirm(self, value):
		'''Метод ввода знаений в поля подтвердить пароль'''
		self.input_value_in_text_box(*RegPageLocators.REG_INPUT_BOX_PASSWORD_CONFIRM, value)


	def send_keys_input_confirm_code(self, value):
		'''Метод ввода подверждающего кода'''
		self.input_value_in_text_box(*RegPageLocators.REG_INPUT_BOX_CONFIRM_CODE, value)


	def click_no_element_for_reg(self):
		'''Метод клика по пустой часте страницы'''
		self.click_no_element(*RegPageLocators.REG_INPUT_BOX_FIRST_NAME)



	def click_continiue_registration_button(self):
		'''Метод клика по кнопки продолжить регистрацию'''
		self.click_element(*RegPageLocators.REG_CONTINUE_BUTTON)


	def send_confirm_code(self, value):
		elem = self.browser.find_element(*RegPageLocators.REG_INPUT_BOX_CONFIRM_CODE)
		elem.send_keys(value)
