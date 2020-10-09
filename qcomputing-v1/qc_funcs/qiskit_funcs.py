import pandas as pd
import os
import sys

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from PIL import Image
from qiskit import *
from qiskit.tools.visualization import plot_histogram 
from qiskit.optimization.algorithms import GroverOptimizer
from qiskit.optimization.problems import QuadraticProgram
from qiskit import BasicAer

import time, json
from typing import List, Optional, Any
from docplex.mp.model import Model
from qiskit.aqua.algorithms import QAOA, NumPyMinimumEigensolver
from qiskit.optimization.algorithms import CobylaOptimizer, MinimumEigenOptimizer
from qiskit.optimization.algorithms.admm_optimizer import ADMMParameters, ADMMOptimizer
'''
Here we define all the functions which we will be using from the qiskit library.
'''

'''
This is implementation of Berstein Vazirani function using the qiskit library
'''
def bvazirani(commandTok):
    secretno = str(commandTok[1])
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
    return response

'''
This is sample implementation of a example function using the qiskit library
'''
def hello(command):
    if command=="hello":
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
        return response

'''
This is implementation of Grover Optimizer function using the qiskit library
'''
def groveropt(commandTokenized):
    backend = BasicAer.get_backend('statevector_simulator')
    mod = QuadraticProgram('Grover_Optimizer_on_Quadratic_Program')
    mod.binary_var(name='x')
    mod.binary_var(name='y')
    mod.binary_var(name='z')
    
    constant_value = int(commandTokenized[1])
    linear_coeff = json.loads(commandTokenized[2])
    quadratic_coeff = json.loads(commandTokenized[3])
    
    mod.minimize(constant=constant_value, linear=linear_coeff, quadratic=quadratic_coeff)

    grover_optimizer = GroverOptimizer(6, num_iterations=1, quantum_instance=backend)
    results = grover_optimizer.solve(mod)
    response = mod.export_as_lp_string() + ".\nsolution of x={}".format(results.x) + ".\n" + "fval={}".format(results.fval)
    return response

'''
This is implementation of Alternating Direction Method of Multipliers (ADMM) Optimizer function using the qiskit library
'''
def admmopt(commandTokenized):
    cobyla = CobylaOptimizer()

    qaoa = MinimumEigenOptimizer(QAOA(quantum_instance=BasicAer.get_backend('statevector_simulator')))

    exact = MinimumEigenOptimizer(NumPyMinimumEigensolver()) # to solve QUBOs

    constant_value = int(commandTokenized[1])
    linear_coeff = json.loads(commandTokenized[2])
    quadratic_coeff = json.loads(commandTokenized[3])
    cons1 = json.loads(commandTokenized[4])
    consense1 = commandTokenized[5]
    cons2 = json.loads(commandTokenized[6])
    consense2 = commandTokenized[7]
    cons3 = json.loads(commandTokenized[8])
    consense3 = commandTokenized[9]

    mod = QuadraticProgram('ADMM_Optimizer')
    mod.continuous_var(name='u')
    mod.binary_var(name='v')
    mod.binary_var(name='w')
    mod.binary_var(name='t')

    mod.linear_constraint(linear={'u': int(cons1[0]), 'v': int(cons1[1]), 'w':int(cons1[2]), 't':int(cons1[3])}, sense=consense1, rhs=int(cons1[4]))
    mod.linear_constraint(linear={'u': int(cons2[0]), 'v': int(cons2[1]), 'w':int(cons2[2]), 't':int(cons2[3])}, sense=consense2, rhs=int(cons2[4]))
    mod.linear_constraint(linear={'u': int(cons3[0]), 'v': int(cons3[1]), 'w':int(cons3[2]), 't':int(cons3[3])}, sense=consense3, rhs=int(cons3[4]))
    mod.minimize(constant=constant_value, linear=linear_coeff, quadratic=quadratic_coeff)

    admm_params = ADMMParameters(
                                rho_initial=1001,
                                beta=1000,
                                factor_c=900,
                                max_iter=10,
                                three_block=True, tol=1.e-6
                            )
    qubo_optimizer = exact
    
    convex_optimizer = cobyla
    
    admm = ADMMOptimizer(params=admm_params,
                        qubo_optimizer=qubo_optimizer,
                        continuous_optimizer=convex_optimizer)

    result = admm.solve(mod)
    plt.plot(result.state.residuals)
    plt.xlabel("Iterations")
    plt.ylabel("Residuals")
    plt.savefig('/tmp/claiqcomputingadmm.png')
    im = Image.open('/tmp/claiqcomputingadmm.png')
    im.show()                   
    response = mod.export_as_lp_string() + "\n solution of function x={}".format(result.x) + "\n fval={:.2f}".format(result.fval)
    return response

def funcheck(tester, command_generated):
    if tester == '0':
        response = bvazirani(command_generated)
    elif tester == '1':
        response = groveropt(command_generated)
    elif tester == '2':
        response = admmopt(command_generated)
    elif tester == '3':
        response = hello("hello")
    else:
	response = "we don't have a option"
    
    return response
