def somatóriaNotas(notas):
    for i,nota in notas:
        notas[i] = nota
    return notas

print(somatóriaNotas)

somatóriaNotas([7, 8, 6, 10])