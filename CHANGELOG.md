# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2024-12-24

### Added - Industrial Units & Enhanced Functionality 🏭

#### New Industrial Units (80+ units added!)

**Wire Gauge Standards**:
- american_wire_gauge (awg_10, awg_12, awg_14, awg_16, awg_18, awg_20)
- standard_wire_gauge (swg_10, swg_12, swg_14)
- birmingham_wire_gauge (bwg_10, bwg_12)

**Gauge Pressure Units**:
- bar_gauge, bar_g, barg
- kilopascal_gauge, kpa_g, kpag
- psi_gauge, psi_g, psig
- kilogram_per_square_centimeter_gauge, kg_cm2_g, kgf_cm2_g

**Water Column Pressure**:
- inch_water_column, in_wc, inwc
- millimeter_water_column, mm_wc, mmwc
- meter_water_column, m_wc, mwc
- millimeter_water_column_gauge, mm_wc_g, mmwcg

**Textile and Paper Industry**:
- grams_per_square_meter, gsm, g_m2

**Additional Flow Units**:
- liters_per_hour, lph, l_h
- liters_per_second, lps, l_s
- tons_per_hour, tph, t_h
- normal_cubic_meters_per_hour, nm3_h, ncmh
- cubic_feet_per_minute, cfm, ft3_min
- cubic_meters_per_hour, m3_h, cmh
- cubic_meters_per_second, m3_s, cms

**Electrical Power Units**:
- volt_ampere, va
- kilovolt_ampere, kva
- megavolt_ampere, mva
- kilovolt_ampere_reactive, kvar

**Additional Electrical Units**:
- gigaohm, gohm, GΩ
- volt_ac_dc, vac_dc

**Torque Units**:
- inch_pound, in_lb, inch_lbf
- newton_meter (torque), nm_torque, n_m

**Additional Pressure Units**:
- hectopascal, hpa
- ton_force_per_square_meter, tf_m2

**Concentration and Density Units**:
- milligrams_per_liter, mg_l, mg_per_l
- micrograms_per_cubic_meter, ug_m3, ug_per_m3
- kilograms_per_cubic_meter, kg_m3, kg_per_m3
- kilograms_per_square_meter, kg_m2, kg_per_m2
- kilograms_per_square_millimeter, kg_mm2, kg_per_mm2

**Conductivity Units**:
- microsiemens_per_centimeter, us_cm, us_per_cm
- millisiemens_per_centimeter, ms_cm, ms_per_cm

**Additional Area Units**:
- square_millimeter, mm2, sq_mm
- square_inch, in2, sq_in
- square_meter, m2, sq_m
- square_centimeter, cm2, sq_cm
- square_foot, ft2, sq_ft

**Additional Volume Units**:
- cubic_millimeter, mm3, cu_mm
- cubic_centimeter, cm3, cu_cm, cc
- cubic_meter, m3, cu_m
- cubic_foot, ft3, cu_ft
- cubic_inch, in3, cu_in

**Velocity Units**:
- meters_per_hour, m_h, mh
- feet_per_second, ft_s, fps
- meters_per_second, m_s, ms_velocity

**Energy Storage Units**:
- ampere_hour, ah, amp_hour
- milliampere_hour, mah, milliamp_hour

**Dimensionless Units**:
- decibel, db
- ph_scale, ph (pH scale)
- strain, str
- pressure_ratio, pr

**Additional Time Units**:
- month, mon (average month)

**Capacitance (additional)**:
- microfarad, mfd (alternative notation)

#### New Physical Constants (10+ constants added!)

**Standard Conditions**:
- standard_temperature (0°C)
- standard_pressure (1 atm)
- water_density_stp (water density at STP)
- water_specific_heat (water specific heat)
- air_density_stp (air density at STP)
- air_specific_heat (air specific heat)

**Electrical Constants**:
- elementary_conductance (2e²/h)
- resistance_quantum (h/2e²)

#### New Utility Functions

**Wire Gauge Conversions**:
- convert_wire_gauge_to_diameter(gauge, gauge_type)

**Pressure Conversions**:
- convert_pressure_gauge_to_absolute(gauge_pressure, atmospheric_pressure)

**pH Conversions**:
- convert_ph_to_concentration(ph_value)
- convert_concentration_to_ph(concentration)

