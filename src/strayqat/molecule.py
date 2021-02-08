'''
  molecule.py                                                          

  This code is distributed under the constitution of GNU-GPL. 
  (c) PearCandy
                                                              
  Log of molecule.py of StrayQat 
                                                              
  2021/1/26  Firset Release
                                                              
                                                           '''
#coding:utf-8
#-------------------------------------------------------------

from __future__ import unicode_literals, division

__author__ = "PearCandy"
__version__ = "0.2"
__maintainer__ = "PearCandy"
__email__ = "y.nishi1980@gmail.com"
__status__ = "Stable"
__date__ = "Jan 26, 2021"

import sys, os
import numpy as np
import matplotlib.pyplot as plt
from openfermion.transforms import get_fermion_operator, jordan_wigner
from openfermion.linalg import get_sparse_operator
from openfermion import MolecularData
from openfermionpyscf import run_pyscf, generate_molecular_hamiltonian
from . import ansatz
from scipy.optimize import minimize
from scipy.sparse.linalg import eigs, eigsh
from pyscf import fci


class Main():
    def __init__(self,
                 basis="sto-3g",
                 multiplicity=1,
                 charge=0,
                 geometry=[["H", [0, 0, 0]], ["H", [0, 0, 0.9]]],
                 n_active_electrons=None,
                 n_active_orbitals=None,
                 description="tmp"):

        self.basis = basis
        self.multiplicity = multiplicity
        self.charge = charge
        self.geometry = geometry
        self.n_active_electrons = n_active_electrons
        self.n_active_orbitals = n_active_orbitals
        self.description = description

    def __str__(self):
        return str({
            "basis": self.basis,
            "multiplicity": self.multiplicity,
            "charge": self.charge,
            "geometry": self.geometry,
            "n_active_electrons": self.n_active_electrons,
            "n_active_orbitals": self.n_active_orbitals
        })

    def get_molecular_data(self):
        if self.n_active_orbitals == None:
            return MolecularData(self.geometry, self.basis, self.multiplicity,
                                 self.charge, self.description)
        else:
            return generate_molecular_hamiltonian(self.geometry, self.basis,
                                                  self.multiplicity,
                                                  self.charge,
                                                  self.n_active_electrons,
                                                  self.n_active_orbitals)

    def run_scf(self):
        molecule = self.get_molecular_data()

        from qulacs.observable import create_observable_from_openfermion_text

        if self.n_active_orbitals == None:
            molscf = run_pyscf(molecule, run_scf=1, run_fci=1)
            self.n_qubits = molecule.n_qubits
            self.n_electron = molscf.n_electrons
            self.fci_energy = molscf.fci_energy
            self.hf_energy = molscf.hf_energy
            self.fermionic_hamiltonian = get_fermion_operator(
                molscf.get_molecular_hamiltonian())
            self.jw_hamiltonian = jordan_wigner(self.fermionic_hamiltonian)
            self.hamiltonian_matrix = get_sparse_operator(self.jw_hamiltonian)
            self.hamiltonian = create_observable_from_openfermion_text(
                str(self.jw_hamiltonian))

        else:
            self.n_qubits = molecule.n_qubits
            self.fermionic_hamiltonian = get_fermion_operator(molecule)
            self.jw_hamiltonian = jordan_wigner(self.fermionic_hamiltonian)
            self.hamiltonian_matrix = get_sparse_operator(self.jw_hamiltonian)
            eigenenergies, eigenvecs = eigs(self.hamiltonian_matrix)
            self.fci_energy = np.real(eigenenergies[0])
            self.hamiltonian = create_observable_from_openfermion_text(
                str(self.jw_hamiltonian))
