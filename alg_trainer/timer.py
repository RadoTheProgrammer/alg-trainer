import pandas as pd
from . import setup_alg
import keyboard
import sys
import time
import os
import random
FILE_ALGS = "data-algs.csv"
FILE_TIMES = "data-times.csv"

def train(category,cases=()):
    df = pd.read_csv(FILE_ALGS)
    #print(df["Case"] in cases)
    df = df[(df["Category"]==category) & (df["Case"].isin(cases) if cases else True) & df["Selected"]]
    print(df)
    while True:
        df_sample = df.sample(n=len(df))
        for i, row in df_sample.iterrows():
            #print(row)
            alg = row["Alg"]


            #print(df)

            print(setup_alg.get(alg))
            input("Apply the setup alg and enter to continue")
            print("Recognition ...")
            reco_time = stopwatch()
            print("Execution ...")
            exec_time = stopwatch()
            print(reco_time,exec_time)
            #if cases!="all":
            if not os.path.exists(FILE_TIMES):
                with open(FILE_TIMES, "w") as f:
                    f.write("Datetime,Category,Case,AlgName,RecoTime,ExecTime\n")

            ts  = pd.Timestamp.now().replace(microsecond=0)
            with open(FILE_TIMES, "a") as f:
                f.write(f"{ts},{category},{row["Case"]},{row["AlgName"]},{reco_time},{exec_time}\n")
def handle_event(e):
    global key_pressed
    if e.event_type == keyboard.KEY_DOWN:
        key_pressed = True
    elif e.event_type == keyboard.KEY_UP:
        key_pressed = False

    
def stopwatch(display=True):
    start_time = time.time()
    pressed = False
    # user has to unpress and press
    next_elapsed = 0

    while True:
    
        elapsed = time.time() - start_time
        if display and elapsed>next_elapsed:
            sys.stdout.write(f"\r{next_elapsed}")
            sys.stdout.flush()
            next_elapsed += 1

        if pressed:
            
            if key_pressed:
                elapsed = round(elapsed, 3)
                sys.stdout.write(f"\r{elapsed:02.3f}\n")

                return elapsed
        elif not key_pressed:

            pressed = True


# while True:
#     event = keyboard.read_event()
#     print(event)
keyboard.hook(handle_event)
key_pressed = False

train("PLL")

input()