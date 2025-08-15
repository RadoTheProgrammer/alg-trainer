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

def get(input_alg):
    reversed_alg = rubik_impl.Alg(input_alg).reverse()
    print(reversed_alg)
    cube = rubik_impl.Cube.solved()
    cube.apply(reversed_alg)
    scramble_alg = cube.scramble(N_RANDOM_MOVES)
    state = convert_to_kociemba(cube)


    output_alg = rubik_impl.Alg(kociemba.solve(SOLVED_STATE,state))
    output_alg += scramble_alg.reverse()
    return output_alg

print(get("R U"))

