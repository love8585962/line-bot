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

line_bot_api = LineBotApi('7adyn6R1SfZQ4Y+D9tMXWiAEICXwNIy3xw4k5Uq5hsdc1cF929PFaiN7moiHicTtjzkX9tq5dnh1MrFWEoQJK697NkgfQlmeYZcrXMyp/iKXOArwpIvQEVMVbVF9YOzOtUASM/tYy3YcqPf++k8BdAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a1009734084246fd2504905ddc3b879a')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = '我看不懂妳在說什麼'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg))


if __name__ == "__main__":
    app.run()