from dataclasses import dataclass
import numpy as np 
import sympy
from typing import Optional


@dataclass
class ssSystem:
    """Class for holding dynamic and msmt info for a State-Space system"""
    A: np.ndarray
    B: Optional[np.ndarray]
    G: Optional[np.ndarray]
    C: Optional[np.ndarray]
    D: Optional[np.ndarray]

@dataclass
class SymSystem:
    """Class for holding dynamic and msmt info for a State-Space system in symbolic form"""
    A: sympy.matrices.dense.MutableDenseMatrix  # state transition matrix 
    B: Optional[sympy.matrices.dense.MutableDenseMatrix]  # control input matrix 
    G: Optional[sympy.matrices.dense.MutableDenseMatrix]  # the process noise input matrix 
    C: Optional[sympy.matrices.dense.MutableDenseMatrix]  # the observation matrix
    D: Optional[sympy.matrices.dense.MutableDenseMatrix]  # the msmt. noise matrix 

@dataclass
class KF:
    """Class for holding Kalman filter information. Note that all varables are updated at each time step."""
    x_hat: np.ndarray   # the msmt. update state estimate 
    P_hat: np.ndarray   # the x_hat's covariance 
    x_bar: np.ndarray   # the time update state estimate 
    P_bar: np.ndarray   # x_bar's covariance 
    z: np.ndarray       # the msmt. vector
    V: np.ndarray       # the covariance of the msmt. noise 
    # 'w,' the noise vector, is not a feature of the class since it is generated 
    W: np.ndarray       # the covariance of the process noise 
    L: np.ndarray       # the Kalman gain
    Phi: np.ndarray     # the state transition matrix 
    Gamma: np.ndarray   # the process noise transition matrix 
