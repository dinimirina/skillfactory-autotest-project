import string
import random
from hashlib import md5
import requests


class TempMail(object):

	def __init__(self, api_key='ERaXR21Qfq8Wf8jrmgwpbTj8MHkvknNh', login=None, domain=None, api_domain='api.apilayer.com/temp_mail'):
		self.login = login
		self.domain = domain
		self.api_domain = api_domain
		self.api_key = api_key

	def __repr__(self):
		return f'<TempMail [{self.get_email_address()}]>'

	@property
	def get_domains(self):
		"""
		Return list of available domains for use in email address.
		"""
		if not hasattr(self, '_get_domains'):
			url = f'https://{self.api_domain}/domains'
			payload = {}
			headers = {
				"apikey": self.api_key
			}

			response = requests.get(url, headers=headers, data=payload)
			domains = response.json()
			setattr(self, '_get_domains', domains)
		return self._get_domains

	def generate_login(self, min_length=6, max_length=10, digits=True):
		"""
		Generate string for email address login with defined length and
		alphabet.

		:param min_length: (optional) min login length.
		Default value is ``6``.
		:param max_length: (optional) max login length.
		Default value is ``10``.
		:param digits: (optional) use digits in login generation.
		Default value is ``True``.
		"""
		chars = string.ascii_lowercase
		if digits:
			chars += string.digits
		length = random.randint(min_length, max_length)
		return ''.join(random.choice(chars) for x in range(length))

	def get_email_address(self):
		"""
		Return full email address from login and domain from params in class
		initialization or generate new.
		"""
		if self.login is None:
			self.login = self.generate_login()

		get_domains = self.get_domains
		if self.domain is None:
			self.domain = random.choice(get_domains)
		elif self.domain not in get_domains:
			raise ValueError('Domain not found in available domains!')
		return f'{self.login}{self.domain}'

	def get_hash(self, email):
		"""
		Return md5 hash for given email address.

		:param email: email address for generate md5 hash.
		"""
		return md5(email.encode('utf-8')).hexdigest()

	def get_mailbox(self, email=None, email_hash=None):
		"""
		Return list of emails in given email address
		or dict with `error` key if mail box is empty.

		:param email: (optional) email address.
		:param email_hash: (optional) md5 hash from email address.
		"""
		if email is None:
			email = self.get_email_address()
		if email_hash is None:
			email_hash = self.get_hash(email)

		url = f'https://{self.api_domain}/mail/id/{email_hash}'
		payload = {}
		headers = {
			"apikey": self.api_key
		}

		response = requests.get(url, headers=headers, data=payload)
		return response.json()
