def solution(spell, dic):
    spell.sort()
    for d in dic :
        if spell == sorted(d) : return 1
    return 2

print(solution(["p", "o", "s"],["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"],["def", "dww", "dzx", "loveaw"]))