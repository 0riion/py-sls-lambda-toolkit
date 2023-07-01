import unittest
from py_sls_lambda_toolkit.http_response import create_response
import json


class TestCreateResponse(unittest.TestCase):

    def _create_headers(self):
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
            'Content-Type': 'application/json',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, PUT, PATCH, DELETE',
            'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, X-API-AUTH, X-Amz-Date, X-Api-Key, X-Amz-Security-Token, X-Amz-User-Agent',
        }
        return headers

    def _create_body(self, data):
        body = json.dumps(data)
        return body

    def test_create_response(self):
        response = create_response({'foo': 'bar'})
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['headers'], self._create_headers())
        self.assertEqual(response['body'], json.dumps({'foo': 'bar'}))
        self.assertEqual(response['headers']
                         ['Access-Control-Allow-Origin'], '*')
        self.assertEqual(response['headers']
                         ['Access-Control-Allow-Credentials'], True)
        self.assertEqual(response['headers']
                         ['Content-Type'], 'application/json')
        self.assertEqual(response['headers']['Access-Control-Allow-Methods'],
                         'GET, POST, OPTIONS, PUT, PATCH, DELETE')
        self.assertEqual(response['headers']['Access-Control-Allow-Headers'],
                         'Origin, X-Requested-With, Content-Type, Accept, X-API-AUTH, X-Amz-Date, X-Api-Key, X-Amz-Security-Token, X-Amz-User-Agent')
        self.assertEqual(response['body'], '{"foo": "bar"}')

    def test_create_response_with_status_code(self):
        response = create_response({'foo': 'bar'}, status_code=201)
        self.assertEqual(response['statusCode'], 201)

    def test_create_response_with_headers(self):
        response = create_response(
            {'foo': 'bar'}, custom_headers={'foo': 'bar'})
        self.assertEqual(response['headers']['foo'], 'bar')

    def test_create_response_with_content_type(self):
        response = create_response({'foo': 'bar'}, content_type='text/html')
        self.assertEqual(response['headers']['Content-Type'], 'text/html')

    def test_create_response_with_no_body(self):
        response = create_response(None)
        self.assertEqual(response['body'], None)

    def test_create_response_with_no_body_and_content_type(self):
        response = create_response(None, content_type='text/html')
        self.assertEqual(response['headers']['Content-Type'], 'text/html')
        self.assertEqual(response['body'], None)

    def test_create_response_with_no_body_and_status_code(self):
        response = create_response(None, status_code=201)
        self.assertEqual(response['statusCode'], 201)
        self.assertEqual(response['body'], None)

    def test_create_response_with_no_body_and_headers(self):
        response = create_response(None, custom_headers={'foo': 'bar'})
        self.assertEqual(response['headers']['foo'], 'bar')
        self.assertEqual(response['body'], None)

    def test_create_reponse_with_many_data_types(self):

        data = {
            'string': 'foo',
            'integer': 1,
            'float': 1.1,
            'boolean': True,
            'list': ["foo", "bar"],
            'dict': {'foo': 'bar'},
            'bigInteger': 1234567890123456789012345678901234567890,
            'bigFloat': 1234567890123456789012345678901234567890.1234567890123456789012345678901234567890,
            'base64': 'Zm9vYmFy',
            'null': None,
            'negativeInteger': -1,
            'negativeFloat': -1.1,
            'negativeBigInteger': -1234567890123456789012345678901234567890,
            'negativeBigFloat': -1234567890123456789012345678901234567890.1234567890123456789012345678901234567890,
            'numericList': [1, -1, 1.1, -1.1, 1234567890123456789012345678901234567890, -1234567890123456789012345678901234567890, 1234567890123456789012345678901234567890.1234567890123456789012345678901234567890, -1234567890123456789012345678901234567890.1234567890123456789012345678901234567890],
        }

        response = create_response(data)

        expected_body = self._create_body(data)
        self.assertEqual(response['body'], expected_body)


if __name__ == '__main__':
    unittest.main()
