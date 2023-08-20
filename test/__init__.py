"""
this module is for getting token from file gen by ce user or CI
"""
from os.path import exists

def get_token() -> str:
    """
    return token as string or raise a exception if file not exist
    """
    if not exists(".token"):
        raise Exception(".token file not found for test")
    with open(".token", 'r') as stream:
        return stream.readline()
