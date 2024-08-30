medias = []
print("Digite as 5 médias:")
for i in range(5):
    media = float(input(f"Média do aluno {i+1}: "))
    medias.append(media)
media_turma = sum(medias) / len(medias)
alunos_abaixo_media = sum(1 for media in medias if media < media_turma)
print(f"{alunos_abaixo_media} aluno(s) estão abaixo da média.")
