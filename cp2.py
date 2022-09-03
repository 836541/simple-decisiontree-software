#!/usr/bin/python3

from sklearn import tree
import platform
import subprocess
from random import randint 
import time
try:
   import pyfiglet 
except:
    pass


def k(a,b):              # random.randint
     return randint(a,b)

def clearTerminal():
    OS = platform.system()
    if OS == "Windows":
        subprocess.call("cls", shell=True) 
    else: 
        subprocess.call("clear", shell=True)


def userInput():
    exercicios, sono, sol, alimentacao, falimentacao, mode = int(),int(),int(),int(),int(),3
    print("__"*38)
    try:
       ascii_header = pyfiglet.figlet_format("BODY HEALTH")
       print(f'{ascii_header}\n')
    except:
        pass 
    print("[!] Bem vindo ao Body Health! Um projeto de Machine Learning com algoritmo de Árvore de Decisões")
    time.sleep(1.5)
    print("[*] Responda às perguntas da triagem e diremos se está no caminho certo para uma boa saúde com o passar das décadas")
    time.sleep(1.5)
    print("__"*38,'\n')
    
    def sleeprint():
        print("__"*38)
        time.sleep(1.5)
        return 


    while mode not in [0,1]:
        mode = int(input("[!!!] Qual modo você deseja?\n\n[0] Alternativas: Você responderá alternativas, é um método em que todos inputs e outputs foram previstos devido a quantia previsível de alternativas.\n\n[1] Dissertativo: Você digitará os valores exatos e serão comparados a uma database gerada randomicamente para simular um training set real. É a opção mais divertida e mais machine learnesca\nResposta: "))
        sleeprint()

    print("[?] Quantos dias por semana você se exercicita ?\n\n")
    if not mode:
       while exercicios not in [1,2,3]:
           exercicios = int(input("[1] Cerca de 5 vezes por semana.\n[2] Cerca de 3 vezes por semana\n[3] Sou mais sedentário\nResposta: "))
    else:
        exercicios = int(input("Resposta: "))
    sleeprint()
    
    print("[?] Quantas horas por dia, em média, você dorme?\n\n")
    if not mode:
       while sono not in [1,2,3]:
           sono = int(input("[1] No mínimo 7h\n[2] No máximo 6 horas\n[3] Em média 4 horas\nResposta: "))
    else:
        sono = int(input("Resposta: "))
    sleeprint()
    
    print("Tomar tanto muito quanto pouco sol são prejudiciais à saúde. Quanto a isso:")
    print("[?] Fazendo a média da semana, quantos minutos por dia de sol você toma?\n\n")
    if not mode:
       while sol not in [1,2,3,4]:
           sol = int(input("[1] Cerca de 20 minutos ao dia\n[2] Cerca de 12-15 minutos\n[3] No máximo 8 minutos\n[4] Cerca de 30 minutos ao dia\nResultado: ")) 
    else:
        sol=int(input("Resposta: "))
    sleeprint()

    print("[?] Em quantos dias da semana você come alimentos saudáveis de forma minimamente volumosa?\n\n")
    if not mode:
       while alimentacao not in [1,2,3]:
           alimentacao = int(input("[1] No mínimo 6 vezes por semana\n[2] No máximo 3-4 vezes por semana\n[3] Menos que 3 vezes por semana\nResposta: "))
    else: 
        alimentacao = int(input("Resposta: "))
    sleeprint() 
    
    print("[?] Quantas refeições principais você faz por dia?\n\n")
    if not mode:
       while falimentacao not in [1,2,3,4]:
           falimentacao = int(input("[1] 3-4 ao dia\n[2] 2 ao dia\n[3] 1-0 ao dia\n[4] Mais de 5 ao dia\nResultado: "))
    else:
        falimentacao = int(input("Resposta: "))
    sleeprint()

    return (exercicios, sono, sol, alimentacao, falimentacao, mode)

