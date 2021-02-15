
![strayqat_logo](https://github.com/pearcandy/strayqat/blob/master/img/logo.png?raw=true)

Tools for quantum chemistry with quantum computer.  
(licensed under the [GPLv3 license](https://github.com/pearcandy/strayqat/blob/master/LICENSE)).

#### Features
- Variational Quantum Eigensolver
- Post HF calculation via pySCF, openfermion
- Quantum Gate calculation via qulacs
 

#### VQE concept

![vqe_concept](https://github.com/pearcandy/strayqat/blob/master/img/VQE_concept.png?raw=true)

> A. Peruzzo et al. , “A variational eigenvalue solver on a photonic quantum processor“ Nat. Commun. 5:4213 doi: 10.1038/ncomms5213 (2014)

#### Performance

- ground state energy of H2 molecular at various bonding length.

![strayqat_demo](https://github.com/pearcandy/strayqat/blob/master/img/demo_H2.png?raw=true)


#### Requirement
- scipy == 1.4.1
- numpy > 1.18.x
- qulacs == 0.2.0
- pyscf  == 1.7.2
- openfermion == 1.0.0
- openfermionpyscf == 0.5

#### Install 
```
pip install git+https://github.com/pearcandy/strayqat
```


#### Uninstall
```
pip uninstall strayqat
```
