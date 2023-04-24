import control
import numpy as np
import matplotlib.pyplot as plt

def freq_resp(sys_ss: control.NonlinearIOSystem | control.LinearIOSystem, omega: np.ndarray, fig_dim_1: int = None, fig_dim_2: int = None):

    mag, phase, omega = control.freqresp(sys_ss, omega)

    # Plot the magnitude and phase response
    # TODO: unsafe when providing fig_dim_2 but not fig_dim_1. Make it a tuple? 
    if fig_dim_1 is None:
        fig, axs = plt.subplots(sys_ss.outputs*2, sys_ss.inputs, sharex=True)
    else:
        fig, axs = plt.subplots(sys_ss.outputs*2, sys_ss.inputs, figsize = (fig_dim_1, fig_dim_2), sharex=True)

    i_phase= 0
    
    for i in range(sys_ss.outputs*2): # times two to capture the magnitude /and/ phase for each input
        if i % 2 == 0:
            i_adj = int(i/2)
            for j in range(sys_ss.inputs):
                axs[i, j].semilogx(omega, 20 * np.log10(np.abs(mag[i_adj, j, :])))
                axs[i, j].set_title(f'Output {i+1} to Input {j+1}')
                axs[i, j].set_ylabel('Magnitude (dB)')
                axs[i, j].set_xlabel('Frequency (rad/s)')
                axs[i, j].grid(True)
                axs[i, j].set_xlim([omega[0], omega[-1]])
        else: 
            for j in range(sys_ss.inputs):
                hld = np.rad2deg(phase[i_phase, j, :])
                axs[i, j].semilogx(omega, np.rad2deg(phase[i_phase, j, :]))
                axs[i, j].set_title(f'Output {i+1} to Input {j+1}')
                axs[i, j].set_ylabel('Phase (deg)')
                axs[i, j].set_xlabel('Frequency (rad/s)')
                axs[i, j].grid(True)
                axs[i, j].set_xlim([omega[0], omega[-1]])
            i_phase = i_phase + 1 

    return mag, phase, omega, plt