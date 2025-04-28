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

