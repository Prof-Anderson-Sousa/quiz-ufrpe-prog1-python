# Imports de Bibliotecas Necessárias para o Projeto
import csv
from fileinput import filename
import time
import os

# Contador de Pontos que Vai ser Utilizado de Forma Global
pontos = 0
# Apresentação do Quiz + Solicitação do Nome do Usuário
name = input("Olá Seja Bem Vindo ao Quiz UFRPE\nQual o Seu Nome?: ")
nivel = ""
# Função com Menu de Possibilidades do Quiz
def start():
    os.system("cls")
    print('''
  ------------------------------------------------------------
  =-=-=-=-=-=-=-=-=-=-=-=-=-M-E-N-U-=-=-=-=-=-=-=-=-=-=-=-=-=-
  [1] - Quiz Nível Fácil
  [2] - Quiz Nível Médio
  [3] - Quiz Nível Difícil
  [4] - Adicionar Questões
  [5] - Remover Questões
  [6] - Sair do Quiz...
  ------------------------------------------------------------
  ''')
    time.sleep(2)
    option1()

# Após a Escolha Acima Entrará em uma das Opções Abaixo
def option1():
    option = int(input("Digite a opção desejada: "))
    # Start Nível Fácil
    if option == 1:
        print("Ótima Escolha!")
        print("Carregando Quiz....")
        time.sleep(3)
        os.system("cls")
        facil()

    # Start Nível Médio
    elif option == 2:
        print("Boa Sorte!")
        time.sleep(1)
        print("Carregando Quiz....")
        time.sleep(3)
        os.system("cls")
        mediana()
    
    # Start Nível Difícil
    elif option == 3:
        print("Confiança é a Chave do Sucesso!")
        time.sleep(1)
        print("Carregando Quiz....")
        time.sleep(3)
        os.system("cls")
        dificil()

    # Start Add Questões
    elif option == 4:
        os.system("cls")
        addQuestions()

    # Start Remove Questões
    elif option == 5:
        os.system("cls")
        removeQuestion()

    # Finish Programa
    elif option == 6:
        os.system("cls")
        print("Obrigado, Até a Próxima!")

    # Digite uma Opção Válida
    else:
        print("Digite uma Opção Válida!")
        time.sleep(2)
        option1()

# Função Para as Questões Fáceis
def facil():
    # definindo a pontuação inicial
    global pontos
    pontos = 0
    global nivel
    nivel = "fácil"
    os.system("cls")
    # abrindo e lendo o arquivo csv. Além disso definimos o utf-8 para que seja permitido acentuação
    csvfile = open('perguntas_faceis.csv', 'r', encoding='utf-8')
    lines = csv.reader(csvfile, delimiter=',')
    # printando e formatando a saída das questões e alternativas para o usuário.
    for q in lines:
        question = q[0]
        print('''
        {}
        '''.format(question))
        posible_answers = (q[1], q[2], q[3], q[4],)
        time.sleep(2)
        print('''
        {} 
        {}
        {}
        {}
        '''.format(posible_answers[0], posible_answers[1], posible_answers[2], posible_answers[3]))
        # neste caso como adicionamos a pergunta no formato de lista, o item na posição 5 é a letra que define a resposta correta 
        answer = q[5]
        user_answer = input("Digite a letra da Opção Desejada: ").upper()
        time.sleep(2)
        print("Gabarito: ", answer)
        # aqui fazemos a comparação da resposta do usuário com a resposta correr=ta
        if user_answer == answer:
            print("Resposta Correta!")
            time.sleep(2)
            # somando pontos ao pontos no caso de acerto
            pontos = pontos + 1
            print("Sua pontuação é - ", pontos)
            print("Próxima....")
            time.sleep(3)
            os.system("cls")

        else:
            print("Resposta Incorreta")
            time.sleep(2)
            print("Sua pontuação é - ", pontos)
            time.sleep(2)
            print("Vamos você consegue!")
            time.sleep(2)
            print("Próxima....")
            time.sleep(3)
            os.system("cls")
    print("Fim das perguntas")
    time.sleep(2)
    # se a quantidade de acertos for menor que 4 enviamos uma mensagem positiva 
    if pontos <= 4:
        print("Ihh, Na Próxima você melhora")
        time.sleep(2)
        print("Sua pontuação foi baixa")
        addRanking()
        time.sleep(2)
        # desponibilizando a opção de o usuário jogar novamente este ou qualquer outro nivel
        option = input("Você quer jogar mais uma vez?\nA) Sim  -  B) Não: ").lower()
        if option == "a":
            print("Escolha entre os níveis\n2) Médio ou 3) Difícil: ")
            option1()
        elif option == "b":
            print("Ok")
            time.sleep(2)
            print("Até a Próxima")
            print("")
    # se a quantidade de acertos for maior que 4 enviamos uma mensagem positiva e deixamos disponivel a opção de jogar novamente 
    elif pontos > 4:
        print("Uau! Você é bom nisso")
        addRanking()
        time.sleep(2)
        print("Você pode jogar mais uma vez :)")
        option3 = input(
            "Escolha entre os níveis\nA) Médio ou B) Difícil. Se você não quer continuar jogando escreva 'n': ").lower()
        if option3 == "a":
            mediana()

        elif option3 == "b":
            dificil()

        elif option3 == "n":
            time.sleep(2)
            print("Até a Próxima")
            print("")
            # Os comentários de questões de nível fácil, mediana e díficil seriam os mesmos, por isso finalizarei aqui.

