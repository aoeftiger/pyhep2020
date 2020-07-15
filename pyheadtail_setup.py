import numpy as np
from scipy.constants import e, m_p, c, physical_constants

### SIS100 parameters (slightly modified)

circumference = 1083.6
Q_x = 10.3
Q_y = 10.4
Ekin_ext_eV = 29e9
gamma = Ekin_ext_eV / (m_p * c**2) * e + 1
charge = e
mass = m_p

Ekin_inj_eV = 4e9
betagamma_inj = np.sqrt((Ekin_inj_eV / (m_p * c**2) * e + 1)**2 - 1)
epsn_x = 13e-6 * betagamma_inj
epsn_y = 4e-6 * betagamma_inj
sigma_z = 24.9 / 4. * 0.6
sigma_dp = 1.1e-3 * 0.6 * 10 * 10 * 1.6

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
    harmonic_list=[10],
    voltage_list=[66e3 * 1000 * 2.5 * 25],#58.2e3 * 100],
    phi_offset_list=[0],
    alpha_array=[8.72643**-2],
    gamma_reference=gamma,
    p_increment=0,
    charge=charge,
    mass=mass,
)

# beam parameters
p0 = np.sqrt(gamma**2 - 1) * mass * c
beam_kwargs = dict(
    charge=charge,
    mass=mass,
    circumference=circumference,
    gamma=gamma,
    beta_z=sigma_z / sigma_dp,
    epsn_x=epsn_x,
    epsn_y=epsn_y,
    epsn_z=sigma_z * sigma_dp * 4 * np.pi * p0 / e,
    limit_n_rms_x=3**2,
    limit_n_rms_y=3**2,
    limit_n_rms_z=3**2,
)
