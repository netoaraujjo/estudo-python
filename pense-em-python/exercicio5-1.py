import time

tempo = time.time()

seg_por_dia = 24 * 60 * 60
seg_por_hora = 60 * 60

dias = int(tempo // seg_por_dia)

tempo = tempo % seg_por_dia

horas = int(tempo // seg_por_hora)

tempo = tempo % seg_por_hora

minutos = int(tempo // 60)

segundos = int(tempo % 60)

print(f'{dias} dias {horas} horas {minutos} minutos {segundos} segundos')