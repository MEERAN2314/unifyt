"""Physical and mathematical constants with units."""

from unifyt.quantity import Quantity
import math
 
# Mathematical constants
pi = math.pi
e = math.e
golden_ratio = (1 + math.sqrt(5)) / 2

# Physical constants (CODATA 2018 values)

# Speed of light in vacuum
speed_of_light = Quantity(299792458, 'meter/second')
c = speed_of_light

# Planck constant
planck = Quantity(6.62607015e-34, 'joule * second')
h = planck
hbar = Quantity(1.054571817e-34, 'joule * second')

# Gravitational constant
gravitational_constant = Quantity(6.67430e-11, 'meter^3 / kilogram / second^2')
G = gravitational_constant

# Elementary charge
elementary_charge = Quantity(1.602176634e-19, 'coulomb')
e_charge = elementary_charge

# Electron mass
electron_mass = Quantity(9.1093837015e-31, 'kilogram')
m_e = electron_mass

# Proton mass
proton_mass = Quantity(1.67262192369e-27, 'kilogram')
m_p = proton_mass

# Neutron mass
neutron_mass = Quantity(1.67492749804e-27, 'kilogram')
m_n = neutron_mass

# Avogadro constant
avogadro = Quantity(6.02214076e23, '1/mole')
N_A = avogadro

# Boltzmann constant
boltzmann = Quantity(1.380649e-23, 'joule/kelvin')
k_B = boltzmann

# Gas constant
gas_constant = Quantity(8.314462618, 'joule/mole/kelvin')
R = gas_constant

# Stefan-Boltzmann constant
stefan_boltzmann = Quantity(5.670374419e-8, 'watt/meter^2/kelvin^4')
sigma = stefan_boltzmann

# Electric constant (permittivity of free space)
electric_constant = Quantity(8.8541878128e-12, 'farad/meter')
epsilon_0 = electric_constant

# Magnetic constant (permeability of free space)
magnetic_constant = Quantity(1.25663706212e-6, 'henry/meter')
mu_0 = magnetic_constant

# Standard acceleration of gravity
standard_gravity = Quantity(9.80665, 'meter/second^2')
g = standard_gravity

# Atmospheric pressure at sea level
standard_atmosphere = Quantity(101325, 'pascal')
atm = standard_atmosphere

# Absolute zero
absolute_zero = Quantity(0, 'kelvin')

# Astronomical constants

# Astronomical unit
astronomical_unit = Quantity(1.495978707e11, 'meter')
AU = astronomical_unit

# Light year
light_year = Quantity(9.4607304725808e15, 'meter')
ly = light_year

# Parsec
parsec = Quantity(3.0856775814913673e16, 'meter')
pc = parsec

# Solar mass
solar_mass = Quantity(1.98847e30, 'kilogram')
M_sun = solar_mass

# Earth mass
earth_mass = Quantity(5.97217e24, 'kilogram')
M_earth = earth_mass

# Earth radius (mean)
earth_radius = Quantity(6.371e6, 'meter')
R_earth = earth_radius

# Atomic and nuclear constants

# Bohr radius
bohr_radius = Quantity(5.29177210903e-11, 'meter')
a_0 = bohr_radius

# Rydberg constant
rydberg = Quantity(10973731.568160, '1/meter')
R_inf = rydberg

# Fine structure constant (dimensionless)
fine_structure = 7.2973525693e-3
alpha = fine_structure

# Atomic mass unit
atomic_mass_unit = Quantity(1.66053906660e-27, 'kilogram')
u = atomic_mass_unit
amu = atomic_mass_unit

# Useful conversion factors

# Electron volt to joules
eV_to_J = 1.602176634e-19

# Calorie to joules
cal_to_J = 4.184

# BTU to joules
BTU_to_J = 1055.06

# Horsepower to watts
hp_to_W = 745.7

# Additional Physical Constants

# Faraday constant
faraday = Quantity(96485.33212, 'coulomb/mole')
F = faraday

# Molar gas constant (same as R, for clarity)
molar_gas_constant = gas_constant

