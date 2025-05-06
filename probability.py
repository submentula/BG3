def Pa(dc):
    if dc <= 1:
        favorable_outcomes = 399
    else:
        count_less_than_dc_in_1_to_19 = min(19, dc - 1)
        outcomes_19x19_max_lt_dc = count_less_than_dc_in_1_to_19 ** 2
        favorable_outcomes = 400 - outcomes_19x19_max_lt_dc
    return favorable_outcomes / 400

def Pb(dc, bonus):
    threshold = dc - bonus
    favorable_outcomes_count = max(0, 21 - max(1, threshold))
    return (favorable_outcomes_count + 1) / 21
