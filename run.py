#!/usr/bin/python

import sys, time
import dynaroach as dr

try:
    infile = sys.argv[2]
    
    if len(sys.argv) > 3:
        dir = sys.argv[3]
        save = True
    else:
        save = False
    
    r = dr.DynaRoach(sys.argv[1])
    
    if save:
        r.run_gyro_calib()
        print("Running gyro calibration...")
        raw_input()
        r.get_gyro_calib_param()
        time.sleep(0.5)
    
    
    t = dr.Trial()
    t.load_from_file(infile)
    r.configure_trial(t)
    ds = dr.datestring()
    if save:
        t.save_to_file('./' + dir + '/' + ds + '_cfg',
                        gyro_offsets=r.gyro_offsets, rid=eval(open('rid.py').read()))
    
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
            pass
    
        r.save_trial_data('./' + dir + '/' + ds + '_mcu.csv')
    r.reset()
except Exception as e:
    print('Caught the following exception: ' + str(e))
finally:
    r.__del__()
    print('Fin')
