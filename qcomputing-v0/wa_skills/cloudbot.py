
#
# Copyright (C) 2020 IBM. All Rights Reserved.
#
# See LICENSE.txt file in the root directory
# of this source tree for licensing information.
#

''' cloud starter-sheet command handler '''

''' imports '''
from clai.server.plugins.qcomputing.wa_skills.utils import call_wa_skill, get_own_name

''' globals '''
__self = get_own_name(__file__) 
__intents = { 'get_hello'   : "hello",
              'get_bvazirani'      : "bvazirani",
              'get_groveropt'      : "goveropt",
              'get_admmopt'      : "admmopt"
              }

def wa_skill_processor_cloudbot(msg, filename):

    response, success = call_wa_skill(msg, filename)
    if not success: return {"text" : response}, 0.0

    # Identify the intent in the user message
    try:

        intent = response["intents"][0]["intent"]
        confidence = response["intents"][0]["confidence"]

    except IndexError or KeyError:

        intent = "generic"
        confidence = 0.0

    data = { "text" : "clai qcomputing " + __intents[intent] } 
    return data, confidence