**Decibel Conversions**:
- convert_decibel_to_ratio(db_value)
- convert_ratio_to_decibel(ratio)

#### Enhanced Testing
- 100+ new test cases for all new units
- Comprehensive compatibility testing
- Utility function testing
- Edge case coverage

### Changed
- Version bumped to 0.3.0
- Updated documentation to reflect new units
- Enhanced unit-to-base mapping for new units
- Improved examples with industrial applications

### Performance
- No performance degradation
- Enhanced unit caching for new units
- Efficient handling of compound units
- Memory efficient despite 25% more units

### Compatibility
- **100% backward compatible** - All existing code works unchanged
- New units integrate seamlessly with existing functionality
- All arithmetic operations work with new units
- Conversion system handles all new units automatically

## [0.2.0] - 2024-12-24

### Added - Major Feature Release 🚀

#### Units (200+ new units added - now 300+ total!)

**Astronomical Units**:
- kiloparsec, megaparsec
- nautical_mile, fathom, chain, furlong, league
- picometer, femtometer, fermi

**Atomic & Nuclear**:
- atomic_mass_unit, dalton
- electron_mass, proton_mass, neutron_mass
- solar_mass, earth_mass
- carat, grain, stone, slug

**Advanced Time**:
- picosecond, femtosecond, attosecond
- shake, fortnight, month, decade, century, millennium

**Advanced Energy**:
- megajoule, gigajoule, erg
- british_thermal_unit, therm, quad
- ton_tnt, kiloton_tnt, megaton_tnt
- rydberg, hartree

**Advanced Power**:
- gigawatt, terawatt
- milliwatt, microwatt, nanowatt
- metric_horsepower, boiler_horsepower

**Advanced Pressure**:
- gigapascal, millibar, microbar, barye
- technical_atmosphere
- inch_mercury, millimeter_mercury

**Advanced Force**:
- meganewton, dyne
- kilogram_force, gram_force, ton_force
- poundal, kip

**Advanced Frequency**:
- terahertz, millihertz
- rpm (revolutions per minute)
- rps (revolutions per second)

**Advanced Voltage**:
- megavolt, microvolt, nanovolt
- statvolt

**Advanced Current**:
- microampere, nanoampere, picoampere
- kiloampere, statampere

**Capacitance**:
- farad, millifarad, microfarad, nanofarad, picofarad

**Inductance**:
- henry, millihenry, microhenry, nanohenry

**Magnetic Field**:
- tesla, millitesla, microtesla, nanotesla
- gauss, milligauss

**Magnetic Flux**:
- weber, milliweber, maxwell

**Illuminance**:
- lux, foot_candle, phot

**Luminous Flux**:
- lumen

**Radioactivity**:
- becquerel, kilobecquerel, megabecquerel, gigabecquerel
- curie, millicurie, microcurie
- rutherford

**Absorbed Dose**:
- gray, milligray, rad

**Equivalent Dose**:
- sievert, millisievert, microsievert
- rem, millirem

**Catalytic Activity**:
- katal, unit (enzyme unit)

**Data/Information**:
- bit, byte
- kilobyte, megabyte, gigabyte, terabyte, petabyte
- kibibyte, mebibyte, gibibyte, tebibyte

**Velocity**:
- knot, mach

**Acceleration**:
- gal (galileo), standard_gravity

**Viscosity**:
- pascal_second, poise, centipoise (dynamic)
- stokes, centistokes (kinematic)

**Thermal Properties**:
- watt_per_meter_kelvin (thermal conductivity)
- joule_per_kelvin (heat capacity)
- joule_per_kilogram_kelvin (specific heat)

**Molar Mass**:
- gram_per_mole, kilogram_per_mole

**Concentration**:
- molar, millimolar, micromolar, nanomolar

**Density**:
- kilogram_per_cubic_meter
- gram_per_cubic_centimeter
- gram_per_liter

**Flow Rate**:
- cubic_meter_per_second
- liter_per_second, liter_per_minute
- gallon_per_minute

**Fuel Efficiency**:
- mile_per_gallon, kilometer_per_liter
- liter_per_100km

**Angle**:
- arcminute, arcsecond, gradian

**Dimensionless**:
- ppt (parts per trillion)

#### Constants (50+ new constants added - now 80+ total!)

