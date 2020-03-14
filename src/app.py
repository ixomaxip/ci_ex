from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

def validate_post_data(data: dict) -> bool:
    if not isinstance(data, dict):
        return False
    if not data.get('name') or isinstance(data['name'], str):
        return False
    if data.get('age') and not isinstance(data['age'], int):
        return False
    return True


@app.route('/', methods=['GET'])
def hello():
    return 'Hell O!'


@app.route('/api', methods=['GET', 'POST'])
def api():
    """
    /api endpoint
    GET - returns json = {'status': 'test'}
    POST - {
        name - str not null
        age - int opt
    }
    :return:
    """

def main():
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()