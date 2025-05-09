def unscramble(scrambled, permutation):
    result = []
    s = scrambled

    for i in range(0, len(s) - len(s) % 3, 3):
        words = s[i:i+3]
        unscrambled = [words[p] for p in permutation]
        result.extend(unscrambled)
    return ''.join(result)

scrambled = "onCragulttianso Y!u ootgth  feagl T.e hlaf ig CsPHYR{E_710UHH7G7R_N5405P711N_04SW34_Y}5"
permutation = [2, 0, 1]

unscrambled = unscramble(scrambled, permutation)
print(unscrambled)
