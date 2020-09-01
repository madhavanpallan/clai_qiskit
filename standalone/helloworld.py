# Program - Hello World
# Courtesy - python

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image

from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
from qiskit.visualization import plot_histogram
from qiskit import IBMQ
from qiskit.tools.monitor import job_monitor

simulator = Aer.get_backend('qasm_simulator')

#Create a quantum circuit
circuit = QuantumCircuit(2, 2)

#Circuit operation
circuit.h(0)

circuit.cx(0, 1)

circuit.measure([0,1], [0,1])

#Job execution
job = execute(circuit, simulator, shots=1000)

result = job.result()

#Return counts
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

#The below part of the program is run on a real Quantum Computer(QC). The job may take time to print result as scheduled by the IBM QC System.
#For the first time you need to save the IBMQ token in your local computer by running below line after importing IBMQ.
#IBM.save_account('IBMQ-API-TOKEN')

IBMQ.load_account()
provider = IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('ibmq_16_melbourne')
job_qc = execute(circuit, backend=qcomp)

job_monitor(job_qc)
result_qc = job_qc.result()
img = plot_histogram(result_qc.get_counts(circuit))
img.show()

