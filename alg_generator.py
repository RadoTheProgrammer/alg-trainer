import rubik_impl
import random 
import kociemba

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
random_moves = "L' F' D'"
print(random_moves)

def convert_to_kociemba(cube):
    # change order
    state = [cube.state[MY_ORDER.index(face)] for face in KOCIEMBA_ORDER]

    cubestring = "".join("".join("".join(facelet for facelet in row) for row in face) for face in state)

    return cubestring

def reverse_algorithm(algorithm:list):
    return [move[0] if "'" in move else move+"'" for move in algorithm[::-1]]
setup_algorithm = rubik_impl.reverse_alg(ALGORITHM)

cube = rubik_impl.Cube()
cube.apply(setup_algorithm)
cube.apply(random_moves)
state = convert_to_kociemba(cube)


alg = rubik_impl.norm_alg(kociemba.solve(SOLVED_STATE,state))
print(alg)
alg += rubik_impl.reverse_alg(random_moves)
print(" ".join(alg))
