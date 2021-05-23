library(reticulate)
library(flacco)
library(parallelMap)
library(parallel)

# Other packages to install
# plyr
# RANN
# numDeriv
# e1071
# mda - needs to install gcc-fortran on Operating system


genTestFeatures <- function(path,pypath, upper=10, lower=-10, n) {
    
    use_python(pypath)
    source_python(path)
    
    X = createInitialSample(n.obs = 500, dim = n, control = list(init_sample.type = 'lhs', init_sample.lower = lower, init_sample.upper = upper))
    
    y = apply(X, 1, main)
    
    testfunc <- createFeatureObject(X = X, y = y, fun = main, lower = lower, upper = upper, blocks = 10)
    
    n.cores = detectCores()
    parallelStart(mode = "local", logging = FALSE, show.info = FALSE)
    system.time((levelset.par = calculateFeatures(testfunc , control = list('cm_angle.show_warnings'=TRUE, 'cm_grad.show_warnings'=TRUE, 'ic.show_warnings'=TRUE))))
    parallelStop()
    
    
}
