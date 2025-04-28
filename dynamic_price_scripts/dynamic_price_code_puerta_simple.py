price_multiplier_puerta_simple_width = {
    '600': 0.1,
    '650': 0.1,
    '700': 0.1,
    '750': 0.1,
    '800': 0,
    '850': 0.1,
    '900': 0,
    '950': 0.1,
    '1000': 0,
    '1050': 0.1,
    '1100': 0
}
price_multiplier_puerta_simple_height = {
    '1850': 0.1,
    '1900': 0.1,
    '1950': 0.1,
    '2000': 0,
    '2050': 0.1,
    '2100': 0,
    '2150': 0.1,
    '2200': 0.1,
    '2250': 0.1,
    '2300': 0.1,
    '2350': 0.2,
    '2400': 0.2
}

ancho_pl_mm = attributes['ANCHO_PL'].value_on_create
alto_pl_mm = attributes['ALTO_PL'].value_on_create

ancho_pl_mm_as_str = str(int(ancho_pl_mm))
alto_pl_mm_as_str = str(int(alto_pl_mm))

current_door_multiplier_width = price_multiplier_puerta_simple_width[ancho_pl_mm_as_str]
current_door_multiplier_height = price_multiplier_puerta_simple_height[alto_pl_mm_as_str]

ancho_pl_mts = ancho_pl_mm / 1000
alto_pl_mts = alto_pl_mm / 1000

superficie_mts = ancho_pl_mts * alto_pl_mts
precio_m2 = template.list_price


if not 'HERRAJES' in attributes:
    variant.list_price = superficie_mts * (precio_m2 * (1 + current_door_multiplier_width + current_door_multiplier_height))
else:
    print('todo herrajes as attributes, enable multi select in attributes')
    # todo: implement multiselect field attribute type
