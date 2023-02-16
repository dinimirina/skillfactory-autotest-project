# python -m pytest -v --tb=line tests\test_reg_page.py

import os
import sys
sys.path.append('..\\')
os.chdir('\\'.join(__file__.split("\\")[:-1]))

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.reg_page import RegPage
from pages.locators import AuthPageLocators, RegPageLocators
from TempMailAPI import TempMail
from supporting import generate_min_valid_password, generate_min_valid_name,\
get_confirm_code, generate_max_valid_name, gen_random_len_valid_name_plus,\
gen_latin_char_name, gen_digit_char_name, gen_punctuation_char_name, gen_no_valid_email

from time import sleep


def test_correctly_load_page(browser):
	'''RT-R-01'''
	url = AuthPageLocators.AUTH_URL
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()


def test_check_location_reg_menu(browser):
	'''RT-R-02'''
	url = AuthPageLocators.AUTH_URL
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.should_be_reg_form()
	page.should_be_reg_form_on_right()

@pytest.mark.xfail()
def test_check_location_slogan(browser):
	'''RT-R-03'''
	url = AuthPageLocators.AUTH_URL
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.should_be_slogan()
	page.should_be_slogan_on_left()



def test_check_availability_reg_boxs(browser):
	'''RT-R-04'''
	url = AuthPageLocators.AUTH_URL
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.should_be_reg_form_input_boxs()


@pytest.mark.xfail()
def test_availability_and_name_continue_button(browser):
	'''RT-R-05'''
	url = AuthPageLocators.AUTH_URL
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.should_be_continue_button()
	page.check_name_continue_button()



@pytest.mark.xfail()
def test_successful_registration_min_name(browser):
	'''RT-R-06'''
	url = AuthPageLocators.AUTH_URL
	tm = TempMail()
	email = tm.get_email_address()
	password = generate_min_valid_password()
	name = generate_min_valid_name()
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.send_keys_input_box_first_name(name)
	page.click_no_element_for_reg()
	page.should_not_be_first_name_validation_msg()
	page.send_keys_input_box_last_name(name)
	page.click_no_element_for_reg()
	page.should_not_be_last_name_validation_msg()
	page.send_keys_input_box_for_email_or_phone_reg(email)
	page.click_no_element_for_reg()
	page.should_not_be_email_or_phone_validation_msg()
	page.send_keys_input_box_password(password)
	page.click_no_element_for_reg()
	page.should_not_be_password_validation_msg()
	page.send_keys_input_box_password_confirm(password)
	page.click_no_element_for_reg()
	page.should_not_be_password_confirm_validation_msg()
	page.check_is_clicable_click_continiue_registration_button()
	page.click_continiue_registration_button()
	page.should_be_confirm_email_title()
	sleep(10) 
	confirm_code = get_confirm_code(tm.get_mailbox(email))
	page.send_confirm_code(confirm_code)
	page.check_corect_redirect_after_sign_in()


@pytest.mark.xfail()
def test_successful_registration_max_name(browser):
	'''RT-R-07'''
	url = AuthPageLocators.AUTH_URL
	tm = TempMail()
	email = tm.get_email_address()
	password = generate_min_valid_password()
	name = generate_max_valid_name()
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.send_keys_input_box_first_name(name)
	page.click_no_element_for_reg()
	page.should_not_be_first_name_validation_msg()
	page.send_keys_input_box_last_name(name)
	page.click_no_element_for_reg()
	page.should_not_be_last_name_validation_msg()
	page.send_keys_input_box_for_email_or_phone_reg(email)
	page.click_no_element_for_reg()
	page.should_not_be_email_or_phone_validation_msg()
	page.send_keys_input_box_password(password)
	page.click_no_element_for_reg()
	page.should_not_be_password_validation_msg()
	page.send_keys_input_box_password_confirm(password)
	page.click_no_element_for_reg()
	page.should_not_be_password_confirm_validation_msg()
	page.check_is_clicable_click_continiue_registration_button()
	page.click_continiue_registration_button()
	page.should_be_confirm_email_title()
	sleep(10) 
	confirm_code = get_confirm_code(tm.get_mailbox(email))
	page.send_confirm_code(confirm_code)
	page.check_corect_redirect_after_sign_in()


