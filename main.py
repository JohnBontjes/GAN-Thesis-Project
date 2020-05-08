#!/usr/bin/env python3

from gan import runNetwork
import os
import sys
import time
import subprocess as sp
import requests

def notify(val):
    url = 'IFTTT Webhook URL Here'
    data= {'value1': val}
    requests.post(url, data=data)

if __name__ == '__main__':
    currdir = os.getcwd()
    datasets = ['celebrity500']
    for dataset in datasets:
        for i in range(5, 101, 5):
            newdir = '{0:s}_{1:03d}_epoch'.format(dataset, i)
            if not os.path.exists(newdir):
                os.mkdir(newdir)
            os.chdir(newdir)
            gen, dis = runNetwork(dataset, i)
            print(i, gen, dis)
            os.chdir(currdir)
            sp.run(['rsync', '-r', newdir, 'jbontjes@cs:~/GAN/models'])
            notify(newdir)
            time.sleep(600)
        notify(dataset)
    notify('Complete Run')


