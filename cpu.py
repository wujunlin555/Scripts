#!/usr/bin/python
#coding: utf-8

from __future__ import division
import re
import time
import sys
import os

cpu_stat_file = '/proc/stat'

def cal(data):

    cpu_num = re.split('\s*', data)[0]
    usr = re.split('\s*', data)[1]
    nice = re.split('\s*', data)[2]    
    sys = re.split('\s*', data)[3]    
    idle = re.split('\s*', data)[4]
    iowait = re.split('\s*', data)[5]
    irq = re.split('\s*', data)[6]
    softirq = re.split('\s*', data)[7]
    stealstolen  = re.split('\s*', data)[8]
    guest = re.split('\s*', data)[9]

    total = int(usr) + int(nice) + int(sys) + int(idle) + int(iowait) + int(irq) + int(softirq) + int(stealstolen) + int(guest)
    usr_per = (int(usr) / total) * 100
    nice_per = (int(nice) / total) * 100
    sys_per = (int(sys) /total) * 100
    idle_per = (int(idle) / total) * 100
    iowait_per = (int(iowait) /total) * 100
    irq_per = (int(irq) / total) * 100
    soft_per = (int(softirq) / total) * 100
    steal_per = (int(stealstolen) /total) * 100
    guest_per = (int(guest) /total) * 100
    print "%s\t%.2lf\t%.2lf\t%.2lf\t%.2lf\t%.2lf\t%.2lf\t%.2lf\t%.2lf\t%.2lf" % (cpu_num,usr_per, nice_per, sys_per, idle_per,iowait_per, irq_per, soft_per, steal_per, guest_per)
    return    

def get_cpu_data():
    with open(cpu_stat_file, 'r') as f:
        print "all\tusr\tnice\tsys\tidle\tiowait\tirq\tsoft\tsteal\tguest"
   
        for data in f:
            if 'cpu' in data:
                cal(data.split('\n')[0])
    return 

if __name__ == '__main__':
    if len(sys.argv) == 1:
       get_cpu_data()

    if len(sys.argv) == 3:
        if '-t' in sys.argv:
            while 1:
                os.system('clear')
                get_cpu_data()
                time.sleep(int(sys.argv[2]))