@pytest.mark.xfail()
def test_successful_registration_double_name(browser):
	'''RT-R-08'''
	url = AuthPageLocators.AUTH_URL
	tm = TempMail()
	email = tm.get_email_address()
	password = generate_min_valid_password()
	name = gen_random_len_valid_name_plus()
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.send_keys_input_box_first_name(name)
	page.click_no_element_for_reg()
	page.should_not_be_first_name_validation_msg()
	page.send_keys_input_box_last_name(name)
	page.click_no_element_for_reg()
	page.should_not_be_last_name_validation_msg()
	page.send_keys_input_box_for_email_or_phone_reg(email)
	page.click_no_element_for_reg()
	page.should_not_be_email_or_phone_validation_msg()
	page.send_keys_input_box_password(password)
	page.click_no_element_for_reg()
	page.should_not_be_password_validation_msg()
	page.send_keys_input_box_password_confirm(password)
	page.click_no_element_for_reg()
	page.should_not_be_password_confirm_validation_msg()
	page.check_is_clicable_click_continiue_registration_button()
	page.click_continiue_registration_button()
	page.should_be_confirm_email_title()
	sleep(10) 
	confirm_code = get_confirm_code(tm.get_mailbox(email))
	page.send_confirm_code(confirm_code)
	page.check_corect_redirect_after_sign_in()





def test_validation_of_required_fields(browser):
	'''RT-R-09'''
	url = AuthPageLocators.AUTH_URL
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.check_is_clicable_click_continiue_registration_button()
	page.click_continiue_registration_button()
	page.should_be_first_name_validation_msg()
	page.should_be_last_name_validation_msg()
	page.should_be_email_or_phone_validation_msg()
	page.should_be_password_validation_msg()
	page.should_be_password_confirm_validation_msg()




def test_validation_for_latin_characters(browser):
	'''RT-R-10'''
	url = AuthPageLocators.AUTH_URL
	name = gen_latin_char_name()
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.check_is_clicable_click_continiue_registration_button()
	page.send_keys_input_box_first_name(name)
	page.click_no_element_for_reg()
	page.should_be_first_name_validation_msg()
	page.send_keys_input_box_last_name(name)
	page.click_no_element_for_reg()
	page.should_be_last_name_validation_msg()



def test_validation_for_digit_characters(browser):
	'''RT-R-11'''
	url = AuthPageLocators.AUTH_URL
	name = gen_digit_char_name()
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.check_is_clicable_click_continiue_registration_button()
	page.send_keys_input_box_first_name(name)
	page.click_no_element_for_reg()
	page.should_be_first_name_validation_msg()
	page.send_keys_input_box_last_name(name)
	page.click_no_element_for_reg()
	page.should_be_last_name_validation_msg()




def test_validation_for_punctuation_characters(browser):
	'''RT-R-12'''
	url = AuthPageLocators.AUTH_URL
	name = gen_punctuation_char_name()
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.check_is_clicable_click_continiue_registration_button()
	page.send_keys_input_box_first_name(name)
	page.click_no_element_for_reg()
	page.should_be_first_name_validation_msg()
	page.send_keys_input_box_last_name(name)
	page.click_no_element_for_reg()
	page.should_be_last_name_validation_msg()



def test_validation_one_character(browser):
	'''RT-R-13'''
	url = AuthPageLocators.AUTH_URL
	name = generate_min_valid_name()[:-1]
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.check_is_clicable_click_continiue_registration_button()
	page.send_keys_input_box_first_name(name)
	page.click_no_element_for_reg()
	page.should_be_first_name_validation_msg()
	page.send_keys_input_box_last_name(name)
	page.click_no_element_for_reg()
	page.should_be_last_name_validation_msg()



