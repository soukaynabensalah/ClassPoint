
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    p3 = Point(6, 0)

    print(p1, p2, p3)

    tp = TroisPoints(p1, p2, p3)
    print( tp.sontalignes())
    print( tp.estisocèle())

    # Test des méthodes statiques
    print("Distance:", Point.calculerdistancestatique(p1, p2))
    print("Milieu :", Point.calculermilieustatique(p1, p2)) 

    
