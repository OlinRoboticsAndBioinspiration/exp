import dynaroach as dr
import sys

d = dr.DynaRoach(sys.argv[1])
d.set_motor_config(.4, .4)
raw_input()
d.set_motor_config(0,0)
