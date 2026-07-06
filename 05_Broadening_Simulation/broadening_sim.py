"""
broadening_sim.py

ES_APPM 421 Final Project:
Modeling Inhomogeneous Broadening through Spin-Spin Interactions in Matrix Isolated Spin Ensembles

Author: Isaac Cross (crossisaac114@gmail.com and/or isaaccross2026@u.northwestern.edu)
Date: December 8, 2025
"""

#Import needed packages
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit
from fractions import Fraction

#define constants to be used
mu0 = 4*np.pi*1e-7 #permeability of free space T m/A
muB = 9.2740100783e-24 #Bohr magneton,J/T
h = 6.62607015e-34 #planck's const J*s
gJ = 2.0023 #electron Lande g-factor, assumed free electron (alkali)

B_const = mu0/(4*np.pi) #const prefactor for B from dipole used later


#Define all helper functions to be called in Monte Carlo broadening simulation
""""
space_dopants:
Creates test cell and fills with atoms/dopants

Sec. "Matrix-Isolated Spin Ensemble"
"""
def space_dopants(density_cm3, L_box_nm):
    #get expected number of dopants
    rho_m3 = density_cm3 * 1e6 # dopant density in atoms/m^3
    V_box_m3 = (L_box_nm * 1e-9)**3 # box volume m^3
    N_mean = rho_m3 * V_box_m3 #ave num dopants in our box

    #generate number of actual dopants, assuming a Poisson distribution 
    N_dopants = np.random.poisson(N_mean) - 1 #subtract 1 for the central dopant 

    #assume random uniform dist in box, positions in nm, spaced from central spin @ (0,0,0)
    dopant_locations = np.random.uniform(
        low=-L_box_nm/2,
        high=L_box_nm/2,
        size=(N_dopants, 3) # Nx3 array. N dopants, at (x,y,z)
    )

    return dopant_locations

"""
lande_gF_factor
Calculates the hyperfine Lande g-factor for the spin state we are looking at

Sec. "Spin-Spin Interaction Model"
"""
def lande_gF_factor(J,I,F):
    return gJ*((F*(F+1.0)-I*(I+1)+J*(J+1))/(2*F*(F+1)))


"""
zeeman_coeff_calc
Calculatye gamma_eff
Sec. "Spin-Spin Interaction Model"
"""
def zeeman_coeff_calc(gF_ground,mF_ground,gF_excited,mF_excited):
    return  muB*(gF_excited*mF_excited-gF_ground*mF_ground)/h #Hz/T



"""
magnetization_dopants
Sec."Determing Spin States and Oreintation" in writeup

Uses gFi determined by possible Fi instead of just F as in writeup
as this is more efficient. Practically they are equivalent. 
"""
def magnetization_dopants(size,
                          gFs, gF_pump, gF_pump_efficiency,
                          mFs, mF_pump, mF_pump_efficiency,
                          allignment_efficiency):

    #pick mF for each state with efficiency mF_pump_efficiency to end in mF_pump
    mF = np.empty(size, dtype=float)
    mF_pumped_mask = np.random.rand(size)<mF_pump_efficiency
    mF[mF_pumped_mask] = mF_pump
    mF[~mF_pumped_mask] = np.random.choice(mFs,size=(~mF_pumped_mask).sum())

    #pick gF for each state with efficiency gF_pump_efficiency to end in gF_pump
    gF = np.empty(size, dtype=float)
    gF_pumped_mask = np.random.rand(size)<gF_pump_efficiency
    gF[gF_pumped_mask] = gF_pump
    gF[~gF_pumped_mask] = np.random.choice(gFs,size=(~gF_pumped_mask).sum())

    #magnitude of magnetic moment each dopant
    m_mag = gF * mF * muB 

    #Magnetic moment orientation
    m = np.tile(np.array([0., 0., 1.]), (size, 1))
    mis = np.random.rand(size) > allignment_efficiency
    n_mis = mis.sum()
    if n_mis > 0:
        #random unit vectors on S^2
        v = np.random.normal(size=(n_mis, 3))
        v /= np.linalg.norm(v, axis=1)[:, None]
        m[mis] = v

    #output final magnetic moment list for all dopants
    return m_mag[:, None] * m #J/T


