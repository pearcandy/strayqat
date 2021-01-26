'''
  vqe.py                                                          
                                                              
  This code is distributed under the constitution of GNU-GPL. 
  (c) PearCandy
                                                              
  Log of vqe.py of StrayQat 
                                                              
  2021/1/26  Firset Release
                                                              
                                                           '''
#coding:utf-8
#-------------------------------------------------------------

from __future__ import unicode_literals, division

__author__ = "PearCandy"
__version__ = "0.1"
__maintainer__ = "PearCandy"
__email__ = "y.nishi1980@gmail.com"
__status__ = "Stable"
__date__ = "Jan 26, 2021"

import sys, os
import numpy as np
import matplotlib.pyplot as plt
from openfermion.transforms import get_fermion_operator, jordan_wigner
from openfermion.transforms import get_sparse_operator
from openfermion.hamiltonians import MolecularData
from openfermionpyscf import run_pyscf, generate_molecular_hamiltonian
from . import ansatz
from scipy.optimize import minimize
from scipy.sparse.linalg import eigs, eigsh
from pyscf import fci


class Main():
    def __init__(self,
                 n_qubit=2,
                 depth=1,
                 theta_list=[],
                 hamiltonian=None,
                 method='CG',
                 ansatz_type='HE',
                 disp=False,
                 maxiter=100,
                 gtol=1e-8,
                 gpu=False,
                 noise=False):

        self.n_qubit = n_qubit
        self.depth = depth
        self.ansatz_type = ansatz_type
        self.theta_list = theta_list
        self.hamiltonian = hamiltonian
        self.method = method
        self.disp = disp
        self.maxiter = maxiter
        self.gtol = gtol
        self.gpu = gpu
        self.noise = noise

    def __str__(self):
        return str({
            "qubit": self.n_qubit,
            "depth": self.depth,
            "ansatz": self.ansatz_type,
            "maxiter": self.maxiter,
            "gtol": self.gtol,
            "noise": self.noise
        })

    def set_qauntum_state(self):
        if self.gpu:
            from qulacs import QuantumStateGpu
            if self.ansatz_type == 'HE':
                state = QuantumStateGpu(self.n_qubit)
            elif self.ansatz_type == 'SYMP':
                state = QuantumStateGpu(self.n_qubit)
                # set HF reference state
                from qulacs.gate import X
                for i in range(self.n_qubit // 2):
                    x_gate = X(i)
                    x_gate.update_quantum_state(state)
            else:
                state = QuantumStateGpu(self.n_qubit)
        else:
            from qulacs import QuantumState
            state = QuantumState(self.n_qubit)
            if self.ansatz_type == 'HE':
                state = QuantumState(self.n_qubit)
            elif self.ansatz_type == 'SYMP':
                state = QuantumState(self.n_qubit)
                # set HF reference state
                from qulacs.gate import X
                for i in range(self.n_qubit // 2):
                    x_gate = X(i)
                    x_gate.update_quantum_state(state)
            else:
                state = QuantumState(self.n_qubit)
        return state

    def cost(self, theta_list):
        state = self.set_qauntum_state()
        pram_circuit = ansatz.Ansatz(self.ansatz_type, self.n_qubit,
                                     self.depth)
        circuit = pram_circuit.circuit(theta_list)
        circuit.update_quantum_state(state)

        if self.noise == False:
            return self.hamiltonian.get_expectation_value(state)
        else:
            return self.hamiltonian.get_expectation_value(
                state) + np.random.normal(0, 0.01)

    def run(self):
        self.cost_history = []
        ans = ansatz.Ansatz(self.ansatz_type, self.n_qubit, self.depth)
        init_theta_list = ans.set_initial_theta()
        self.cost_history.append(self.cost(init_theta_list))
        options = {
            "disp": self.disp,
            "maxiter": self.maxiter,
            "gtol": self.gtol
        }
        opt = minimize(
            self.cost,
            init_theta_list,
            method=self.method,
            callback=lambda x: self.cost_history.append(self.cost(x)),
            options=options)
