'''
  ansatz.py                                                          
                                                              
  This code is distributed under the constitution of GNU-GPL. 
  (c) PearCandy                              
                                                              
  Log of vqe.py of StrayQat                                                   
                                                              
  2021/1/26  Firset Release

                                                           '''
#coding:utf-8
#-------------------------------------------------------------

from __future__ import unicode_literals, division

import numpy as np
import qulacs
from qulacs import QuantumState, QuantumCircuit
from qulacs.gate import CZ, RY, RZ, merge, CNOT
from qulacs import Observable
from qulacs.observable import create_observable_from_openfermion_text
from scipy.sparse.linalg import eigs, eigsh


class Ansatz():
    def __init__(self, ansatz_type, n_qubit, depth):
        version = "0.2"
        self.ansatz_type = ansatz_type
        self.n_qubit = n_qubit
        self.depth = depth
        self.version = version

    def set_initial_theta(self):
        if self.ansatz_type == "HE":
            init_theta_list = np.random.random(2 * self.n_qubit *
                                               (self.depth + 1)) * 1e-1
        elif self.ansatz_type == "SYMP":
            init_theta_list = np.random.random(
                (self.n_qubit - 1) * self.depth) * 1.e-1
        else:
            init_theta_list = np.random.random(2 * self.n_qubit *
                                               (self.depth + 1)) * 1e-1
        return init_theta_list

    def circuit(self, theta_list):
        if self.ansatz_type == "HE":
            circuit = self.HE_circuit(theta_list)
        elif self.ansatz_type == "SYMP":
            circuit = self.SYMP_circuit(theta_list)
        else:
            circuit = self.HE_circuit(theta_list)
        return circuit

    def HE_circuit(self, theta_list):
        """
        Hardware Efficiency ansatz
        Returns hardware efficient ansatz circuit.
    
        Args:
        n_qubit (:class:`int`):
           the number of qubit used (equivalent to the number of fermionic modes)
        depth (:class:`int`):
           depth of the circuit.
        theta_list (:class:`numpy.ndarray`):
           rotation angles.
        Returns:
           class:`qulacs.QuantumCircuit`
        """
        # quantum circuit
        circuit = QuantumCircuit(self.n_qubit)
        for d in range(self.depth):
            for i in range(self.n_qubit):
                circuit.add_gate(
                    merge(RY(i, theta_list[2 * i + 2 * self.n_qubit * d]),
                          RZ(i, theta_list[2 * i + 1 + 2 * self.n_qubit * d])))
            for i in range(self.n_qubit // 2):
                circuit.add_gate(CZ(2 * i, 2 * i + 1))
            for i in range(self.n_qubit // 2 - 1):
                circuit.add_gate(CZ(2 * i + 1, 2 * i + 2))
        for i in range(self.n_qubit):
            circuit.add_gate(
                merge(
                    RY(i, theta_list[2 * i + 2 * self.n_qubit * self.depth]),
                    RZ(i,
                       theta_list[2 * i + 1 + 2 * self.n_qubit * self.depth])))
        return circuit

    def SYMP_circuit(self, theta_list):
        """
        Symmetry-Preserving ansatz
        Returns hardware efficient ansatz circuit.
            
        Args:
        n_qubit (:class:`int`):
           the number of qubit used (equivalent to the number of fermionic modes)
        depth (:class:`int`):
           depth of the circuit.
        theta_list (:class:`numpy.ndarray`):
           rotation angles.
        Returns:
           class:`qulacs.QuantumCircuit`
        """
        # quantum circuit
        circuit = QuantumCircuit(self.n_qubit)
        for d in range(self.depth):
            for i in range(self.n_qubit // 2):
                circuit.add_gate(CNOT(i * 2,
                                      i * 2 + 1))  # CNOT(control, target)
                circuit.add_gate(
                    RY(i * 2,
                       theta_list[i * 2 + (self.n_qubit - 1) * d] * (-1.0)))
                circuit.add_gate(CNOT(i * 2 + 1, i * 2))
                circuit.add_gate(
                    RY(i * 2, theta_list[i * 2 + (self.n_qubit - 1) * d]))
                circuit.add_gate(CNOT(i * 2, i * 2 + 1))
            for i in range(self.n_qubit // 2 - 1):
                circuit.add_gate(CNOT(2 * i + 1,
                                      2 * i + 2))  # CNOT(control, target)
                circuit.add_gate(
                    RY(2 * i + 1, theta_list[2 * i + 1 +
                                             (self.n_qubit - 1) * d] * (-1.0)))
                circuit.add_gate(CNOT(2 * i + 2, 2 * i + 1))
                circuit.add_gate(
                    RY(2 * i + 1,
                       theta_list[2 * i + 1 + (self.n_qubit - 1) * d]))
                circuit.add_gate(CNOT(2 * i + 1, 2 * i + 2))
        return circuit
