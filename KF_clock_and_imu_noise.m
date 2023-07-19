clear
close all

c = 2.99792458e8;
L5 = 1176.45e6;
lam5 = c/L5;

CN0dBHz = -0;
CN0 = 10.^(CN0dBHz/10);
R = 1/CN0;

%% CLOCK -- LPFRS

h0 = 1.5e-22;
h0 = h0*20;     % *20 w/ vibration
h_2 = 8.5e-32;

Sf = h0/2*L5^2;
Sg = 2*pi^2*h_2*L5^2;

Fc = [0 1; 0 0];
Gc = eye(2);
Qc = diag([Sf Sg]);
Hc = [1 0];

sysc = ss(Fc,Gc,Hc,[]);
[KESTc,Lc,Pc] = kalman(sysc,Qc,R,[]);
KFc = [1 0]*KESTc;
tf(KFc)
figure(1);
bode(KFc); grid

sig_phase_clk_deg = sqrt(Pc(1,1))*180/pi
sig_phase_clk_cm = sig_phase_clk_deg*25.5/360







%% ACCELEROMETER -- Ellipse2

g = 9.81; % m/s^2

VRW = 0.033; % m/s/sqrt(hr)
Qaw = (VRW/60)^2;  % (m/s^2)^2/Hz

tauab = 500; % sec
sigab = 0.014; % mg
sab = sigab/1000*g; % m/^2 
Qab = 2*tauab*sab^2;

Fi = [0 1 0; 0 0 1; 0 0 -1/tauab];
Gi = [0 0; 1 0; 0 1/tauab];
Qi = diag([Qaw Qab]);
Hi = [1 0 0];

sysi = ss(Fi,Gi,Hi,[]);
[KESTi,Li,Pi] = kalman(sysi,Qi,R,[]);
KFi = [1 0 0 0]*KESTi;
tf(KFi)
figure(2); 
bode(KFi); grid

sig_phase_imu_deg = sqrt(Pi(1,1))*180/pi
sig_phase_imu_cm = sig_phase_imu_deg*lam5/360