def alimentacaoTree(sol,alimentacao,falimentacao, mode):
    '''
    Alimentação         -> Resultado Final: (BOA, OK, RUIM)
    Alimentação é classificada através de 3 features:
    1- Frequência de Alimentação Boa, como verduras e frutas
    2- Refeições Principais por dia 
    3- Quantia de Sol tomada por dia

    Primeiro quanto ao modo ALTERNATIVAS do software:

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
    Sol Ruim  = 0-8 e 30+           Frequência Alimentar Ruim = 0-1 e 4+      Alimentação ruim = 0-3
    Sol Médio = 8-20                Média = 2                                 Média = 3-4
    Sol Bom = 20-30                 Boa = 3-4                                 Boa   = 5+
    '''
    if not mode:
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
    
    '''
    Agora quanto ao modo DISSERTATIVO do software:
    É gerado uma database aleatória em que certos ranges de números indicam determinados outputs.
    O training set utilizado foi de conjunto de features por resultado possível (BOM, MÉDIO, RUIM)

    Em range de números:
    Sol Ruim  = 0-8 e 30+           Frequência Alimentar Ruim = 0-1 e 4+      Alimentação ruim = 0-3
    Sol Médio = 8-20                Média = 2                                 Média = 3-4
    Sol Bom = 20-30                 Boa = 3-4                                 Boa   = 5+
    
    Database: a função k é uma herdeira de random.randint para gerar números aleatórios.
    Os resultados de classificação (o "Y" dos X) é o mesmo do dataset do modo alternativas, pois esse aqui foi feito baseado nele.
    ['k(20,30)', 'k(5,10)', 'k(3,4)']
    ['k(20,30)', 'k(5,10)', 2]
    ['k(20,30)', 'k(5,10)', 'k(0-1)']
    ['k(20,30)', 'k(3,4)', 'k(3,4)']
    ['k(20,30)', 'k(3,4)', 2]
    ['k(20,30)', 'k(3,4)', 'k(4,9)']
    ['k(20,30)', 'k(0,3)', 'k(3,4)']
    ['k(20,30)', 'k(0,3)', 2]
    ['k(20,30)', 'k(0,3)', 'k(4,8)']
    ['k(8-20)', 'k(5,10)', 'k(3,4)']
    ['k(8-20)', 'k(5,10)', 2]
    ['k(8-20)', 'k(5,10)', 'k(0-1)']
    ['k(8-20)', 'k(3,4)', 'k(3,4)']
    ['k(8-20)', 'k(3,4)', 2]
    ['k(8-20)', 'k(3,4)', 'k(4,12)']
    ['k(8-20)', 'k(0,3)', 'k(3,4)']
    ['k(8-20)', 'k(0,3)', 2]
    ['k(8-20)', 'k(0,3)', 'k(0-1)']
    ['k(0-8)', 'k(5,10)', 'k(3,4)']
    ['k(30,60)', 'k(5,10)', 2]
    ['k(0-8)', 'k(5,10)', 'k(0-1)']
    ['k(0-8)', 'k(3,4)', 'k(3,4)']
    ['k(30,40)', 'k(3,4)', 2]
    ['k(0-8)', 'k(3,4)', 'k(4,8)']
    ['k(30,100)', 'k(0,3)', 'k(3,4)']
    ['k(0-8)', 'k(0,3)', 2]
    ['k(30,40)', 'k(0,3)', 'k(0-1)']
   '''

    if mode: 
        habitos= [
        [k(20,30), k(5,10), k(3,4)],
        [k(20,30), k(5,10), 2],
        [k(20,30), k(5,10), k(0,1)],
        [k(20,30), k(3,4), k(3,4)],
        [k(20,30), k(3,4), 2],
        [k(20,30), k(3,4), k(4,9)],
        [k(20,30), k(0,3), k(3,4)],
        [k(20,30), k(0,3), 2],
        [k(20,30), k(0,3), k(4,8)],
        [k(8,20), k(5,10), k(3,4)],
        [k(8,20), k(5,10), 2],
        [k(8,20), k(5,10), k(0,1)],
        [k(8,20), k(3,4), k(3,4)],
        [k(8,20), k(3,4), 2],
        [k(8,20), k(3,4), k(4,12)],
        [k(8,20), k(0,3), k(3,4)],
        [k(8,20), k(0,3), 2],
        [k(8,20), k(0,3), k(0,1)],
        [k(0,8), k(5,10), k(3,4)],
        [k(30,60), k(5,10), 2],
        [k(0,8), k(5,10), k(0,1)],
        [k(0,8), k(3,4), k(3,4)],
        [k(30,40), k(3,4), 2],
        [k(0,8), k(3,4), k(4,8)],
        [k(30,100), k(0,3), k(3,4)],
        [k(0,8), k(0,3), 2],
        [k(30,40), k(0,3), k(0,1)]
        ]
        


    resultados = [1,1,2,1,1,2,2,3,3,1,1,2,1,2,2,2,3,3,2,2,2,2,2,3,3,3,3]
    classificador = tree.DecisionTreeClassifier()
    classificador = classificador.fit(habitos, resultados)
    tree_result = classificador.predict( [[sol,alimentacao,falimentacao]] )

    return tree_result[0]

