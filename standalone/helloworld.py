# Program - Hello World
# Courtesy - pytoh

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image

from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
from qiskit.visualization import plot_histogram

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.h(0)

circuit.cx(0, 1)

circuit.measure([0,1], [0,1])

job = execute(circuit, simulator, shots=1000)

result = job.result()

counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)

print("Please, find below diagram for qiskit circuit")
cirprint = circuit.draw()
print(cirprint)
 
print("Please, find below histogram for the same.")
plot_histogram(counts)
plt.plot()
plt.savefig('/tmp/claifigure.png')
im = Image.open('/tmp/claifigure.png')
im.show()
