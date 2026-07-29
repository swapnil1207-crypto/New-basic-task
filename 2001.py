print("Swapnil Dadaso Lohar(2001) ")
print("Implement Crypt Arithmetic Problem Using Python")
from itertools import permutations


letters = ('B','O','M','A','S','E','G')

digits = range(10)

for perm in permutations(digits, len(letters)):
    assign = dict(zip(letters, perm))


    if assign['B'] == 0 or assign['B'] == 0:
        continue

    bomb = (
      
        assign['B']*1000 +
        assign['O']*100 +
        assign['M']*10+
        assign['B']
    )

    base = (
        
        assign['B']*1000 +
        assign['A']*100 +
        assign['S']*10+
        assign['E']
    )

    games = (
        
        assign['G']*10000 +
        assign['A']*1000 +
        assign['M']*100+
        assign['E']*10+
        assign['S']
    )

    if bomb + base == games:
        print("Solution Found")
        print(assign)
        print("BOMB =", bomb)
        print("BASE =", base)
        print("GAMES =", games)
        break
