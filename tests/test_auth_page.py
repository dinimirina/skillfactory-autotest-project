#  python -m pytest -v --tb=line tests\test_auth_page.py


import os
import sys
sys.path.append('..\\')
os.chdir('\\'.join(__file__.split("\\")[:-1]))


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from pages.locators import AuthPageLocators


@pytest.mark.xfail()
def test_check_location_auth_menu(browser):
	'''RT-A-01'''
	url = AuthPageLocators.AUTH_URL
	page = AuthPage(browser, url)
	page.open()
	page.should_be_load_page()
	page.should_be_auth_menu()
	page.auth_menu_should_be_on_the_left()

@pytest.mark.xfail()
def test_check_location_slogan(browser):
	'''RT-A-02'''
	url = AuthPageLocators.AUTH_URL
	page = AuthPage(browser, url)
	page.open()
	page.should_be_load_page()
	page.should_be_slogan()
	page.slogan_should_be_on_right()



def test_availability_and_sequence_tabs_auth_menu(browser):
	'''RT-A-03'''
	url = AuthPageLocators.AUTH_URL
	page = AuthPage(browser, url)
	page.open()
	page.should_be_load_page()
	page.should_be_four_tabs_in_auth_menu()
	page.check_tab_sequence_auth_menu()


def test_default_active_tab(browser):
	'''RT-A-04'''
	url = AuthPageLocators.AUTH_URL
	page = AuthPage(browser, url)
	page.open()
	page.should_be_load_page()
	page.should_be_default_active_tab_is_phone()


def test_presence_of_two_input_box(browser):
	'''RT-A-05'''
	url = AuthPageLocators.AUTH_URL
	page = AuthPage(browser, url)
	page.open()
	page.should_be_load_page()
	page.should_be_two_input_box()


def test_auto_tab_change_data_type_email(browser):
	'''RT-A-06'''
	url = AuthPageLocators.AUTH_URL
	page = AuthPage(browser, url)
	page.open()
	page.should_be_load_page()
	page.check_is_clicable_auth_input_u()
	page.send_keys_input_box_u('exmaple@email.ru')
	page.click_no_element_for_input_box_u()
	page.should_be_active_tab_is_email()


def test_auto_tab_change_data_type_phone(browser):
	'''RT-A-07'''
	url = AuthPageLocators.AUTH_URL
	page = AuthPage(browser, url)
	page.open()
	page.should_be_load_page()
	page.click_tab('email')
	page.check_is_clicable_auth_input_u()
	page.send_keys_input_box_u('+79821113344')
	page.click_no_element_for_input_box_u()
	page.should_be_active_tab_is_phone()


def test_auto_tab_change_data_type_login(browser):
	'''RT-A-08'''
	url = AuthPageLocators.AUTH_URL
	page = AuthPage(browser, url)
	page.open()
	page.should_be_load_page()
	page.click_tab('email')
	page.check_is_clicable_auth_input_u()
	page.send_keys_input_box_u('Login')
	page.click_no_element_for_input_box_u()
	page.should_be_active_tab_is_login()


def test_auto_tab_change_data_type_ls(browser):
	'''RT-A-09'''
	url = AuthPageLocators.AUTH_URL
	page = AuthPage(browser, url)
	page.open()
	page.should_be_load_page()
	page.click_tab('login')
	page.check_is_clicable_auth_input_u()
	page.send_keys_input_box_u('123456789122')
	page.click_no_element_for_input_box_u()
	page.should_be_active_tab_is_ls()

@pytest.mark.xfail()
def test_check_active_tab_and_input_text(browser):
	'''RT-A-10'''
	url = AuthPageLocators.AUTH_URL
	page = AuthPage(browser, url)
	page.open()
	page.should_be_load_page()
	page.click_tab('phone')
	page.check_text_for_input_form_u_active_tab_phone()
	page.click_tab('email')
	page.check_text_for_input_form_u_active_tab_email()
	page.click_tab('login')
	page.check_text_for_input_form_u_active_tab_login()
	page.click_tab('ls')
	page.check_text_for_input_form_u_active_tab_ls()



def test_authorization_registered_user(browser):
	'''RT-A-11'''
	url = AuthPageLocators.AUTH_URL
	page = AuthPage(browser, url)
	page.open()
	page.click_tab('email')
	page.should_be_active_tab_is_email()
	page.check_is_clicable_auth_input_u()
	page.send_keys_input_box_u('sifeje8923@otanhome.com')
	page.check_is_clicable_auth_input_p()
	page.send_keys_input_box_p('NWknA7s5insJuEg')
	page.should_be_sign_in_button_is_clicable()
	page.click_sign_in_button()
	page.check_corect_redirect_after_sign_in()



def test_authorization_no_registered_user(browser):
	'''RT-A-12'''
	url = AuthPageLocators.AUTH_URL
	page = AuthPage(browser, url)
	page.open()
	page.click_tab('email')
	page.should_be_active_tab_is_email()
	page.check_is_clicable_auth_input_u()
	page.send_keys_input_box_u('notaut@mail.ru')
	page.check_is_clicable_auth_input_p()
	page.send_keys_input_box_p('QWERTY')
	page.should_be_sign_in_button_is_clicable()
	page.click_sign_in_button()
	page.should_be_error_auth_message()

