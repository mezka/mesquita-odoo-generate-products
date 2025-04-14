from enum import Enum
from typing import Dict

class EnumToOdooProductAttributeMixin(Enum):
    @classmethod
    def get_snake_case_class_name(cls) -> str:
        return ''.join('_' + c if c.isupper() else c for c in cls.__name__).lstrip('_').upper()

    @classmethod
    def to_attribute_config_mixin(cls, *, display_type: str) -> Dict:
        attribute_name = cls.get_snake_case_class_name()
        return {
            'product_attribute_name': attribute_name,
            'product_attribute_values': [
                {
                    'id': f'product_attribute_value_{attribute_name.lower()}_{class_property.name.lower()}',
                    'name': class_property.value,
                    'attribute_id/id': f'product_attribute_{attribute_name.lower()}',
                    'is_custom': 'FALSE',
                    'sequence': index,
                }
                for index, class_property in enumerate(cls)
            ],
            'product_attribute_display_type': display_type,
        }

class EnumToOdooProductAttributeMixinForPriceMultipliers(Enum):
    @classmethod
    def get_snake_case_class_name(cls) -> str:
        return ''.join('_' + c if c.isupper() else c for c in cls.__name__).lstrip('_').upper()

    @classmethod
    def to_attribute_config_mixin(cls) -> Dict:
        attribute_name = cls.get_snake_case_class_name()
        return {
            'product_attribute_name': attribute_name,
            'product_attribute_values': [
                {
                    'id': f'product_attribute_value_{attribute_name.lower()}_{class_property.name.lower()}',
                    'name': class_property.name,
                    'attribute_id/id': f'product_attribute_{attribute_name.lower()}',
                    'is_custom': 'FALSE',
                    'sequence': index,
                    'value_on_create': float(class_property.value)
                }
                for index, class_property in enumerate(cls)
            ],
            'product_attribute_display_type': 'select',
            'active': 'FALSE'
        }


class Sentido(EnumToOdooProductAttributeMixin):
    IZQUIERDA = 'IZQUIERDA'
    DERECHA = 'DERECHA'

class HojaActiva(EnumToOdooProductAttributeMixin):
    ACTIVA_IZQUIERDA = 'ACTIVA_IZQUIERDA'
    ACTIVA_DERECHA = 'ACTIVA_DERECHA'

class Marco(EnumToOdooProductAttributeMixin):
    INT_100_EXT_130 = 'INT_100_EXT_130'
    INT_120_EXT_150 = 'INT_120_EXT_150'
    INT_140_EXT_170 = 'INT_140_EXT_170'
class Grampa(EnumToOdooProductAttributeMixin):
    DURLOCK = 'DURLOCK'
    MAMPOSTERIA = 'MAMPOSTERIA'

class Acabado(EnumToOdooProductAttributeMixin):
    SIN_PINTAR = 'SIN_PINTAR'
    IMPRESION_GRIS = 'IMPRESION_GRIS'
    IMPRESION_BLANCA = 'IMPRESION_BLANCA'
    IMPRESION_ROJA = 'IMPRESION_ROJA'

class PriceMultiplierPuertaSimpleWidth(EnumToOdooProductAttributeMixinForPriceMultipliers):
    PL600 = 0.1
    PL650 = 0.1
    PL700 = 0.1
    PL750 = 0.1
    PL800 = 0
    PL850 = 0.1
    PL900 = 0
    PL950 = 0.1
    PL1000 = 0
    PL1050 = 0.1
    PL1100 = 0

class PriceMultiplierPuertaSimpleHeight(EnumToOdooProductAttributeMixinForPriceMultipliers):
    PL1850 = 0.1
    PL1900 = 0.1
    PL1950 = 0.1
    PL2000 = 0
    PL2050 = 0.1
    PL2100 = 0
    PL2150 = 0.1
    PL2200 = 0.1
    PL2250 = 0.1
    PL2300 = 0.1
    PL2350 = 0.2
    PL2400 = 0.2

class PriceMultiplierPuertaDobleWidth(EnumToOdooProductAttributeMixinForPriceMultipliers):
    PL1200 = 0
    PL1250 = 0.1
    PL1300 = 0
    PL1350 = 0.1
    PL1400 = 0
    PL1450 = 0.1
    PL1500 = 0
    PL1550 = 0.1
    PL1600 = 0
    PL1650 = 0.1
    PL1700 = 0
    PL1750 = 0.1
    PL1800 = 0
    PL1850 = 0.1
    PL1900 = 0
    PL1950 = 0.1
    PL2000 = 0
    PL2050 = 0.1
    PL2100 = 0
    PL2150 = 0.1
    PL2200 = 0
class PriceMultiplierPuertaDobleHeight(EnumToOdooProductAttributeMixinForPriceMultipliers):
    PL1850 = 0.15
    PL1900 = 0.15
    PL1950 = 0.15
    PL2000 = 0
    PL2050 = 0.15
    PL2100 = 0.2
    PL2150 = 0.2
    PL2200 = 0.2
    PL2250 = 0.2
    PL2300 = 0.3
    PL2350 = 0.3
    PL2400 = 0.5
