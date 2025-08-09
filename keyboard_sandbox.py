import keyboard
keyboard.add_abbreviation("@email", "test@example.com")
keyboard.add_hotkey("ctrl+alt+p", lambda: print("CTRL+ALT+P Pressed!"))
# keyboard.is_pressed()
print(keyboard.is_pressed('ctrl'))
keyboard.send("space")
#keyboard.send("windows+d")
key_pressed = False

def on_key_press(event):
    global key_pressed
    key_pressed = True
    print(event)
    print(f"Key pressed: {event.name}")

def on_key_release(event):
    global key_pressed
    key_pressed = False

# Attach the event listeners
keyboard.on_press(on_key_press)
keyboard.on_release(on_key_release)

print("Press any key (CTRL+C to exit)")

while True:
    if key_pressed:
        # This runs while any key is being held down
        pass 
input()
