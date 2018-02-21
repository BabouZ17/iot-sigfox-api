#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Python script to communicate with the Sigfox API

import requests

class Sigfox_API:
	"""
	Sigfox API Object use to communicate with the Sigfox API,
	using the user credentials (username and password) thanks
	to basic authentication over https.
	"""

	def __init__(self, username, password):
		"""
		Main constructor using credentials:
			-	username (string)
			-	password (string)
		"""

		self.username = username
		self.password = password

	def get_value_from_device(self, device_id, quantity = 1):
		"""
		Get value from device from the Sigfox API according to:
			-	device id (string)
			-	quantity of value to return (int)
		"""

		url = 'https://backend.sigfox.com/api/devices/{}/messages?limit={}'.format(device_id, quantity)

		r = requests.get(url = url, auth = (self.username, self.password))

		return r.json()

	def get_device_info(self, device_id):
		"""
		Get device informations from the Sigfox API according to:
			-	device id (string)
		"""

		url = 'https://backend.sigfox.com/api/devices/{}'.format(device_id)

		r = requests.get(url = url, auth = (self.username, self.password))

		return r.json()

	def get_device_token_state(self, device_id):
		"""
		Get token state from device from the Sigfox API according to:
			-	device id (string)
		"""

		url = 'https://backend.sigfox.com/api/devices/{}/token-state'.format(device_id)

		r = requests.get(url = url, auth= (self.username, self.password))

		return r.json()

	def get_devices_for_a_given_device_type(self, device_type):
		"""
		Get all devices for a given device_type from the Sigfox API according to:
			-	device_type (string)
		"""

		url = 'https://backend.sigfox.com/api/devicetypes/{}/devices?'.format(device_type)

		r = requests.get(url = url, auth = (self.username, self.password))

		return r.json()

	def get_errors_for_a_device(self, device_id):
		"""
		Get error status events for a given device from the Sigfox API according to:
			-	device_id (string)
		"""

		url = 'https://backend.sigfox.com/api/devices/{}/status/error'.format(device_id)

		r = requests.get(url = url, auth = (self.username, self.password))

		return r.json()

	def get_warning_status_for_a_device(self, device_id):
		"""
		Get warning status events for a given device from the Sigfox API according to:
			-	device_id (string)
		"""
		url = 'https://backend.sigfox.com/api/devices/{}/status/warn'.format(device_id)

		r = requests.get(url = url, auth = (self.username, self.password))

		return r.json()

	def get_network_status_for_a_device(self, device_id):
		"""
		Get the network status for a given device from the Sigfox API according to:
			-	device_id (string)
		"""

		url = 'https://backend.sigfox.com/api/devices/{}/networkstate'.format(device_id)

		r = requests.get(url = url, auth = (self.username, self.password))

		return r.json()

	def get_messages_not_sent_this_month(self):
		"""
		Get the messages not sent for the current month from the Sigfox API
		"""

		url = 'https://backend.sigfox.com/api/callbacks/messages/error'

		r = requests.get(url = url, auth = (self.username, self.password))

		return r.json()
