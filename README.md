# Translation API

This is a simple Flask application that provides a translation API using python [googletrans](https://py-googletrans.readthedocs.io/en/latest/).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/chienhung1519/translation-api.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. Send a POST request to `http://localhost:6868/translate` with the following JSON payload:

    ```json
    {
        "text": "Hello, world!",
        "target_language": "zh-tw"
    }
    ```

    Replace `"Hello, world!"` with the text you want to translate, and `"zh-tw"` with the target language code.

3. The API will respond with the translated text:

    ```json
    {
        "translated_text": "Bonjour, le monde!"
    }
    ```

4. Example:

    ```bash
    curl -X POST http://localhost:6868/translate \
        -H 'Content-Type: application/json' \
        -d '{"text":"hi, how are you", "target_language": "zh-tw"}'
    # {"translated_text": "你好你好嗎"}
    ```
