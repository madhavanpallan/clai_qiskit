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
import pandas as pd

import os
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from PIL import Image
from qiskit import *
from qiskit.tools.visualization import plot_histogram 
  
class QCOMPUTING(Agent):
    def __init__(self):
        super(QCOMPUTING, self).__init__()

    def get_next_action(self, state: State) -> Action:

        # user typed in, in natural language
        command = state.command

        try:
            logger.info("Command passed in qcomputing: " + command)
            commandStr = str(command)
            commandTokenized = commandStr.split(" ")
            if len(commandTokenized) == 3:
                if commandTokenized[1] == 'bvazirani':
                    secretno = str(commandTokenized[2])
                    circuit = QuantumCircuit(len(secretno) +1, len(secretno))

                    circuit.h(range(len(secretno)))
                    circuit.x(len(secretno))
                    circuit.h(len(secretno))

                    circuit.barrier()
                    for ii, yesno in enumerate(reversed(secretno)):
                        if yesno == '1':
                            circuit.cx(ii, len(secretno))

                    circuit.barrier()
                    circuit.h(range(len(secretno)))
                    circuit.barrier()
                    circuit.measure(range(len(secretno)), range(len(secretno)))
                    circuit.draw()  

                    simulator = Aer.get_backend('qasm_simulator')
                    result = execute(circuit, simulator, shots=1).result()
                    counts = result.get_counts()
                    cirprint = circuit.draw()
                    response = "You Secret code is:- " + str(counts) + "\n" + str(cirprint) + "."
                
            elif len(commandTokenized) == 2:
                if commandTokenized[1] == 'hello':
                    simulator = Aer.get_backend('qasm_simulator')
                    circuit = QuantumCircuit(2, 2)
                    circuit.h(0)
                    circuit.cx(0, 1)
                    circuit.measure([0,1], [0,1])
                    job = execute(circuit, simulator, shots=1000)
                    result = job.result()
                    counts = result.get_counts(circuit)
                    cirprint = circuit.draw()
                    response = "Total count for 00 and 11 are:-" + str(counts) + ".\nPlease Find below circuit diagram for the following.\n" + str(cirprint) + "\nPlease, find the popup for the plot of histogram for the same."
                    plot_histogram(counts)
                    plt.plot()
                    plt.savefig('/tmp/claiqisfigure.png')
                    im = Image.open('/tmp/claiqisfigure.png')
                    im.show()                   
                    
            else:
                response = "\nFew parts missing. Please, Try >> clai qcomputing bvazirani secretnumber or Try >> clai qcomputing hello"
            
            confidence = 0.0

            return Action(
                suggested_command=NOOP_COMMAND,
                execute=True,
                description=Colorize().info().append(response).to_console(),
                confidence=confidence)

        except Exception as ex:
            return [ { "text" : "Method failed with status " + str(ex) }, 0.0 ]

# Reference:-
# Courtesy for Method Hello World function/ Documentation:- https://qiskit.org/documentation/getting_started.html
# Courtesy for Method Bernstein Vazirani function:- https://www.youtube.com/watch?v=sqJIpHYl7oo&list=PLOFEBzvs-Vvp2xg9-POLJhQwtVktlYGbY&index=6
