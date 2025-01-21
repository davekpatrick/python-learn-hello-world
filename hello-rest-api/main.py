# imports
import requests
import logging
import os
import json

# 
logger = logging.getLogger(__name__)
urlHost = 'https://httpbin.org'
urlBearer = os.environ['HELLO_TOKEN']

def main():
    logging.basicConfig(level=logging.INFO)
    #
    response = requests.get(
            urlHost + '/bearer', 
            headers={'Authorization': 'Bearer ' + urlBearer}
            )
    if response.status_code != 200:
        print (response.headers)
        logger.info ( "Authentication failure" )
        exit (1)
    else:
        logger.info ( "successfully authenticated" )
    #
    response = requests.get(
        urlHost + '/anything',
        headers={'accept': 'application/json'}
        )
    if response.status_code != 200:
        logger.info ( "Failed to get anything" )
        exit (1)
    logger.info ( "successfully got anything" )
    responseJson = response.json()
    json_mylist = json.dumps(responseJson, separators=(',', ':'))
    logger.info ( json_mylist )
# 
if __name__ == '__main__':
    main()

