import traceback
import sys
from hashlib import sha256
from json import load


def encrypt(string: str) -> str:
    return sha256(string.encode('utf-8')).hexdigest()


def load_resource(file_name: str) -> dict | list[dict]:
    print(file_name)
    resource: dict = {}
    try:        
        with open(file_name, 'r') as file:
            resource = load(file)
    except IOError as exc:
        print(f'Error importing file: {file_name}.\n{exc.args}\n{traceback.format_exc}')
    return resource


def generate_path(*args) -> str:
    sep = "\\" if sys.platform == 'win32' else "/"
    return sep.join(args)
