========
StrayQat
========
.. image:: ./img/sq.png
   :scale: 20%
   :height: 100px
   :width: 200px
   :align: left

A toolkit for quantum chemistry with quantum computer


Key Features
=======
- Variational Quantum Eigensolver
   | **support Ansatz**
   | "Hardware Efficiency"
   | "Symmetry Preserving" 
   | (Unitary Coupled Cluster ansatz will be implemented in next version.)

- Post HF calculation via pySCF, openfermion
   | `pySCF <https://github.com/pyscf/pyscf>`_
   | `OpenFermion <https://github.com/quantumlib/OpenFermion>`_
- Quantum Gate calculation via qulacs
   | `qulacs <https://github.com/qulacs/qulacs>`_

  
Performance
===========
- Grand state energy of H2 molecule for each distance between H atoms
   .. image:: ./img/demo_H2.png
    :scale: 40%
    :height: 100px
    :width: 200px
    :align: left

- Grand state energy for some small molecules
   ==============   ========== ========== 
         \            FCI [Hr]    VQE [Hr]
   ==============   ========== ==========
   H2O              -75.0124    -74.9629
   CH4 (CAS(6.4))   -39.7283    -38.3572
   CO2 (CAS(2,2))   -185.0913   -185.0913
   ==============   ========== ==========



rRquirement
===========
- scipy < 1.5.x
- numpy > 1.19.x
- qulacs
- pyscf
- openfermion
- openfermionpyscf

Install
=======

to install strayqat:

.. code-block:: sh
		
    git clone https://github.com/pearcandy/strayqat
    cd strayqat
    python setup.py install


    
Uninstall
=========

.. code-block:: sh
		
    python setup.py install --record file.txt  
    cat file.txt | xargs rm -rvf  

