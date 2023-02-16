import os

os.chdir('\\'.join(__file__.split("\\")[:-1]))

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
# from .locators import BasePageLocators


class BasePage(): 


	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

	def open(self):
		self.browser.get(self.url)

	def get_url(self):
		'''Метод получения текущего URL страницы'''
		return self.browser.current_url


	def check_status_code_200(self, url):
		'''
		Данная функция провряет, что ресурс доступен
		'''
		import requests

		response = requests.get(url)

		if response.status_code == 200:
			return True




	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True


	def is_not_element_present(self, how, what, timeout=5):
		try:
			WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True

		return False


	def get_element_location(self, how, what):
		'''Данный метод возвращает координаты элемента'''
		return self.browser.find_element(how,what).location


	def get_element_right_or_left(self, how, what):
		'''
		Данный метод опредяется справа или слева находится элемент
		'''
		location = self.get_element_location(how, what)

		if location['x'] > 0:
			return "R" 

		elif location['x'] < 0:
			return "L"


	def get_count_elements(self, how, what):
		'''
		Данный метод позволяет определить количество элементов на странице
		'''
		return len(self.browser.find_elements(how, what))


	def get_span_element(self, how, what):
		return self.browser.find_element(how, what).text


	def get_list_span_elements(self, how, what):
		'''Данный метод возращает текст элементов в виде списка'''
		elements = self.browser.find_elements(how, what)
		list_span_elements = [element.text for element in elements]
		return list_span_elements

	def is_element_clickable(self, how, what, timeout=4):
		'''Данный метод проверяет кликабельность элемента'''
		try:
			WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
		except TimeoutException:
			return False

		return True


	def input_value_in_text_box(self, how, what, value):
		'''Данный метод осущестявлет ввод значения в поле ввода'''
		input_box = self.browser.find_element(how, what)
		for char in value:
			input_box.send_keys(char)


	def click_element(self, how, what):
		self.browser.find_element(how,what).click()


	def click_no_element(self, how, what):
		element = self.browser.find_element(how, what)
		action = ActionChains(self.browser)
		action.move_to_element_with_offset(element, -122, 0).click().perform()