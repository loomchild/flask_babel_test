#!/usr/bin/env python
import unittest
from flask_babel_test import app

class FlaskBabelTestTest(unittest.TestCase):

    def test(self):
        rv = app.test_client().get()
        assert 'Hello' in str(rv.data)

    def test_pl(self):
        with app.test_request_context():
            app.config['BABEL_DEFAULT_LOCALE'] = 'pl'
            rv = app.test_client().get('/')
            assert 'Witaj' in str(rv.data)

if __name__ == '__main__':
    unittest.main()
