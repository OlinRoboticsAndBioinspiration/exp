#!/usr/bin/python

import sys, time
import dynaroach as dr

infile = sys.argv[1]

if len(sys.argv) > 2:
    dir = sys.argv[2]
    save = True
else:
    save = False

r = dr.DynaRoach()

if save:
    r.run_gyro_calib()
    print("Running gyro calibration...")
    raw_input()
    r.get_gyro_calib_param()
    time.sleep(0.5)


t = dr.Trial()
t.load_from_file(infile)
r.configure_trial(t)

if save:
    ds = dr.datestring()
    t.save_to_file('./' + dir + '/' + ds + '_cfg',
                   gyro_offsets=r.gyro_offsets, rid=eval(open('rid.py').read()))


print("Press any key to begin clearing memory.")
raw_input()

r.erase_mem_sector(0x100)
time.sleep(1)
r.erase_mem_sector(0x200)
time.sleep(1)
r.erase_mem_sector(0x300)

print("Press any key to start the trial running.")
raw_input()

r.run_trial()
print("Press any key to request the mcu data from the robot.")
raw_input()

if save:
    r.transmit_saved_data()
    print("Press any key to save transmitted data to a file.")
    input = raw_input()
    if input == 'q':
        r.__del__()

    r.save_trial_data('./' + dir + '/' + ds + '_mcu.csv')

r.__del__()
print('Fin')
