# -*- coding: utf-8 -*-
import os
import tempfile
import unittest

from flask_testing import TestCase

import cutter


class CutterTestCase(TestCase):

    TESTING = True

    def create_app(self):
        return cutter.app

    def setUp(self):
        self.db_fd, cutter.app.config['DATABASE'] = tempfile.mkstemp()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(cutter.app.config['DATABASE'])


class TestShortenUrl(CutterTestCase):

    def setUp(self):
        super(TestShortenUrl, self).setUp()
        cutter.app.config['WTF_CSRF_ENABLED'] = False

    def test_shorten_url_happy_path(self):
        long_url = 'http://example.com'
        rv = self.client.post('/shorten/', data={'long_url': long_url})
        self.assert_200(rv)
        short_url = rv.json['short_url']
        rv = self.client.get('/{}'.format(short_url))
        self.assertRedirects(rv, long_url)

    def test_schemaless_urls(self):
        long_url = 'http://кириллический.домен'
        rv = self.client.post('/shorten/', data={'long_url': long_url})
        short_url_1 = rv.data
        schemaless_url = 'кириллический.домен'
        rv = self.client.post('/shorten/', data={'long_url': schemaless_url})
        short_url_2 = rv.data
        self.assertEqual(short_url_1, short_url_2)

    def test_too_long_url(self):
        too_long_url = 'http://' + 'a'*3000
        rv = self.client.post('/shorten/', data={'long_url': too_long_url})
        self.assert_400(rv)


if __name__ == "__main__":
    unittest.main()
