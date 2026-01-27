"""Unit class for representing physical units."""

from __future__ import annotations
from typing import Dict, Optional
from unifyt.dimensions import Dimension


class Unit:
    """
    Represents a physical unit.
    
    Examples:
        >>> meter = Unit('meter')
        >>> second = Unit('second')
        >>> speed_unit = meter / second
    """
    
    # Base SI units
    _BASE_UNITS = {
         'meter': Dimension(length=1),
         'kilogram': Dimension(mass=1),
         'second': Dimension(time=1),
         'ampere': Dimension(current=1),
         'kelvin': Dimension(temperature=1),
         'mole': Dimension(amount=1),
         'candela': Dimension(luminosity=1),
         'dimensionless': Dimension(),
        # Derived units with their dimensions
        'joule': Dimension(mass=1, length=2, time=-2),  # kg⋅m²/s²
        'kilogram_per_square_meter': Dimension(mass=1, length=-2),  # kg/m²
    }
    
    # Conversion factors to base units
    _CONVERSIONS = {
        # Length
        'meter': 1.0, 'm': 1.0, 'meters': 1.0,
        'kilometer': 1000.0, 'km': 1000.0, 'kilometers': 1000.0,
        'centimeter': 0.01, 'cm': 0.01, 'centimeters': 0.01,
        'millimeter': 0.001, 'mm': 0.001, 'millimeters': 0.001,
        'micrometer': 1e-6, 'um': 1e-6, 'micrometers': 1e-6,
        'nanometer': 1e-9, 'nm': 1e-9, 'nanometers': 1e-9,
        'angstrom': 1e-10, 'Å': 1e-10,
        'mile': 1609.344, 'mi': 1609.344, 'miles': 1609.344,
        'yard': 0.9144, 'yd': 0.9144, 'yards': 0.9144,
        'foot': 0.3048, 'ft': 0.3048, 'feet': 0.3048,
        'inch': 0.0254, 'in': 0.0254, 'inches': 0.0254,
        
        # Mass
        'kilogram': 1.0, 'kg': 1.0, 'kilograms': 1.0,
        'gram': 0.001, 'g': 0.001, 'grams': 0.001,
        'milligram': 1e-6, 'mg': 1e-6, 'milligrams': 1e-6,
        'microgram': 1e-9, 'ug': 1e-9, 'micrograms': 1e-9,
        'pound': 0.453592, 'lb': 0.453592, 'pounds': 0.453592,
        'ounce': 0.0283495, 'oz': 0.0283495, 'ounces': 0.0283495,
        'ton': 1000.0, 'tons': 1000.0, 'tonne': 1000.0, 'tonnes': 1000.0,
        
        # Time
        'second': 1.0, 's': 1.0, 'seconds': 1.0, 'sec': 1.0,
        'millisecond': 0.001, 'ms': 0.001, 'milliseconds': 0.001,
        'microsecond': 1e-6, 'us': 1e-6, 'microseconds': 1e-6,
        'nanosecond': 1e-9, 'ns': 1e-9, 'nanoseconds': 1e-9,
        'minute': 60.0, 'min': 60.0, 'minutes': 60.0,
        'hour': 3600.0, 'h': 3600.0, 'hr': 3600.0, 'hours': 3600.0,
        'day': 86400.0, 'd': 86400.0, 'days': 86400.0,
        'week': 604800.0, 'weeks': 604800.0,
        'year': 31536000.0, 'yr': 31536000.0, 'years': 31536000.0,
        
        # Temperature (offset handled separately)
        'kelvin': 1.0, 'K': 1.0,
        'celsius': 1.0, 'C': 1.0, 'degC': 1.0,
        'fahrenheit': 5.0/9.0, 'F': 5.0/9.0, 'degF': 5.0/9.0,
        
        # Current
        'ampere': 1.0, 'A': 1.0, 'amperes': 1.0, 'amp': 1.0, 'amps': 1.0,
        'milliampere': 0.001, 'mA': 0.001,
        
        # Amount
        'mole': 1.0, 'mol': 1.0, 'moles': 1.0,
        
        # Luminosity
        'candela': 1.0, 'cd': 1.0,
        
        # Energy
        'joule': 1.0, 'J': 1.0, 'joules': 1.0,
        'kilojoule': 1000.0, 'kJ': 1000.0,
        'calorie': 4.184, 'cal': 4.184, 'calories': 4.184,
        'kilocalorie': 4184.0, 'kcal': 4184.0, 'Calorie': 4184.0,
        'electronvolt': 1.602176634e-19, 'eV': 1.602176634e-19,
        'kiloelectronvolt': 1.602176634e-16, 'keV': 1.602176634e-16,
        'megaelectronvolt': 1.602176634e-13, 'MeV': 1.602176634e-13,
        'gigaelectronvolt': 1.602176634e-10, 'GeV': 1.602176634e-10,
        'teraelectronvolt': 1.602176634e-7, 'TeV': 1.602176634e-7,
        'watt_hour': 3600.0, 'Wh': 3600.0,
        'kilowatt_hour': 3.6e6, 'kWh': 3.6e6,
        
        # Power
        'watt': 1.0, 'W': 1.0, 'watts': 1.0,
        'kilowatt': 1000.0, 'kW': 1000.0, 'kilowatts': 1000.0,
        'megawatt': 1e6, 'MW': 1e6, 'megawatts': 1e6,
        'horsepower': 745.7, 'hp': 745.7,
        
        # Pressure
        'pascal': 1.0, 'Pa': 1.0,
        'kilopascal': 1000.0, 'kPa': 1000.0,
        'megapascal': 1e6, 'MPa': 1e6,
        'bar': 1e5, 'bars': 1e5,
        'atmosphere': 101325.0, 'atm': 101325.0,
        'psi': 6894.76, 'PSI': 6894.76,
        'torr': 133.322, 'Torr': 133.322,
        
        # Force
        'newton': 1.0, 'N': 1.0, 'newtons': 1.0,
        'kilonewton': 1000.0, 'kN': 1000.0,
        'pound_force': 4.44822, 'lbf': 4.44822,
        
        # Frequency
        'hertz': 1.0, 'Hz': 1.0,
        'kilohertz': 1000.0, 'kHz': 1000.0,
        'megahertz': 1e6, 'MHz': 1e6,
        'gigahertz': 1e9, 'GHz': 1e9,
        
        # Voltage
        'volt': 1.0, 'V': 1.0, 'volts': 1.0,
        'millivolt': 0.001, 'mV': 0.001,
        'kilovolt': 1000.0, 'kV': 1000.0,
        
        # Charge
        'coulomb': 1.0, 'C': 1.0, 'coulombs': 1.0,
        
        # Resistance
        'ohm': 1.0, 'Ω': 1.0, 'ohms': 1.0,
        'kiloohm': 1000.0, 'kΩ': 1000.0,
        'megaohm': 1e6, 'MΩ': 1e6,
        
        # Volume
        'liter': 0.001, 'L': 0.001, 'liters': 0.001, 'litre': 0.001, 'litres': 0.001,
        'milliliter': 1e-6, 'mL': 1e-6, 'milliliters': 1e-6,
        'gallon': 0.00378541, 'gal': 0.00378541, 'gallons': 0.00378541,
        'quart': 0.000946353, 'qt': 0.000946353,
        'pint': 0.000473176, 'pt': 0.000473176,
        'cup': 0.000236588, 'cups': 0.000236588,
        'fluid_ounce': 2.95735e-5, 'fl_oz': 2.95735e-5,
        
        # Area (derived but commonly used)
        'hectare': 10000.0, 'ha': 10000.0,
        'acre': 4046.86, 'acres': 4046.86,
        
        # Angle
        'radian': 1.0, 'rad': 1.0, 'radians': 1.0,
        'degree': 0.0174533, 'deg': 0.0174533, 'degrees': 0.0174533,
        'arcminute': 0.000290888, 'arcmin': 0.000290888,
        'arcsecond': 4.84814e-6, 'arcsec': 4.84814e-6,
        'gradian': 0.015708, 'grad': 0.015708,
        
        # Dimensionless
        'dimensionless': 1.0,
        'percent': 0.01, '%': 0.01,
        'ppm': 1e-6,
        'ppb': 1e-9,
        'ppt': 1e-12,
        
        # Advanced Length (Astronomical & Microscopic)
        'astronomical_unit': 1.495978707e11, 'au': 1.495978707e11,
        'light_year': 9.4607304725808e15, 'ly': 9.4607304725808e15,
        'parsec': 3.0856775814913673e16, 'pc': 3.0856775814913673e16,
        'kiloparsec': 3.0856775814913673e19, 'kpc': 3.0856775814913673e19,
        'megaparsec': 3.0856775814913673e22, 'Mpc': 3.0856775814913673e22,
        'picometer': 1e-12, 'pm': 1e-12,
        'femtometer': 1e-15, 'fm': 1e-15,
        'fermi': 1e-15,
        'nautical_mile': 1852.0, 'nmi': 1852.0,
        'fathom': 1.8288,
        'chain': 20.1168,
        'furlong': 201.168,
        'league': 4828.03,
        
        # Advanced Mass (Atomic & Large Scale)
        'atomic_mass_unit': 1.66053906660e-27, 'amu': 1.66053906660e-27, 'u': 1.66053906660e-27,
        'dalton': 1.66053906660e-27, 'Da': 1.66053906660e-27,
        'electron_mass': 9.1093837015e-31, 'm_e': 9.1093837015e-31,
        'proton_mass': 1.67262192369e-27, 'm_p': 1.67262192369e-27,
        'neutron_mass': 1.67492749804e-27, 'm_n': 1.67492749804e-27,
        'solar_mass': 1.98847e30, 'M_sun': 1.98847e30,
        'earth_mass': 5.97217e24, 'M_earth': 5.97217e24,
        'carat': 0.0002, 'ct': 0.0002,
        'grain': 6.479891e-5, 'gr': 6.479891e-5,
        'stone': 6.35029, 'st': 6.35029,
        'slug': 14.5939,
        
        # Advanced Time
        'picosecond': 1e-12, 'ps': 1e-12,
        'femtosecond': 1e-15, 'fs': 1e-15,
        'attosecond': 1e-18, 'as': 1e-18,
        'shake': 1e-8,
        'fortnight': 1209600.0,
        'month': 2629800.0,  # Average month (365.25/12 days)
        'decade': 315576000.0,
        'century': 3155760000.0,
        'millennium': 31557600000.0,
        
        # Advanced Energy
        'megajoule': 1e6, 'MJ': 1e6,
        'gigajoule': 1e9, 'GJ': 1e9,
        'erg': 1e-7,
        'british_thermal_unit': 1055.06, 'BTU': 1055.06, 'btu': 1055.06,
        'therm': 1.05506e8,
        'quad': 1.05506e18,
        'ton_tnt': 4.184e9,
        'kiloton_tnt': 4.184e12,
        'megaton_tnt': 4.184e15,
        'rydberg': 2.1798723611035e-18, 'Ry': 2.1798723611035e-18,
        'hartree': 4.3597447222071e-18, 'Ha': 4.3597447222071e-18,
        
        # Advanced Power
        'gigawatt': 1e9, 'GW': 1e9,
        'terawatt': 1e12, 'TW': 1e12,
        'milliwatt': 0.001, 'mW': 0.001,
        'microwatt': 1e-6, 'uW': 1e-6,
        'nanowatt': 1e-9, 'nW': 1e-9,
        'metric_horsepower': 735.5, 'PS': 735.5,
        'boiler_horsepower': 9809.5,
        
        # Advanced Pressure
        'gigapascal': 1e9, 'GPa': 1e9,
        'millibar': 100.0, 'mbar': 100.0,
        'microbar': 0.1, 'ubar': 0.1,
        'barye': 0.1,
        'technical_atmosphere': 98066.5, 'at': 98066.5,
        'inch_mercury': 3386.39, 'inHg': 3386.39,
        'millimeter_mercury': 133.322, 'mmHg': 133.322,
        'pound_per_square_inch': 6894.76, 'psi': 6894.76,
        
        # Advanced Force
        'meganewton': 1e6, 'MN': 1e6,
        'dyne': 1e-5, 'dyn': 1e-5,
        'kilogram_force': 9.80665, 'kgf': 9.80665,
        'gram_force': 0.00980665, 'gf': 0.00980665,
        'ton_force': 9806.65, 'tf': 9806.65,
        'poundal': 0.138255,
        'kip': 4448.22,
        
        # Advanced Frequency
        'terahertz': 1e12, 'THz': 1e12,
        'millihertz': 0.001, 'mHz': 0.001,
        'rpm': 1/60.0,  # Revolutions per minute
        'rps': 1.0,  # Revolutions per second
        
        # Advanced Voltage
        'megavolt': 1e6, 'MV': 1e6,
        'microvolt': 1e-6, 'uV': 1e-6,
        'nanovolt': 1e-9, 'nV': 1e-9,
        'statvolt': 299.792458,
        
        # Advanced Current
        'microampere': 1e-6, 'uA': 1e-6,
        'nanoampere': 1e-9, 'nA': 1e-9,
        'picoampere': 1e-12, 'pA': 1e-12,
        'kiloampere': 1000.0, 'kA': 1000.0,
        'statampere': 3.33564e-10,
        
        # Capacitance
        'farad': 1.0, 'F': 1.0,
        'millifarad': 0.001, 'mF': 0.001,
        'microfarad': 1e-6, 'uF': 1e-6,
        'nanofarad': 1e-9, 'nF': 1e-9,
        'picofarad': 1e-12, 'pF': 1e-12,
        
        # Inductance
        'henry': 1.0, 'H': 1.0,
        'millihenry': 0.001, 'mH': 0.001,
        'microhenry': 1e-6, 'uH': 1e-6,
        'nanohenry': 1e-9, 'nH': 1e-9,
        
        # Magnetic Field
        'tesla': 1.0, 'T': 1.0,
        'millitesla': 0.001, 'mT': 0.001,
        'microtesla': 1e-6, 'uT': 1e-6,
        'nanotesla': 1e-9, 'nT': 1e-9,
        'gauss': 1e-4, 'G': 1e-4,
        'milligauss': 1e-7, 'mG': 1e-7,
        
        # Magnetic Flux
        'weber': 1.0, 'Wb': 1.0,
        'milliweber': 0.001, 'mWb': 0.001,
        'maxwell': 1e-8, 'Mx': 1e-8,
        
        # Illuminance
        'lux': 1.0, 'lx': 1.0,
        'foot_candle': 10.764, 'fc': 10.764,
        'phot': 10000.0, 'ph': 10000.0,
        
        # Luminous Flux
        'lumen': 1.0, 'lm': 1.0,
        
        # Radioactivity
        'becquerel': 1.0, 'Bq': 1.0,
        'kilobecquerel': 1000.0, 'kBq': 1000.0,
        'megabecquerel': 1e6, 'MBq': 1e6,
        'gigabecquerel': 1e9, 'GBq': 1e9,
        'curie': 3.7e10, 'Ci': 3.7e10,
        'millicurie': 3.7e7, 'mCi': 3.7e7,
        'microcurie': 3.7e4, 'uCi': 3.7e4,
        'rutherford': 1e6, 'Rd': 1e6,
        
        # Absorbed Dose
        'gray': 1.0, 'Gy': 1.0,
        'milligray': 0.001, 'mGy': 0.001,
        'rad': 0.01,
        
        # Equivalent Dose
        'sievert': 1.0, 'Sv': 1.0,
        'millisievert': 0.001, 'mSv': 0.001,
        'microsievert': 1e-6, 'uSv': 1e-6,
        'rem': 0.01,
        'millirem': 1e-5, 'mrem': 1e-5,
        
        # Catalytic Activity
        'katal': 1.0, 'kat': 1.0,
        'unit': 1.66667e-8, 'U': 1.66667e-8,  # Enzyme unit
        
        # Data/Information
        'bit': 1.0, 'b': 1.0,
        'byte': 8.0, 'B': 8.0,
        'kilobyte': 8000.0, 'kB': 8000.0,
        'megabyte': 8e6, 'MB': 8e6,
        'gigabyte': 8e9, 'GB': 8e9,
        'terabyte': 8e12, 'TB': 8e12,
        'petabyte': 8e15, 'PB': 8e15,
        'kibibyte': 8192.0, 'KiB': 8192.0,
        'mebibyte': 8388608.0, 'MiB': 8388608.0,
        'gibibyte': 8589934592.0, 'GiB': 8589934592.0,
        'tebibyte': 8796093022208.0, 'TiB': 8796093022208.0,
        
        # Velocity
        'knot': 0.514444, 'kt': 0.514444, 'kn': 0.514444,
        'mach': 343.0,  # At sea level, 15°C
        
        # Acceleration
        'gal': 0.01,  # Galileo
        'standard_gravity': 9.80665, 'g0': 9.80665,
        
        # Viscosity (Dynamic)
        'pascal_second': 1.0, 'Pa_s': 1.0,
        'poise': 0.1, 'P': 0.1,
        'centipoise': 0.001, 'cP': 0.001,
        
        # Viscosity (Kinematic)
        'stokes': 1e-4, 'St': 1e-4,
        'centistokes': 1e-6, 'cSt': 1e-6,
        
        # Thermal Conductivity
        'watt_per_meter_kelvin': 1.0, 'W_m_K': 1.0,
        
        # Heat Capacity
        'joule_per_kelvin': 1.0, 'J_K': 1.0,
        
        # Specific Heat
        'joule_per_kilogram_kelvin': 1.0, 'J_kg_K': 1.0,
        
        # Molar Mass
        'gram_per_mole': 0.001, 'g_mol': 0.001,
        'kilogram_per_mole': 1.0, 'kg_mol': 1.0,
        
        # Concentration
        'molar': 1000.0, 'M': 1000.0,  # mol/L
        'millimolar': 1.0, 'mM': 1.0,
        'micromolar': 0.001, 'uM': 0.001,
        'nanomolar': 1e-6, 'nM': 1e-6,
        
        # Density
        'kilogram_per_cubic_meter': 1.0, 'kg_m3': 1.0,
        'gram_per_cubic_centimeter': 1000.0, 'g_cm3': 1000.0,
        'gram_per_liter': 1.0, 'g_L': 1.0,
        
        # Surface Density (mass per area)
        'kilogram_per_square_meter': 1.0, 'kg_m2': 1.0, 'kg_per_m2': 1.0,
        
        # Flow Rate
        'cubic_meter_per_second': 1.0, 'm3_s': 1.0,
        'liter_per_second': 0.001, 'L_s': 0.001,
        'liter_per_minute': 1.66667e-5, 'L_min': 1.66667e-5,
        'gallon_per_minute': 6.30902e-5, 'gpm': 6.30902e-5,
        
        # Fuel Efficiency
        'mile_per_gallon': 425144.0, 'mpg': 425144.0,  # Inverse meters
        'kilometer_per_liter': 1000.0, 'km_L': 1000.0,
        'liter_per_100km': 0.01, 'L_100km': 0.01,
        
        # Wire Gauge Standards (diameter in mm)
        'american_wire_gauge_10': 0.002588, 'awg_10': 0.002588,  # 10 AWG
        'american_wire_gauge_12': 0.002053, 'awg_12': 0.002053,  # 12 AWG
        'american_wire_gauge_14': 0.001628, 'awg_14': 0.001628,  # 14 AWG
        'american_wire_gauge_16': 0.001291, 'awg_16': 0.001291,  # 16 AWG
        'american_wire_gauge_18': 0.001024, 'awg_18': 0.001024,  # 18 AWG
        'american_wire_gauge_20': 0.000812, 'awg_20': 0.000812,  # 20 AWG
        'standard_wire_gauge_10': 0.003251, 'swg_10': 0.003251,  # 10 SWG
        'standard_wire_gauge_12': 0.002642, 'swg_12': 0.002642,  # 12 SWG
        'standard_wire_gauge_14': 0.002032, 'swg_14': 0.002032,  # 14 SWG
        'birmingham_wire_gauge_10': 0.003404, 'bwg_10': 0.003404,  # 10 BWG
        'birmingham_wire_gauge_12': 0.002769, 'bwg_12': 0.002769,  # 12 BWG
        
        # Gauge Pressure Units (same conversion as absolute, context indicates gauge)
        'bar_gauge': 1e5, 'bar_g': 1e5, 'barg': 1e5,
        'kilopascal_gauge': 1000.0, 'kpa_g': 1000.0, 'kpag': 1000.0,
        'psi_gauge': 6894.76, 'psi_g': 6894.76, 'psig': 6894.76,
        'kilogram_per_square_centimeter_gauge': 98066.5, 'kg_cm2_g': 98066.5, 'kgf_cm2_g': 98066.5,
        
        # Water Column Pressure
        'inch_water_column': 249.1, 'in_wc': 249.1, 'inwc': 249.1,
        'millimeter_water_column': 9.807, 'mm_wc': 9.807, 'mmwc': 9.807,
        'meter_water_column': 9807.0, 'm_wc': 9807.0, 'mwc': 9807.0,
        'millimeter_water_column_gauge': 9.807, 'mm_wc_g': 9.807, 'mmwcg': 9.807,
        
        # Textile and Paper Industry (surface density: g/m² to kg/m²)
        'grams_per_square_meter': 0.001, 'gsm': 0.001, 'g_m2': 0.001,
        
        # Additional Flow Units
        'liters_per_hour': 2.77778e-7, 'lph': 2.77778e-7, 'l_h': 2.77778e-7,
        'liters_per_second': 0.001, 'lps': 0.001, 'l_s': 0.001,
        'tons_per_hour': 0.277778, 'tph': 0.277778, 't_h': 0.277778,
        'normal_cubic_meters_per_hour': 2.77778e-4, 'nm3_h': 2.77778e-4, 'ncmh': 2.77778e-4,
        
        # Electrical Power Units
        'volt_ampere': 1.0, 'va': 1.0,
        'kilovolt_ampere': 1000.0, 'kva': 1000.0,
        'megavolt_ampere': 1e6, 'mva': 1e6,
        'kilovolt_ampere_reactive': 1000.0, 'kvar': 1000.0,
        
        # Additional Electrical Units
        'gigaohm': 1e9, 'gohm': 1e9, 'GΩ': 1e9,
        'volt_ac_dc': 1.0, 'vac_dc': 1.0,  # Context-dependent voltage
        
        # Torque Units
        'inch_pound': 0.112985, 'in_lb': 0.112985, 'inch_lbf': 0.112985,
        'newton_meter': 1.0, 'nm_torque': 1.0, 'n_m': 1.0,
        
        # Additional Pressure Units
        'hectopascal': 100.0, 'hpa': 100.0,
        'ton_force_per_square_meter': 9806.65, 'tf_m2': 9806.65,
        
        # Concentration and Density Units
        'milligrams_per_liter': 0.001, 'mg_l': 0.001, 'mg_per_l': 0.001,
        'micrograms_per_cubic_meter': 1e-9, 'ug_m3': 1e-9, 'ug_per_m3': 1e-9,
        'kilograms_per_cubic_meter': 1.0, 'kg_m3': 1.0, 'kg_per_m3': 1.0,
        'kilograms_per_square_meter': 1.0, 'kg_m2': 1.0, 'kg_per_m2': 1.0,
        'kilograms_per_square_millimeter': 1e6, 'kg_mm2': 1e6, 'kg_per_mm2': 1e6,
        
        # Conductivity Units
        'microsiemens_per_centimeter': 1e-4, 'us_cm': 1e-4, 'us_per_cm': 1e-4,
        'millisiemens_per_centimeter': 0.1, 'ms_cm': 0.1, 'ms_per_cm': 0.1,
        
        # Additional Time Units
        'month': 2629800.0, 'mon': 2629800.0,  # Average month
        
        # Capacitance (additional)
        'microfarad': 1e-6, 'mfd': 1e-6,  # Alternative notation
        
        # Dimensionless and Ratios
        'decibel': 1.0, 'db': 1.0,  # Logarithmic unit (dimensionless)
        'ph_scale': 1.0, 'ph': 1.0,  # pH scale (dimensionless)
        'strain': 1.0, 'str': 1.0,  # Strain (dimensionless)
        'pressure_ratio': 1.0, 'pr': 1.0,  # Pressure ratio (dimensionless)
        
        # Additional Area Units
        'square_millimeter': 1e-6, 'mm2': 1e-6, 'sq_mm': 1e-6,
        'square_inch': 0.00064516, 'in2': 0.00064516, 'sq_in': 0.00064516,
        'square_meter': 1.0, 'm2': 1.0, 'sq_m': 1.0,
        'square_centimeter': 1e-4, 'cm2': 1e-4, 'sq_cm': 1e-4,
        'square_foot': 0.092903, 'ft2': 0.092903, 'sq_ft': 0.092903,
        
        # Volume Units (additional)
        'cubic_millimeter': 1e-9, 'mm3': 1e-9, 'cu_mm': 1e-9,
        'cubic_centimeter': 1e-6, 'cm3': 1e-6, 'cu_cm': 1e-6, 'cc': 1e-6,
        'cubic_meter': 1.0, 'm3': 1.0, 'cu_m': 1.0,
        'cubic_foot': 0.0283168, 'ft3': 0.0283168, 'cu_ft': 0.0283168,
        'cubic_inch': 1.63871e-5, 'in3': 1.63871e-5, 'cu_in': 1.63871e-5,
        
        # Flow Rate (additional)
        'cubic_feet_per_minute': 4.71947e-4, 'cfm': 4.71947e-4, 'ft3_min': 4.71947e-4,
        'cubic_meters_per_hour': 2.77778e-4, 'm3_h': 2.77778e-4, 'cmh': 2.77778e-4,
        'cubic_meters_per_second': 1.0, 'm3_s': 1.0, 'cms': 1.0,
        
        # Velocity Units (additional)
        'meters_per_hour': 2.77778e-4, 'm_h': 2.77778e-4, 'mh': 2.77778e-4,
        'feet_per_second': 0.3048, 'ft_s': 0.3048, 'fps': 0.3048,
        'meters_per_second': 1.0, 'm_s': 1.0, 'ms_velocity': 1.0,
        
        # Energy Storage
        'ampere_hour': 3600.0, 'ah': 3600.0, 'amp_hour': 3600.0,
        'milliampere_hour': 3.6, 'mah': 3.6, 'milliamp_hour': 3.6,
    }
    
    # Map units to their base unit (auto-generated from conversions)
    _UNIT_TO_BASE = None  # Will be generated dynamically
    
    # Temperature offset units (special handling)
    _TEMPERATURE_OFFSETS = {
        'celsius': 273.15,
        'C': 273.15,
        'degC': 273.15,
        'fahrenheit': 459.67,
        'F': 459.67,
        'degF': 459.67,
    }
    
    # Cache for parsed units
    _unit_cache: Dict[str, 'Unit'] = {}
    
    @classmethod
    def _build_unit_to_base_map(cls) -> Dict[str, str]:
        """Build the unit to base unit mapping."""
        if cls._UNIT_TO_BASE is not None:
            return cls._UNIT_TO_BASE
        
        mapping = {}
        # Length units
        length_units = ['meter', 'm', 'meters', 'kilometer', 'km', 'kilometers', 
                       'centimeter', 'cm', 'centimeters', 'millimeter', 'mm', 'millimeters',
                       'micrometer', 'um', 'micrometers', 'nanometer', 'nm', 'nanometers',
                       'angstrom', 'Å', 'mile', 'mi', 'miles', 'yard', 'yd', 'yards',
                       'foot', 'ft', 'feet', 'inch', 'in', 'inches',
                       # Astronomical units
                       'astronomical_unit', 'au', 'light_year', 'ly', 'parsec', 'pc',
                       'kiloparsec', 'kpc', 'megaparsec', 'Mpc', 'picometer', 'pm',
                       'femtometer', 'fm', 'fermi', 'nautical_mile', 'nmi', 'fathom',
                       'chain', 'furlong', 'league']
        for u in length_units:
            mapping[u] = 'meter'
        
        # Mass units
        mass_units = ['kilogram', 'kg', 'kilograms', 'gram', 'g', 'grams',
                     'milligram', 'mg', 'milligrams', 'microgram', 'ug', 'micrograms',
                     'pound', 'lb', 'pounds', 'ounce', 'oz', 'ounces',
                     'ton', 'tons', 'tonne', 'tonnes',
                     # Advanced mass units
                     'atomic_mass_unit', 'amu', 'u', 'dalton', 'Da', 'electron_mass', 'm_e',
                     'proton_mass', 'm_p', 'neutron_mass', 'm_n', 'solar_mass', 'M_sun',
                     'earth_mass', 'M_earth', 'carat', 'ct', 'grain', 'gr', 'stone', 'st', 'slug']
        for u in mass_units:
            mapping[u] = 'kilogram'
        
        # Time units
        time_units = ['second', 's', 'seconds', 'sec', 'millisecond', 'ms', 'milliseconds',
                     'microsecond', 'us', 'microseconds', 'nanosecond', 'ns', 'nanoseconds',
                     'minute', 'min', 'minutes', 'hour', 'h', 'hr', 'hours',
                     'day', 'd', 'days', 'week', 'weeks', 'year', 'yr', 'years',
                     # Advanced time units
                     'picosecond', 'ps', 'femtosecond', 'fs', 'attosecond', 'as', 'shake',
                     'fortnight', 'month', 'decade', 'century', 'millennium']
        for u in time_units:
            mapping[u] = 'second'
        
        # Temperature units
        temp_units = ['kelvin', 'K', 'celsius', 'C', 'degC', 'fahrenheit', 'F', 'degF']
        for u in temp_units:
            mapping[u] = 'kelvin'
        
        # Current units
        current_units = ['ampere', 'A', 'amperes', 'amp', 'amps', 'milliampere', 'mA']
        for u in current_units:
            mapping[u] = 'ampere'
        
        # Amount units
        amount_units = ['mole', 'mol', 'moles']
        for u in amount_units:
            mapping[u] = 'mole'
        
        # Luminosity units
        lum_units = ['candela', 'cd']
        for u in lum_units:
            mapping[u] = 'candela'
        
        # Dimensionless
        mapping['dimensionless'] = 'dimensionless'
        mapping['percent'] = 'dimensionless'
        mapping['%'] = 'dimensionless'
        mapping['ppm'] = 'dimensionless'
        mapping['ppb'] = 'dimensionless'
        
        # Energy units (joule = kg⋅m²/s²)
        # These are derived units that need special handling
        # We'll mark them as 'joule' base and handle conversion via _CONVERSIONS
        energy_units = ['joule', 'J', 'joules', 'kilojoule', 'kJ', 'megajoule', 'MJ', 
                       'gigajoule', 'GJ', 'calorie', 'cal', 'calories', 'kilocalorie', 
                       'kcal', 'Calorie', 'electronvolt', 'eV', 'kiloelectronvolt', 'keV',
                       'megaelectronvolt', 'MeV', 'gigaelectronvolt', 'GeV', 
                       'teraelectronvolt', 'TeV', 'watt_hour', 'Wh', 
                       'kilowatt_hour', 'kWh', 'erg', 'british_thermal_unit', 'BTU', 
                       'btu', 'quad', 'ton_tnt', 'kiloton_tnt', 'megaton_tnt', 
                       'rydberg', 'Ry', 'hartree', 'Ha']
        for u in energy_units:
            mapping[u] = 'joule'
        
        # Power units
        power_units = ['watt', 'W', 'watts', 'kilowatt', 'kW', 'kilowatts', 'megawatt', 'MW',
                      'gigawatt', 'GW', 'terawatt', 'TW', 'milliwatt', 'mW', 'microwatt', 'uW',
                      'nanowatt', 'nW', 'horsepower', 'hp', 'metric_horsepower', 'PS',
                      'boiler_horsepower', 'volt_ampere', 'va', 'kilovolt_ampere', 'kva',
                      'megavolt_ampere', 'mva', 'kilovolt_ampere_reactive', 'kvar']
        for u in power_units:
            mapping[u] = 'watt'
        
        # Pressure units
        pressure_units = ['pascal', 'Pa', 'kilopascal', 'kPa', 'megapascal', 'MPa',
                         'gigapascal', 'GPa', 'bar', 'bars', 'millibar', 'mbar',
                         'microbar', 'ubar', 'barye', 'atmosphere', 'atm',
                         'technical_atmosphere', 'at', 'psi', 'PSI', 'pound_per_square_inch',
                         'torr', 'Torr', 'inch_mercury', 'inHg', 'millimeter_mercury', 'mmHg',
                         'bar_gauge', 'bar_g', 'barg', 'kilopascal_gauge', 'kpa_g', 'kpag',
                         'psi_gauge', 'psi_g', 'psig', 'kilogram_per_square_centimeter_gauge',
                         'kg_cm2_g', 'kgf_cm2_g', 'inch_water_column', 'in_wc', 'inwc',
                         'millimeter_water_column', 'mm_wc', 'mmwc', 'meter_water_column',
                         'm_wc', 'mwc', 'millimeter_water_column_gauge', 'mm_wc_g', 'mmwcg',
                         'hectopascal', 'hpa', 'ton_force_per_square_meter', 'tf_m2']
        for u in pressure_units:
            mapping[u] = 'pascal'
        
        # Force units
        force_units = ['newton', 'N', 'newtons', 'kilonewton', 'kN', 'meganewton', 'MN',
                      'dyne', 'dyn', 'kilogram_force', 'kgf', 'gram_force', 'gf',
                      'ton_force', 'tf', 'pound_force', 'lbf', 'poundal', 'kip']
        for u in force_units:
            mapping[u] = 'newton'
        
        # Frequency units
        freq_units = ['hertz', 'Hz', 'millihertz', 'mHz', 'kilohertz', 'kHz',
                     'megahertz', 'MHz', 'gigahertz', 'GHz', 'terahertz', 'THz',
                     'rpm', 'rps']
        for u in freq_units:
            mapping[u] = 'hertz'
        
        # Voltage units
        voltage_units = ['volt', 'V', 'volts', 'millivolt', 'mV', 'microvolt', 'uV',
                        'nanovolt', 'nV', 'kilovolt', 'kV', 'megavolt', 'MV',
                        'statvolt', 'volt_ac_dc', 'vac_dc']
        for u in voltage_units:
            mapping[u] = 'volt'
        
        # Current units
        current_units = ['ampere', 'A', 'amperes', 'amp', 'amps', 'milliampere', 'mA',
                        'microampere', 'uA', 'nanoampere', 'nA', 'picoampere', 'pA',
                        'kiloampere', 'kA', 'statampere']
        for u in current_units:
            mapping[u] = 'ampere'
        
        # Resistance units
        resistance_units = ['ohm', 'Ω', 'ohms', 'kiloohm', 'kΩ', 'megaohm', 'MΩ',
                           'gigaohm', 'gohm', 'GΩ']
        for u in resistance_units:
            mapping[u] = 'ohm'
        
        # Capacitance units
        capacitance_units = ['farad', 'F', 'millifarad', 'mF', 'microfarad', 'uF',
                            'nanofarad', 'nF', 'picofarad', 'pF', 'mfd']
        for u in capacitance_units:
            mapping[u] = 'farad'
        
        # Inductance units
        inductance_units = ['henry', 'H', 'millihenry', 'mH', 'microhenry', 'uH',
                           'nanohenry', 'nH']
        for u in inductance_units:
            mapping[u] = 'henry'
        
        # Magnetic field units
        magnetic_units = ['tesla', 'T', 'millitesla', 'mT', 'microtesla', 'uT',
                         'nanotesla', 'nT', 'gauss', 'G', 'milligauss', 'mG']
        for u in magnetic_units:
            mapping[u] = 'tesla'
        
        # Area units (derived from length²)
        area_units = ['hectare', 'ha', 'acre', 'acres', 'square_millimeter', 'mm2', 'sq_mm',
                     'square_inch', 'in2', 'sq_in', 'square_meter', 'm2', 'sq_m',
                     'square_centimeter', 'cm2', 'sq_cm', 'square_foot', 'ft2', 'sq_ft']
        for u in area_units:
            mapping[u] = 'meter^2'  # Will be handled as derived unit
        
        # Volume units (derived from length³)
        volume_units = ['liter', 'L', 'liters', 'litre', 'litres', 'milliliter', 'mL',
                       'milliliters', 'gallon', 'gal', 'gallons', 'quart', 'qt',
                       'pint', 'pt', 'cup', 'cups', 'fluid_ounce', 'fl_oz',
                       'cubic_millimeter', 'mm3', 'cu_mm', 'cubic_centimeter', 'cm3',
                       'cu_cm', 'cc', 'cubic_meter', 'm3', 'cu_m', 'cubic_foot', 'ft3',
                       'cu_ft', 'cubic_inch', 'in3', 'cu_in']
        for u in volume_units:
            mapping[u] = 'meter^3'  # Will be handled as derived unit
        
        # Wire gauge units (map to length)
        wire_gauge_units = ['american_wire_gauge_10', 'awg_10', 'american_wire_gauge_12', 'awg_12',
                           'american_wire_gauge_14', 'awg_14', 'american_wire_gauge_16', 'awg_16',
                           'american_wire_gauge_18', 'awg_18', 'american_wire_gauge_20', 'awg_20',
                           'standard_wire_gauge_10', 'swg_10', 'standard_wire_gauge_12', 'swg_12',
                           'standard_wire_gauge_14', 'swg_14', 'birmingham_wire_gauge_10', 'bwg_10',
                           'birmingham_wire_gauge_12', 'bwg_12']
        for u in wire_gauge_units:
            mapping[u] = 'meter'
        
        # Torque units (force × length)
        torque_units = ['inch_pound', 'in_lb', 'inch_lbf', 'newton_meter', 'nm_torque', 'n_m']
        for u in torque_units:
            mapping[u] = 'newton*meter'  # Will be handled as compound unit
        
        # Flow rate units (volume/time)
        flow_units = ['cubic_meter_per_second', 'm3_s', 'liter_per_second', 'L_s',
                     'liter_per_minute', 'L_min', 'gallon_per_minute', 'gpm',
                     'liters_per_hour', 'lph', 'l_h', 'liters_per_second', 'lps', 'l_s',
                     'tons_per_hour', 'tph', 't_h', 'normal_cubic_meters_per_hour', 'nm3_h',
                     'ncmh', 'cubic_feet_per_minute', 'cfm', 'ft3_min', 'cubic_meters_per_hour',
                     'm3_h', 'cmh', 'cubic_meters_per_second', 'm3_s', 'cms']
        for u in flow_units:
            mapping[u] = 'meter^3/second'  # Will be handled as compound unit
        
        # Velocity units (length/time)
        velocity_units = ['knot', 'kt', 'kn', 'mach', 'meters_per_hour', 'm_h', 'mh',
                         'feet_per_second', 'ft_s', 'fps', 'meters_per_second', 'm_s',
                         'ms_velocity']
        for u in velocity_units:
            mapping[u] = 'meter/second'  # Will be handled as compound unit
        
        # Density/concentration units
        density_units = ['kilogram_per_cubic_meter', 'kg_m3', 'gram_per_cubic_centimeter',
                        'g_cm3', 'gram_per_liter', 'g_L', 'milligrams_per_liter', 'mg_l', 'mg_per_l',
                        'micrograms_per_cubic_meter', 'ug_m3', 'ug_per_m3',
                        'kilograms_per_cubic_meter', 'kg_m3', 'kg_per_m3']
        for u in density_units:
            mapping[u] = 'kilogram/meter^3'
        
        # Surface density units (mass per area)
        surface_density_units = ['grams_per_square_meter', 'gsm', 'g_m2',
                               'kilograms_per_square_meter', 'kg_m2', 'kg_per_m2',
                               'kilograms_per_square_millimeter', 'kg_mm2', 'kg_per_mm2']
        for u in surface_density_units:
            mapping[u] = 'kilogram_per_square_meter'
        
        # Conductivity units
        conductivity_units = ['microsiemens_per_centimeter', 'us_cm', 'us_per_cm',
                             'millisiemens_per_centimeter', 'ms_cm', 'ms_per_cm']
        for u in conductivity_units:
            mapping[u] = 'siemens/meter'  # Will be handled as compound unit
        
        # Energy storage units
        energy_storage_units = ['ampere_hour', 'ah', 'amp_hour', 'milliampere_hour', 'mah',
                               'milliamp_hour']
        for u in energy_storage_units:
            mapping[u] = 'ampere*second'  # Will be handled as compound unit
        
        # Dimensionless units
        dimensionless_units = ['dimensionless', 'percent', '%', 'ppm', 'ppb', 'ppt',
                              'decibel', 'db', 'ph_scale', 'ph', 'strain', 'str',
                              'pressure_ratio', 'pr']
        for u in dimensionless_units:
            mapping[u] = 'dimensionless'
        
        cls._UNIT_TO_BASE = mapping
        return mapping
    
    def __init__(self, unit_str: str, scale: float = 1.0):
        """
        Initialize a Unit.
        
        Args:
            unit_str: String representation of the unit
            scale: Scale factor for the unit
        """
        # Check cache first
        cache_key = f"{unit_str}:{scale}"
        if cache_key in Unit._unit_cache:
            cached = Unit._unit_cache[cache_key]
            self._name = cached._name
            self._components = cached._components
            self._scale = cached._scale
            return
        
        self._parse_unit(unit_str)
        self._scale = scale
        
        # Cache the unit
        if len(Unit._unit_cache) < 1000:  # Limit cache size
            Unit._unit_cache[cache_key] = self
    
    def _parse_unit(self, unit_str: str) -> None:
        """Parse unit string into components."""
        # Simple parsing - handle basic units and compound units
        if '/' in unit_str:
            parts = unit_str.split('/')
            numerator = parts[0].strip()
            denominator = parts[1].strip()
            
            num_unit = Unit(numerator)
            den_unit = Unit(denominator)
            
            self._components = num_unit._components.copy()
            for unit, power in den_unit._components.items():
                self._components[unit] = self._components.get(unit, 0) - power
            self._name = unit_str
        elif '*' in unit_str or ' ' in unit_str:
            # Handle multiplication
            separator = '*' if '*' in unit_str else ' '
            parts = [p.strip() for p in unit_str.split(separator) if p.strip()]
            
            self._components: Dict[str, float] = {}
            for part in parts:
                unit = Unit(part)
                for u, p in unit._components.items():
                    self._components[u] = self._components.get(u, 0) + p
            self._name = unit_str
        else:
            # Single unit
            self._name = unit_str.strip()
            self._components = {self._name: 1.0}
    
    @property
    def dimensionality(self) -> Dimension:
        """Get the dimensionality of this unit."""
        # Build mapping if not done yet
        unit_to_base = self._build_unit_to_base_map()
        
        dim = Dimension()
        for unit, power in self._components.items():
            base_unit = unit_to_base.get(unit, unit)
            if base_unit in self._BASE_UNITS:
                base_dim = self._BASE_UNITS[base_unit]
                dim = dim + (base_dim * power)
        return dim
    
    def is_compatible_with(self, other: Unit) -> bool:
        """Check if this unit is compatible with another."""
        return self.dimensionality == other.dimensionality
    
    def conversion_factor_to(self, other: Unit) -> float:
        """Get conversion factor to another unit."""
        if not self.is_compatible_with(other):
            raise ValueError(f"Incompatible units: {self} and {other}")
        
        # Handle temperature conversions with offsets
        if self._is_temperature_unit() and other._is_temperature_unit():
            return self._temperature_conversion_factor(other)
        
        # Calculate conversion factor for regular units
        self_factor = 1.0
        for unit, power in self._components.items():
            self_factor *= self._CONVERSIONS.get(unit, 1.0) ** power
        
        other_factor = 1.0
        for unit, power in other._components.items():
            other_factor *= other._CONVERSIONS.get(unit, 1.0) ** power
        
        return self_factor / other_factor * self._scale / other._scale
    
    def _is_temperature_unit(self) -> bool:
        """Check if this is a temperature unit."""
        temp_units = {'kelvin', 'K', 'celsius', 'C', 'degC', 'fahrenheit', 'F', 'degF'}
        return len(self._components) == 1 and list(self._components.keys())[0] in temp_units
    
    def _temperature_conversion_factor(self, other: Unit) -> float:
        """Handle temperature conversions with proper offset handling."""
        from_unit = list(self._components.keys())[0]
        to_unit = list(other._components.keys())[0]
        
        # For now, return scale factor only (offset handled in Quantity.to())
        from_scale = self._CONVERSIONS.get(from_unit, 1.0)
        to_scale = other._CONVERSIONS.get(to_unit, 1.0)
        
        return from_scale / to_scale
    
    def to_base_units(self) -> Unit:
        """Convert to base SI units."""
        unit_to_base = self._build_unit_to_base_map()
        
        base_components: Dict[str, float] = {}
        for unit, power in self._components.items():
            base_unit = unit_to_base.get(unit, unit)
            base_components[base_unit] = base_components.get(base_unit, 0) + power
        
        # Build base unit string
        numerator = []
        denominator = []
        for unit, power in base_components.items():
            if power > 0:
                if power == 1:
                    numerator.append(unit)
                else:
                    numerator.append(f"{unit}^{power}")
            elif power < 0:
                if power == -1:
                    denominator.append(unit)
                else:
                    denominator.append(f"{unit}^{-power}")
        
        if not numerator and not denominator:
            return Unit("dimensionless")
        elif not denominator:
            return Unit(" * ".join(numerator))
        elif not numerator:
            return Unit("1 / " + " * ".join(denominator))
        else:
            return Unit(" * ".join(numerator) + " / " + " * ".join(denominator))
    
    def is_dimensionless(self) -> bool:
        """Check if unit is dimensionless."""
        return self.dimensionality == Dimension()
    
    def __mul__(self, other: Unit) -> Unit:
        """Multiply units."""
        new_components = self._components.copy()
        for unit, power in other._components.items():
            new_components[unit] = new_components.get(unit, 0) + power
        
        # Build new unit string
        parts = []
        for unit, power in new_components.items():
            if power != 0:
                if power == 1:
                    parts.append(unit)
                else:
                    parts.append(f"{unit}^{power}")
        
        unit_str = " * ".join(parts) if parts else "dimensionless"
        result = Unit.__new__(Unit)
        result._name = unit_str
        result._components = new_components
        result._scale = self._scale * other._scale
        return result
    
    def __truediv__(self, other: Unit) -> Unit:
        """Divide units."""
        new_components = self._components.copy()
        for unit, power in other._components.items():
            new_components[unit] = new_components.get(unit, 0) - power
        
        # Build new unit string
        numerator = []
        denominator = []
        for unit, power in new_components.items():
            if power > 0:
                if power == 1:
                    numerator.append(unit)
                else:
                    numerator.append(f"{unit}^{power}")
            elif power < 0:
                if power == -1:
                    denominator.append(unit)
                else:
                    denominator.append(f"{unit}^{abs(power)}")
        
        if not numerator and not denominator:
            unit_str = "dimensionless"
        elif not denominator:
            unit_str = " * ".join(numerator)
        elif not numerator:
            unit_str = "1 / " + " * ".join(denominator)
        else:
            unit_str = " * ".join(numerator) + " / " + " * ".join(denominator)
        
        result = Unit.__new__(Unit)
        result._name = unit_str
        result._components = new_components
        result._scale = self._scale / other._scale
        return result
    
    def __pow__(self, exponent: float) -> Unit:
        """Raise unit to a power."""
        new_components = {unit: power * exponent for unit, power in self._components.items()}
        
        # Clean up components with zero power
        new_components = {unit: power for unit, power in new_components.items() if abs(power) > 1e-10}
        
        parts = []
        for unit, power in new_components.items():
            if abs(power - 1.0) < 1e-10:
                parts.append(unit)
            else:
                parts.append(f"{unit}^{power}")
        
        unit_str = " * ".join(parts) if parts else "dimensionless"
        result = Unit.__new__(Unit)
        result._name = unit_str
        result._components = new_components
        result._scale = self._scale ** exponent
        return result
    
    def __eq__(self, other: object) -> bool:
        """Check equality."""
        if not isinstance(other, Unit):
            return False
        return self._components == other._components
    
    def __repr__(self) -> str:
        """String representation."""
        return f"Unit('{self._name}')"
    
    def __str__(self) -> str:
        """Human-readable string."""
        return self._name