# Função Para as Questões Medianas
def mediana():
    global pontos
    pontos = 0
    global nivel
    nivel = "médio"
    os.system("cls")

    csvfile = open('perguntas_medianas.csv', 'r',  encoding='utf-8')
    lines = csv.reader(csvfile, delimiter=',')

    for q in lines:
        question = q[0]
        print('''
        {}
        '''.format(question))
        posible_answers = (q[1], q[2], q[3], q[4],)
        time.sleep(2)
        print('''
        {} 
        {}
        {}
        {}
        '''.format(posible_answers[0], posible_answers[1], posible_answers[2], posible_answers[3]))
        answer = q[5]
        user_answer = input("Digite a letra da Opção Desejada: ").upper()
        time.sleep(2)
        print("Gabarito: ", answer)
        if user_answer == answer:
            print("Resposra Correta!")
            time.sleep(2)
            pontos = pontos + 1
            print("Sua pontuação é - ", pontos)
            print("Próxima....")
            time.sleep(3)
            os.system("cls")

        else:
            print("Resposta Incorreta")
            time.sleep(2)
            print("Sua pontuação é - ", pontos)
            time.sleep(2)
            print("Vamos você consegue!")
            time.sleep(2)
            print("Próxima....")
            time.sleep(3)
            os.system("cls")
    print("Fim das perguntas")
    time.sleep(2)

    if pontos <= 4:
        print("Ihh, Na Próxima você melhora")
        time.sleep(2)
        print("Sua pontuação foi baixa")
        time.sleep(2)
        print("Você conseguiu apenas",pontos,"pontos")
        addRanking()
        time.sleep(2)

        option = input(
            "Você quer jogar mais uma vez?\nA) Sim  -  B) Não: ").lower()
        if option == "a":
            print("Escolha entre os níveis\n1) Fácil ou 3) Difícil: ")
            option1()

        elif option == "b":
            print("Ok")
            time.sleep(2)
            print("Até a Próxima")
            print("")

    elif pontos > 4:
        print("Uau! Você é bom nisso")
        time.sleep(2)
        print("Você acertou", pontos, "questões.")
        addRanking()
        time.sleep(2)
        print("Você pode jogar mais uma vez :)")
        option3 = input(
            "Você pode escolher entre os níveis\nA) Fácil ou B) Difícil. Se você não quer continuar jogando escreva 'n': ").lower()
        if option3 == "a":
            facil()

        elif option3 == "b":
            dificil()

        elif option3 == "n":
            time.sleep(2)
            print("Até a Próxima")
            print("")

# Função Para as Questões Difíceis
def dificil():
    global pontos
    pontos = 0
    global nivel
    nivel = "difícil"

    csvfile = open('perguntas_dificeis.csv', 'r', encoding='utf-8')

    lines = csv.reader(csvfile, delimiter=',')
    for q in lines:
        question = q[0]
        print('''
        {}
        '''.format(question))
        posible_answers = (q[1], q[2], q[3], q[4],)
        time.sleep(2)
        print('''
        {} 
        {}
        {}
        {}
        '''.format(posible_answers[0], posible_answers[1], posible_answers[2], posible_answers[3]))
        answer = q[5]
        user_answer = input("Digite a letra da Opção Desejada: ").upper()
        time.sleep(2)
        print("Gabarito: ", answer)
        if user_answer == answer:
            print("Resposra Correta!")
            time.sleep(2)
            pontos = pontos + 1
            print("Sua pontuação é - ", pontos)
            print("Próxima....")
            time.sleep(3)
            os.system("cls")

        else:
            print("Resposta Incorreta")
            time.sleep(2)
            print("Sua pontuação é - ", pontos)
            time.sleep(2)
            print("Vamos você consegue!")
            time.sleep(2)
            print("Próxima....")
            time.sleep(3)
            os.system("cls")

    print("Fim das perguntas")
    time.sleep(2)

    if pontos <= 4:
        print("Vocêprecisa estudar um pouco mais :(")
        time.sleep(2)
        print("Sua pontuação foi baixa")
        time.sleep(2)
        print("Você conseguiu apenas",pontos,"pontos")
        addRanking()
        time.sleep(2)

        option = input(
            "Você quer jogar mais uma vez?\nA) Sim  -  B) Não: ").lower()
        if option == "a":
            print("Escolha entre os níveis\n1) Fácil ou 2) Médio: ")
            option1()

        elif option == "b":
            print("Ok")
            time.sleep(2)
            print("Até a Próxima")
            print("")

    elif pontos > 4:
        print("Uau! Você é bom nisso")
        addRanking()
        time.sleep(2)
        print("Você acertou", pontos, "questões.")
        time.sleep(2)
        print("Você pode jogar mais uma vez :)")
        option3 = input(
            "Você pode escolher entre nível A) Fácil ou B)Médio. Se você não quer continuar jogando escreva 'n'").lower()
        if option3 == "a":
            facil()

        elif option3 == "b":
            mediana()

        elif option3 == "n":
            time.sleep(2)
            print("Até a Próxima")
            print("")

