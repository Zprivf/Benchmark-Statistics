Hydro-Benchmark: Python Benchmarking Tool for Hydrological Models
Welcome to Hydro-Benchmark, a comprehensive Python library dedicated to the evaluation of hydrological models. This repository provides Python code to compute benchmark statistics including Pearson’s correlation coefficient r, Nash-Sutcliffe Efficiency (NSE), Kling-Gupta Efficiency (KGE), and Percent Bias (PBIAS).

Features
Versatility: The code is designed to work with any hydrological model results, making it a versatile tool for researchers and practitioners in the field of hydrology.
USGS Station Support: The library includes functionality to fetch and process data from USGS stations, allowing users to compare their model results with real-world observations.
Benchmark Statistics: The core feature of this library is the computation of key benchmark statistics. These include:
Pearson’s correlation coefficient r: A measure of the linear correlation between the modeled and observed data.
Nash-Sutcliffe Efficiency (NSE): Evaluates the relative magnitude of the residual variance compared to the measured data variance.
Kling-Gupta Efficiency (KGE): A three-component metric that assesses the simultaneous correlation, bias, and variability between the modeled and observed data.
Percent Bias (PBIAS): Measures the average tendency of the simulated data to be larger or smaller than their observed counterparts.
Usage
The Python scripts provided in this repository are easy to use and well-documented. Users can compute the benchmark statistics for their model results against USGS station data with just a few lines of code.

We invite you to explore this repository, try out the code, and contribute to its development. Your feedback and contributions are greatly appreciated!

Note: This project is open-source and is intended for educational and research purposes. Please ensure appropriate citation if you use this tool in your research
