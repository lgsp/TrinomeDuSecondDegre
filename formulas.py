def build_basic_formulas():
    algebra = {
        'FC' : ('Forme canonique', 'a*(x - alpha)**2 + beta'),
        'FD' : ('Forme développée', 'a*x**2 + b*x + c'),
        'D' : ('Delta', 'b**2 - 4*a*c'),
        'A' : ('alpha', '-b/(2*a)'), 
        'B' : ('beta', '-Delta/(4*a)'),
        'DNeg' : ("Delta < 0", "a*T(x) > 0"),
        'DNul' : ("Delta = 0", "T(x) = a*(x - alpha)**2"),
        'DPos' : ("Delta > 0", "T(x) = a*(x - x1)*(x - x2)"),
        'x1' : ('x1', '( -b - sqrt(Delta) ) / ( 2*a )'),
        'x2' : ('x2', '( -b + sqrt(Delta) ) / ( 2*a )'),
    }
    geometry = {
        'Sym' : ('Axe de symétrie', 'x = alpha'), 
        'min' : ('a > 0', 'minimum'),
        'Max' : ('a < 0', 'maximum'),
        'DNeg' : ("Delta < 0", "0 intersection avec l'axe des abscisses (Ox)"),
        'DNul' : ("Delta = 0", "1 intersection (alpha, beta) avec l'axe des abscisses (Ox)"),
        'DPos' : ("Delta > 0", "2 intersections (x1, 0) et (x2, 0) avec l'axe des abscisses (Ox)")
    }    
    return algebra, geometry

def print_formulas(topic, title):
    print(f"\n{title}\n")
    for k in topic: 
        for elt in topic[k]: 
            print(elt)
        print()


def watch_basic_formulas(algebra, geometry):
    menu = '''
    1) Algèbre
    2) Géométrie
    Q) Quitter
    Choix : '''
    cond = True
    while cond:
        choix = input(menu)
        if choix == '1': print_formulas(algebra, "Approche algébrique")
        elif choix == '2': print_formulas(geometry, "Approche géométrique")
        elif choix.upper() == 'Q': cond = False
        else: print('Entrer 1 ou 2 ou Q')