tempo_dia_seg = 6*60*60 + 52*60 #representação em segundos da hora de partida

tempo_deslocamento_seg = (8*60+15) + (3 * (7*60+12)) + (8*60+15) #tempo de deslocamento em segundos

tempo_total_dia = tempo_dia_seg + tempo_deslocamento_seg #Total de segundos decorridos no dia

horas_dia = tempo_total_dia//(60 * 60)

min_dia = tempo_total_dia%(60*60)//60

seg_dia = tempo_total_dia%(60*60)%60

print(f'Hora de chegada: {horas_dia}:{min_dia}:{seg_dia}')