import json
from .parsers import SnakeToCamelConverter


def create_response(response, status_code=200, custom_headers=None, content_type='application/json'):
    """
        Creates an HTTP response object.

        Parameters:
            response (dict): The response body.
            status_code (int): The HTTP status code to be returned. Default is 200.
            headers (dict): The headers to be returned with the response. Default is None.
            content_type (str): The content type of the response. Default is 'application/json'.

        Returns:
            dict: The HTTP response object with keys statusCode, headers, and body.
    """
    # TODO: Add support for binary data
    # TODO: Add to global config
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': True,
        'Content-Type': content_type,
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, PUT, PATCH, DELETE',
        'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, X-API-AUTH, X-Amz-Date, X-Api-Key, X-Amz-Security-Token, X-Amz-User-Agent',
    }

    if custom_headers is not None:
        headers.update(custom_headers)

    body = SnakeToCamelConverter.convert(response)

    return {
        'statusCode': status_code,
        'headers': headers,
        'body': json.dumps(body) if body is not None else None
    }
