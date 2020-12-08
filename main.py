from qiskit import IBMQ
from qiskit.aqua import QuantumInstance
from shors import Shors

IBMQ.enable_account(
    '8cd11e82260ef3b66215a7699d2ae154e1c7cd2b94cea401741b2abe7e7f39fc2258b45c4a31a5bd6c47de7f0e10c8f5c3abd0bdd23b0abb81cea1d56d0c6032')
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator')  # Specifies the quantum device

print('\n Shors Algorithm')
print('--------------------')
print('\nExecuting...\n')

factors = Shors(21, 3)  # Function to run Shor's algorithm where 21 is the integer to be factored

print(factors.gcd())

# result_dict = factors.run(QuantumInstance(backend, shots=1, skip_qobj_validation=False))
# result = result_dict['factors']  # Get factors from results
#
# print(result)
# print('\nPress any key to close')
# input()
