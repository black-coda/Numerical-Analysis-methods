# **Numerical Techniques**

> A Numerical method is a mathematical tool designed to solve numerical problems. The implementation of a numerical method with an appropriate convergence check in a programming language is called a numerical algorithm.

 #### It is the study of numerical methods that attempt at finding approximate solutions of problems rather than the exact ones.



 ### **Numerical method used for solving Ordinary Differential Equations:**

 1. Euler's Method
2. Modified Euler's Method
3. Heun's Method or Improved Euler's method

<br/>
<br/>
<br/>



### [**Euler's Method**](https://github.com/black-coda/Numerical-Analysis-methods/blob/main/methods_utils/eulers_method.py)
<br/>


>  Euler method (also called the forward Euler method) is a first-order numerical procedure for solving ordinary differential equations (ODEs) with a given initial value. It is the most basic explicit method for numerical integration of ordinary differential equations and is the simplest Runge–Kutta method
<br/>

#### **Geometric Description**

> In Euler’s method, you can approximate the curve of the solution by the tangent in each interval (that is, by a sequence of short line segments), at steps of h.




<br/>
<br/>
<br/>

![Euler's method](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn7.png)

<br/>

![Euler's method](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn_new_2.png)


#### **Pseudocode**

![Euler's method](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn_new_1.png)



<br/>
<br/>
<br/>

### [**Euler's Modified Method**](https://github.com/black-coda/Numerical-Analysis-methods/blob/main/methods_utils/eulers_modified.py)
<br/>


> Euler's method may be very easy to implement but it can't give accurate solutions.    A  very small step size is required for any meaningful result.  In this scheme, since, the starting point of each sub-interval is used to find the slope of the solution curve,  the solution would be correct only if the function is linear. So an improvement over this is to take the arithmetic average of the slopes at xi  and xi+1(that is, at the end points of each sub-interval). The scheme so obtained is called modified Euler's method. It works first by approximating a value to yi+1 and then improving it by making use of average slope. 


<br><br>

![Modified euler's method](https://lh3.googleusercontent.com/UirPkDHKkQQ5cK0MQ95jmh7uoDruX0ExqPYyVwrKxF2VND1a32FFDUfeTwQwhRcHGSFYlrx-ZKB2vcAVJyIqxVJrwcewrgnNEQPncRo0uh31nic9YOjwPTBVxPO3MIuxFAJMvBq-=s0)

<br>

![Modified euler's method](https://lh4.googleusercontent.com/B_zaZ_K5O-Dmd4NkQED988iUSwrhnAhFGxHJ4HIkKCFqyZIup51BQwzbQuelxUIOJECdDUovF-oA7ILxdLQYov2uNivqjQv0U_x73n7EJkUvywVMk385_s6kokCedlne8Bxn0VZ6=s0)




### [**Euler's Improved Method**](https://github.com/black-coda/Numerical-Analysis-methods/blob/main/methods_utils/heuns_method.py)
<br/>


> In mathematics and computational science, Heun's method may refer to the improved[1] or modified Euler's method (that is, the explicit trapezoidal rule[2]), or a similar two-stage Runge–Kutta method. It is named after Karl Heun and is a numerical procedure for solving ordinary differential equations (ODEs) with a given initial value. Both variants can be seen as extensions of the Euler method into two-stage second-order Runge–Kutta methods. <br>
The improved Euler method for solving the initial value problem is based on approximating the integral curve of Equation.

Derivation of Heuns or improved method can be found [Here](https://en.wikipedia.org/wiki/Heun%27s_method)



<br><br>

![Modified euler's method](https://personal.math.ubc.ca/~israel/m215/impeuler/img10.png)

<br>

![Modified euler's method](https://personal.math.ubc.ca/~israel/m215/impeuler/img12.png)




