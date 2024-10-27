total_aulas = int(input('Digite o número de aulas totais: '))
falta = int(input('Digite o número de faltas: '))
aulas_assistidas = total_aulas - falta
resultado = (aulas_assistidas / total_aulas) * 100
print(f'A frquencia é: {resultado:.2f}')