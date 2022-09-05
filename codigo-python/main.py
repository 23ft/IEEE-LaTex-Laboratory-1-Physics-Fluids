"""

    23ft - 2022
    Work Python for Physic Fluid Class.

"""
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np


L_values_measure = [0, 6, 12, 18, 25]   # Valores L medidos en practica.
L_values_stimate = np.arange(0,10,0.5)  # valores estimados L para modelo.

h_values_measure = [0, 2.7, 4.8, 8, 10.6]   # Valores h medidos en practica.


m_lab_calculate = 0.428     # pendiente determinada en la practica.
h = m_lab_calculate*L_values_stimate    # function principal h(L) with M calculated in lab.

def create_graf_measures():
    fig = plt.figure()
    gs = gridspec.GridSpec(2, 3, figure=fig)
    ax = fig.add_subplot(gs[0, :])
    ax.set_title("Graphics  Measures collected in test.")
    ax.set_xlabel("L -lenght [cm]")
    ax.set_ylabel("h- lenght [cm]")
    ax.plot(L_values_measure, h_values_measure, 'o', color="blue")
    
    ax2 = fig.add_subplot(gs[1, :])
    #plt.subplot(212)
    ax2.set_xlabel("L -lenght [cm]")
    ax2.set_ylabel("h -lenght [cm]")
    ax2.plot(L_values_measure, h_values_measure, color="blue")
    
    #plt.show()
    plt.savefig('plot-1-data-collected.pdf')
    
def create_graf_estimate():
    fig = plt.figure()
    gs = gridspec.GridSpec(2, 3, figure=fig)
    ax = fig.add_subplot(gs[0, :])
    ax.set_title("Graphics  Estimate of system.")
    ax.set_xlabel("L -lenght [cm]")
    ax.set_ylabel("h- lenght [cm]")
    ax.plot(L_values_stimate, h, 'o', color="red")
    
    ax2 = fig.add_subplot(gs[1, :])
    #plt.subplot(212)
    ax2.set_xlabel("L -lenght [cm]")
    ax2.set_ylabel("h -lenght [cm]")
    ax2.plot(L_values_stimate, h, color="red")
    
    #plt.show()
    plt.savefig('plot-2-estimate-L.pdf')
    
    
create_graf_measures()
create_graf_estimate()