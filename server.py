import flask
from waitress import serve

import os

app = flask.Flask(__name__)

PARENT_FOLDER = 'database'
FILE_NAME = 'temp.txt'
PATH_FILE = os.path.join(PARENT_FOLDER, FILE_NAME)


if os.path.exists(PARENT_FOLDER) == False:
    os.makedirs('database')

if os.path.exists(PATH_FILE) == False:
    f = open(PATH_FILE, 'w+')
    f.write(f'{0}')
    f.close()


def write_int_to_txt(number):
    f = open(PATH_FILE, 'w')
    f.write(f'{number}')
    f.close()


def get_number_of_visitor():
    f = open(PATH_FILE, 'r')
    number = f.readline()
    return int(number)


@app.route('/', methods=['POST', 'GET'])
def main():
    count = get_number_of_visitor()
    count += 1
    write_int_to_txt(count)
    return f'Fuck that shit !!! - Number of visitors: {count} - made by ngoc.airo@gmail.com'


if __name__ == "__main__":

    serve(
        app,
        host="0.0.0.0",
        port=6689,
        # threaded=True,
    )
