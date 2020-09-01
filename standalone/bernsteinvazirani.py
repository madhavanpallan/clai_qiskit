# Program - Bernstein Vazirani Algorithm.
# Courtesy - https://www.youtube.com/watch?v=sqJIpHYl7oo&list=PLOFEBzvs-Vvp2xg9-POLJhQwtVktlYGbY&index=6

from qiskit import *
from qiskit.tools.visualization import plot_histogram 

#Secret number
secretno = str('10101111')

#Creating a modular Quantum circuit
circuit = QuantumCircuit(len(secretno) +1, len(secretno))

#Adding Hadamard gate.
circuit.h(range(len(secretno)))
circuit.x(len(secretno))
circuit.h(len(secretno))

#Applying berstein Vazirani Algorithm
circuit.barrier()
for ii, yesno in enumerate(reversed(secretno)):
    if yesno == '1':
        circuit.cx(ii, len(secretno))

circuit.barrier()
circuit.h(range(len(secretno)))
circuit.barrier()

#Measuring the value along the qubits and storing in the classical bits
circuit.measure(range(len(secretno)), range(len(secretno)))
circuit.draw()  

#Running on the simulator
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, simulator, shots=1000).result()

#Returns counts
counts = result.get_counts()
print("You Secret code is:- ", counts)
cirprint = circuit.draw()
print(cirprint)