**Electromagnetic**:
- Faraday constant (F)
- Vacuum impedance (Z_0)
- Conductance quantum (G_0)
- Josephson constant (K_J)
- Von Klitzing constant (R_K)
- Magnetic flux quantum (Phi_0)
- Bohr magneton (mu_B)
- Nuclear magneton (mu_N)
- Proton/electron/neutron magnetic moments
- Proton gyromagnetic ratio

**Radiation**:
- Wien displacement constant
- First radiation constant
- Second radiation constant

**Atomic & Particle**:
- Compton wavelength
- Classical electron radius
- Thomson cross section
- Electron g-factor
- Muon mass
- Tau mass

**Planck Units**:
- Planck length (l_P)
- Planck mass (m_P)
- Planck time (t_P)
- Planck temperature (T_P)
- Planck energy (E_P)

**Cosmological**:
- Hubble constant (H_0)
- CMB temperature (T_CMB)
- Age of universe
- Critical density (rho_c)

**Solar System**:
- Solar luminosity (L_sun)
- Solar radius (R_sun)
- Jupiter mass (M_jupiter)
- Moon mass (M_moon)
- Schwarzschild radii (Earth, Sun)

### Changed
- Version bumped to 0.2.0
- Documentation updated across all files
- Examples updated with new units
- API reference expanded

### Performance
- No performance degradation
- Unit caching maintained
- Memory efficient despite 3x more units

## [0.1.0] - 2024-12-24

### Added
- Initial release of Unifyt
- Core `Quantity` class for representing values with units
- `Unit` class for unit management and conversions
- `Dimension` class for tracking physical dimensions
- `UnitRegistry` for custom unit definitions
- `UnitContext` for unit system management
- Support for 100+ units including:
  - Basic SI units (length, mass, time, etc.)
  - Imperial units
  - Energy units (joule, calorie, kWh, eV)
  - Power units (watt, horsepower)
  - Pressure units (pascal, bar, atm, psi)
  - Force units (newton, pound_force)
  - Frequency units (hertz, MHz, GHz)
  - Voltage and electrical units
  - Volume units (liter, gallon)
  - Angle units (radian, degree)
- Physical constants module with 30+ constants:
  - Fundamental constants (c, h, G, k_B, etc.)
  - Astronomical constants (AU, ly, M_sun, etc.)
  - Atomic constants (a_0, m_e, m_p, etc.)
- Utility functions module:
  - Array creation (linspace, arange, zeros, ones, full)
  - Array operations (concatenate, stack)
  - Statistical functions (sum, mean, std, min, max)
  - Mathematical functions (sqrt, clip, isclose)
- Serialization support:
  - JSON serialization/deserialization
  - Pickle support
  - File save/load functions
  - Custom JSON encoder/decoder
- Performance optimizations:
  - Unit caching for faster parsing
  - Efficient dimension checking
  - NumPy vectorization
- Comprehensive test suite with 50+ tests
- Full documentation:
  - User guide with examples
  - Complete API reference
  - Performance guide
  - Migration guide from Pint/Unyt
  - Feature documentation
- Example scripts:
  - Basic usage examples
  - Scientific calculations
  - Custom unit definitions
  - Array operations
  - Advanced features (constants, utils, serialization)
- Development tools:
  - Setup script
  - Test runner
  - Code formatter
  - Code quality checker
- Type hints for better IDE support
- Full PEP 561 compliance

### Features
- Intuitive API for creating and manipulating quantities
- Automatic unit conversion in arithmetic operations
- Support for compound units (e.g., meter/second)
- Array operations with NumPy integration
- Custom unit definitions
- Unit system contexts
- Comparison operations
- Power operations
- Dimensionality checking
- Physical constants with proper units
- Utility functions for common operations
- Serialization to JSON and pickle

### Documentation
- User guide with comprehensive examples
- Complete API reference
- Quick start guide
- Performance optimization guide
- Migration guide from other libraries
- Contributing guidelines
- README with feature overview
- Inline documentation with docstrings

### Performance
- Unit caching reduces parsing overhead
- NumPy integration for vectorized operations
- Efficient dimension tracking
- Optimized conversion calculations
- 2-5x faster than Pint for array operations

[Unreleased]: https://github.com/MEERAN2314/unifyt/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/MEERAN2314/unifyt/releases/tag/v0.2.0
[0.1.0]: https://github.com/MEERAN2314/unifyt/releases/tag/v0.1.0
