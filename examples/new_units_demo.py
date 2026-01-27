"""Demonstration of newly added units in Unifyt library."""

from unifyt import Quantity, utils, constants
import numpy as np

print("=" * 70)
print("UNIFYT - NEW UNITS DEMONSTRATION")
print("=" * 70)

# ============================================================================
# 1. WIRE GAUGE STANDARDS
# ============================================================================
print("\n1. WIRE GAUGE STANDARDS")
print("-" * 70)

# American Wire Gauge (AWG)
awg_12 = Quantity(1, 'awg_12')
print(f"AWG 12 wire diameter: {awg_12.to('millimeter'):.2f}")

awg_14 = Quantity(1, 'awg_14')
print(f"AWG 14 wire diameter: {awg_14.to('millimeter'):.2f}")

# Standard Wire Gauge (SWG)
swg_10 = Quantity(1, 'swg_10')
print(f"SWG 10 wire diameter: {swg_10.to('millimeter'):.2f}")

# Birmingham Wire Gauge (BWG)
bwg_12 = Quantity(1, 'bwg_12')
print(f"BWG 12 wire diameter: {bwg_12.to('millimeter'):.2f}")

# Using utility function
diameter = utils.convert_wire_gauge_to_diameter(12, 'awg')
print(f"AWG 12 calculated diameter: {diameter.to('millimeter'):.2f}")

# ============================================================================
# 2. GAUGE PRESSURE UNITS
# ============================================================================
print("\n2. GAUGE PRESSURE UNITS")
print("-" * 70)

# Gauge pressures (relative to atmospheric)
tire_pressure = Quantity(32, 'psi_gauge')
print(f"Tire pressure (gauge): {tire_pressure}")
print(f"Tire pressure in bar: {tire_pressure.to('bar'):.2f}")

boiler_pressure = Quantity(5, 'bar_gauge')
print(f"Boiler pressure (gauge): {boiler_pressure}")
print(f"Boiler pressure in PSI: {boiler_pressure.to('psi'):.1f}")

# Convert gauge to absolute pressure
absolute_pressure = utils.convert_pressure_gauge_to_absolute(tire_pressure)
print(f"Tire absolute pressure: {absolute_pressure.to('bar'):.2f}")

# ============================================================================
# 3. WATER COLUMN PRESSURE
# ============================================================================
print("\n3. WATER COLUMN PRESSURE")
print("-" * 70)

# Water column measurements (common in HVAC)
static_pressure = Quantity(0.5, 'in_wc')
print(f"Static pressure: {static_pressure}")
print(f"In pascals: {static_pressure.to('pascal'):.1f}")

mm_wc_pressure = Quantity(25, 'mm_wc')
print(f"MM water column: {mm_wc_pressure}")
print(f"In inches WC: {mm_wc_pressure.to('in_wc'):.2f}")

# ============================================================================
# 4. TEXTILE AND PAPER INDUSTRY
# ============================================================================
print("\n4. TEXTILE AND PAPER INDUSTRY")
print("-" * 70)

# Grams per square meter (GSM) - paper weight
paper_weight = Quantity(80, 'gsm')
print(f"Paper weight: {paper_weight}")
print(f"In kg/m²: {paper_weight.to('kilogram/meter^2'):.3f}")

# Heavy cardboard
cardboard = Quantity(300, 'gsm')
print(f"Cardboard weight: {cardboard}")
print(f"In oz/yd²: {cardboard.to('ounce/yard^2'):.2f}")

# ============================================================================
# 5. ADDITIONAL FLOW UNITS
# ============================================================================
print("\n5. ADDITIONAL FLOW UNITS")
print("-" * 70)

# Liters per hour (common in medical equipment)
iv_flow = Quantity(125, 'lph')
print(f"IV drip rate: {iv_flow}")
print(f"In mL/min: {iv_flow.to('milliliter/minute'):.1f}")

# Tons per hour (industrial processes)
material_flow = Quantity(50, 'tph')
print(f"Material flow: {material_flow}")
print(f"In kg/s: {material_flow.to('kilogram/second'):.1f}")

