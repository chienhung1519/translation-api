from flask import Flask, request
import googletrans
from gevent.pywsgi import WSGIServer
import json
import argparse

app = Flask(__name__)

translator = googletrans.Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data['text']
    target_language = data['target_language']

    response = translator.translate(text, dest=target_language)
    translated_text = response.text

    return json.dumps({'translated_text': translated_text}, ensure_ascii=False)

if __name__ == '__main__':
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=6868)
    args = parser.parse_args()

    host = args.host
    port = args.port

    # Development
    # app.run(host=host, port=port)

    # Production
    print(f'Translation server listening on {host}:{port}')
    http_server = WSGIServer((host, port), app)
    http_server.serve_forever()