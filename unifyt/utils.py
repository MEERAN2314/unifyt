"""Utility functions for Unifyt."""

from typing import Union, List, Tuple
import numpy as np
from unifyt.quantity import Quantity
from unifyt.unit import Unit


def linspace(start: Quantity, stop: Quantity, num: int = 50) -> Quantity:
    """
    Create evenly spaced quantities over a specified interval.
    
    Args:
        start: Starting quantity
        stop: Ending quantity (will be converted to start's units)
        num: Number of samples
        
    Returns:
        Quantity with array of evenly spaced values
        
    Examples:
        >>> temps = linspace(Quantity(0, 'celsius'), Quantity(100, 'celsius'), 11)
    """
    stop_converted = stop.to(start.unit)
    values = np.linspace(start.magnitude, stop_converted.magnitude, num)
    return Quantity(values, start.unit)


def arange(start: Quantity, stop: Quantity, step: Quantity) -> Quantity:
    """
    Create quantities with evenly spaced values within a given interval.
    
    Args:
        start: Starting quantity
        stop: Ending quantity
        step: Step size
        
    Returns:
        Quantity with array of values
        
    Examples:
        >>> distances = arange(Quantity(0, 'meter'), Quantity(100, 'meter'), 
        ...                    Quantity(10, 'meter'))
    """
    stop_converted = stop.to(start.unit)
    step_converted = step.to(start.unit)
    values = np.arange(start.magnitude, stop_converted.magnitude, step_converted.magnitude)
    return Quantity(values, start.unit)


def zeros(shape: Union[int, Tuple[int, ...]], unit: Union[str, Unit]) -> Quantity:
    """
    Create a quantity array of zeros.
    
    Args:
        shape: Shape of the array
        unit: Unit for the quantity
        
    Returns:
        Quantity with zeros
        
    Examples:
        >>> z = zeros(10, 'meter')
        >>> z2d = zeros((3, 4), 'kilogram')
    """
    return Quantity(np.zeros(shape), unit)


def ones(shape: Union[int, Tuple[int, ...]], unit: Union[str, Unit]) -> Quantity:
    """
    Create a quantity array of ones.
    
    Args:
        shape: Shape of the array
        unit: Unit for the quantity
        
    Returns:
        Quantity with ones
        
    Examples:
        >>> o = ones(5, 'second')
    """
    return Quantity(np.ones(shape), unit)


def full(shape: Union[int, Tuple[int, ...]], fill_value: Quantity) -> Quantity:
    """
    Create a quantity array filled with a specific value.
    
    Args:
        shape: Shape of the array
        fill_value: Quantity to fill with
        
    Returns:
        Quantity filled with the value
        
    Examples:
        >>> f = full(10, Quantity(5, 'meter'))
    """
    arr = np.full(shape, fill_value.magnitude)
    return Quantity(arr, fill_value.unit)


def concatenate(quantities: List[Quantity], axis: int = 0) -> Quantity:
    """
    Concatenate quantities along an axis.
    
    Args:
        quantities: List of quantities to concatenate
        axis: Axis along which to concatenate
        
    Returns:
        Concatenated quantity
        
    Examples:
        >>> q1 = Quantity(np.array([1, 2]), 'meter')
        >>> q2 = Quantity(np.array([3, 4]), 'meter')
        >>> result = concatenate([q1, q2])
    """
    if not quantities:
        raise ValueError("Need at least one quantity to concatenate")
    
    # Convert all to first quantity's units
    base_unit = quantities[0].unit
    arrays = [q.to(base_unit).value for q in quantities]
    result = np.concatenate(arrays, axis=axis)
    return Quantity(result, base_unit)


def stack(quantities: List[Quantity], axis: int = 0) -> Quantity:
    """
    Stack quantities along a new axis.
    
    Args:
        quantities: List of quantities to stack
        axis: Axis along which to stack
        
    Returns:
        Stacked quantity
        
    Examples:
        >>> q1 = Quantity(np.array([1, 2]), 'meter')
        >>> q2 = Quantity(np.array([3, 4]), 'meter')
        >>> result = stack([q1, q2])
    """
    if not quantities:
        raise ValueError("Need at least one quantity to stack")
    
    base_unit = quantities[0].unit
    arrays = [q.to(base_unit).value for q in quantities]
    result = np.stack(arrays, axis=axis)
    return Quantity(result, base_unit)


def sum(quantity: Quantity, axis: int = None) -> Quantity:
    """
    Sum of quantity elements.
    
    Args:
        quantity: Input quantity
        axis: Axis along which to sum
        
    Returns:
        Sum as a quantity
        
    Examples:
        >>> q = Quantity(np.array([1, 2, 3, 4]), 'meter')
        >>> total = sum(q)
    """
    result = np.sum(quantity.value, axis=axis)
    return Quantity(result, quantity.unit)


