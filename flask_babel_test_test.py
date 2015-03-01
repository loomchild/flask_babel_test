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
            # flask.ext.babel.refresh()
            rv = app.test_client().get('/')
            # rv = app.test_client().get('/', headers=[("Accept-Language", "pl")])
            assert 'Witaj' in str(rv.data)

if __name__ == '__main__':
    unittest.main()
