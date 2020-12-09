from qiskit import IBMQ
from qiskit.aqua import QuantumInstance
from shors import Shors
import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
from math import gcd
from numpy.random import randint
import pandas as pd
from fractions import Fraction

IBMQ.enable_account(
    '8cd11e82260ef3b66215a7699d2ae154e1c7cd2b94cea401741b2abe7e7f39fc2258b45c4a31a5bd6c47de7f0e10c8f5c3abd0bdd23b0abb81cea1d56d0c6032')
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator')  # Specifies the quantum device

print('\n Shors Algorithm')
print('--------------------')
print('\nExecuting...\n')

N = 35
a = 3
factors = Shors(N, a)  # Function to run Shor's algorithm where 21 is the integer to be factored

xvals = factors.order()
yvals = [np.mod(a ** x, N) for x in xvals]

# getting possible period values
r = yvals[1:].index(1) + 1
print(r)

check = a**(r/2) + 1
print(check)
if check != 0:
    print(factors.gcd())
