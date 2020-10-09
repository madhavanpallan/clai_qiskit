#
# Copyright (C) 2020 IBM. All Rights Reserved.
#
# See LICENSE.txt file in the root directory
# of this source tree for licensing information.
#

from clai.server.agent import Agent
from clai.server.command_message import State, Action, NOOP_COMMAND
from clai.tools.colorize_console import Colorize

from clai.server.logger import current_logger as logger

from clai.server.plugins.qcomputing.wa_skills.cloudbot import wa_skill_processor_cloudbot as wa_cmd
from clai.server.plugins.qcomputing.qc_funcs.qiskit_funcs import funcheck as funcheck

class QCOMPUTING(Agent):
    def __init__(self):
        super(QCOMPUTING, self).__init__()

    def get_next_action(self, state: State) -> Action:
    
        commandRec = state.command
        command_op, confidence = wa_cmd(commandRec)
        command_generated = command_op['text']
        tester = str(command_generated[0])
        return Action(suggested_command=NOOP_COMMAND, 
                                execute=True,
                                description=Colorize().info().append("Here are the functions" + funcheck(tester,command_generated)).to_console(),
                                confidence=1.0)
