"""
Unifyt - A powerful library for unit conversion and calculations.

Combines the best features of Pint and Unyt for intuitive and high-performance
unit handling in Python.
"""

from unifyt.quantity import Quantity
from unifyt.unit import Unit
from unifyt.unit_registry import UnitRegistry
from unifyt.dimensions import Dimension
from unifyt.context import UnitContext
from unifyt import constants
from unifyt import utils

# Import serialization if available
try:
    from unifyt.serialization import (
        quantity_to_dict,
        dict_to_quantity,
        quantity_to_json,
        json_to_quantity,
        save_quantity,
        load_quantity,
        QuantityEncoder,
        quantity_decoder,
    )
    _HAS_SERIALIZATION = True
except ImportError:
    _HAS_SERIALIZATION = False

from unifyt.exceptions import (
    # Base exception
    UnifytException,
    
    # Unit errors
    UnitError,
    DimensionalityError,
    UnitNotFoundError,
    UnitParseError,
    ConversionError,
    
    # Quantity errors
    QuantityError,
    InvalidValueError,
    OperationError,
    ComparisonError,
    ArrayError,
    QuantityOverflowError,
    
    # Registry errors
    RegistryError,
    UnitDefinitionError,
    UnitAlreadyExistsError,
    UnitSystemError,
    
    # Serialization errors
    SerializationError,
    SerializationFormatError,
    DeserializationError,
    SerializationVersionError,
    
    # Context errors
    ContextError,
    InvalidUnitSystemError,
    ContextStateError,
    
    # Other errors
    ConstantError,
    UtilityError,
    ValidationError,
    PrecisionError,
    ConfigurationError,
    
    # Utilities
    ErrorContext,
    create_exception,
)

__version__ = "0.3.0"

# Build __all__ dynamically based on what's available
__all__ = [
    # Core classes
    "Quantity",
    "Unit",
    "UnitRegistry",
    "Dimension",
    "UnitContext",
    
    # Modules
    "constants",
    "utils",
    
    # Exceptions - Base
    "UnifytException",
    
    # Exceptions - Unit errors
    "UnitError",
    "DimensionalityError",
    "UnitNotFoundError",
    "UnitParseError",
    "ConversionError",
    
    # Exceptions - Quantity errors
    "QuantityError",
    "InvalidValueError",
    "OperationError",
    "ComparisonError",
    "ArrayError",
    "QuantityOverflowError",
    
    # Exceptions - Registry errors
    "RegistryError",
    "UnitDefinitionError",
    "UnitAlreadyExistsError",
    "UnitSystemError",
    
    # Exceptions - Serialization errors
    "SerializationError",
    "SerializationFormatError",
    "DeserializationError",
    "SerializationVersionError",
    
    # Exceptions - Context errors
    "ContextError",
    "InvalidUnitSystemError",
    "ContextStateError",
    
    # Exceptions - Other
    "ConstantError",
    "UtilityError",
    "ValidationError",
    "PrecisionError",
    "ConfigurationError",
    
    # Exception utilities
    "ErrorContext",
    "create_exception",
]

# Add serialization to __all__ if available
if _HAS_SERIALIZATION:
    __all__.extend([
        "quantity_to_dict",
        "dict_to_quantity",
        "quantity_to_json",
        "json_to_quantity",
        "save_quantity",
        "load_quantity",
        "QuantityEncoder",
        "quantity_decoder",
    ])

# Create default unit registry
default_registry = UnitRegistry()
