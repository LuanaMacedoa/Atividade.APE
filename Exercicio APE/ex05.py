aprovados = int(input('Digite o número de alunos aprovados: '))
reprovados = int(input('Digite o número de alunos reprovados: '))
total = aprovados + reprovados
porcentagem = aprovados / total * 100
print(f'A porcetagem de alunos aprovados foi de: {porcentagem:.1f}%')