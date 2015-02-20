import dynaroach as dr
import sys
import time

d = dr.DynaRoach(sys.argv[1])
#d.echo()
#raw_input()


while True:
    print d.hall_current_pos()

    time.sleep(0.15)

    #d.set_motor_config(0, 0)
    #raw_input()
    #d.set_motor_config(-.7, -.7)
    #d.set_motor_config(-.5, -.5)
    #raw_input()
    #d.set_motor_config(0,0)
    #raw_input()
    #d.test_hallenc()
    #raw_input()



