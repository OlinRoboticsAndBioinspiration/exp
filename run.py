#!/usr/bin/python
"""
Example: python run.py COM14 70x70 test
arg1 --> Robot address COM14
arg2 --> config file for the trial, 70x70.csv
arg3 --> output dir test
"""

run_robot = True
run_mocap = False

import sys, time
import dynaroach as dr

if run_mocap:
    import natnethelper as nt
    import NatNet

r = None
try:
    if len(sys.argv) != 4:
        print "Please input 3 arguments:"
        print "python run.py <robot_adress> <config file> <output_dir>"
        print "Example: python run.py COM14 70x70.csv test"
        sys.exit(1)
    #collect data and run the robot switch

    if run_mocap:
        nat_net_client = NatNet.NatNetClient(1);
        nat_net_client.Initialize("","");

    infile = sys.argv[2]
    
    if len(sys.argv) > 3:
        dir = sys.argv[3]
        save = True
    else:
        save = False
    ds = dr.datestring()

    if run_robot:
        r = dr.DynaRoach(sys.argv[1])
        
        if save:
            r.run_gyro_calib()
            print("Running gyro calibration...")
            time.sleep(0.5)
            r.get_gyro_calib_param()
            time.sleep(0.5)

        while r.gyro_offsets == None:
            print "Waiting on gyro offset"
            time.sleep(2)
        print "Received gyro offset"

        t = dr.Trial()
        if save:
            t.save_to_file('./' + dir + '/' + ds + '_cfg',
                gyro_offsets=r.gyro_offsets, rid=eval(open('rid.py').read()))
        t.load_from_file(infile)
        r.configure_trial(t)
    
        if save:
            t.save_to_file('./' + dir + '/' + ds + '_cfg',
                            gyro_offsets=r.gyro_offsets, rid=eval(open('rid.py').read()))

    print("Press any key to start the trial running.")
    raw_input()
    if run_mocap:
        print("Starting Motion Capture") 
        mocap_data = nt.start_collection(nat_net_client)
    if run_robot:
        r.run_trial()
    print("Press any key to request the mcu data from the robot.")
    raw_input()
    if run_mocap:
        print("Stopping mocap collection");
        nt.stop_collection(nat_net_client);
    
    if save:
        if run_robot:
            r.transmit_saved_data()
            print("Press any key when data is done transmitting.")
            input = raw_input()
            if input == 'q':
                r.__del__()
                pass
            r.save_trial_data('./' + dir + '/' + ds + '_mcu.csv')
            r.erase_mem_sector(0x100)
            time.sleep(1)
            r.erase_mem_sector(0x200)
            time.sleep(1)
            r.erase_mem_sector(0x300)
            time.sleep(1)
            r.reset(do_wait=False)
        if run_mocap:
            nt.csv_from_data(nat_net_client, mocap_data, './' + dir + '/' + ds + '_mocap.csv');
except Exception as e:
    print('Caught the following exception: ' + str(e))
finally:
    if r:
        r.__del__()
    print('Fin')