"""
Bz_origin_calc

Calcualte magnetic field at central test spin caused by all neighboring spins
Sec. "Spin-Spin Interaction Model" and
Sec. "Central Spin's Frequency Shift"
"""
def Bz_origin_calc(dopant_locations, m_dopants):
    # Bz given ~ consts*(3rhat(m dot rhat) - m)/rmag^3

    # dopant r is currently relative to origin, but want
    # magnetic field located at -r relative to dopant
    R = -dopant_locations*1e-9 #convert from nm to m

    R_mag = np.linalg.norm(R, axis = 1)[:,None] #get magnitude of R, will be importnat for Rhat used in B field  calc
    R_hat = R/R_mag

    m_dot_R_hat = np.sum(m_dopants*R_hat, axis=1)[:,None]

    B_vecs = B_const*(3*m_dot_R_hat*R_hat - m_dopants)/(R_mag**3) #get full vector B field from each dipole (N,3)
    B_z = B_vecs[:,2] #only care about Bz (N,1)
    B_z_tot = np.sum(B_z) #sum to get total effective B field at origin
    return B_z_tot #T


"""
lorentzian

Lorentzian function for fitting
Sec. "ANALYSIS" 
"""
def lorentzian(v, A, v0, Gamma):
    return A * (Gamma/2)/((v - v0)**2 + (Gamma/2)**2)