# Função para Adicionar Questões
def addQuestions(): 
    os.system("cls")
    question_level_add = int(input('''Você gostaria de adicionar questões de que nível?
    Digite:
    1- Fácil
    2- Médio
    3- Difícil
    4- Voltar ao menu '''))
    # Abrindo e Dando Permissão Para Adicionar Questões
    if question_level_add == 1:
        csvfile = open('perguntas_faceis.csv', 'a', newline="")
    elif question_level_add == 2:
        csvfile = open('prguntas_medianas.csv', 'a', newline="")
    elif question_level_add == 3:
        csvfile = open('perguntas_dificeis.csv', 'a', newline="")
    elif question_level_add == 4:
        option1()
    else:
        print("Escolha uma opção de adicionar válida.")
        addQuestions()
    # Questões e Alternativa Correta, Salva em Variáveis e Adicionadas em Arquivo .CSV
    question = input("Escreva aqui sua pergunta: ")
    answer1 = input('''Escreva aqui a primeira opção de alternativa:
    Ex.: A)Programação
    ''')
    answer2 = input('''Escreva aqui a segunda opção de alternativa:
    Ex.: B)Livros
    ''')
    answer3 = input('''Escreva aqui a terceira opção de alternativa:
    Ex.: C)Sapatos
    ''')
    answer4 = input('''Escreva aqui a quarta opção de alternativa:
    Ex.: D)Brinquedos
    ''')
    correctAnswer = input('''Agora escreva a letra da alternativa correta:
    Ex.: A
    ''')
    # Adicionando Todos Valores a Variável
    questions_and_answers = (question, answer1, answer2, answer3, answer4, correctAnswer)
    # Habilitando Escrita em Arquivos 
    writer = csv.writer(csvfile)
    # Comando Para Escrever em Nova Linha
    writer.writerow(questions_and_answers)
    print("Questão registrada. Obrigada!")
    csvfile.close()
    start()

# Função Para Remover Questões
def removeQuestion():
    os.system("cls")
    # Escolha do Nível de Remoção das Questões
    question_file = int(input('''De qual destes quiz você gostaria de remover a pergunta?
    Digite:
    1- Fácil
    2- Médio
    3- Difícil
    4- Voltar ao menu
    '''))
    # função especifica de deletar que tem seus parâmetros modificados a partir da escolha do usuário
    def delete_line(filename, line_number):
      # abrindo e lendo todo o arquivo 
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        # verificando se o valor que o usuário está depositando é válido para a quantidade de perguntas existentes no arquivo
        if (line_number <= len(lines)):
          # comando para deletar linha
            del lines[line_number - 1]
            with open(filename, "w") as file:
                for line in lines:
                    file.write(line)

        else:
            print("Essa linha", line_number, "não existe no arquivo.")
            print("Este arquivo tem", len(lines), "linhas.")
  # Apartir daqui as condicionais partem da decisão do usuário modificando os valores dos parâmetros e mostrando para o usuário todas as perguntas existentes
  # no arquivo para que ele escolha pelo número qual deseja deletar.
    if question_file == 1:
        delete_filename = 'perguntas_faceis.csv'
        archive = open(delete_filename)
        questions = csv.reader(archive)
        for question in questions:
            print('''{}
      '''.format(question))
        delete_line_number = int(
            input("Qual dessas questões deseja remover? Escreva o número a partir de 1."))
        delete_line(delete_filename, delete_line_number)
        option1()
    elif question_file == 2:
        delete_filename = 'perguntas_medianas.csv'
        archive = open(delete_filename)
        questions = csv.reader(archive)
        for question in questions:
            print('''{}
      '''.format(question))
        delete_line_number = int(
            input("Qual dessas questões deseja remover? Escreva o número a partir de 1."))
        delete_line(delete_filename, delete_line_number)
        option1()
    elif question_file == 3:
        delete_filename = 'perguntas_dificeis.csv'
        archive = open(delete_filename)
        questions = csv.reader(archive)
        for question in questions:
            print('''{}
      '''.format(question))
        delete_line_number = int(
            input("Qual dessas questões deseja remover? Escreva o número a partir de 1."))
        delete_line(delete_filename, delete_line_number)
        option1()
    elif question_file == 4:
        option1()
    else:
        print("Digite uma opção válida.")
        removeQuestion()

def addRanking():
    os.system("cls")
    resp = "Jogador",name,"Fez",pontos,"Pontos no Nível",nivel
    csvfile = open('ranking.csv', 'a', encoding='utf-8', newline="")
    writer = csv.writer(csvfile)
    writer.writerow(resp)
    print("Pontuação Registrada no Ranking!")
    csvfile.close()

start()