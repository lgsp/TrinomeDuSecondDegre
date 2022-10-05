import random
from math import sqrt
from pub import *
from formulas import *
from scores import *
from capabilities import *
from difflib import SequenceMatcher

    
def practice_basics(topic):
    score = 0
    attempts = 0
    
    for key in topic:
        attempts += 1
        exercice = input(f"{topic[key][0]} : ")
        solution = topic[key][1]
        similarity = SequenceMatcher(a=right_ans, b=user_ans).ratio()
        score = incr_score(score, condition=exercice==solution, answer=solution)
    
    return final_score(attempts, score)
    

    
    
def numerical_practice():
    score = 0
    attempts = 0
    a = random.randint(-10, 10)
    while a == 0: a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    alpha = round(-b / (2*a), 2)
    Delta = round(b**2 - 4 * a * c, 2)
    beta = round(-Delta / (4 *a), 2)
    fd = f"{a}*x**2 + ({b})*x + ({c})"
    fc = f"{a}*( x - ({alpha}) )**2 + ({beta})"
    if Delta < 0: 
        nb_root = 0
        chance = random.randint(0, 100)
        if chance % 2 == 0: print(f"T(x) = {fc}")
        else: print(f"T(x) = {fd}")
        score = nb_root_score(nb_root, score)
        attempts += 1
        score = extremum_score(a, score)
        attempts += 1
    elif Delta == 0: 
        nb_root = 1
        fc = f"{a}*( x - ({alpha}) )**2"
        ff = fc
        chance = random.randint(0, 100)
        if chance % 2 == 0: print(f"T(x) = {fc}")
        else: print(f"T(x) = {fd}")
        score = nb_root_score(nb_root, score)
        attempts += 1
        score = extremum_score(a, score)
        attempts += 1
        x = float(input("Résoudre l'équation T(x) = 0. Arrondir à 2 chiffres, x = "))
        score = incr_score(score, condition=abs(x - alpha) < 0.01, answer=alpha)
        attempts += 1
    else:
        nb_root = 2
        x1 = round( ( -b - sqrt(Delta) ) / ( 2*a ), 2 )
        x2 = round( ( -b + sqrt(Delta) ) / ( 2*a ), 2 )
        true_x1, true_x2 = min(x1, x2), max(x1, x2)
        ff = f"{a}*( x - ({x1}) )*( x - ({x2}) )"
        chance = random.randint(0, 100)
        if chance % 3 == 0: print(f"T(x) = {fc}")
        elif chance % 3 == 1: print(f"T(x) = {fd}")
        else: print(f"T(x) = {ff}")
        score = nb_root_score(nb_root, score)
        attempts += 1
        score = extremum_score(a, score)
        attempts += 1
        print("Résoudre l'équation T(x) = 0. Arrondir à 2 chiffres.")
        x1_std = float(input("x1 = "))
        score = incr_score(score, condition=abs(x1_std - true_x1) < 0.01, answer=x1)
        attempts += 1
        x2_std = float(input("x2 = "))
        score = incr_score(score, condition=abs(x2_std - true_x2) < 0.01, answer=x2)        
        attempts += 1
    return final_score(attempts, score)




        
algebra, geometry = build_basic_formulas()       
menu = '''
0) Créer des fichiers de leçons
1) Revoir les formules de base
2) Pratiquer les formules algébriques de base
3) Pratiquer les interprétrations géométriques de base
4) Pratiquer avec des valeurs numériques
5) Travailler les capacités attendues
6) Do you find it too much difficult?
7) Do you want more?
8) Do you find it too easy?
9) Do you want private lessons with me?
Q) Quit
Your choice: '''
cond = True
while cond:
    choice = input(menu)
    if choice == '0':
        create_lesson_files()
    elif choice == '1':
        watch_basic_formulas(algebra, geometry)
    elif choice == '2':
        practice_basics(algebra)
    elif choice == '3':
        practice_basics(geometry)
    elif choice == '4':
        numerical_practice()
    elif choice == '5':
        expected_capabilities(bo_prem)
    elif choice == '6':
        request = "find these exercises too much difficult"
        options = [
            f"Review previous level: {pm2}", 
            f"Get more content from this level: {pm1}",
            f"Contact me on Superprof for private lessons: {annonce_superprof}"
        ]
        get_more(request, options)     
    elif choice == '7':
        request = "want more of my work"
        options = [
            f"Get more content from this level: {pm1}",
            f"Contact me on Superprof for private lessons: {annonce_superprof}",
            f"Subscribe to my YouTube channel: {pr_glump}"
        ]
        get_more(request, options)
    elif choice == '8':
        request = "want private lessons with me"
        options = [
            f"Contact me on Superprof for private lessons: {annonce_superprof}",
            f"If you are okay to pay me with bitcoins you can contact me at: {cl}",
            f"Join my affiliate program to access to Podia chat: {affiliate}"
        ]
        get_more(request, options)
    elif choice == '9':
        request = "want more of my work"
        options = [
            f"Get more content from this level: {pm1}",
            f"Contact me on Superprof for private lessons: {annonce_superprof}",
            f"Subscribe to my YouTube channel: {pr_glump}"
        ]
        get_more(request, options)
    elif choice.upper() == 'Q':
        cond = False
        request = "want to leave"
        options = [
            f"Get more content from this level: {pm1}",
            f"Contact me on Superprof for private lessons: {annonce_superprof}",
            f"Subscribe to my YouTube channel: {pr_glump}"
        ]
        get_more(request, options)
        print('Goodbye. See you soon.')
    else:
        print("ERROR!!! Please type '1' or '2' or 'Q'")
    

    