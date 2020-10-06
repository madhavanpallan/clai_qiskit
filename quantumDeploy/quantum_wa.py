import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import atexit
import os
import json

def intent_caller(input_text):
    data = {'message':input_text}
    authenticator = IAMAuthenticator('BhyZ9zId0kAE6xq9KLObO1CbI7qOLJSq2qbw3r38h9tw')
    assistant = AssistantV2(
        version='2020-04-01',
        authenticator=authenticator
    )

    assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/713864eb-b727-460c-8729-fd785c0fb6b7')
    session_response = assistant.create_session(
        assistant_id='82470d8a-52cd-48be-a959-3ff169167096'
    ).get_result()

    session_json = json.dumps(session_response,indent=2)
    response = assistant.message(
        assistant_id='82470d8a-52cd-48be-a959-3ff169167096',
        session_id=session_response["session_id"],
        input={
            'message_type': 'text',
            'text': input_text
        }
    ).get_result()
    return response
