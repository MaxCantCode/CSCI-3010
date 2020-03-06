# CSCI-3010
Simulation and Modeling

https://colab.research.google.com/github/MaxCantCode/CSCI-3010/blob/master/Crystal-Simulation.ipynb

Chapter 1 in the MATH 3050U text on Crystallization dynamics.  In particular, the formula (1.9) on page 11 requires the distribution of the volumes of the Voronoi cells associated with a uniform distribution of nucleation sites.  Formulate this as a 2-D not a 3-D problem (note (1.9) will change slightly) and then try to numerically compute what is now the distribution of area size for the Voronoi cells.  Once you know this, you can compute $\varphi(t)$ and see if you can get it to fit the data on page 18.

$ \displaystyle \varphi(t)=
\int\limits_{0}^{k t^{3}} s f{\left(s \right)}\, ds + k t^{3} \int\limits_{0}^{\infty} f{\left(s \right)}\, ds\quad(1.9)
\\\displaystyle
\varphi(t)=
\int\limits_{0}^{k t^{2}} s f{\left(s \right)}\, ds + k t^{2} \int\limits_{0}^{\infty} f{\left(s \right)}\, ds\quad(1.9) \text{ in 2-D}$

data on page 18:

`dd = [0.0802 0.011;...
0.1522 0.020;... 0.2955 0.044;...
0.3674 0.059;... 0.4391 0.081;...
0.5827 0.135;... 0.7259 0.250;... 0.8696 0.361;... 0.9842 0.476;... 1.0132 0.520;...
1.1564 0.690;... 1.2284 0.777;...
1.3000 0.841;... 1.3741 0.900;...
1.5049 0.962;... 1.6158 0.989;... 1.7305 0.9972];
t = dd(:,1); y = dd(:,2);`

or

$ \displaystyle \varphi(t)=
\int\limits_{0}^{k t^{3}} s f{\left(s \right)}\, ds + k t^{3} \int\limits_{0}^{\infty} f{\left(s \right)}\, ds$

with the empirical choice of

$\displaystyle f(s)= \beta s^{2} e^{- \gamma s^{2}},\beta=2\gamma^2=\frac{32}{\pi^2},k=.3193$

or

$ \displaystyle \varphi(t)=
\dfrac{1}{8\lambda }\left( 1-e^{-8\lambda kt^{3}}\right)$

when
$\displaystyle f(s)= 8\lambda e^{-8\lambda s}$ (systematic deriv)

what i want to simulate https://www.youtube.com/watch?v=hibmI6aGOso

Periodic boundary conditions:
https://pythoninchemistry.org/sim_and_scat/important_considerations/pbc.html
