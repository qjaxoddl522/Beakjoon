n, m = list(map(int, input().split()))
pokemon = {}
for i in range(1, n+1):
    pokemon[i] = input()
pokemon_reversed = dict(map(reversed, pokemon.items()))
for _ in range(m):
    q = input()
    if q.isdigit():
        print(pokemon.get(int(q)))
    else:
        print(pokemon_reversed.get(q))
