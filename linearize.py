import numpy as np
import sympy

def linearize(A: sympy.matrices.dense.MutableDenseMatrix, vars: list, dim: tuple):
    n = dim[0] # get dimensions from input argument 
    m = dim[1]
    # initialize and populate linearized A matrix
    dA = sympy.Matrix(np.zeros((n, m)))
    for i in range(0,n,1):
        for j in range(0,m,1):
            dA[i,j] = sympy.diff(A[i,0],vars[j])
    varsa = list(dA.free_symbols)

    return dA, varsa

    # init_map = Dict{Sym, Float64}()
    # accumulator = 1;
    # for var in vars[eachindex(vars)]
    #     init_map[var] = initials[accumulator] # note: this enforces a certain convention for how initial conditions are accepted
    #     accumulator = accumulator + 1; 
    # end
    # println("init_map \n", init_map)

    # initStruct = initMap(init_map,varsa,varsb)
    # sysout = sysd_sym(dA,dB,C,D,varsx,varsu)
    # return sysout, initStruct, vars 
 