# Wien displacement constant
wien = Quantity(2.897771955e-3, 'meter * kelvin')
b_wien = wien

# First radiation constant
radiation_first = Quantity(3.741771852e-16, 'watt * meter^2')
c1 = radiation_first

# Second radiation constant
radiation_second = Quantity(1.438776877e-2, 'meter * kelvin')
c2 = radiation_second

# Compton wavelength
compton_wavelength = Quantity(2.42631023867e-12, 'meter')
lambda_C = compton_wavelength

# Classical electron radius
electron_radius = Quantity(2.8179403262e-15, 'meter')
r_e = electron_radius

# Thomson cross section
thomson_cross_section = Quantity(6.6524587321e-29, 'meter^2')
sigma_T = thomson_cross_section

# Vacuum impedance
vacuum_impedance = Quantity(376.730313668, 'ohm')
Z_0 = vacuum_impedance

# Conductance quantum
conductance_quantum = Quantity(7.748091729e-5, 'siemens')
G_0 = conductance_quantum

# Josephson constant
josephson = Quantity(483597.8484e9, 'hertz/volt')
K_J = josephson

# Von Klitzing constant
von_klitzing = Quantity(25812.80745, 'ohm')
R_K = von_klitzing

# Magnetic flux quantum
flux_quantum = Quantity(2.067833848e-15, 'weber')
Phi_0 = flux_quantum

# Bohr magneton
bohr_magneton = Quantity(9.2740100783e-24, 'joule/tesla')
mu_B = bohr_magneton

# Nuclear magneton
nuclear_magneton = Quantity(5.0507837461e-27, 'joule/tesla')
mu_N = nuclear_magneton

# Proton magnetic moment
proton_magnetic_moment = Quantity(1.41060679736e-26, 'joule/tesla')
mu_p_mag = proton_magnetic_moment

# Electron magnetic moment
electron_magnetic_moment = Quantity(-9.2847647043e-24, 'joule/tesla')
mu_e_mag = electron_magnetic_moment

# Neutron magnetic moment
neutron_magnetic_moment = Quantity(-9.6623651e-27, 'joule/tesla')
mu_n_mag = neutron_magnetic_moment

# Proton gyromagnetic ratio
proton_gyromagnetic = Quantity(2.6752218744e8, 'radian/(second*tesla)')
gamma_p = proton_gyromagnetic

# Electron g-factor
electron_g_factor = -2.00231930436256

# Muon mass
muon_mass = Quantity(1.883531627e-28, 'kilogram')
m_mu = muon_mass

# Tau mass
tau_mass = Quantity(3.16754e-27, 'kilogram')
m_tau = tau_mass

# Planck length
planck_length = Quantity(1.616255e-35, 'meter')
l_P = planck_length

# Planck mass
planck_mass = Quantity(2.176434e-8, 'kilogram')
m_P = planck_mass

# Planck time
planck_time = Quantity(5.391247e-44, 'second')
t_P = planck_time

# Planck temperature
planck_temperature = Quantity(1.416784e32, 'kelvin')
T_P = planck_temperature

# Planck energy
planck_energy = Quantity(1.9561e9, 'joule')
E_P = planck_energy

# Hubble constant (approximate)
hubble_constant = Quantity(2.3e-18, '1/second')  # ~70 km/s/Mpc
H_0 = hubble_constant

# Cosmic microwave background temperature
cmb_temperature = Quantity(2.725, 'kelvin')
T_CMB = cmb_temperature

# Solar luminosity
solar_luminosity = Quantity(3.828e26, 'watt')
L_sun = solar_luminosity

# Solar radius
solar_radius = Quantity(6.96e8, 'meter')
R_sun = solar_radius

# Jupiter mass
jupiter_mass = Quantity(1.898e27, 'kilogram')
M_jupiter = jupiter_mass

# Moon mass
moon_mass = Quantity(7.342e22, 'kilogram')
M_moon = moon_mass

# Schwarzschild radius of Earth
schwarzschild_earth = Quantity(8.87e-3, 'meter')

