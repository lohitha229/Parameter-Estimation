# Inverse Parameter Estimation of a Parametric Curve

## Objective

The objective of this assignment is to estimate the unknown parameters of the given parametric curve using the provided dataset (`xy_data.csv`). The unknown parameters are θ (theta), M, and X.

## Given Equation

x = t * cos(θ) - e^(M|t|) * sin(0.3t) * sin(θ) + X

y = 42 + t * sin(θ) + e^(M|t|) * sin(0.3t) * cos(θ)

where:

- 0° < θ < 50°
- -0.05 < M < 0.05
- 0 < X < 100
- 6 < t < 60


## Approach

I started by loading the given `xy_data.csv` file using Pandas. Then, I implemented the parametric equations in Python. Since the values of θ, M, X, and t were unknown, I used the `least_squares` optimization function from the SciPy library to estimate them.

The optimization algorithm repeatedly adjusted the parameter values until the predicted curve matched the given data points as closely as possible. After finding the best-fit parameters, I calculated the Mean L1 Distance to check how well the estimated curve matched the original data. Finally, I plotted both the given points and the fitted curve to visually verify the result.


## Estimated Parameters

| Parameter | Estimated Value |
|-----------|----------------:|
| θ | 29.999973° |
| M | 0.030000 |
| X | 54.999998 |


## Mean L1 Distance

**0.000003**

The very small L1 distance shows that the estimated curve closely matches the given data.


## Final Equation (LaTeX)

```latex
\left(
t\cos(29.999973^\circ)-e^{0.030000|t|}\sin(0.3t)\sin(29.999973^\circ)+54.999998,\;
42+t\sin(29.999973^\circ)+e^{0.030000|t|}\sin(0.3t)\cos(29.999973^\circ)
\right)
```


## Desmos Equation

```text
(t*cos(0.5235983)-e^(0.03*abs(t))*sin(0.3t)*sin(0.5235983)+54.999998,
42+t*sin(0.5235983)+e^(0.03*abs(t))*sin(0.3t)*cos(0.5235983))
```


## Desmos Link

https://www.desmos.com/calculator/tqpjny5avl


## Files Included

- `estimateParameters.py`
- `xy_data.csv`
- `requirements.txt`
- `curve.png`
- `README.md`


## Tools Used

- Python
- NumPy
- Pandas
- SciPy
- Matplotlib


## Output

The predicted curve almost completely overlaps the given data points. This confirms that the estimated values of θ, M, and X provide an excellent fit for the given dataset.


## Conclusion

In this assignment, I estimated the unknown parameters of the given parametric curve using nonlinear least-squares optimization. The estimated values produced a curve that closely matched the provided data points, resulting in a very small Mean L1 Distance. This shows that the optimization method was able to recover the unknown parameters accurately.
