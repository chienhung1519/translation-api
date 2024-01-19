from flask import Flask, request
import googletrans
from gevent.pywsgi import WSGIServer
import json

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
    host = '0.0.0.0'
    port = 6868

    # Development
    # app.run(host=host, port=port)

    # Production
    print(f'Translation server listening on {host}:{port}')
    http_server = WSGIServer((host, port), app)
    http_server.serve_forever()