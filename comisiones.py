# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona

# lista de vendedores
VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]

ANCHO_SEPARADOR = 44
UMBRAL_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BAJA = 0.05
UMBRAL_BONO = 50000
MONTO_BONO = 500

def calcular_comisiones():
    total_pagado = 0
    print("=" * ANCHO_SEPARADOR)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_SEPARADOR)
    # recorre la lista
    for vendedor in VENDEDORES:
        # si vendio mas de 30000
        if vendedor[1] > UMBRAL_COMISION_ALTA:
            # calcula la comision del 8%
            comision = vendedor[1] * TASA_COMISION_ALTA
            comision = round(comision, 2)
            # el bono es de 300
            if vendedor[1] > UMBRAL_BONO:
                bono = MONTO_BONO
            else:
                bono = 0
            total_vendedor = round(comision + bono, 2)
            total_pagado = total_pagado + total_vendedor
            print(vendedor[0] + ": Q " + str(total_vendedor))
        else:
            # calcula la comision del 5%
            comision = vendedor[1] * TASA_COMISION_BAJA
            comision = round(comision, 2)
            bono = 0
            total_vendedor = round(comision + bono, 2)
            total_pagado = total_pagado + total_vendedor
            print(vendedor[0] + ": Q " + str(total_vendedor))
    # ta = tp * 1.12
    # print("con iva", ta)
    print("-" * ANCHO_SEPARADOR)
    print("Total a pagar: Q " + str(round(total_pagado, 2)))

calcular_comisiones()