# Cubic feet per minute (HVAC)
air_flow = Quantity(2000, 'cfm')
print(f"Air flow: {air_flow}")
print(f"In m³/h: {air_flow.to('cubic_meter_per_hour'):.0f}")

# ============================================================================
# 6. ELECTRICAL POWER UNITS
# ============================================================================
print("\n6. ELECTRICAL POWER UNITS")
print("-" * 70)

# Volt-Ampere (apparent power)
apparent_power = Quantity(1500, 'va')
print(f"Apparent power: {apparent_power}")
print(f"In kVA: {apparent_power.to('kva'):.2f}")

# Kilovolt-Ampere
transformer_rating = Quantity(500, 'kva')
print(f"Transformer rating: {transformer_rating}")
print(f"In VA: {transformer_rating.to('va'):,.0f}")

# Reactive power
reactive_power = Quantity(300, 'kvar')
print(f"Reactive power: {reactive_power}")

# ============================================================================
# 7. ADDITIONAL ELECTRICAL UNITS
# ============================================================================
print("\n7. ADDITIONAL ELECTRICAL UNITS")
print("-" * 70)

# Gigaohm resistance (high voltage applications)
insulation_resistance = Quantity(10, 'gohm')
print(f"Insulation resistance: {insulation_resistance}")
print(f"In MΩ: {insulation_resistance.to('megaohm'):,.0f}")

# AC/DC voltage notation
supply_voltage = Quantity(24, 'vac_dc')
print(f"Supply voltage: {supply_voltage}")

# ============================================================================
# 8. TORQUE UNITS
# ============================================================================
print("\n8. TORQUE UNITS")
print("-" * 70)

# Inch-pounds (small fasteners)
screw_torque = Quantity(15, 'in_lb')
print(f"Screw torque: {screw_torque}")
print(f"In N⋅m: {screw_torque.to('newton_meter'):.2f}")

# Newton-meters
wheel_torque = Quantity(100, 'nm_torque')
print(f"Wheel lug torque: {wheel_torque}")
print(f"In ft⋅lb: {wheel_torque.to('foot*pound_force'):.1f}")

# ============================================================================
# 9. CONCENTRATION AND DENSITY UNITS
# ============================================================================
print("\n9. CONCENTRATION AND DENSITY UNITS")
print("-" * 70)

# Water quality measurements
chlorine_level = Quantity(2.5, 'mg_l')
print(f"Chlorine level: {chlorine_level}")
print(f"In ppm: {chlorine_level.to('gram_per_liter') * 1000:.1f}")

# Air quality
pm25_level = Quantity(35, 'ug_m3')
print(f"PM2.5 level: {pm25_level}")

# Surface density
coating_thickness = Quantity(150, 'kg_m2')
print(f"Coating density: {coating_thickness}")

# ============================================================================
# 10. CONDUCTIVITY UNITS
# ============================================================================
print("\n10. CONDUCTIVITY UNITS")
print("-" * 70)

# Water conductivity
tap_water_cond = Quantity(500, 'us_cm')
print(f"Tap water conductivity: {tap_water_cond}")

# High conductivity solution
salt_water_cond = Quantity(50, 'ms_cm')
print(f"Salt water conductivity: {salt_water_cond}")
print(f"In μS/cm: {salt_water_cond.to('us_cm'):,.0f}")

# ============================================================================
# 11. AREA AND VOLUME UNITS
# ============================================================================
print("\n11. AREA AND VOLUME UNITS")
print("-" * 70)

# Small areas
chip_area = Quantity(25, 'mm2')
print(f"Microchip area: {chip_area}")
print(f"In square inches: {chip_area.to('in2'):.4f}")

# Small volumes
droplet_volume = Quantity(5, 'mm3')
print(f"Droplet volume: {droplet_volume}")
print(f"In microliters: {droplet_volume.to('milliliter') * 1000:.1f}")

# ============================================================================
# 12. VELOCITY UNITS
# ============================================================================
print("\n12. VELOCITY UNITS")
print("-" * 70)

