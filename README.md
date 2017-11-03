# smartEuler

This project is an assignment for the class Differential Equations, MATH229, conducted during Fall 2017 at Wesleyan University. Our task was to create a modification of Euler's Method such that the step size changes depending on the estimated inaccuracy of Euler's method.

## Getting Started

This project was coded using python3 so make sure python3 is installed on your computer.

### Prerequisites

This project requires the following packages:
Matplotlib
NumPy
mpmath

A quick way to install these dependencies would be to use Python Package Index.
Type the following command into your terminal.
```
pip3 install matplotlib numpy mpmath
```

### Installing

Clone or pull the git repository into your local directory.

## Description of Modules

A brief description of the various modules will be included below

### RKeuler

Contains an implementation of Euler's Method and Runge-Kutta 4. They both accept the following arguments in the following order:
1) Differential Equation
2) Beginning timestep for Numerical Integration
3) End timestep Numerical Integration
4) Initial Condition
5) Step Size

```
eulerMethod(function,tstart,tend,yinitial,dt)
```

### smartEuler

Contains our implementation of Euler's Method with an adaptive step size. It accepts the same arguments as the functions in RKeuler
```
adaptiveEuler(function,tstart,tend,yinitial,h)
```
Note: Since step size changes dynamically in this function, dt has been renamed h since.

### test 


## Authors

* **Tristan Ang** - [tristanang](https://github.com/tristanang)
* **Desmond Yao**
* **Scott Ji**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Mom
* Dad
