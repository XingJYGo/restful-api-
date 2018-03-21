import unittest
import json
import requests

class JenkinsGet(unittest.TestCase):
	def setUp(self):
		self.r = requests.get('http://localhost:8080/jenkins/api/json?tree=jobs[name]')

	def test_get_all_job_names(self):
		result = self.r.text
		json_result = json.loads(result)
		print json_result
		self.assertEqual(json_result['jobs'][0]['name'], 'appium_calc')
		self.assertEqual(json_result['jobs'][-1]['name'], 'wordpress_test_pyunit')

	def test_get_all_jobs_names_simple_way(self):
		json_result = self.r.json()
		self.assertEqual(json_result['jobs'][0]['name'], 'appium_calc')
		self.assertEqual(json_result['jobs'][-1]['name'], 'wordpress_test_pyunit')

	# 思考题：如何测试开启鉴权的jenkins接口

if __name__ == '__main__':
	unittest.main()