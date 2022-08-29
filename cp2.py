#!/usr/bin/python3
'''
Leonardo Dalantonia Poloni RM95523 
Checkpoint 02 do Semestre 02 - FIAP 
GPL3.0-or-foward
Version 1.0

Body Health Software
Decision Tree Algorithm to predict how healthy a person will be in thirty years.
'''
from sklearn import tree
import platform
import subprocess
import time
try:
   import pyfiglet 
except:
    pass


def clearTerminal():
    OS = platform.system()
    if OS == "Windows":
        subprocess.call("cls", shell=True) 
    else: 
        subprocess.call("clear", shell=True)


def userInput():
    exercicios, sono, sol, alimentacao, falimentacao = int(),int(),int(),int(),int()
    print("__"*38)
    try:
       ascii_header = pyfiglet.figlet_format("BODY HEALTH")
       print(f'{ascii_header}\n')
    except:
        pass 
    print("[!] Bem vindo ao Body Health! Um projeto de Machine Learning com algoritmo de Árvore de Decisões")
    time.sleep(1.5)
    print("[*] Responda às perguntas da triagem utilizando os números indicados para cada opção e diremos se está no caminho certo para uma boa saúde com o passar das décadas")
    time.sleep(1.5)
    print("__"*38,'\n')
    
    while exercicios not in [1,2,3]:
        exercicios = int(input("[?] Com qual frequência você se exercicita ?\n\n[1] Pelo menos 5 vezes por semana.\n[2] Pelo menos 3 vezes por semana\n[3] No máximo 2 vezes por semana.\nResposta: "))
        print("__"*38)
        time.sleep(1.5)

    while sono not in [1,2,3]:
        sono = int(input("[?] Quantas horas por dia, em média, você dorme?\n\n[1] No mínimo 7h\n[2] No máximo 6 horas\n[3] Em média 4 horas\nResposta: "))
        print("__"*38)
        time.sleep(1.5)

    while sol not in [1,2,3,4]:
        print("Tomar tanto muito quanto pouco sol são prejudiciais à saúde. Quanto a isso:")
        sol = int(input("[?] Fazendo a média da semana, quantos minutos por dia de sol você toma?\n\n[1] Cerca de 20 minutos ao dia\n[2] Cerca de 12-15 minutos\n[3] No máximo 8 minutos\n[4] Cerca de 30 minutos ao dia\nResultado: ")) 
        print("__"*38)
        time.sleep(1.5)

    while alimentacao not in [1,2,3]:
        alimentacao = int(input("[?] Com que frequência você come alimentos saudáveis como carnes brancas, verduras e frutas?\n\n[1] No mínimo 6 vezes por semana\n[2] No máximo 3-4 vezes por semana\n[3] Menos que 3 vezes por semana\nResposta: "))
        print("__"*38) 
        time.sleep(1.5)  
    
    while falimentacao not in [1,2,3,4]:
        falimentacao = int(input("[?] Quantas refeições principais você faz por dia?\n\n[1] 3-4 ao dia\n[2] 2 ao dia\n[3] 1-0 ao dia\n[4] Mais de 5 ao dia\nResultado: "))
        print("__"*38)
        time.sleep(1.5)

    return (exercicios, sono, sol, alimentacao, falimentacao)

