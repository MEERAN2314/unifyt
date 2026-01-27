"""Tests for newly added units in Unifyt library."""

import pytest
import numpy as np
from unifyt import Quantity, Unit, utils


class TestWireGaugeUnits:
    """Test wire gauge units."""
    
    def test_awg_units(self):
        """Test American Wire Gauge units."""
        awg_12 = Quantity(1, 'awg_12')
        assert awg_12.magnitude == 1
        
        # Test conversion to millimeters
        diameter_mm = awg_12.to('millimeter')
        assert abs(diameter_mm.magnitude - 2.053) < 0.01
    
    def test_swg_units(self):
        """Test Standard Wire Gauge units."""
        swg_10 = Quantity(1, 'swg_10')
        diameter_mm = swg_10.to('millimeter')
        assert diameter_mm.magnitude > 3.0  # SWG 10 is about 3.25mm
    
    def test_bwg_units(self):
        """Test Birmingham Wire Gauge units."""
        bwg_12 = Quantity(1, 'bwg_12')
        diameter_mm = bwg_12.to('millimeter')
        assert diameter_mm.magnitude > 2.5  # BWG 12 is about 2.77mm


class TestGaugePressureUnits:
    """Test gauge pressure units."""
    
    def test_bar_gauge(self):
        """Test bar gauge pressure."""
        pressure = Quantity(2, 'bar_gauge')
        assert pressure.magnitude == 2
        
        # Should be compatible with absolute pressure
        absolute = pressure.to('bar')
        assert absolute.magnitude == 2  # Same value, different context
    
    def test_psi_gauge(self):
        """Test PSI gauge pressure."""
        pressure = Quantity(15, 'psi_gauge')
        bar_pressure = pressure.to('bar')
        assert abs(bar_pressure.magnitude - 1.034) < 0.01
    
    def test_kpa_gauge(self):
        """Test kPa gauge pressure."""
        pressure = Quantity(200, 'kpa_gauge')
        bar_pressure = pressure.to('bar')
        assert abs(bar_pressure.magnitude - 2.0) < 0.01


class TestWaterColumnPressure:
    """Test water column pressure units."""
    
    def test_inch_water_column(self):
        """Test inches water column."""
        pressure = Quantity(10, 'in_wc')
        pascal_pressure = pressure.to('pascal')
        assert abs(pascal_pressure.magnitude - 2491) < 10
    
    def test_mm_water_column(self):
        """Test millimeters water column."""
        pressure = Quantity(100, 'mm_wc')
        pascal_pressure = pressure.to('pascal')
        assert abs(pascal_pressure.magnitude - 980.7) < 1
    
    def test_meter_water_column(self):
        """Test meters water column."""
        pressure = Quantity(1, 'm_wc')
        kpa_pressure = pressure.to('kilopascal')
        assert abs(kpa_pressure.magnitude - 9.807) < 0.01


class TestTextileUnits:
    """Test textile and paper industry units."""
    
    def test_gsm(self):
        """Test grams per square meter."""
        gsm = Quantity(200, 'gsm')
        kg_m2 = gsm.to('kilogram/meter^2')
        assert abs(kg_m2.magnitude - 0.2) < 0.001


class TestAdditionalFlowUnits:
    """Test additional flow rate units."""
    
    def test_liters_per_hour(self):
        """Test liters per hour."""
        flow = Quantity(3600, 'lph')
        lps = flow.to('liter_per_second')
        assert abs(lps.magnitude - 1.0) < 0.01
    
    def test_tons_per_hour(self):
        """Test tons per hour."""
        flow = Quantity(1, 'tph')
        kg_s = flow.to('kilogram/second')
        assert abs(kg_s.magnitude - 0.278) < 0.01
    
    def test_cubic_feet_per_minute(self):
        """Test cubic feet per minute."""
        flow = Quantity(100, 'cfm')
        m3_s = flow.to('cubic_meter_per_second')
        assert flow.magnitude == 100
        assert m3_s.magnitude > 0.04


class TestElectricalPowerUnits:
    """Test electrical power units."""
    
    def test_volt_ampere(self):
        """Test volt-ampere units."""
        power = Quantity(1000, 'va')
        assert power.magnitude == 1000
        
        kva = power.to('kva')
        assert abs(kva.magnitude - 1.0) < 0.001
    
    def test_kilovolt_ampere(self):
        """Test kilovolt-ampere units."""
        power = Quantity(10, 'kva')
        va = power.to('va')
        assert va.magnitude == 10000
    
    def test_kvar(self):
        """Test kilovolt-ampere reactive."""
        power = Quantity(5, 'kvar')
        assert power.magnitude == 5


