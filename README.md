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

A brief description of the various modules will be included below.

### RKeuler

Contains an implementation of Euler's Method and Runge-Kutta 4. They both accept the following arguments in the following order:
1) Differential Equation
2) Beginning timestep for Numerical Integration
3) End timestep Numerical Integration
4) Initial Condition
5) Step Size

The output the function is two lists. The first list is a list of time values. The second list is the calculated values of the solution at the coressponding time values in the first list.
```
eulerMethod(function,tstart,tend,yinitial,dt)
```

### smartEuler

Contains our implementation of Euler's Method with an adaptive step size. It accepts the same arguments as the functions in RKeuler
```
adaptiveEuler(function,tstart,tend,yinitial,h)
```
The output format is the same as the functions above.
Note: Since step size changes dynamically in this function, dt has been renamed h since.

### test 
Contains many useful functions for comparing our adaptiveEuler method to eulerMethod.

#### functions[i],diffEQs[i]
Two indexed lists of functions with a given initial condition and its corresponding differential equation.

#### calcSquareError
Takes two inputs, the analytic solution the the function and the chosen numerical integration function with all the appropriate arguments. Returns the average of the squared difference between the actual solution and the numerical integration at every time step. 
```
calcSquareError(functions[0],adaptiveEuler(diffEQs[0],0,1,1,1))
```

#### visualTest
Takes the following arguments:
1) Actual Solution
2) Differential Equation
3) Initial condition
4) Beginning timestep for Numerical Integration
5) End timestep Numerical Integration
6) Step Size
7) Method for Numerical Integration (adaptiveEuler by default)

Plots the graph of the numerical solution and the actual solution such that we can qualitatively see if our integration is accurate.

```
visualTest(functions[0],diffEQs[0],1,0,5,1,eulerMethod)
```

#### timeWrapper
Takes the following arguments:
1) Differential Equation
2) Initial condition
3) Beginning timestep for Numerical Integration
4) End timestep Numerical Integration
5) Step Size
6) Method for Numerical Integration (adaptiveEuler by default)

Returns amount of time taken to run computation 10000 times.
```
calcSquareError(functions[0],adaptiveEuler(diffEQs[0],0,1,1,1))
```

## Authors

* **Tristan Ang** - [tristanang](https://github.com/tristanang)
* **Desmond Yao** - [SASVDERDBGTYS](https://github.com/SASVDERDBGTYS)
* **Scott Ji**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Mom
* Dad
