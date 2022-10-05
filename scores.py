def incr_score(score, condition, answer):
    if condition:
        score += 1
        print(f"Bien joué ! Ton score actuel est : {score}")
    else:
        print(f"Faux ! Ton score est toujours : {score}")
        print(f"La bonne réponse était : {answer}")
    return score



def final_score(attempts, score):
    print(f"Ton score final est : {score}")
    if attempts < 2: print(f"Tu as fait {attempts} tentative.")
    else: print(f"Tu as fait {attempts} tentatives.")
    print(f"Donc ton pourcentage de succès est {100*score/attempts:.2f}%")
    ggb = "https://geogebra.org/classic"
    print(f"Va voir le site Geogebra pour expérimenter avec différentes valeurs : {ggb}")
    cond = False
    return cond

def nb_root_score(nb_root, score):
    nb_rac = int(input("Nombre d'intersection(s) avec l'axe des abcisses (Ox) : "))
    score = incr_score(score, condition=nb_rac==nb_root, answer=nb_root)
    return score



def extremum_score(a, score):
    answer = "minimum" if a > 0 else "Maximum"
    extrem = int(input("1) Maximum\n2) minimum\nTa réponse : "))
    score = incr_score(score, condition=a * extrem > a or a * extrem > 2*a, answer=answer)
    return score