def mean(quantity: Quantity, axis: int = None) -> Quantity:
    """
    Mean of quantity elements.
    
    Args:
        quantity: Input quantity
        axis: Axis along which to compute mean
        
    Returns:
        Mean as a quantity
        
    Examples:
        >>> q = Quantity(np.array([1, 2, 3, 4]), 'meter')
        >>> avg = mean(q)
    """
    result = np.mean(quantity.value, axis=axis)
    return Quantity(result, quantity.unit)


def std(quantity: Quantity, axis: int = None) -> Quantity:
    """
    Standard deviation of quantity elements.
    
    Args:
        quantity: Input quantity
        axis: Axis along which to compute std
        
    Returns:
        Standard deviation as a quantity
        
    Examples:
        >>> q = Quantity(np.array([1, 2, 3, 4]), 'meter')
        >>> s = std(q)
    """
    result = np.std(quantity.value, axis=axis)
    return Quantity(result, quantity.unit)


def min(quantity: Quantity, axis: int = None) -> Quantity:
    """
    Minimum of quantity elements.
    
    Args:
        quantity: Input quantity
        axis: Axis along which to find minimum
        
    Returns:
        Minimum as a quantity
    """
    result = np.min(quantity.value, axis=axis)
    return Quantity(result, quantity.unit)


def max(quantity: Quantity, axis: int = None) -> Quantity:
    """
    Maximum of quantity elements.
    
    Args:
        quantity: Input quantity
        axis: Axis along which to find maximum
        
    Returns:
        Maximum as a quantity
    """
    result = np.max(quantity.value, axis=axis)
    return Quantity(result, quantity.unit)


def sqrt(quantity: Quantity) -> Quantity:
    """
    Square root of a quantity.
    
    Args:
        quantity: Input quantity
        
    Returns:
        Square root as a quantity
        
    Examples:
        >>> area = Quantity(25, 'meter^2')
        >>> side = sqrt(area)
    """
    return quantity ** 0.5


def clip(quantity: Quantity, min_val: Quantity, max_val: Quantity) -> Quantity:
    """
    Clip quantity values to a range.
    
    Args:
        quantity: Input quantity
        min_val: Minimum value
        max_val: Maximum value
        
    Returns:
        Clipped quantity
        
    Examples:
        >>> q = Quantity(np.array([1, 5, 10]), 'meter')
        >>> clipped = clip(q, Quantity(2, 'meter'), Quantity(8, 'meter'))
    """
    min_converted = min_val.to(quantity.unit).magnitude
    max_converted = max_val.to(quantity.unit).magnitude
    result = np.clip(quantity.value, min_converted, max_converted)
    return Quantity(result, quantity.unit)


def isclose(q1: Quantity, q2: Quantity, rtol: float = 1e-5, atol: float = 1e-8) -> bool:
    """
    Check if two quantities are close in value.
    
    Args:
        q1: First quantity
        q2: Second quantity
        rtol: Relative tolerance
        atol: Absolute tolerance
        
    Returns:
        True if quantities are close
        
    Examples:
        >>> q1 = Quantity(1.0, 'meter')
        >>> q2 = Quantity(1.0000001, 'meter')
        >>> isclose(q1, q2)
    """
    if not q1.unit.is_compatible_with(q2.unit):
        return False
    q2_converted = q2.to(q1.unit)
    return np.allclose(q1.value, q2_converted.value, rtol=rtol, atol=atol)


def allclose(q1: Quantity, q2: Quantity, rtol: float = 1e-5, atol: float = 1e-8) -> bool:
    """
    Alias for isclose - check if two quantities are close in value.
    
    Args:
        q1: First quantity
        q2: Second quantity
        rtol: Relative tolerance
        atol: Absolute tolerance
        
    Returns:
        True if quantities are close
    """
    return isclose(q1, q2, rtol, atol)


def logspace(start: Quantity, stop: Quantity, num: int = 50, base: float = 10.0) -> Quantity:
    """
    Create quantities with logarithmically spaced values.
    
    Args:
        start: Starting quantity
        stop: Ending quantity (will be converted to start's units)
        num: Number of samples
        base: Base of the logarithm
        
    Returns:
        Quantity with array of logarithmically spaced values
        
    Examples:
        >>> distances = logspace(Quantity(1, 'meter'), Quantity(1000, 'meter'), 5)
    """
    stop_converted = stop.to(start.unit)
    
    # Calculate log values
    start_log = np.log(start.magnitude) / np.log(base)
    stop_log = np.log(stop_converted.magnitude) / np.log(base)
    
    # Create logspace
    log_values = np.linspace(start_log, stop_log, num)
    values = base ** log_values
    
    return Quantity(values, start.unit)


