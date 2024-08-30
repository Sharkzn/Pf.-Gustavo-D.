Artistas = [
    "Travis scott",
    "Neymar Jr",
    "Cristiano Ronaldo",
    "Messi",
    "Bruno Mars",
    "Taylor Swift",
    "Ed.Sheeran",
    "Vini Jr",
    "Bellinghan",
    "Will Smith"
]
artista_cancelado = 'Messi'
novo_artista = 'Rodrygo'
indice_cancelado = Artistas.index(artista_cancelado)
Artistas.pop(indice_cancelado)
Artistas.insert(indice_cancelado, novo_artista)
print("Agenda Atualizada:")
Artistas.sort()
Artistas.append("Rodrygo")
y = 1
print(y)
for x in Artistas:
    print(y,"-",x)
    y = y + 2