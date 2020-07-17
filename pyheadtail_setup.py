import numpy as np
from scipy.constants import e, m_p, c, physical_constants

### SIS100 parameters (slightly modified)

circumference = 26658.8832
Q_x = 64.31
Q_y = 59.32
p0 = 6.5e12 * e / c
mass = m_p
gamma = p0 / (mass * c)
charge = e

epsn_x = 2e-6
epsn_y = 2e-6
beta_z = 6.4385396386E+02 * 82/75.
sigma_z = 1e-9 / 4. * c

sigma_dp = sigma_z / beta_z

# transverse map
transverse_map_kwargs = dict(
    s=[0, circumference],
    alpha_x=[0] * 2,
    beta_x=[circumference / (2 * np.pi * Q_x)] * 2,
    D_x=[0] * 2,
    alpha_y=[0] * 2,
    beta_y=[circumference / (2 * np.pi * Q_y)] * 2,
    D_y=[0] * 2,
    accQ_x=Q_x,
    accQ_y=Q_y,
)

# longitudinal map
longitudinal_map_kwargs = dict(
    circumference=circumference,
    harmonic_list=[35640],
    voltage_list=[16e6],
    phi_offset_list=[0],
    alpha_array=[54**-2],
    gamma_reference=gamma,
    p_increment=0,
    charge=charge,
    mass=mass,
)

# beam parameters
beam_kwargs = dict(
    charge=charge,
    mass=mass,
    circumference=circumference,
    gamma=gamma,
    beta_z=beta_z,
    epsn_x=epsn_x,
    epsn_y=epsn_y,
    epsn_z=sigma_z * sigma_dp * 4 * np.pi * p0 / e,
    limit_n_rms_x=3**2,
    limit_n_rms_y=3**2,
    limit_n_rms_z=3**2,
)
