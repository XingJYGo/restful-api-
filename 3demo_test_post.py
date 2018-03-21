import unittest
import json
import requests
from requests.auth import HTTPBasicAuth

class JenkinsPost(unittest.TestCase):
	def setUp(self):
		self.build_job_url = 'http://localhost:8080/jenkins/job/check_python_version/build'
		self.disable_job_url = 'http://localhost:8080/jenkins/job/check_python_version/disable'
		self.job_url = 'http://localhost:8080/jenkins/job/check_python_version/api/json'

	def test_build_job(self):
		r = requests.post(self.build_job_url, data={}, auth=('admin', 'admin'))
		# print r.status_code
		self.assertEqual(r.status_code, 201)

	def test_disable_job(self):
		status = self.get_job_status()
		self.assertTrue(status)

		r = requests.post(self.disable_job_url, data={}, auth=('admin', 'admin'))
		# print r.status_code
		self.assertEqual(r.status_code, 200)

		status = self.get_job_status()
		self.assertFalse(status)

	def get_job_status(self):
		job_info = requests.get(self.job_url, auth=('admin', 'admin')).json()
		return job_info['buildable']

if __name__ == '__main__':
	unittest.main()