def alimentacaoTree(sol,alimentacao,falimentacao):
    '''
    (1: BOA | 2: MEDIO | 3: RUIM) para todos elementos 
    Alimentação         -> (BOA, OK, RUIM)
    Alimentação é classificada através de 3 features:
    1- Frequência de Alimentação Boa, como verduras e frutas
    2- Refeições Principais por dia 
    3- Quantia de Sol tomada por dia
    Apesar de algumas perguntas terem 4 opções, só há 3 classificadores para cada uma delas. Logo:
    Possibilidade de combinações entre as 3 respostas : 3.3.3 = 27 respostas úteis possíveis 
    Cada uma das respostas terá uma classificação própria.

    SOL/DIA|   QUALIDADE ALIM | FREQUENCIA ALIMENTACAO| RESULTADO (1:Bom,2:medio,3:ruim)
    ['SOL BOM', 'ALIM BOA', 'FALIM BOA']                     1
    ['SOL BOM', 'ALIM BOA', 'FALIM MEDIA']                   1
    ['SOL BOM', 'ALIM BOA', 'FALIM RUIM']                    2
    ['SOL BOM', 'ALIM MEDIA', 'FALIM BOA']                   1
    ['SOL BOM', 'ALIM MEDIA', 'FALIM MEDIA']                 1
    ['SOL BOM', 'ALIM MEDIA', 'FALIM RUIM']                  2
    ['SOL BOM', 'ALIM RUIM', 'FALIM BOA']                    2
    ['SOL BOM', 'ALIM RUIM', 'FALIM MEDIA']                  3
    ['SOL BOM', 'ALIM RUIM', 'FALIM RUIM']                   3
    ['SOL MEDIO', 'ALIM BOA', 'FALIM BOA']                   1
    ['SOL MEDIO', 'ALIM BOA', 'FALIM MEDIA']                 1
    ['SOL MEDIO', 'ALIM BOA', 'FALIM RUIM']                  2
    ['SOL MEDIO', 'ALIM MEDIA', 'FALIM BOA']                 1
    ['SOL MEDIO', 'ALIM MEDIA', 'FALIM MEDIA']               2
    ['SOL MEDIO', 'ALIM MEDIA', 'FALIM RUIM']                2
    ['SOL MEDIO', 'ALIM RUIM', 'FALIM BOA']                  2
    ['SOL MEDIO', 'ALIM RUIM', 'FALIM MEDIA']                3
    ['SOL MEDIO', 'ALIM RUIM', 'FALIM RUIM']                 3
    ['SOL RUIM', 'ALIM BOA', 'FALIM BOA']                    2
    ['SOL RUIM', 'ALIM BOA', 'FALIM MEDIA']                  2
    ['SOL RUIM', 'ALIM BOA', 'FALIM RUIM']                   2
    ['SOL RUIM', 'ALIM MEDIA', 'FALIM BOA']                  2
    ['SOL RUIM', 'ALIM MEDIA', 'FALIM MEDIA']                2
    ['SOL RUIM', 'ALIM MEDIA', 'FALIM RUIM']                 3
    ['SOL RUIM', 'ALIM RUIM', 'FALIM BOA']                   3
    ['SOL RUIM', 'ALIM RUIM', 'FALIM MEDIA']                 3
    ['SOL RUIM', 'ALIM RUIM', 'FALIM RUIM']                  3
    '''

    if sol == 4:   # sol exagerado faz tanto mal quanto sol escasso
        sol = 3

    if falimentacao == 4:  # alimentacao exagerada é tao ruim quanto alimentacao escassa
        falimentacao = 3

    habitos = [
    [1, 1, 1],
    [1, 1, 2],
    [1, 1, 3],
    [1, 2, 1],
    [1, 2, 2],
    [1, 2, 3],
    [1, 3, 1],
    [1, 3, 2],
    [1, 3, 3],
    [2, 1, 1],
    [2, 1, 2],
    [2, 1, 3],
    [2, 2, 1],
    [2, 2, 2],
    [2, 2, 3],
    [2, 3, 1],
    [2, 3, 2],
    [2, 3, 3],
    [3, 1, 1],
    [3, 1, 2],
    [3, 1, 3],
    [3, 2, 1],
    [3, 2, 2],
    [3, 2, 3],
    [3, 3, 1],
    [3, 3, 2],
    [3, 3, 3],
    ]

    resultados = [1,1,2,1,1,2,2,3,3,1,1,2,1,2,2,2,3,3,2,2,2,2,2,3,3,3,3]

    classificador = tree.DecisionTreeClassifier()
    classificador = classificador.fit(habitos, resultados)
    tree_result = classificador.predict( [[sol,alimentacao,falimentacao]] )

    return tree_result[0]

