import rubik_impl
import random 
ALGORITHM = "R U R' U'"
N_RANDOM_MOVES = 3
MOVES = {"U","L","F","R","B","D"}
SOLVED_STATE = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
MY_ORDER,KOCIEMBA_ORDER = "ULFRBD", "URFDLB"
# Generate random moves
random_moves = []
move = None
for i in range(N_RANDOM_MOVES):
    move = random.choice(tuple(MOVES-{move}))
    random_moves.append(move+("'" if random.randrange(2) else ""))
print(random_moves)

def convert_to_kociemba(cube):
    # change order
    cube = [cube[MY_ORDER.index(cube.cube)] for face in KOCIEMBA_ORDER]

    cubestring = "".join("".join("".join(facelet for facelet in row) for row in face) for face in cube)

    return cubestring
cube = rubik_impl.Cube()
cube.apply(ALGORITHM)
cube.apply(random_moves)
cube = convert_to_kociemba(cube)

print(cube.cube)
