import random

src = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ 1234567890!@#$%¨&*()-=_+"
objetivo = "Hello World!"

def gerarPalavra():
    palavra = "".join(random.sample(src, len(objetivo)))
    return palavra

def trocarLetra(palavra):
    pos = random.randrange(len(objetivo))
    letra = random.sample(src, 2)
    if(letra[0] == palavra[pos]):
        palavra = palavra[:pos] + letra[1] + palavra[pos + 1:]
    else:
        palavra = palavra[:pos] + letra[0] + palavra[pos + 1:]
    return palavra

def compararPalavras(palavra):
    cont = 0
    for c in range(len(palavra)):
        if(palavra[c] == objetivo[c]):
            cont += 1
    return cont

palavra = gerarPalavra()
atual = compararPalavras(palavra)
numPassos = 1
print("Palavra atual: ", palavra, " | Alcance: (", atual,"/", len(objetivo),") | Passos dados: ", numPassos, "     \t(  + 0  \t)")
ultima = numPassos
while compararPalavras(palavra) < len(objetivo):
    novaPalavra = trocarLetra(palavra)
    numPassos += 1
    if (compararPalavras(novaPalavra) > atual):
        palavra = novaPalavra
        atual = compararPalavras(palavra)
        print("Palavra atual: ", palavra, " | Alcance: (", atual,"/", len(objetivo),") | Passos dados: ", numPassos,"   \t(  +",numPassos - ultima," \t)")
        ultima = numPassos

