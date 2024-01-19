# Translation API

This is a simple Flask application that provides a translation API using python [googletrans](https://py-googletrans.readthedocs.io/en/latest/).

**Note on library usage** (from [googletrans](https://py-googletrans.readthedocs.io/en/latest/))
* The maximum character limit on a single text is 15k.
* Due to limitations of the web version of google translate, this API does not guarantee that the library would work properly at all times. (so please use this library if you don’t care about stability.)
* If you want to use a stable API, I highly recommend you to use Google’s official translate API.
* If you get HTTP 5xx error or errors like #6, it’s probably because Google has banned your client IP address.

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
        "translated_text": "你好世界！"
    }
    ```

4. Example:

    ```bash
    curl -X POST http://localhost:6868/translate \
        -H 'Content-Type: application/json' \
        -d '{"text":"Hello, world!", "target_language": "zh-tw"}'
    # {"translated_text": "你好世界！"}
    ```
