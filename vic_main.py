""" Simulation of VIC"""

# Simulation of hyperelastic solid in initial configuration

from dolfin import *
from vic_func import *
import pdb
import matplotlib.pyplot as plt

import vic_func
reload(vic_func)

# Begin simulation
m_num   = 4
p_order = 1
T_total = 40.0
dt      = 4.0    # time step
omega   = 0.5    # forward Euler: 0, backward Euler: 1, Crank-Nicholson: 0.5 
gamma   = 0.0
tau     = 1.0
Ee      = 10.0
nu      = 0.45
perm    = 0.001
top_Trac    = (0.0,0.0,1.0)

u_max = vic_func.vic_sim( m_num, p_order, dt, T_total, omega, Ee, nu, gamma, tau, perm, top_Trac )

plt.plot(u_max, '-o')
plt.show()
