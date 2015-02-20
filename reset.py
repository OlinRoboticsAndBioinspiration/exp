#!/usr/bin/python

import sys, time
import dynaroach as dr

r = dr.DynaRoach(sys.argv[1])
r.reset(do_wait=False)
  