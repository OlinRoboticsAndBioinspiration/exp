#!/usr/bin/python

import sys, time

import natnethelper as nt
import NatNet
import dynaroach as dr

nat_net_client = NatNet.NatNetClient(1);
nat_net_client.Initialize("","");

dir = sys.argv[1]

print("Press any key to start the trial running.")
raw_input()
print("Starting Motion Capture") 
mocap_data = nt.start_collection(nat_net_client)
raw_input()
print("Stopping mocap collection");
nt.stop_collection(nat_net_client);
ds = dr.datestring()
nt.csv_from_data(nat_net_client, mocap_data, './' + dir + '/' + ds + '_mocap.csv');
