#!/usr/bin/python

import sys, time
import dynaroach as dr

r = dr.DynaRoach(sys.argv[1])
r.set_motor_config(-.5, -.5)
raw_input()
r.set_motor_config(0, 0)
