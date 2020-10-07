#
# Copyright (C) 2020 IBM. All Rights Reserved.
#
# See LICENSE.txt file in the root directory
# of this source tree for licensing information.
#

''' cloud starter-sheet command handler '''

''' imports '''
import requests
import json 
from wa_skills.utils import call_wa_skill, get_own_name
import re

def wa_skill_processor_cloudbot(msg):
    confidence = 0.0 

    # Identify the intent in the user message
    response, success = call_wa_skill(msg, "cloudbot")
    if not success: return {"text" : response}, 0.0
    
    try:

        intent = response["intents"][0]["intent"]
        confidence = response["intents"][0]["confidence"]

    except IndexError or KeyError:

        intent = "generic"
        confidence = 0.0
   
    intents = { 'get_hello'   : {"text": ['3']},
                'get_bvazirani'      : {"text":get_parameter(msg, ['0'])},
                'get_grover'      : {"text":get_parameter(msg, ['1'])},
                'get_admm'      : {"text":get_parameter(msg, ['2'])}
                }
    
    if intent in intents: data = intents[intent]
    else: pass

    return data, confidence

def get_parameter(command, tokens):
    strToken = command.split(" ")
    j = 0
    startValue = len(strToken) + 1
    endValue = len(strToken)
    responseStr = ""
    for token in strToken:
        brackstart = re.match("{", token)
        brackend = re.search("}", token)
        j = j + 1
        if brackstart != None:
            strToken[j - 1] = strToken[j - 1].replace("{","")
            startValue = j
        
        if brackend != None:
            strToken[j - 1] = strToken[j - 1].replace("}","")
            endValue = j

        if startValue<=j and endValue>=j:
            tokens.append(strToken[j - 1])

    return tokens
