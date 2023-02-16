import requests	
import string
import random
import re

																								   
def generate_min_valid_password():
	'''Функция генерирует минимальный валидный пароль'''
	letters = string.ascii_lowercase
	upper_letters = string.ascii_uppercase
	password = ''.join(random.choice(letters) for i in range(8))
	password = list(password)
	password[random.randint(0, 6)] = random.choice(upper_letters)
	password = ''.join(password)
	return password


def generate_min_valid_name():
	'''Функция генерирует минимально валидное ФИ'''
	russian_chars_lowercase = "йцукенгшщзхъфывапролджэячсмитьбюё"
	name = ''.join(random.choice(russian_chars_lowercase) for i in range(2))
	return name


def generate_max_valid_name():
	'''Функция генерирует максимальное валидное ФИО'''
	russian_chars_lowercase = "йцукенгшщзхъфывапролджэячсмитьбюё"
	name = ''.join(random.choice(russian_chars_lowercase) for i in range(30))
	return name


def gen_random_len_valid_name_plus():
	'''Функция генериует ФИ через - '''
	russian_chars_lowercase = "йцукенгшщзхъфывапролджэячсмитьбюё"
	name = ''.join(random.choice(russian_chars_lowercase) for i in range(random.randint(1,14)))\
	+ '-' + ''.join(random.choice(russian_chars_lowercase) for i in range(random.randint(1,14))) 
	return name


def gen_latin_char_name():
	'''Функция генерирует ФИ с латинским символом'''
	russian_chars_lowercase = "йцукенгшщзхъфывапролджэячсмитьбюё"
	name = ''.join(random.choice(russian_chars_lowercase) for i in range(random.randint(1,29)))
	name += random.choice(string.ascii_lowercase)
	return name


def gen_digit_char_name():
	'''Функция генерирует ФИ с цифровым символом'''
	russian_chars_lowercase = "йцукенгшщзхъфывапролджэячсмитьбюё"
	name = ''.join(random.choice(russian_chars_lowercase) for i in range(random.randint(1,29)))
	name += random.choice(string.digits)
	return name


def gen_punctuation_char_name():
	'''Функция генерирует ФИ с латинским символом'''
	russian_chars_lowercase = "йцукенгшщзхъфывапролджэячсмитьбюё"
	name = ''.join(random.choice(russian_chars_lowercase) for i in range(random.randint(1,29)))
	name += random.choice(string.punctuation)
	return name


def gen_no_valid_email():
	'''Функция генерирует не валиилный email'''
	chars = string.ascii_lowercase + string.ascii_uppercase + '@.'
	email = name = ''.join(random.choice(chars) for i in range(random.randint(1,29)))
	return email


def get_confirm_code(msg_list):
	'''Данная функция получает код из сообщения'''
	msg = msg_list[0]['mail_text_only']
	text = re.search(r"Ваш код : \d+", msg).group(0)
	return text.replace(' ','').replace('Вашкод:', '')
