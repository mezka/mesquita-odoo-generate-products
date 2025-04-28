price_muiltiplier_puerta_doble_width = {
    '600': 0.2,
    '700': 0.2,
    '800': 0.2,
    '900': 0.2,
    '1000': 0.2,
    '1100': 0.2,
    '1150': 0.2,
    '1200': 0,
    '1250': 0.1,
    '1300': 0,
    '1350': 0.1,
    '1400': 0,
    '1450': 0.1,
    '1500': 0,
    '1550': 0.1,
    '1600': 0,
    '1650': 0.1,
    '1700': 0,
    '1750': 0.1,
    '1800': 0,
    '1850': 0.1,
    '1900': 0,
    '1950': 0.1,
    '2000': 0,
    '2050': 0.1,
    '2100': 0.1,
    '2150': 0.1,
    '2200': 0.1
}

price_multiplier_puerta_doble_height = {
    '1850': 0.15,
    '1900': 0.15,
    '1950': 0.15,
    '2000': 0,
    '2050': 0.2,
    '2100': 0.2,
    '2150': 0.2,
    '2200': 0.2,
    '2250': 0.2,
    '2300': 0.3,
    '2350': 0.3,
    '2400': 0.5
}

ancho_pl_hoja_activa_mm = attributes['ANCHO_PL_HOJA_ACTIVA'].value_on_create
ancho_pl_hoja_pasiva_mm = attributes['ANCHO_PL_HOJA_PASIVA'].value_on_create

ancho_pl_mm = ancho_pl_hoja_activa_mm + ancho_pl_hoja_pasiva_mm
alto_pl_mm = attributes['ALTO_PL'].value_on_create

ancho_pl_mm_as_str = str(int(ancho_pl_mm))
alto_pl_mm_as_str = str(int(alto_pl_mm))

current_door_multiplier_width = price_muiltiplier_puerta_doble_width[ancho_pl_mm_as_str]
current_door_multiplier_height = price_multiplier_puerta_doble_height[alto_pl_mm_as_str]

ancho_pl_mts = ancho_pl_mm / 1000
alto_pl_mts = alto_pl_mm / 1000

superficie_mts = ancho_pl_mts * alto_pl_mts
precio_m2 = template.list_price

if not 'HERRAJES' in attributes:
    variant.list_price = superficie_mts * (precio_m2 * (1 + current_door_multiplier_width + current_door_multiplier_height))
else:
    print('todo herrajes as attributes, enable multi select in attributes')
    # todo: implement multiselect field attribute type