def test_validation_big_len_character(browser):
	'''RT-R-14'''
	url = AuthPageLocators.AUTH_URL
	name = generate_max_valid_name()+'a'
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.check_is_clicable_click_continiue_registration_button()
	page.send_keys_input_box_first_name(name)
	page.click_no_element_for_reg()
	page.should_be_first_name_validation_msg()
	page.send_keys_input_box_last_name(name)
	page.click_no_element_for_reg()
	page.should_be_last_name_validation_msg()



def test_validation_no_pattern_email(browser):
	'''RT-R-15'''
	url = AuthPageLocators.AUTH_URL
	email = gen_no_valid_email()
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.check_is_clicable_click_continiue_registration_button()
	page.send_keys_input_box_for_email_or_phone_reg(email)
	page.click_no_element_for_reg()
	page.should_be_email_or_phone_validation_msg()



def test_validation_small_len_password(browser):
	'''RT-R-16'''
	url = AuthPageLocators.AUTH_URL
	password = generate_min_valid_password()[:-1]
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.check_is_clicable_click_continiue_registration_button()
	page.send_keys_input_box_password(password)
	page.click_no_element_for_reg()
	page.should_be_password_validation_msg()
	page.send_keys_input_box_password_confirm(password)
	page.click_no_element_for_reg()
	page.should_be_password_confirm_validation_msg()



def test_validation_no_upper_char_password(browser):
	'''RT-R-17'''
	url = AuthPageLocators.AUTH_URL
	password = generate_min_valid_password().lower()
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.check_is_clicable_click_continiue_registration_button()
	page.send_keys_input_box_password(password)
	page.click_no_element_for_reg()
	page.should_be_password_validation_msg()
	page.send_keys_input_box_password_confirm(password)
	page.click_no_element_for_reg()
	page.should_be_password_confirm_validation_msg()






def test_validation_russian_char_password(browser):
	'''RT-R-18'''
	url = AuthPageLocators.AUTH_URL
	password = generate_min_valid_password() + 'я'
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.check_is_clicable_click_continiue_registration_button()
	page.send_keys_input_box_password(password)
	page.click_no_element_for_reg()
	page.should_be_password_validation_msg()
	page.send_keys_input_box_password_confirm(password)
	page.click_no_element_for_reg()
	page.should_be_password_confirm_validation_msg()



def test_validation_password_mismatch(browser):
	'''RT-R-19'''
	url = AuthPageLocators.AUTH_URL
	password = generate_min_valid_password()
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.check_is_clicable_click_continiue_registration_button()
	page.send_keys_input_box_password(password)
	page.click_no_element_for_reg()
	page.send_keys_input_box_password_confirm(password+'z')
	page.click_no_element_for_reg()
	page.should_be_password_confirm_validation_msg()



def test_successful_registration_temp(browser):
	'''RT-R-20*'''
	url = AuthPageLocators.AUTH_URL
	tm = TempMail()
	email = tm.get_email_address()
	password = 'NWknA7s5insJuEg'
	name = generate_min_valid_name()
	page = RegPage(browser, url)
	page.open()
	page.should_be_sign_up_button_is_clicable()
	page.click_sign_up_button()
	page.check_correct_load_page()
	page.send_keys_input_box_first_name(name)
	page.click_no_element_for_reg()
	page.should_not_be_first_name_validation_msg()
	page.send_keys_input_box_last_name(name)
	page.click_no_element_for_reg()
	page.should_not_be_last_name_validation_msg()
	page.send_keys_input_box_for_email_or_phone_reg(email)
	page.click_no_element_for_reg()
	page.should_not_be_email_or_phone_validation_msg()
	page.send_keys_input_box_password(password)
	page.click_no_element_for_reg()
	page.should_not_be_password_validation_msg()
	page.send_keys_input_box_password_confirm(password)
	page.click_no_element_for_reg()
	page.should_not_be_password_confirm_validation_msg()
	page.check_is_clicable_click_continiue_registration_button()
	page.click_continiue_registration_button()
	page.should_be_confirm_email_title()
	sleep(10) 
	confirm_code = get_confirm_code(tm.get_mailbox(email))
	print(confirm_code)
	page.send_confirm_code(confirm_code)
	page.check_corect_redirect_after_sign_in()