class TestAdditionalElectricalUnits:
    """Test additional electrical units."""
    
    def test_gigaohm(self):
        """Test gigaohm resistance."""
        resistance = Quantity(1, 'gohm')
        megaohm = resistance.to('megaohm')
        assert megaohm.magnitude == 1000
    
    def test_volt_ac_dc(self):
        """Test AC/DC voltage notation."""
        voltage = Quantity(120, 'vac_dc')
        volt = voltage.to('volt')
        assert volt.magnitude == 120


class TestTorqueUnits:
    """Test torque units."""
    
    def test_inch_pound(self):
        """Test inch-pound torque."""
        torque = Quantity(10, 'in_lb')
        nm = torque.to('newton_meter')
        assert abs(nm.magnitude - 1.13) < 0.01
    
    def test_newton_meter_torque(self):
        """Test newton-meter torque."""
        torque = Quantity(5, 'nm_torque')
        in_lb = torque.to('in_lb')
        assert abs(in_lb.magnitude - 44.25) < 0.5


class TestAdditionalPressureUnits:
    """Test additional pressure units."""
    
    def test_hectopascal(self):
        """Test hectopascal."""
        pressure = Quantity(1013, 'hpa')
        bar = pressure.to('bar')
        assert abs(bar.magnitude - 1.013) < 0.001


class TestConcentrationUnits:
    """Test concentration and density units."""
    
    def test_milligrams_per_liter(self):
        """Test mg/L concentration."""
        conc = Quantity(100, 'mg_l')
        g_l = conc.to('gram_per_liter')
        assert abs(g_l.magnitude - 0.1) < 0.001
    
    def test_micrograms_per_cubic_meter(self):
        """Test μg/m³ concentration."""
        conc = Quantity(50, 'ug_m3')
        assert conc.magnitude == 50
    
    def test_kg_per_square_meter(self):
        """Test kg/m² density."""
        density = Quantity(10, 'kg_m2')
        assert density.magnitude == 10


class TestConductivityUnits:
    """Test conductivity units."""
    
    def test_microsiemens_per_cm(self):
        """Test μS/cm conductivity."""
        cond = Quantity(500, 'us_cm')
        assert cond.magnitude == 500
    
    def test_millisiemens_per_cm(self):
        """Test mS/cm conductivity."""
        cond = Quantity(2, 'ms_cm')
        us_cm = cond.to('us_cm')
        assert us_cm.magnitude == 2000


class TestAreaVolumeUnits:
    """Test additional area and volume units."""
    
    def test_square_units(self):
        """Test square area units."""
        area_mm2 = Quantity(1000, 'mm2')
        area_cm2 = area_mm2.to('cm2')
        assert abs(area_cm2.magnitude - 10) < 0.01
        
        area_in2 = Quantity(1, 'in2')
        area_cm2 = area_in2.to('cm2')
        assert abs(area_cm2.magnitude - 6.45) < 0.01
    
    def test_cubic_units(self):
        """Test cubic volume units."""
        vol_mm3 = Quantity(1000, 'mm3')
        vol_cm3 = vol_mm3.to('cm3')
        assert abs(vol_cm3.magnitude - 1) < 0.01
        
        vol_in3 = Quantity(1, 'in3')
        vol_cm3 = vol_in3.to('cm3')
        assert abs(vol_cm3.magnitude - 16.39) < 0.01


class TestVelocityUnits:
    """Test additional velocity units."""
    
    def test_meters_per_hour(self):
        """Test m/h velocity."""
        velocity = Quantity(3600, 'm_h')
        ms = velocity.to('meter/second')
        assert abs(ms.magnitude - 1.0) < 0.01
    
    def test_feet_per_second(self):
        """Test ft/s velocity."""
        velocity = Quantity(10, 'ft_s')
        ms = velocity.to('meter/second')
        assert abs(ms.magnitude - 3.048) < 0.01


