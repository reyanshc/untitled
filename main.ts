input.onButtonPressed(Button.A, function () {
    radio.sendString("there is a meeting now")
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(1)
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("is it micro bit time")
})
radio.setGroup(255)
let hour = 1
let after = hour
music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.Once)
basic.forever(function () {
    radio.setTransmitPower(7)
})
