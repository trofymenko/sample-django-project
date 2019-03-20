# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.test import TestCase, TransactionTestCase
from rest_framework.test import RequestsClient
import json
from django.db import close_old_connections

class SampleTestCase(TransactionTestCase):

 def test_sample(self):
     self.assertEqual(0, 0)
