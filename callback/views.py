from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

line_bot_api = LineBotApi('/4aw0vAmkugjb7dsnrV89Hv8PF/nr6KDOUTYPl7/0hY+VBnPZaV5emLQdt0aM1egeEDPJXicMZ7CElF6RDxPxCzFSWgSQkx5JZtmzQ3/sSOODeBa1g4rqSJ1+dzKW1ZU8oJ5ZBrbwXd0qsneDYDVTQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a61f08e961371507261d240502798dd9')

def index(request):
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