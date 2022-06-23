# from flask import Flask, request
# import os
# import dialogflow
# from google.api_core.exceptions import InvalidArgument
# from twilio.twiml.messaging_response import MessagingResponse
# import requests
#
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =  'private_key.json'
#
# DIALOGFLOW_PROJECT_ID = 'small-talk-qega'
# DIALOGFLOW_LANGUAGE_CODE = 'ru'
# SESSION_ID = 'me'
#
# app = Flask(__name__)
# app.config['DEBUG'] = True
#
#
# @app.route('/')
# def root():
#     return "WhatsApp Chatbot"
#
# @app.route('/api/getMessage', methods=['POST'])
# def home():
#     message=request.form.get('Body')
#     mobnum=request.form.get('From')
#     session_client = dialogflow.SessionsClient()
#     session = session_client. session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
#     text_input = dialogflow.types. TextInput(text=message, language_code=DIALOGFLOW_LANGUAGE_CODE)
#     query_input = dialogflow. types. QueryInput(text=text_input)
#     try:
#         response = session_client.detect_intent(session=session, query_input=query_input)
#     except InvalidArgument:
#         raise
#     print("Query text:", response.query_result.query_text)
#     print("Detected intent:", response.query_result.intent.display_name)
#     print("Detected intent confidence:", response.query_result. intent_detection_confidence)
#     print("Fulfillment text:", response.query_result. fulfillment_text)
#
#     sendMessage(mobnum, response.query_result. fulfillment_text)
#     return response.query_result. fulfillment_text
#
#
# def sendMessage(mobnum, message):
#     print("Mobile number : ",mobnum)
#     print("Message is : ",message)
#     url = "https://api.twilio.com/2010-04-01/Accounts/AC3b4e9356a0acfb55cceeece7f5752f19/Messages.json"
#     payload = {'From': 'whatsapp:+14155238886',
#     'Body': message,
#     'To': mobnum}
#     headers = {
#         'Autherization': 'c3aabad1e2447605dd40c3e1ce769723'
#     }
#     response = requests.request('POST', url, headers=headers, data=payload)
#     print(response.text.encode('utf8'))
#     return ""
#
# if __name__ == '__main__':
#     app.run()



# 85O-UKdcZu_L1HUqmeJc_pj6uoskWGpUDMDP_ccB


#----------------------------------------

from twilio.rest import Client

account_sid = 'ACd2bc7bd073925c1628e0b205cc01c800'
auth_token = 'c3aabad1e2447605dd40c3e1ce769723'
client = Client(account_sid, auth_token)

# message = client.messages.create(
#     from_='whatsapp:+14155238886',
#     body='Hello!',
#     to='whatsapp:+77028574975'
# )

# print(message.sid)


from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hello!',
        to='whatsapp:+77028574975'
    )
    message.sid
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)



# from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
#
# response = MessagingResponse()
# message = Message()
# message.body('Hello World!')
# response.append(message)
# response.redirect('https://timberwolf-mastiff-9776.twil.io/demo-reply')
#
# print(response)



# def sendMessage(mobnum, message):
#     print("Mobile number : ",mobnum)
#     print("Message is : ",message)
#     url = "https://api.twilio.com/2010-04-01/Accounts/AC3b4e9356a0acfb55cceeece7f5752f19/Messages.json"
#     payload = {'From': 'whatsapp:+18784445244',
#     'Body': message,
#     'To': mobnum}
#     headers = {
#         'Autherization': 'Basic <token>'
#     }
#     response = requests.request('POST', url, headers=headers, data=payload)
#     print(response.text.encode('utf8'))
#     return ""
