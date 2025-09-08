from generate_dimension_attribute_mixin import generate_dimension_attribute_mixin
from attributes import Acabado, Grampa, Marco, Sentido, HojaActiva
from pathlib import Path

height_mixin = generate_dimension_attribute_mixin('ALTO_PL', 500, 2400, 50, 50)
acabado_mixin = Acabado.to_attribute_config_mixin(display_type='radio')
marco_mixin = Marco.to_attribute_config_mixin(display_type='radio')
grampa_mixin = Grampa.to_attribute_config_mixin(display_type='radio')
sentido_mixin = Sentido.to_attribute_config_mixin(display_type='radio')
hoja_activa_mixin = HojaActiva.to_attribute_config_mixin(display_type='radio')

width_mixin_puerta_simple = generate_dimension_attribute_mixin('ANCHO_PL', 500, 1100, 50, 100)
width_mixin_hoja_activa_puerta_doble = generate_dimension_attribute_mixin('ANCHO_PL_HOJA_ACTIVA', 300, 1100, 50, 100)
width_mixin_hoja_pasiva_puerta_doble = generate_dimension_attribute_mixin('ANCHO_PL_HOJA_PASIVA', 300, 1100, 50, 100)

attributes_puerta_simple = [width_mixin_puerta_simple, height_mixin, acabado_mixin, marco_mixin, grampa_mixin, sentido_mixin]
attributes_puerta_doble = [width_mixin_hoja_activa_puerta_doble, width_mixin_hoja_pasiva_puerta_doble, height_mixin, acabado_mixin, marco_mixin, grampa_mixin, hoja_activa_mixin]

product_template_rf_30_plus_simple = {
    'id': 'product_template_rf_30_plus_simple',
    'name': 'PUERTA RF30 PLUS SIMPLE',
    'description': 'PUERTA RF30 PLUS SIMPLE',
    'attributes': attributes_puerta_simple,
    'dynamic_price_code': Path('./dynamic_price_scripts/dynamic_price_code_puerta_simple.py').read_text()
}

product_template_rf_60_lite_simple = {
    'id': 'product_template_rf_60_lite_simple',
    'name': 'PUERTA RF60 LITE SIMPLE',
    'description': 'PUERTA RF60 LITE SIMPLE',
    'attributes': attributes_puerta_simple,
    'dynamic_price_code': Path('./dynamic_price_scripts/dynamic_price_code_puerta_simple.py').read_text()
}

product_template_rf_60_plus_simple = {
    'id': 'product_template_rf_60_plus_simple',
    'name': 'PUERTA RF60 PLUS SIMPLE',
    'description': 'PUERTA RF60 PLUS SIMPLE',
    'attributes': attributes_puerta_simple,
    'dynamic_price_code': Path('./dynamic_price_scripts/dynamic_price_code_puerta_simple.py').read_text()
}

product_template_rf_60_plus_doble = {
    'id': 'product_template_rf_60_plus_doble',
    'name': 'PUERTA RF60 PLUS DOBLE',
    'description': 'PUERTA RF60 PLUS DOBLE',
    'attributes': attributes_puerta_doble,
    'dynamic_price_code': Path('./dynamic_price_scripts/dynamic_price_code_puerta_doble.py').read_text()
}

product_template_rf_90_plus_simple = {
    'id': 'product_template_rf_90_plus_simple',
    'name': 'PUERTA RF90 PLUS SIMPLE',
    'description': 'PUERTA RF90 PLUS SIMPLE',
    'attributes': attributes_puerta_simple,
    'dynamic_price_code': Path('./dynamic_price_scripts/dynamic_price_code_puerta_simple.py').read_text()
}

product_template_rf_90_plus_doble = {
    'id': 'product_template_rf_90_plus_doble',
    'name': 'PUERTA RF90 PLUS DOBLE',
    'description': 'PUERTA RF90 PLUS DOBLE',
    'attributes': attributes_puerta_doble,
    'dynamic_price_code': Path('./dynamic_price_scripts/dynamic_price_code_puerta_doble.py').read_text()
}

product_template_rf_120_plus_simple = {
    'id': 'product_template_rf_120_plus_simple',
    'name': 'PUERTA RF120 PLUS SIMPLE',
    'description': 'PUERTA RF90 PLUS SIMPLE',
    'attributes': attributes_puerta_simple,
    'dynamic_price_code': Path('./dynamic_price_scripts/dynamic_price_code_puerta_simple.py').read_text()
}

product_template_rf120_plus_doble = {
    'id': 'product_template_rf_120_plus_doble',
    'name': 'PUERTA RF120 PLUS DOBLE',
    'description': 'PUERTA RF120 PLUS DOBLE',
    'attributes': attributes_puerta_doble,
    'dynamic_price_code': Path('./dynamic_price_scripts/dynamic_price_code_puerta_doble.py').read_text(),
}

width_mixin_puerta_simple_euro = generate_dimension_attribute_mixin('ANCHO_PL', 900, 1000, 100, 100)
attributes_puerta_simple_euro = [width_mixin_puerta_simple, height_mixin, acabado_mixin, marco_mixin, grampa_mixin, sentido_mixin, price_mutiplier_mixin_puerta_simple_height]

product_template_rf_30_euro_simple = {
   'id': 'product_template_rf_30_euro_simple',
    'name': 'PUERTA RF30 EURO SIMPLE',
    'description': 'PUERTA RF30 EURO SIMPLE',
    'attributes': attributes_puerta_simple_euro,
    'dynamic_price_code': Path('./dynamic_price_scripts/dynamic_price_code_puerta_simple.py').read_text()
}

product_template_rf_60_euro_simple = {
   'id': 'product_template_rf_60_euro_simple',
    'name': 'PUERTA RF60 EURO SIMPLE',
    'description': 'PUERTA RF60 EURO SIMPLE',
    'attributes': attributes_puerta_simple_euro,
    'dynamic_price_code': Path('./dynamic_price_scripts/dynamic_price_code_puerta_simple.py').read_text()
}

product_template_rf_90_euro_simple = {
   'id': 'product_template_rf_90_euro_simple',
    'name': 'PUERTA RF90 EURO SIMPLE',
    'description': 'PUERTA RF90 EURO SIMPLE',
    'attributes': attributes_puerta_simple_euro,
    'dynamic_price_code': Path('./dynamic_price_scripts/dynamic_price_code_puerta_simple.py').read_text() 
}

product_template_rf_120_euro_simple = {
   'id': 'product_template_rf_120_euro_simple',
    'name': 'PUERTA RF120 EURO SIMPLE',
    'description': 'PUERTA RF120 EURO SIMPLE',
    'attributes': attributes_puerta_simple_euro,
    'dynamic_price_code': Path('./dynamic_price_scripts/dynamic_price_code_puerta_simple.py').read_text()
}