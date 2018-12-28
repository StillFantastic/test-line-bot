from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('JHDXjzCuoVF9uquQD2iQGvNoIAu0YU3bwPSXGQ7EcdtLLbnaXkHvVOceiXDhOowGLB3QLZ3abOUV7WXz+pf/Ue6pqxPZHtS+15T+nWwTaVDx+uWF2Dc7gid432Pd82++QQrpFio9oY7pTD9zpKQkdwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('950860c63f41d82acf13e0387edeaffb')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@app.route("/", methods=["POST", "GET"])
def main():
    return "Hello"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
