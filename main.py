# notas = [67, 90, 42, 69]

# media = sum(notas) / len(notas)

# print(media)

# if media >= 60:
#     print("Aprovado")
# else: 
#     print("Passou nao paizao")

alunos = [
    {'nome' : 'Yasmin', 'notas' : [6, 5], 'idade' : 16, 'frequencia' : 300},
    {'nome' : 'Bruno', 'notas' : [6, 9], 'idade' : 16, 'frequencia' : 220}
]

def calcular_media(soma, qtde):
    return soma / qtde


def status_aprovacao(nota):
    if nota >= 6:
        return 'aprovado'
    return 'reprovado'

def faltas(frequencia):
    if frequencia >= 225:
        return 'Sem problemas'
    return 'Reprovado por faltas'
    
for aluno in alunos:
    qtde_notas = len(aluno['notas'])
    soma = sum(aluno['notas'])

    nota = calcular_media(soma, qtde_notas)
    print(f'Aluno: {aluno['nome']}, Nota: {nota}, Status: {status_aprovacao(nota)}, Frequencia: {faltas(aluno['frequencia'])}')


    # if nota >= 6:
    #     print('Status: Aprovado')
    # else:
    #     print('Status: Reprovado')
