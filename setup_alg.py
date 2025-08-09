import rubik_impl
import random 
import kociemba

N_RANDOM_MOVES = 2
MOVES = {"U","L","F","R","B","D"}
SOLVED_STATE = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
MY_ORDER,KOCIEMBA_ORDER = "ULFRBD", "URFDLB"

def convert_to_kociemba(cube):
    # change order
    state = [cube.state[MY_ORDER.index(face)] for face in KOCIEMBA_ORDER]

    cubestring = "".join("".join("".join(facelet for facelet in row) for row in face) for face in state)

    return cubestring

def get(alg):
    reversed_alg = rubik_impl.reverse_alg(alg)

    random_moves = []
    move = None
    for i in range(N_RANDOM_MOVES):
        move = random.choice(tuple(MOVES-{move}))
        random_moves.append(move+("'" if random.randrange(2) else ""))
    print(reversed_alg)
    cube = rubik_impl.Cube.solved()
    cube.apply(reversed_alg)
    cube.apply(random_moves)
    state = convert_to_kociemba(cube)


    alg = rubik_impl.norm_alg(kociemba.solve(SOLVED_STATE,state))
    print(alg)
    alg += rubik_impl.reverse_alg(random_moves)
    return " ".join(alg)

