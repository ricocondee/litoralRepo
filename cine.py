#Andrus Correa Web A
def calcular_costo_boletas(info):
    tipo_sala = info['tipo_sala']
    num_boletas = info['num_boletas']
    hora = info['hora']
    medio_pago = info['medio_pago']
    reserva = info['reserva']
    
    if tipo_sala == 'Dinamix':
        tarifa_basica = 18800
    elif tipo_sala == '3D':
        tarifa_basica = 15500
    elif tipo_sala == '2D':
        tarifa_basica = 11300
    else:
        print('Tipo de sala no válido')
        return None
   
    if hora not in ['pico1', 'pico2']:
        descuento_hora_no_pico = 0.1 * tarifa_basica
        if num_boletas >= 3:
            descuento_varias_boletas = 500 * (num_boletas - 3)
            descuento_total = descuento_hora_no_pico + descuento_varias_boletas
        else:
            descuento_total = descuento_hora_no_pico
    else:
        descuento_total = 0
        
    if medio_pago == 'tarjeta':
        descuento_tarjeta = 0.05 * tarifa_basica
    else:
        descuento_tarjeta = 0
       
    if reserva:
        recargo_reserva = 2000 * num_boletas
    else:
        recargo_reserva = 0
        
    if hora == 'pico1':
        if tipo_sala == '2D' or tipo_sala == '3D':
            aumento_hora_pico = 0.25 * tarifa_basica
        else:
            aumento_hora_pico = 0.5 * tarifa_basica
    else:
        aumento_hora_pico = 0
    
    costo_total = (tarifa_basica - descuento_total - descuento_tarjeta + aumento_hora_pico
                   + recargo_reserva) * num_boletas
    
    return costo_total

info = {'tipo_sala': '2D',
        'num_boletas': 3,
        'hora': 'pico1',
        'medio_pago': 'tarjeta',
        'reserva': False}

costo_total = calcular_costo_boletas(info)
print(f'El costo total de las boletas es: {costo_total} pesos')
