"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

# notes from Kevin's talk on django testing

# unti test for a model: create, increment, assert amount in attribute.
# unit test of form - form  = QuestinoForm()
# self.assertEqual()
# self.assertNotEqual()

# test post action; assertEqual stuff in db 
# functional : logging in with selenium
# get url for admin site
 
# find element named un, put un in
# find elemnt for pw, put pw in
# using selenium

# TDD
# write test first.

#  example: Torquemada.  is on heroku live too.  https://github.com/kcharvey/testing-in-django

# http://bit.ly/XHjcAi

# from sleenium import webdriver

#from django.test import LiveServerTestCase
# class QuestionsTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_read bla bla

# pip install selenium

# he makes a direcotry called tests with an __init.py file too
# he has two diff files, one for func_tests and one for unit_tests

# in the init he has 
from func_tests import *
from unit_tests import *

assert template use ?

# selenium:
self.browser.get()

# selenium not a testing tool - tool to control browser.  You can do anything with it.
self.browser.find_element_by_blabla - css_selector is most useful.
# element or elements, item or list.
element.click()
#forms
text_field = self.browser.find....
text_field.clear()
text_field.send_keys("bla bla")
then click submit

# testing in existing project
# write tests for bug reports.  test first - functional tests.
# new features
# write unit tests for existing code while doing the above

# continuous integration
# Jenkins - Java program
# pip install django-jenkins, add it to installed apps, tell it what tests to run, then you get some manage.py commands.  
# you need some plugins
# configure tests, tell it how often to build, etc.
# Jenkins as a service companies, or raspberry pie
# 
# javascript testing: Doctest.js,  http://doctestjs.org

# Fixtures:
# json descriptions of your models.  manage.py loaddata
# use python manage.py dumpdata to get teh original file
# for each test case you can include fixtures

# you can test migrations too....

# browser testing  - you can subclass test cases and change the setup method for each browser

# there's also a django thing called django-webtest , can't test javascript

# slides will be on slideshare - everyting will be on readme on github

# selenium web recorder to write tests?
# power of recorder is to get first test written
# setup code must be written in python
# 
# selenium : page object deisgn pattern

# functional test shoudl also test bad info as well as success cases
