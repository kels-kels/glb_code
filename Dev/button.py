from gpiozero import LED, Button
from signal import pause

led = LED(17)
buttom = BUtton(2)

button.when_pressed = led.on
button.when released = led.off

pause()

