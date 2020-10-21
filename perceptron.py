pesos = [0.1, 0.3]
bias = -0.5
entradas = [
    [1,1],
    [1,0],
    [0,0]
]
saidas = [1,1,1,0]
geracoes = 10
modo_debbug = True
taxa_aprendizagem = 0.5

def somatoria(entrada):
    s = bias
    for i,sinal in enumerate(entrada):
        s = s + (sinal * pesos[i])

    if modo_debbug:
        print("\n Somatório = ", s)

    return s

def funcaoAtivacao(v):
    return 1.0 if v >= 0.0 else 0.0


def atualizarPesos(erro, entrada):
    for indice, valor in enumerate(entrada):
        variação_peso = taxa_aprendizagem * erro * valor
        pesos[indice] += variação_peso
        print(variação_peso)


def learnig():
    entrada_atual = 0

    for gen in range(geracoes):
        if modo_debbug:
            print("\n \n Geração = ", gen)
        valor = neuronio(entradas[entrada_atual])
        erro =  saidas[entrada_atual] - valor
        if modo_debbug:
            print("\n \n Erro = ", erro)
        if erro != 0:
            atualizarPesos(erro, entradas[entrada_atual])
            if modo_debbug:
                print("\n \n Atualizar pesos = ", pesos)

        if entrada_atual < len(entradas)-1:        
            entrada_atual +=1
        else:
            entrada_atual = 0

def neuronio(entrada):
    return funcaoAtivacao(somatoria(entrada))

def teste():
    x = int(input("entre os valor 1 : "))
    y = int(input("entre os valor 2 : "))
    print("Resultado : ", neuronio([x,y]))


if __name__ == '__main__':
    learnig()
    while True:
        teste()

