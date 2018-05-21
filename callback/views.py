from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseBadRequest, HttpResponseForbidden
from linebot import LineBotApi, WebhookHandler, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
line_bot_api = LineBotApi('/4aw0vAmkugjb7dsnrV89Hv8PF/nr6KDOUTYPl7/0hY+VBnPZaV5emLQdt0aM1egeEDPJXicMZ7CElF6RDxPxCzFSWgSQkx5JZtmzQ3/sSOODeBa1g4rqSJ1+dzKW1ZU8oJ5ZBrbwXd0qsneDYDVTQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a61f08e961371507261d240502798dd9')
parser = WebhookParser('a61f08e961371507261d240502798dd9')

def index(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=event.message.text)
                    )

        return HttpResponse()
    else:
        return HttpResponseBadRequest() 

def index_old(request):
    print ("callback")
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    
    #app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        raise Http404("error in message")

    return 'OK'
    #return HttpResponse("Hello, world. You're at the polls index.")