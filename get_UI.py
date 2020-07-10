import os
import time
from natsort import natsorted
from recalc import node_analysis as na
from recalc import r_util

def analyzes(savedir, tl, startt):
    with open(savedir + '/runtime.txt', mode='a') as f:
        f.write("%s\n" % tl[len(tl) - 1])

        r_util.del_node_params(savedir)

        tl.append(['end', time.time() - startt - tl[len(tl) - 1][1]])
        f.write("%s\n" % tl[len(tl) - 1])

        experiment = list()
        for dir in natsorted(os.listdir(savedir + '/act')):
            experiment.append(savedir + '/act/' + dir)

        print('start_get_nodedata')
        na.get_nodedata(experiment, savedir)
        tl.append(['output error time series', time.time() - startt - tl[len(tl) - 1][1]])
        f.write("%s\n" % tl[len(tl) - 1])

        tl.append(['total', time.time() - startt])
        f.write("%s\n" % tl[len(tl) - 1])

    return 0


for savedir in natsorted(os.listdir('runs')):
    savedir = 'runs/' + savedir
    with open(savedir + '/runtime.txt', mode='a') as f:
        f.write("addtional analysis\n")
    print('start_analysis',savedir)
    tl=list()#time list
    startt=time.time()
    tl.append(['analysis start',time.time()-startt])
    analyzes(savedir, tl, startt)