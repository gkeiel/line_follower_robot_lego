from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait


ME = Motor(Port.A)
MD = Motor(Port.B)
S1 = ColorSensor(Port.S1)

k_p = 1.0
k_i = 0.0
k_d = 3.0

vel   = 360 # in degrees/second
r     = 50
e_ant = 0
i_ant = 0

while True:
    y = S1.reflection()
    e = r -y

    p = k_p*e
    i = k_i*e +i_ant
    d = k_d*(e -e_ant)
    u = p +i +d

    ME.run(vel +u)
    MD.run(vel -u)

    e_ant = e
    i_ant = i
    wait(10)