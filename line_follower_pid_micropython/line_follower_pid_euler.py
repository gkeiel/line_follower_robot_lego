from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait


ME = Motor(Port.A)
MD = Motor(Port.B)
S1 = ColorSensor(Port.S1)

k_p = 100
k_i = 0
k_d = 300
T_s = 0.010
N   = 1000*T_s

vel   = 360 # in degrees/second
r     = 50
e_ant = 0
i_ant = 0

while True:
    y = S1.reflection()
    e = r -y

    p = k_p*e
    i = k_i*T_s*e +i_ant
    d = k_d*(e -e_ant)/T_s
    u = p +i +d

    ME.run(vel +u)
    MD.run(vel -u)

    e_ant = e
    i_ant = i
    wait(N)