def where(condition: np.ndarray, x: Quantity, y: Quantity) -> Quantity:
    """
    Return elements chosen from x or y depending on condition.
    
    Args:
        condition: Boolean array condition
        x: Quantity to choose from where condition is True
        y: Quantity to choose from where condition is False
        
    Returns:
        Quantity with selected values
        
    Examples:
        >>> temps = Quantity(np.array([10, 25, 35]), 'celsius')
        >>> condition = temps.value > 20
        >>> result = where(condition, temps, Quantity(20, 'celsius'))
    """
    # Convert y to x's units if needed
    if not x.unit.is_compatible_with(y.unit):
        raise ValueError(f"Incompatible units: {x.unit} and {y.unit}")
    
    y_converted = y.to(x.unit)
    result_values = np.where(condition, x.value, y_converted.value)
    return Quantity(result_values, x.unit)


def convert_wire_gauge_to_diameter(gauge: int, gauge_type: str = 'awg') -> Quantity:
    """
    Convert wire gauge number to diameter.
    
    Args:
        gauge: Wire gauge number
        gauge_type: Type of gauge ('awg', 'swg', 'bwg')
        
    Returns:
        Wire diameter as Quantity
        
    Examples:
        >>> diameter = convert_wire_gauge_to_diameter(12, 'awg')
        >>> print(diameter.to('millimeter'))
    """
    gauge_type = gauge_type.lower()
    
    if gauge_type == 'awg':
        # AWG formula: diameter = 0.005 * 92^((36-n)/39) inches
        diameter_inches = 0.005 * (92 ** ((36 - gauge) / 39))
        return Quantity(diameter_inches * 0.0254, 'meter')  # Convert to meters
    elif gauge_type == 'swg':
        # SWG uses lookup table - simplified formula
        diameter_inches = 0.3 * (0.89 ** gauge)
        return Quantity(diameter_inches * 0.0254, 'meter')
    elif gauge_type == 'bwg':
        # BWG uses lookup table - simplified formula  
        diameter_inches = 0.34 * (0.89 ** gauge)
        return Quantity(diameter_inches * 0.0254, 'meter')
    else:
        raise ValueError(f"Unknown gauge type: {gauge_type}")


def convert_pressure_gauge_to_absolute(gauge_pressure: Quantity, 
                                     atmospheric_pressure: Quantity = None) -> Quantity:
    """
    Convert gauge pressure to absolute pressure.
    
    Args:
        gauge_pressure: Gauge pressure reading
        atmospheric_pressure: Local atmospheric pressure (default: 1 atm)
        
    Returns:
        Absolute pressure as Quantity
        
    Examples:
        >>> gauge = Quantity(2, 'bar_gauge')
        >>> absolute = convert_pressure_gauge_to_absolute(gauge)
        >>> print(absolute.to('bar'))  # ~3.01 bar
    """
    if atmospheric_pressure is None:
        atmospheric_pressure = Quantity(101325, 'pascal')  # 1 atm
    
    # Convert both to same units
    atm_converted = atmospheric_pressure.to(gauge_pressure.unit)
    return gauge_pressure + atm_converted


def convert_ph_to_concentration(ph_value: float) -> Quantity:
    """
    Convert pH value to hydrogen ion concentration.
    
    Args:
        ph_value: pH value (dimensionless)
        
    Returns:
        H+ concentration in mol/L
        
    Examples:
        >>> conc = convert_ph_to_concentration(7.0)  # Neutral water
        >>> print(conc)  # 1e-7 mol/L
    """
    concentration = 10 ** (-ph_value)
    return Quantity(concentration, 'molar')


def convert_concentration_to_ph(concentration: Quantity) -> float:
    """
    Convert hydrogen ion concentration to pH value.
    
    Args:
        concentration: H+ concentration
        
    Returns:
        pH value (dimensionless)
        
    Examples:
        >>> ph = convert_concentration_to_ph(Quantity(1e-7, 'molar'))
        >>> print(ph)  # 7.0
    """
    conc_molar = concentration.to('molar').magnitude
    return -np.log10(conc_molar)


def convert_decibel_to_ratio(db_value: float) -> float:
    """
    Convert decibel value to linear ratio.
    
    Args:
        db_value: Value in decibels
        
    Returns:
        Linear ratio (dimensionless)
        
    Examples:
        >>> ratio = convert_decibel_to_ratio(20)  # 20 dB
        >>> print(ratio)  # 100 (voltage ratio)
    """
    return 10 ** (db_value / 20)  # For voltage/current ratios


def convert_ratio_to_decibel(ratio: float) -> float:
    """
    Convert linear ratio to decibel value.
    
    Args:
        ratio: Linear ratio
        
    Returns:
        Value in decibels
        
    Examples:
        >>> db = convert_ratio_to_decibel(100)
        >>> print(db)  # 40.0 dB (power ratio)
    """
    return 20 * np.log10(ratio)  # For voltage/current ratios