class TestEnergyStorageUnits:
    """Test energy storage units."""
    
    def test_ampere_hour(self):
        """Test ampere-hour."""
        capacity = Quantity(10, 'ah')
        coulomb = capacity.to('coulomb')
        assert coulomb.magnitude == 36000
    
    def test_milliampere_hour(self):
        """Test milliampere-hour."""
        capacity = Quantity(2000, 'mah')
        ah = capacity.to('ah')
        assert abs(ah.magnitude - 2.0) < 0.01


class TestDimensionlessUnits:
    """Test dimensionless units."""
    
    def test_decibel(self):
        """Test decibel unit."""
        db = Quantity(20, 'db')
        assert db.magnitude == 20
    
    def test_ph_scale(self):
        """Test pH scale unit."""
        ph = Quantity(7, 'ph')
        assert ph.magnitude == 7
    
    def test_strain(self):
        """Test strain unit."""
        strain = Quantity(0.001, 'str')
        assert strain.magnitude == 0.001


class TestUtilityFunctions:
    """Test new utility functions."""
    
    def test_wire_gauge_conversion(self):
        """Test wire gauge to diameter conversion."""
        diameter = utils.convert_wire_gauge_to_diameter(12, 'awg')
        mm_diameter = diameter.to('millimeter')
        assert abs(mm_diameter.magnitude - 2.05) < 0.1
    
    def test_gauge_to_absolute_pressure(self):
        """Test gauge to absolute pressure conversion."""
        gauge = Quantity(2, 'bar')
        absolute = utils.convert_pressure_gauge_to_absolute(gauge)
        assert absolute.magnitude > 3.0  # Should be ~3.01 bar
    
    def test_ph_concentration_conversion(self):
        """Test pH to concentration conversion."""
        conc = utils.convert_ph_to_concentration(7.0)
        assert abs(conc.magnitude - 1e-7) < 1e-8
        
        ph = utils.convert_concentration_to_ph(conc)
        assert abs(ph - 7.0) < 0.01
    
    def test_decibel_ratio_conversion(self):
        """Test decibel to ratio conversion."""
        ratio = utils.convert_decibel_to_ratio(20)
        assert abs(ratio - 10) < 0.01  # 20 dB = 10x voltage ratio
        
        db = utils.convert_ratio_to_decibel(100)
        assert abs(db - 40) < 0.01  # 100x = 40 dB


class TestUnitCompatibility:
    """Test that new units are compatible with existing ones."""
    
    def test_pressure_compatibility(self):
        """Test pressure unit compatibility."""
        p1 = Quantity(1, 'bar')
        p2 = Quantity(100, 'kpa')
        
        # Should be able to add compatible pressures
        total = p1 + p2
        assert total.magnitude > 1.9  # ~2 bar total
    
    def test_flow_compatibility(self):
        """Test flow rate compatibility."""
        f1 = Quantity(1, 'lps')
        f2 = Quantity(60, 'lpm')
        
        # Should be able to add compatible flows
        total = f1 + f2
        assert total.magnitude == 2.0  # 2 L/s total
    
    def test_electrical_compatibility(self):
        """Test electrical unit compatibility."""
        p1 = Quantity(1, 'kva')
        p2 = Quantity(500, 'va')
        
        # Should be able to add compatible power units
        total = p1 + p2
        assert abs(total.magnitude - 1.5) < 0.01  # 1.5 kVA total


class TestCompoundUnits:
    """Test compound units work with new units."""
    
    def test_flow_rate_compound(self):
        """Test flow rate as compound unit."""
        volume = Quantity(1, 'm3')
        time = Quantity(1, 'hour')
        flow = volume / time
        
        # Should be able to convert to standard flow units
        m3h = flow.to('m3_h')
        assert abs(m3h.magnitude - 1.0) < 0.01
    
    def test_pressure_compound(self):
        """Test pressure as compound unit."""
        force = Quantity(1000, 'newton')
        area = Quantity(1, 'm2')
        pressure = force / area
        
        # Should be able to convert to pressure units
        kpa = pressure.to('kilopascal')
        assert abs(kpa.magnitude - 1.0) < 0.01
    
    def test_concentration_compound(self):
        """Test concentration as compound unit."""
        mass = Quantity(100, 'milligram')
        volume = Quantity(1, 'liter')
        conc = mass / volume
        
        # Should be able to convert to concentration units
        mg_l = conc.to('mg_l')
        assert abs(mg_l.magnitude - 100) < 0.01
