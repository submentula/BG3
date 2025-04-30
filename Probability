def Pa(dc):
    favorable_outcomes = 0
    for d1 in range(1, 21):
        for d2 in range(1, 21):
            if d1 == 20 or d2 == 20:
                favorable_outcomes += 1
                continue
            if d1 == 1 and d2 == 1:
                continue
            if max(d1, d2) >= dc:
                favorable_outcomes += 1
    return favorable_outcomes / 400

def Pb(dc, bonus):
    if dc - bonus >= 20:
        return 1 / 20
    if dc - bonus <= 1:
        return 19 / 20
    favorable_outcomes = 0
    for result in range(1, 21):
        if result + bonus >= dc:
            favorable_outcomes += 1
    return favorable_outcomes / 20
    
