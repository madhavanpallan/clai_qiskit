# Program - Hello World
# Courtesy - https://www.youtube.com/watch?v=sqJIpHYl7oo&list=PLOFEBzvs-Vvp2xg9-POLJhQwtVktlYGbY&index=6
from qiskit import *
from qiskit.tools.visualization import plot_histogram 

secretno = str('10101111')

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
result = execute(circuit, simulator, shots=1000).result()

# Returns counts
counts = result.get_counts()
print("You Secret code is:- ", counts)
cirprint = circuit.draw()
print(cirprint)
