import control
import numpy as np
import matplotlib.pyplot as plt
import math 

def freq_resp(sys_ss: control.NonlinearIOSystem | control.LinearIOSystem, omega: np.ndarray, tol: float, fig_dim_1: int = None, fig_dim_2: int = None):

    mag, phase, omega = control.freqresp(sys_ss, omega)
    tau_arr = np.empty([])

    # Plot the magnitude and phase response
    # TODO: unsafe when providing fig_dim_2 but not fig_dim_1. Make it a tuple? 
    if fig_dim_1 is None:
        fig, axs = plt.subplots(sys_ss.noutputs*2, sys_ss.ninputs, sharex=True)
    else:
        fig, axs = plt.subplots(sys_ss.noutputs*2, sys_ss.ninputs, figsize = (fig_dim_1, fig_dim_2), sharex=True)

    i_phase= 0
    
    for i in range(sys_ss.noutputs*2): # times two to capture the magnitude /and/ phase for each input
        if i % 2 == 0:
            i_adj = int(i/2)
            for j in range(sys_ss.ninputs):
                axs[i, j].semilogx(omega, 20 * np.log10(np.abs(mag[i_adj, j, :])))
                axs[i, j].set_title(f'Output {i+1} to Input {j+1}')
                axs[i, j].set_ylabel('Magnitude (dB)')
                axs[i, j].set_xlabel('Frequency (rad/s)')
                axs[i, j].grid(True)
                axs[i, j].set_xlim([omega[0], omega[-1]])

                # Find the corner frequency
                mag_db = 20 * np.log10(np.abs(mag[i_adj, j, :]))
                max_mag = mag_db[np.argmax(mag_db)]
                if not math.isinf(max_mag): 
                    corner_freq = max_mag - 3 
                    label_point = np.where((mag_db > corner_freq - tol) & (mag_db < corner_freq + tol))[0][0]
                    xlims = axs[i, j].get_xlim()
                    ylims = axs[i, j].get_ylim()
                    axs[i,j].annotate(f'Corner Frequency: {corner_freq:.2f}', xy=(omega[label_point], mag_db[label_point]),
                        xytext=(xlims[0] + (xlims[1]-xlims[0])/2, ylims[1]*0.9), ha='left', va='bottom',
                        arrowprops=dict(arrowstyle='->', color='black'))
                    tau = 1/(2*np.pi*corner_freq)
                    tau_arr = np.append(tau_arr, tau)
        else: 
            for j in range(sys_ss.ninputs):
                hld = np.rad2deg(phase[i_phase, j, :])
                axs[i, j].semilogx(omega, np.rad2deg(phase[i_phase, j, :]))
                axs[i, j].set_title(f'Output {i+1} to Input {j+1}')
                axs[i, j].set_ylabel('Phase (deg)')
                axs[i, j].set_xlabel('Frequency (rad/s)')
                axs[i, j].grid(True)
                axs[i, j].set_xlim([omega[0], omega[-1]])
            i_phase = i_phase + 1 

    return mag, phase, omega, tau_arr, plt