
# QComputing

`Quantum-Computing` `Data-Analytics` `NLP` `Support` `Plots` `Quantum-Circuts`

[Quantum Computing](https://en.wikipedia.org/wiki/Quantum_computing) is what next technology which specializes in the use of quantum phenomena such as superposition and entanglement to perform computation. Here, we use [Qiskit](https://qiskit.org/) which is an opensource SDK for working with quantum computers at the level of pulses, circuit and algorithms (Qiskit - Definition). Researchers with the advances of this technology can leverage for innovating and creating apparatus of Greater good. QComputing Plugin in Project (CLAI) Command Line AI implements primary tasks like a) [Hello World](https://qiskit.org/documentation/getting_started.html) on Quantum Circuit while plotting the circuit and b) guesses the secret code using ["Berstein Vazirani"](https://www.youtube.com/watch?v=sqJIpHYl7oo&list=PLOFEBzvs-Vvp2xg9-POLJhQwtVktlYGbY&index=6) algorithm, while plotting the circuit involved in it. A goto plugin like QComputing comes handy with myriad of analysis for future quantum computing needs.

## Implementation

Command usage:- clai qcomputing function attribute
e.g. 
1) `>> clai qcomputing hello`, when this command is executed one can view the sample example of hello world and outputs the circuit diagram for the same.
![figure1](https://github.com/madhavanpallan/clai_qiskit/blob/devel/qcomputing-v0/figures/qiskit_helloworld.png) 

2) `>> clai qcomputing bvazirani 5_digit_binary_number`, when this command is executed one can view the secret number entered, which is identified by the Berstein Vazirani algorithm and output of the circuit diagram is shown for the same. The execution is currently limited to 5 digits of the binary number as input(e.g. 10101 local system restriction).
![figure2](https://github.com/madhavanpallan/clai_qiskit/blob/devel/qcomputing-v0/figures/qiskit_bernstein_vazirani.png)

3) `>> clai qcomputing groveropt constant_value list_coefficient_linear_variable list_coefficient_quadratic_variable`, when this command is executed one can find minimization of a Quadratic unconstrained Binary Optimization problem and get solution to the variable and value of minimized objective function. The definition can be seen below.Grover Optimizer utilizes a techniques called GAS(here, GAS is Grover Adaptive Search (GAS) which has been explored as a possible solution for combinatorial optimization problems, alongside variational algorithms such as Variational Quantum Eigensolver (VQE) and Quantum Approximate Optimization Algorithm (QAOA)), by minimizing a Quadratic Unconstrained Binary Optimization (QUBO) problem. [read more](https://qiskit.org/documentation/tutorials/optimization/4_grover_optimizer.html)
>* Change the value of iterations, for better result in Grover Optimizer.
![figure3](https://github.com/madhavanpallan/clai_qiskit/blob/devel/qcomputing-v0/figures/qiskit_grover_optimization.png)

4) `>> clai clai qcomputing admmopt arg1 arg2 arg3 arg4 arg5 arg6 arg7 arg8 arg9 `, Alternating Direction Method of Multipliers (ADMM) Optimizer is used to solve classes of mixed-binary constrained optimization problems and is used in logistic, finance, and operation research. [More details](https://qiskit.org/documentation/tutorials/optimization/5_admm_optimizer.html)

here, We consider an objective function with 4 variables (3 binary, 1 continuous)
>* arg1 - constant in the objective function
>* arg2 - list of the coefficient of linear variables
>* arg3 - list of the coefficient of the quadratic variable
>* arg4 - list of the coefficient of linear constraint 1 and RHS value 
>* arg5 - sense of linear constraint 1. EQ - equal, LQ - less than equal
>* arg6 - list of the coefficient of linear constraint 2 and RHS value 
>* arg7 - sense of linear constraint 2
>* arg8 - list of the coefficient of linear constraint 3 and RHS value 
>* arg9 - sense of linear constraint 3
>* Change the value of iterations, for better result in ADMM Optimizer.
![figure4](https://github.com/madhavanpallan/clai_qiskit/blob/devel/qcomputing-v0/figures/qiskit_admm_optimization.png)

*** Courtesy of Qiskit [code](https://qiskit.org) and [tutorial](https://www.youtube.com/qiskit).
## News 

## [xkcd](https://uni.xkcd.com/)

We actually reached the future about three years ago.

![alt text](https://imgs.xkcd.com/comics/startling.png "We actually reached the future about three years ago.")