# Schwarzschild radius of Sun
schwarzschild_sun = Quantity(2.95e3, 'meter')

# Age of universe (approximate)
universe_age = Quantity(4.35e17, 'second')  # ~13.8 billion years

# Critical density of universe
critical_density = Quantity(9.47e-27, 'kilogram/meter^3')
rho_c = critical_density

# Standard atmospheric conditions
standard_temperature = Quantity(273.15, 'kelvin')  # 0°C
standard_pressure = standard_atmosphere

# Water properties at standard conditions
water_density_stp = Quantity(1000.0, 'kilogram/meter^3')
water_specific_heat = Quantity(4184.0, 'joule/kilogram/kelvin')

# Air properties at standard conditions
air_density_stp = Quantity(1.225, 'kilogram/meter^3')
air_specific_heat = Quantity(1005.0, 'joule/kilogram/kelvin')

# Electrical constants
elementary_conductance = Quantity(7.748091729e-5, 'siemens')  # 2e²/h
resistance_quantum = Quantity(12906.4037278, 'ohm')  # h/2e²

# Dictionary of all constants for easy access
CONSTANTS = {
    # Mathematical
    'pi': pi,
    'e': e,
    'golden_ratio': golden_ratio,
    
    # Fundamental Physical
    'c': c,
    'h': h,
    'hbar': hbar,
    'G': G,
    'e_charge': e_charge,
    'm_e': m_e,
    'm_p': m_p,
    'm_n': m_n,
    'N_A': N_A,
    'k_B': k_B,
    'R': R,
    'sigma': sigma,
    'epsilon_0': epsilon_0,
    'mu_0': mu_0,
    'g': g,
    'atm': atm,
    
    # Astronomical
    'AU': AU,
    'ly': ly,
    'pc': pc,
    'M_sun': M_sun,
    'M_earth': M_earth,
    'R_earth': R_earth,
    'L_sun': L_sun,
    'R_sun': R_sun,
    'M_jupiter': M_jupiter,
    'M_moon': M_moon,
    'H_0': H_0,
    'T_CMB': T_CMB,
    'universe_age': universe_age,
    'rho_c': rho_c,
    
    # Atomic & Nuclear
    'a_0': a_0,
    'R_inf': R_inf,
    'alpha': alpha,
    'u': u,
    'F': F,
    'lambda_C': lambda_C,
    'r_e': r_e,
    'sigma_T': sigma_T,
    'mu_B': mu_B,
    'mu_N': mu_N,
    'm_mu': m_mu,
    'm_tau': m_tau,
    
    # Electromagnetic
    'Z_0': Z_0,
    'G_0': G_0,
    'K_J': K_J,
    'R_K': R_K,
    'Phi_0': Phi_0,
    'elementary_conductance': elementary_conductance,
    'resistance_quantum': resistance_quantum,
    
    # Planck Units
    'l_P': l_P,
    'm_P': m_P,
    't_P': t_P,
    'T_P': T_P,
    'E_P': E_P,
    
    # Radiation
    'b_wien': b_wien,
    'c1': c1,
    'c2': c2,
    
    # Standard Conditions
    'standard_temperature': standard_temperature,
    'standard_pressure': standard_pressure,
    'water_density_stp': water_density_stp,
    'water_specific_heat': water_specific_heat,
    'air_density_stp': air_density_stp,
    'air_specific_heat': air_specific_heat,
}


def get_constant(name: str) -> Quantity:
    """
    Get a physical constant by name.
    
    Args:
        name: Name of the constant
        
    Returns:
        Quantity representing the constant
        
    Raises:
        KeyError: If constant not found
        
    Examples:
        >>> c = get_constant('c')
        >>> print(c)
        299792458 meter/second
    """
    if name in CONSTANTS:
        return CONSTANTS[name]
    raise KeyError(f"Constant '{name}' not found")


def list_constants() -> list:
    """
    List all available constants.
    
    Returns:
        List of constant names
    """
    return sorted(CONSTANTS.keys())
