
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


*** Courtesy of Qiskit [code](https://qiskit.org) and [tutorial](https://www.youtube.com/qiskit).

## [xkcd](https://uni.xkcd.com/)

We actually reached the future about three years ago.

![alt text](https://imgs.xkcd.com/comics/startling.png "We actually reached the future about three years ago.")
