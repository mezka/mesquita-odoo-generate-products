from generate_dimension_attribute_mixin import generate_dimension_attribute_mixin
from attributes import Acabado, Grampa, Marco, Sentido

height_mixin = generate_dimension_attribute_mixin('ALTO_PL', 500, 2400, 50, 50)
acabado_mixin = Acabado.to_attribute_config_mixin(display_type='radio')
marco_mixin = Marco.to_attribute_config_mixin(display_type='radio')
grampa_mixin = Grampa.to_attribute_config_mixin(display_type='radio')
sentido_mixin = Sentido.to_attribute_config_mixin(display_type='radio')

width_mixin_puerta_simple = generate_dimension_attribute_mixin('ANCHO_PL', 500, 1100, 50, 100)

product_template_rf30_lite_simple = {
    'id': 'product_template_rf_30_lite_simple',
    'name': 'PUERTA RF30 LITE SIMPLE',
    'description': 'PUERTA RF30 LITE SIMPLE',
    'attributes': [width_mixin_puerta_simple, height_mixin, acabado_mixin, marco_mixin, grampa_mixin, sentido_mixin]
}

width_mixin_hoja_activa_puerta_doble = generate_dimension_attribute_mixin('ANCHO_PL_HOJA_ACTIVA', 500, 1100, 50, 100)
width_mixin_hoja_pasiva_puerta_doble = generate_dimension_attribute_mixin('ANCHO_PL_HOJA_PASIVA', 500, 1100, 50, 100)

product_template_rf30_lite_doble = {
    'id': 'product_template_rf_30_lite_doble',
    'name': 'PUERTA RF30 LITE DOBLE',
    'description': 'PUERTA RF30 LITE DOBLE',
    'attributes': [width_mixin_hoja_activa_puerta_doble, width_mixin_hoja_pasiva_puerta_doble, height_mixin, acabado_mixin, marco_mixin, grampa_mixin, sentido_mixin]
}