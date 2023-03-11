import numpy as np 
import sympy 
import scipy as sp
import header as h
import simMeasurements as sm
import initialize as init
import pandas as pd

def KalmanFilter(sys: h.SymSystem, init_args: dict, traj: np.matrix, stats: dict, Ts: float, T: float, u: np.matrix, opt: str):
    # convert symbolic, non-linear system to a numeric one. 
    # It will need to be relinearized by passing a column of "traj"
    # as the "initials" field in "init_args"
    sys_num = init.initialize(init_args)
    Phik  = sys_num.A 
    GamUk = sys_num.B
    GamWk = sys_num.G
    Hk    = np.matrix(sys_num.C)
    # D     = sys_num.D
    W     = stats["W"]
    V     = stats["V"]

    nx = Phik.shape[0]
    xbar = np.matrix(np.zeros((Phik.shape[1],int(T*Ts)))) 
    xhat = np.matrix(np.zeros((Phik.shape[1],int(T*Ts)+1))) # plus one is from initial conditions
    xhat[:,0] = np.transpose(np.matrix(stats["x0"]))
    Pbar_list = np.matrix(np.zeros((nx,int(T*Ts)*nx)))
    Phat_list = np.matrix(np.zeros((nx,int(T*Ts)*nx+1)))
    Phat_list[0:nx,0:nx] = np.matrix(stats["P0"])
    Phat = np.matrix(stats["P0"])
    K_list = np.matrix(np.zeros((nx,Hk.shape[0]*int(T*Ts))))
    Hk_list = np.matrix(np.zeros((Hk.shape[0],Hk.shape[1]*int(T*Ts))))
    Phik_list = np.matrix(np.zeros((nx,int(T*Ts)*nx)))
    
    if opt == "S":
        zk = sm.simMeas(V, init_args, traj.shape[1], traj) # simulates measurements of the system
        # convert array into dataframe
        DF = pd.DataFrame(zk)
        # save the dataframe as a csv file
        DF.to_csv("zk.csv")
    if opt == "R":
        zk = np.matrix(pd.read_csv('zk.csv'))
        zk = zk[0:int(T*Ts)]

    for k in range(1,int(T*Ts),1):
        # time update 
        xbar[:,k] = Phik @ xhat[:,k-1] + GamUk @ u[:,k-1]
        Pbar = Phik @ Phat @ np.transpose(Phik) + GamWk @ W @ np.transpose(GamWk) # ASSUMES CONSTANT W AND V
        # measurement update 
        K = Pbar @ np.transpose(Hk) @ np.linalg.inv((V + Hk @ Pbar @ np.transpose(Hk))) # ASSUMES CONSTANT W AND V 
        xhat[:,k] = xbar[:,k] + K @ (zk[:,k] - Hk @ xbar[:,k])
        #Phat = np.linalg.inv(Pbar) + np.transpose(Hk)*np.linalg.inv(V)*Hk
        Phat = (np.eye(nx,nx) - K @ Hk) @ Pbar
        # relinearize for next epoch of KF 
        fill = np.matrix([[1],[np.pi/2]]) # these are the signal amplitude and inital phase. They are constant for now.
        initals_hold = np.array(np.concatenate((traj[:,k],fill), axis=0))
        init_args["initials"] = initals_hold
        sys_num = init.initialize(init_args)
        Phik  = sys_num.A 
        GamUk = sys_num.B
        GamWk = sys_num.G
        Hk    = np.matrix(sys_num.C)
        # D     = sys_num.D
        # store covariance information 
        Pbar_list[:,k*nx:(k+1)*nx] = Pbar
        Phat_list[:,k*nx:(k+1)*nx] = Phat
        K_list[:,(k-1)*Hk.shape[0]:k*Hk.shape[0]]
        Hk_list[:,(k-1)*Hk.shape[1]:k*Hk.shape[1]]
        Phik_list[:,k*nx:(k+1)*nx] = Phik
    return xhat, Phat_list, Pbar_list, K_list, Hk_list, Phik_list 

