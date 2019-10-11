#!/usr/bin/env python3

import unittest
import subprocess

class test(unittest.TestCase):
	def test(self):
		try:
			subprocess.check_output("unbuffer make attack > res.txt", shell=True)
		except:
			pass
		with open("res.txt", "rb") as f:
			res = f.read()
		print(res.decode(errors="replace"))
		self.assertTrue(res.find("root:".encode()) >= 0)
		self.assertTrue(res.find("student:".encode()) >= 0)


if __name__ == '__main__':
	unittest.main()