# Slow velocities
conveyor_speed = Quantity(10, 'm_h')
print(f"Conveyor speed: {conveyor_speed}")
print(f"In mm/s: {conveyor_speed.to('millimeter/second'):.2f}")

# Projectile velocity
bullet_speed = Quantity(2800, 'ft_s')
print(f"Bullet velocity: {bullet_speed}")
print(f"In m/s: {bullet_speed.to('meter/second'):.0f}")

# ============================================================================
# 13. ENERGY STORAGE UNITS
# ============================================================================
print("\n13. ENERGY STORAGE UNITS")
print("-" * 70)

# Battery capacity
car_battery = Quantity(70, 'ah')
print(f"Car battery capacity: {car_battery}")
print(f"In coulombs: {car_battery.to('coulomb'):,.0f}")

# Phone battery
phone_battery = Quantity(3000, 'mah')
print(f"Phone battery: {phone_battery}")
print(f"In Ah: {phone_battery.to('ah'):.1f}")

# ============================================================================
# 14. DIMENSIONLESS UNITS
# ============================================================================
print("\n14. DIMENSIONLESS UNITS")
print("-" * 70)

# Sound level
noise_level = Quantity(85, 'db')
print(f"Noise level: {noise_level}")

# pH measurement
pool_ph = Quantity(7.2, 'ph')
print(f"Pool pH: {pool_ph}")

# Material strain
steel_strain = Quantity(0.002, 'str')
print(f"Steel strain: {steel_strain}")

# Using utility functions for conversions
ph_concentration = utils.convert_ph_to_concentration(7.2)
print(f"H+ concentration at pH 7.2: {ph_concentration:.2e}")

db_ratio = utils.convert_decibel_to_ratio(85)
print(f"85 dB as voltage ratio: {db_ratio:.0f}")

# ============================================================================
# 15. PRACTICAL CALCULATIONS
# ============================================================================
print("\n15. PRACTICAL CALCULATIONS")
print("-" * 70)

# HVAC calculation
room_volume = Quantity(100, 'm3')
air_changes = 6  # per hour
required_flow = room_volume * air_changes / Quantity(1, 'hour')
print(f"Required air flow: {required_flow.to('cfm'):.0f}")

# Electrical calculation
voltage = Quantity(480, 'volt')
current = Quantity(20, 'ampere')
apparent_power_calc = voltage * current
print(f"Calculated apparent power: {apparent_power_calc.to('kva'):.1f}")

# Water pressure calculation
water_height = Quantity(10, 'meter')
water_pressure = constants.water_density_stp * constants.g * water_height
print(f"Water pressure at 10m depth: {water_pressure.to('kpa'):.1f}")

# Wire resistance calculation (simplified)
wire_length = Quantity(100, 'meter')
wire_area = Quantity(2.5, 'mm2')
copper_resistivity = Quantity(1.7e-8, 'ohm*meter')  # Approximate
wire_resistance = copper_resistivity * wire_length / wire_area
print(f"Wire resistance: {wire_resistance.to('milliohm'):.1f}")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("SUMMARY OF NEW UNITS ADDED")
print("=" * 70)
print("✓ Wire gauge standards (AWG, SWG, BWG)")
print("✓ Gauge pressure units (bar_g, psi_g, kpa_g)")
print("✓ Water column pressure (in_wc, mm_wc, m_wc)")
print("✓ Textile units (gsm)")
print("✓ Additional flow units (lph, tph, cfm)")
print("✓ Electrical power units (va, kva, mva, kvar)")
print("✓ Additional electrical units (gohm, vac_dc)")
print("✓ Torque units (in_lb, nm_torque)")
print("✓ Concentration units (mg_l, ug_m3)")
print("✓ Conductivity units (us_cm, ms_cm)")
print("✓ Area/volume units (mm2, in2, mm3, in3)")
print("✓ Velocity units (m_h, ft_s)")
print("✓ Energy storage units (ah, mah)")
print("✓ Dimensionless units (db, ph, str)")
print("✓ Utility functions for conversions")
print("=" * 70)
print("Total new units added: 80+")
print("All units are fully compatible with existing Unifyt functionality!")