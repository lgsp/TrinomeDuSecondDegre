from pub import *
import random
from scores import *


def capacites_attendues():
    ca = {
        'signe' : "Étudier le signe d'une fonction polynôme du second degré donnée sous forme factorisée.",
        'racines' : "Déterminer les fonctions polynômes du second degré s'annulant en deux nombres réels distincts.",
        'factoriser' : "Factoriser une fonction polynôme du second degré, en diversifiant les stratégies : racine évidente, détection des racines par leur somme et leur produit, identité remarquable, application des formules générales.",
        'forme' : "Choisir une forme adaptée (développée réduite, canonique, factorisée) d'une fonction polynôme du second degré dans le cadre de la résolution d'un problème (équation, inéquation, optimisation, variations)."
    }
    return ca


    
def ca1_sign(bo_premm, ca_k):
    ca = capacites_attendues()
    print(f"D'après le programme officiel accessible via cette URL :\n{bo_prem}\n")
    print(f"L'élève doit être capable de :\n{ca[ca_k]}\n")
    if random.randint(0, 10) % 2 == 0: a = random.randint(1, 10)
    else: a = round(random.uniform(-10, -1), 2)
    if random.randint(0, 10) % 2 == 0: x1 = random.randint(-10, 10)
    else: x1 = round(random.uniform(-10, 10), 2)
    if random.randint(0, 10) % 2 == 1: x2 = random.randint(-10, 10)
    else: x2 = round(random.uniform(-10, 10), 2)
    return a, x1, x2
 
        
def work_expected_capability1(bo_prem, ca_k):
    attempts = 0
    score = 0
    cond = True
    while cond:
        a, x1, x2 = ca1_sign(bo_prem, ca_k)
        print(f"Soit la fonction polynôme T(x) = {a}*(x - ({x1}))*(x - ({x2}))")
        print("Prenez du papier et de quoi écrire parce que vous allez devoir raisonner.\n")
        
        questions = ["Quelle est l'abscisse du point d'intersection avec (Ox) le plus à gauche ?",
                     "Quelle est l'abscisse du point d'intersection avec (Ox) le plus à droite ?", 
                    f"Quel est le signe (-1 ou 1) de T sur l'intervalle ]-∞ ; {min(x1, x2)}] ?",
                    f"Quel est le signe (-1 ou 1) de T sur l'intervalle ]{min(x1, x2)} ; {max(x1, x2)}] ?",
                    f"Quel est le signe (-1 ou 1) de T sur l'intervalle ]{max(x1, x2)} ; +∞] ?"]
        answers = [min(x1, x2), max(x1, x2), abs(a)/a, -abs(a)/a, abs(a)/a]
        q_and_a = dict(zip(questions, answers))
        for q in q_and_a:
            print(q)
            right_ans = q_and_a[q]
            user_ans = float(input("Votre réponse = "))
            score = incr_score(score, right_ans == user_ans, right_ans)
            attempts += 1
            continuer = input("Souhaitez-vous continuer ? (O|N) ")
            if continuer.upper() == "N": 
                cond = final_score(attempts, score)
                break
        cond = final_score(attempts, score)



def ca2_roots(bo_prem, ca_k):
    ca = capacites_attendues()
    print(f"D'après le programme officiel accessible via cette URL :\n{bo_prem}\n")
    print(f"L'élève doit être capable de :\n{ca[ca_k]}\n")
    if random.randint(0, 10) % 2 == 0: x1 = random.randint(-10, 10)
    else: x1 = round(random.uniform(-10, 10), 2)
    if random.randint(0, 10) % 2 == 1: x2 = random.randint(-10, 10)
    else: x2 = round(random.uniform(-10, 10), 2)
    return x1, x2


def work_expected_capability2(bo_prem, ca_k):
    attempts = 0
    score = 0
    cond = True
    while cond:
        x1, x2 = ca2_roots(bo_prem, ca_k)
        print(f"Soit une fonction polynôme T(x) = a*x**2 b*x + c s'annulant en {x1} et {x2}") 
        print("Prenez du papier et de quoi écrire parce que vous allez devoir raisonner.")
        print("Lorsque la réponse impliquera des valeurs numériques, arrondir à 2 décimales.\n")
        
        questions = [f"Quelle est la forme factorisée de T en fonction de {x1} et {x2}?",
                     "Si a = 1 alors que vaut b ?", 
                     "Si a = 1 alors que vaut c ?",
                     "Si a = -1 alors que vaut b ?", 
                     "Si a = -1 alors que vaut c ?",]
        answers = [f"a*(x - ({x1}))*(x - ({x2}))", 
                   round(-(x1+x2), 2), 
                   round(x1*x2, 2), 
                   round(x1+x2, 2), 
                   round(-x1*x2, 2)]
        q_and_a = dict(zip(questions, answers))
        for q in q_and_a:
            print(q)
            right_ans = q_and_a[q]
            if isinstance(right_ans, float) or isinstance(right_ans, int):
                print("Arrondir à 2 décimales")
                user_ans = float(input("Votre réponse = "))
                score = incr_score(score, abs(right_ans - user_ans) < 0.01, right_ans)
                attempts += 1
            else: 
                print("Écrire toutes les parenthèses nécessaires (même pour les nombres positifs)")
                user_ans = input("Votre réponse = ")
                score = incr_score(score, right_ans == user_ans, right_ans)
                attempts += 1
                
            continuer = input("Souhaitez-vous continuer ? (O|N) ")
            if continuer.upper() == "N": 
                cond = final_score(attempts, score)
                break
        cond = final_score(attempts, score)


def expected_capabilities(bo_prem):
    print("Quelle capacité souhaitez-vous travailler ?")
    ca = capacites_attendues()
    for c in ca:
        print("\n", ca[c].upper(), "\n")
        print(f'Pour travailler cette capacité tapez : "{c}" sinon tapez "entrée."')
        ca_k = input("Votre choix : ")
        if ca_k.lower() == 'signe':
            work_expected_capability1(bo_prem, ca_k)
        elif ca_k.lower() == 'racines':
            work_expected_capability2(bo_prem, ca_k)
            