# GPplus
GPplus combines a parametric model for the relationship between the target feature and location specific characteristics and an additive nonparametric model for spatial dependencies using Gaussian Processes (GP). The combination of Bayesian linear regression and spatial dependencies is extremely flexible and applicable to a large suite of data science problems, as tested in social-demographic, crime, environment, and geophysical analysis. 

Inference about model parameters and their uncertainty is carried out via a fast parallel Markov chain Monte Carlo (MCMC) sampler, which is a very efficient way for multidimensional integration. For sampling the posterior distribution, GPplus uses the affine-invariante MCMC ensemple sampler, "emcee" (Foreman-Mackey et al, 2013, Goodman and Weare, 2010).

The implemented method is a fully probabilistic approach, allowing uncertainties in prediction and inference to be quantified via the posterior distributions of interest. By using Bayesian updating, these predictions and inferences are dynamic in the sense that they change as new information becomes available. 


