# Vamos definir o número de jogadas
jogadas = 0
tentativas_erradas = []  # Inicializa a lista de tentativas erradas

# Definir uma lista de palavras que vão ser escolhidas
palavras_facil = 'codigo'
palavras_medio = 'programa'
palavras_dificil = 'desenvolvimento'
palavras = [palavras_facil, palavras_medio, palavras_dificil]

# O usuário vai escolher a dificuldade do jogo
dificuldade = input('Qual a dificuldade do jogo? (facil, medio, dificil): ').lower()

# Definir a função para escolher a palavra com base na dificuldade
def escolha_da_dificuldade():
    if dificuldade == 'facil' or dificuldade == 'fácil': #minimizando os erros 
        return palavras_facil
    elif dificuldade == 'medio' or dificuldade == 'médio' or dificuldade == 'média': #minimizando os erros
        return palavras_medio
    elif dificuldade == 'dificil' or dificuldade == 'difícil': #minimizando os erros
        return palavras_dificil
    else:
        print('Escolha uma dificuldade válida')
        return None #dando um retorno para finalizar a função

# Resultado da escolha da dificuldade
palavra_secreta = escolha_da_dificuldade()

if palavra_secreta:
    def partida():
        letras_que_faltam = ['_'] * len(palavra_secreta)
        max_jogadas = 16  # Número máximo de jogadas incorretas
        global jogadas  # Declarar que vamos modificar a variável global `jogadas`

        while jogadas < max_jogadas and '_' in letras_que_faltam:
            print(' '.join(letras_que_faltam))
            letra = input('Qual letra você deseja chutar? ').lower()

            if letra in palavra_secreta: #procurando a letra na palavra secreta
                for i in range(len(palavra_secreta)): #se a letra estiver na palavra, substitui a letra que falta
                    if palavra_secreta[i] == letra: #comparaando a letra da palavra com a letra que o jogador chutou
                        letras_que_faltam[i] = letra #fazendo a substitução
            else:
                jogadas += 1
                tentativas_erradas.append(letra) #adicionando a letra errada na lista de tentativas erradas
                tentativas_restantes = max_jogadas - jogadas #calculando as tentativas restantes
                print(f'Você perdeu uma jogada! Tentativas restantes: {tentativas_restantes}. Letras usadas: {", ".join(tentativas_erradas)}')

            if '_' not in letras_que_faltam: #condição para ganhar o jogo
                print(f"Parabéns! Você acertou a palavra: {palavra_secreta}")
                break
        else:
            if jogadas >= max_jogadas:
                print(f"Você perdeu! A palavra era: {palavra_secreta}")

    if __name__ == "__main__": #chamando a função partida
        partida()
else:
    print("Erro ao selecionar a palavra. Certifique-se de que escolheu uma dificuldade válida.") # caso a dificuldade escolhida não seja válida
