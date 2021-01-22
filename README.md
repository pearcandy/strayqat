
![strayqat_logo](https://github.com/pearcandy/strayqat/blob/master/img/logo.png?raw=true)

## StrayQat

StrayQat is a toolkit for quantum chemistry with quantum computer.

StrayQat is licensed under the [GNU lv3 license](https://github.com/pearcandy/strayqat/blob/master/LICENSE).

### Key Features
- Variational Quantum Eigensolver
- Post HF calculation via pySCF, openfermion
- Quantum Gate calculation via qulacs

### Performance

### Requirement
- scipy < 1.5.x
- numpy > 1.19.x
- qulacs
- pyscf
- openfermion
- openfermionpyscf

### Install
```
git clone https://github.com/pearcandy/strayqat
cd strayqat
python setup.py install
```

### Uninstall
```
python setup.py install --record file.txt  
cat file.txt | xargs rm -rvf
```
