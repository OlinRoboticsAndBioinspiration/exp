
from rbt import rbt

# runs calibration processes on slider data in any .csv's in cal/ that 
# don't have a corresponding _cal.py file in cal/dat/
#rbt.do(di='cal',dev='opti',trk='slider',procs=rbt.cal,exclude='_cal.py')

# runs ukf processes on rbt data in any .csv's in straight/ that
# don't have a corresponding _ukf.npz file in straight/dat/
#rbt.do(di='straight',dev='opti',trk='rbt',procs=rbt.ukf,exclude='_ukf.npz')
#rbt.do(di='left',dev='opti',trk='rbt',procs=rbt.ukf,exclude='_ukf.npz')
#rbt.do(di='right',dev='opti',trk='rbt',procs=rbt.ukf,exclude='_ukf.npz')
#rbt.do(di='straight',dev='opti',trk='l',procs=rbt.ukf,exclude='_ukf.npz')

#rbt.do(di='inair',dev='opti',trk='',procs=rbt.air,exclude='_dat.npz')
#rbt.do(di='tracklegs',dev='opti',trk='',procs=rbt.air,exclude='_dat.npz')

rbt.do(di='test',dev='opti',trk='rbt',procs=rbt.ukf,exclude='_ukf.npz')

