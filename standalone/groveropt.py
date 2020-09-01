# Program - Grover Optimization Algorithm.
# Courtesy - https://qiskit.org/documentation/tutorials/optimization/4_grover_optimizer.html

from qiskit.aqua.algorithms import NumPyMinimumEigensolver
from qiskit.optimization.algorithms import GroverOptimizer, MinimumEigenOptimizer
from qiskit.optimization.problems import QuadraticProgram
from qiskit import BasicAer
from docplex.mp.model import Model
import sys

backend = BasicAer.get_backend('statevector_simulator')
model = Model()

#Defining binary variable
x0 = model.binary_var(name='x0')
x1 = model.binary_var(name='x1')
x2 = model.binary_var(name='x2')

#Model minmizing
model.minimize(-x0+2*x1-3*x2-2*x0*x2-1*x1*x2)
qp = QuadraticProgram()
qp.from_docplex(model)

print(qp.export_as_lp_string())

#Applying grover optimization
grover_optimizer = GroverOptimizer(6, num_iterations=10, quantum_instance=backend)
results = grover_optimizer.solve(qp)
print("x={}".format(results.x))
print("fval={}".format(results.fval))