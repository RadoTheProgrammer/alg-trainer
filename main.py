import pandas as pd
import setup_alg
import keyboard

FILE_ALGS = "data-algs.csv"
FILE_TIMES = "data-times.csv"

def train(category,cases=()):
    df = pd.read_csv(FILE_ALGS)
    #print(df["Case"] in cases)
    df = df[(df["Category"]==category) & (df["Case"].isin(cases))]
    alg = df.loc[0,"Alg"]



    input("Tell when ready")
    print(setup_alg.get(alg))
    wait_until_press() # user applying setup alg
    print("Recognition ...")
    wait_until_press()
    #if cases!="all":

def wait_until_press():
    while key_pressed:pass
    while not key_pressed:pass

def on_press(event):
    global key_pressed
    key_pressed = True


def on_release(event):
    global key_pressed
    key_pressed = False

key_pressed = False
# Attach the event listeners
keyboard.on_press(on_press)
keyboard.on_release(on_release)

train("PLL",("Ua perm",))

input()