def mainTree(habitos, exercicios, sono):
    '''
    Agora que uma Árvore já decidiu se nossos hábitos gerais (na documentação do CP seria a Alimentação) são bons
    usarei os outros dados inputados pelo usuário: 
    Educação Física     -> (1: BOM, 2: MEDIO, 3:RUIM)
    Qualidade do Sono   -> (1: BOM, 2:MEDIO, 3: RUIM)
    
    Juntando Hábitos Gerais com Educação Física e Qualidade de Sono o software conseguirá dar a previsão final.

    Assim como na Tree anterior, há 3 opções por feature.
    3.3.3 = 27 possibilidades
    
    HABITOS      |     EXERCICIOS            |  SONO                       RESULTADO(1:bom até 5:morte iminente)
    ['HABITOS BONS', 'BOM TEMPO EXERCICITANDO', 'BOM TEMPO DE SONO']           1
    ['HABITOS BONS', 'BOM TEMPO EXERCICITANDO', 'TEMPO DE SONO OKAY']          1
    ['HABITOS BONS', 'BOM TEMPO EXERCICITANDO', 'TEMPO DE SONO RUIM']          3
    ['HABITOS BONS', 'EXERCICIO MEDIANO', 'BOM TEMPO DE SONO']                 1 
    ['HABITOS BONS', 'EXERCICIO MEDIANO', 'TEMPO DE SONO OKAY']                2
    ['HABITOS BONS', 'EXERCICIO MEDIANO', 'TEMPO DE SONO RUIM']                3
    ['HABITOS BONS', 'SEDENTARISMO', 'BOM TEMPO DE SONO']                      2 
    ['HABITOS BONS', 'SEDENTARISMO', 'TEMPO DE SONO OKAY']                     3
    ['HABITOS BONS', 'SEDENTARISMO', 'TEMPO DE SONO RUIM']                     4
    ['HABITOS MEDIANOS', 'BOM TEMPO EXERCICITANDO', 'BOM TEMPO DE SONO']       1
    ['HABITOS MEDIANOS', 'BOM TEMPO EXERCICITANDO', 'TEMPO DE SONO OKAY']      2 
    ['HABITOS MEDIANOS', 'BOM TEMPO EXERCICITANDO', 'TEMPO DE SONO RUIM']      4
    ['HABITOS MEDIANOS', 'EXERCICIO MEDIANO', 'BOM TEMPO DE SONO']             2
    ['HABITOS MEDIANOS', 'EXERCICIO MEDIANO', 'TEMPO DE SONO OKAY']            3
    ['HABITOS MEDIANOS', 'EXERCICIO MEDIANO', 'TEMPO DE SONO RUIM']            4
    ['HABITOS MEDIANOS', 'SEDENTARISMO', 'BOM TEMPO DE SONO']                  2
    ['HABITOS MEDIANOS', 'SEDENTARISMO', 'TEMPO DE SONO OKAY']                 3
    ['HABITOS MEDIANOS', 'SEDENTARISMO', 'TEMPO DE SONO RUIM']                 4
    ['HABITOS RUINS', 'BOM TEMPO EXERCICITANDO', 'BOM TEMPO DE SONO']          3
    ['HABITOS RUINS', 'BOM TEMPO EXERCICITANDO', 'TEMPO DE SONO OKAY']         3
    ['HABITOS RUINS', 'BOM TEMPO EXERCICITANDO', 'TEMPO DE SONO RUIM']         4
    ['HABITOS RUINS', 'EXERCICIO MEDIANO', 'BOM TEMPO DE SONO']                3
    ['HABITOS RUINS', 'EXERCICIO MEDIANO', 'TEMPO DE SONO OKAY']               4
    ['HABITOS RUINS', 'EXERCICIO MEDIANO', 'TEMPO DE SONO RUIM']               5
    ['HABITOS RUINS', 'SEDENTARISMO', 'BOM TEMPO DE SONO']                     4
    ['HABITOS RUINS', 'SEDENTARISMO', 'TEMPO DE SONO OKAY']                    5
    ['HABITOS RUINS', 'SEDENTARISMO', 'TEMPO DE SONO RUIM']                    5
    '''
    resultados_possiveis={
        "1": "Perfeito, você viverá uma vida longa e saudável se continuar assim",
        "2": "Muito bem, você viverá bem e saudável, mas pode melhorar ainda",
        "3": "Okay, você é saudável, mas não há tantas garantias de um bom envelhecimento, ainda mais se você já for velho",
        "4": "Cuidado, seu estado não é tao ruim, mas você tem coisas sérias pra melhorar",
        "5": "Se você passou dos 30 foi milagre :), MELHORE URGENTEMENTE !"
    }

    triagem = [
    [1, 1, 1],
    [1, 1, 2],
    [1, 1, 3],
    [1, 2, 1],
    [1, 2, 2],
    [1, 2, 3],
    [1, 3, 1],
    [1, 3, 2],
    [1, 3, 3],
    [2, 1, 1],
    [2, 1, 2],
    [2, 1, 3],
    [2, 2, 1],
    [2, 2, 2],
    [2, 2, 3],
    [2, 3, 1],
    [2, 3, 2],
    [2, 3, 3],
    [3, 1, 1],
    [3, 1, 2],
    [3, 1, 3],
    [3, 2, 1],
    [3, 2, 2],
    [3, 2, 3],
    [3, 3, 1],
    [3, 3, 2],
    [3, 3, 3],
    ]

    resultados = [1,1,3,1,2,3,2,3,4,1,2,4,2,3,4,2,3,4,3,3,4,3,4,5,4,5,5]

    classificador = tree.DecisionTreeClassifier()
    classificador = classificador.fit(triagem, resultados)

    diagnostico = classificador.predict( [[habitos, exercicios, sono]] )[0]
    
    print("__"*38)
    try:
       print(pyfiglet.figlet_format("RESULTADOS"))
    except:
        pass
    print("[!] Seu diagnóstico foi feito !\n")
    time.sleep(2)
    print(f"[*]{resultados_possiveis[str(diagnostico)]}")


if __name__=="__main__": 
    while True:
       clearTerminal()
       exercicios, sono, sol, alimentacao, falimentacao = userInput()

       habitos = alimentacaoTree(sol,alimentacao,falimentacao)
       mainTree(habitos,exercicios,sono)
       time.sleep(1)
       
       userexit = str()
       while userexit not in ["s","n"]:
          userexit = str(input("\n[] Deseja sair ou refazer (s/n) ?  "))
       
       if userexit == "n":
          continue

       break









