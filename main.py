def on_button_pressed_a():
    radio.send_string("there is meeting now")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_number(1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_string("is it micro bit time")
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(255)
hour = 1
after = hour
music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
    MelodyOptions.ONCE)

def on_forever():
    pass
basic.forever(on_forever)
