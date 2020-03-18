from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    handler(resp, msg)


def handler(resp, msg):
    text = format(msg)
    if text == "Hola":
        handlingHello(resp)
    elif text == "Products":
        handlingProducts(resp)
    else:
        resp.message("You said: {}".format(msg))
        return str(resp)

def handlingHello(resp):
    resp.message("Hola que tal")
    return str(resp)


def handlingProducts(resp):
    resp.message("Products:\n" + 
                "1 - aaaaaaaa\n" + 
                "2 - aaaaaaaa\n" + 
                "3 - aaaaaaaa\n" + 
                "4 - aaaaaaaa\n" + 
                "5 - aaaaaaaa\n" 
    )

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