def mainTree(habitos, exercicios, sono, mode):
    '''
    Agora que uma Árvore já decidiu se nossos hábitos gerais (na documentação do CP seria a Alimentação) são bons
    usarei os outros dados inputados pelo usuário: 
    - Educação Física     
    - Qualidade do Sono  
    
    Juntando Hábitos Gerais com Educação Física e Qualidade de Sono o software conseguirá dar a previsão final.
    
    Quanto ao modo ALTERNATIVAS do software:
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
        "4": "Cuidado, seu estado está ruim, você tem coisas sérias pra melhorar",
        "5": "Se você passou dos 30 foi milagre :), MELHORE URGENTEMENTE !"
    }
    if not mode:
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
    '''
    Agora quanto ao modo DISSERTATIVO do software:
    Habitos            Ex Bom: 5+         Sono Bom: 7+                      
    1 a 3              Ex Medio: 3-4        
    (funcao anterior)  Ex ruim: <2        Sono Mediano: 5-6                 
                                          Sono Baixo: Menos de 5
    Os outputs para cada conjunto de features desse dataset é o mesmo do acima desse, pois foi baseado em tal. Ou seja, também há 27 conjuntos e 27 respostas.

    [1, 'k(5,10', 'k(7,10)']
    [1, 'k(5,10', 'k(5,6)']
    [1, 'k(5,10', 'k(0,5)']
    [1, 'k(3,4)', 'k(7,10)']
    [1, 'k(3,4)', 'k(5,6)']
    [1, 'k(3,4)', 'k(0,5)']
    [1, 'k(0,2)', 'k(7,10)']
    [1, 'k(0,2)', 'k(5,6)']
    [1, 'k(0,2)', 'k(0,5)']
    [2, 'k(5,10', 'k(7,10)']
    [2, 'k(5,10', 'k(5,6)']
    [2, 'k(5,10', 'k(0,5)']
    [2, 'k(3,4)', 'k(7,10)']
    [2, 'k(3,4)', 'k(5,6)']
    [2, 'k(3,4)', 'k(0,5)']
    [2, 'k(0,2)', 'k(7,10)']
    [2, 'k(0,2)', 'k(5,6)']
    [2, 'k(0,2)', 'k(0,5)']
    [3, 'k(5,10', 'k(7,10)']
    [3, 'k(5,10', 'k(5,6)']
    [3, 'k(5,10', 'k(0,5)']
    [3, 'k(3,4)', 'k(7,10)']
    [3, 'k(3,4)', 'k(5,6)']
    [3, 'k(3,4)', 'k(0,5)']
    [3, 'k(0,2)', 'k(7,10)']
    [3, 'k(0,2)', 'k(5,6)']
    [3, 'k(0,2)', 'k(0,5)']


    '''    
    if mode:
        triagem=[
        [1, k(5,10), k(7,10)],
        [1, k(5,10), k(5,6)],
        [1, k(5,10), k(0,5)],
        [1, k(3,4), k(7,10)],
        [1, k(3,4), k(5,6)],
        [1, k(3,4), k(0,5)],
        [1, k(0,2), k(7,10)],
        [1, k(0,2), k(5,6)],
        [1, k(0,2), k(0,5)],
        [2, k(5,10), k(7,10)],
        [2, k(5,10), k(5,6)],
        [2, k(5,10), k(0,5)],
        [2, k(3,4), k(7,10)],
        [2, k(3,4), k(5,6)],
        [2, k(3,4), k(0,5)],
        [2, k(0,2), k(7,10)],
        [2, k(0,2), k(5,6)],
        [2, k(0,2), k(0,5)],
        [3, k(5,10), k(7,10)],
        [3, k(5,10), k(5,6)],
        [3, k(5,10), k(0,5)],
        [3, k(3,4), k(7,10)],
        [3, k(3,4), k(5,6)],
        [3, k(3,4), k(0,5)],
        [3, k(0,2), k(7,10)],
        [3, k(0,2), k(5,6)],
        [3, k(0,2), k(0,5)]
        ]



    resultados = [1,1,3,1,2,3,2,3,4,1,2,4,2,3,4,2,3,4,3,3,4,3,4,5,5,5,5]

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
    print(f"[*]\33[31;1m{resultados_possiveis[str(diagnostico)]}\33[m")

if __name__=="__main__": 
    while True:
       clearTerminal()
       exercicios, sono, sol, alimentacao, falimentacao, mode = userInput()

       habitos = alimentacaoTree(sol,alimentacao,falimentacao, mode)
       mainTree(habitos,exercicios,sono,mode)
       time.sleep(1)
       
       userexit = str()
       while userexit not in ["s","n"]:
          userexit = str(input("\n[] Deseja sair ou refazer (s/n) ?  "))
       
       if userexit == "n":
          continue

       break