"""
broadening_simulation

key to Monte Carlo model of spin-spin interaction and corresponding inhomogeneous broadening
Uses all helper functions defined above. 
Sec. "ANALYSIS" 
"""
def broadening_simulation(N,density_cm3,L_box_nm,
                        J,I,F_ground,mF_ground,
                        F_excited,mF_excited,
                        F_pump_efficiency,mF_pump_efficiency,allignment_efficiency,
                        plot = True):
    
    #get coefficients/constants
    #gF consts
    gF_ground = lande_gF_factor(J,I,F_ground)
    gF_excited = lande_gF_factor(J,I,F_excited)
    #zeem shift coeff
    zeeman_coeff = zeeman_coeff_calc(gF_ground,mF_ground,gF_excited,mF_excited) #Hz/T

    gFs =[gF_ground,gF_excited]
    mFs = np.arange(-F_ground,F_ground+1,1)
        
    #create empty list to fill with shifts
    delta_freqs = np.empty(N)

    #simualte new configuration and calculate shifts N times
    for k in range(N):

        dopant_locations = space_dopants(density_cm3, L_box_nm) #nm

        num_dopants = dopant_locations.shape[0]

        m_dopants = magnetization_dopants(num_dopants,
                                        gFs, gF_ground, F_pump_efficiency,
                                        mFs, mF_ground, mF_pump_efficiency,
                                        allignment_efficiency) #J/T

        magnetic_field_z = Bz_origin_calc(dopant_locations,m_dopants)  #T

        delta_freqs[k] = zeeman_coeff*magnetic_field_z #Hz

    #convert from Hz to kHz
    delta_freqs_khz = delta_freqs*1e-3 #kHz
    
    #get guesses for p0 in lorentzian fit, and set bounds on fit

    #use central 97% of the data as the fitting range
    low_q, high_q = np.percentile(delta_freqs_khz, [3, 97])
    padding = 0.1 * (high_q - low_q)

    rangeset = (low_q - padding, high_q + padding)
    
    # create histogram bins but do NOT use the counts for fitting
    hist_vals, bin_edges = np.histogram(delta_freqs_khz, bins=500, range = rangeset)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    # initial guesses
    A0 = max(hist_vals)
    x0_0 = 0

    indices = np.where(hist_vals >= A0/2)[0]    
    FWHM_est = bin_centers[indices[-1]] - bin_centers[indices[0]]
    gamma0 = FWHM_est

    popt, pcov = curve_fit(lorentzian, bin_centers, hist_vals, p0=[A0, x0_0, gamma0])
    A, x0, gamma = popt

    T2_star_ms = 1/(np.pi*gamma)
    
    #determine if we output a plot
    if plot:
        #create figrue/plot
        fig = plt.figure(figsize=(13,6)) 

        #plot example dopant dist
        ax1 = fig.add_subplot(1,2,1,projection="3d")
        x_nm = dopant_locations[:,0]
        y_nm = dopant_locations[:,1]
        z_nm = dopant_locations[:,2]

        ax1.scatter(x_nm, y_nm, z_nm, s=20, label='Neighbor Spins') # neighbor spins
        ax1.scatter(0, 0, 0, s=60, color='red', label='Central Test Spin') # central test spin
        ax1.legend(loc='upper right', fontsize=10)
        
        ax1.set_xlabel("x (nm)", fontsize=14)
        ax1.set_ylabel("y (nm)", fontsize=14)
        ax1.set_zlabel("z (nm)",fontsize=14)
        ax1.set_xlim(-L_box_nm/2,L_box_nm/2)
        ax1.set_ylim(-L_box_nm/2,L_box_nm/2)
        ax1.set_zlim(-L_box_nm/2,L_box_nm/2)
 
        ax1.text(
            0.02, 0.10,0.0,
            f"Dopant Density: {density_cm3:.1e} atoms/cm³",
            transform=ax1.transAxes,
            fontsize=10,
            va='top',
            ha='left',
            bbox=dict(boxstyle="round", fc="white", ec="black", alpha=0.8)
        )

        ax1.set_title("Example dopant configuration", fontsize=24)

        #Plot historgram with relevant output values, T2*, Gamma, as well as input paramters. 
        ax2 = fig.add_subplot(1,2,2)

        ax2.hist(delta_freqs_khz, bins=500,range=rangeset,alpha=0.5, label="Monte Carlo Shift Data")

        x=np.linspace(rangeset[0],rangeset[1],2000)
        ax2.plot(x, lorentzian(x, *popt), 'r-', 
                label=f"Lorentzian fit\n$\Gamma$={gamma:.3g} (kHz)\n"
                        f"$T_2^*$ = {T2_star_ms:.3g} (ms)")

        param_text = (
            f"N = {N}\n"
            f"L = {L_box_nm} nm\n"
            f"Density = {density_cm3:.2e} cm⁻³\n"
            f"J and I: {Fraction(J).limit_denominator()} and {Fraction(I).limit_denominator()}\n"
            f"Transition: |{F_ground},{mF_ground}⟩ → |{F_excited},{mF_excited}⟩\n"
            f"gF_ground = {gF_ground:.4f}\n"
            f"gF_excited = {gF_excited:.4f}"
        )

        ax2.text(0.98, 0.95, param_text, fontsize=12,
                transform=plt.gca().transAxes,
                va='top', ha='right',
                bbox=dict(boxstyle="round", fc="white", ec="black", alpha=0.8))   


        ax2.set_xlabel(r"$\Delta\nu$ (kHz)", fontsize=20)
        ax2.set_ylabel("Count", fontsize=20)
        ax2.legend(loc="upper left", fontsize=12)
        ax2.set_title("Inhomogeneous Broadening Simulation", fontsize=24)

        plt.tight_layout()
        plt.show()
 
    # return values so can run simulation and compare results in different document 
    return {
        "gamma_kHz": gamma,
        "T2_star_ms": T2_star_ms,
        "delta_freqs_kHz": delta_freqs_khz,
        "F_ground": F_ground, 
        "mF_ground": mF_ground,
        "F_excited": F_excited,
        "mF_excited": mF_excited
    }



