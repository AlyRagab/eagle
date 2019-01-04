#!/usr/bin/python
import socket
import time
import os

from tools import resources as res
from tools import joutput as jout
from tools import es
import config as cf
import messages as msg
import alerts as alert


x = res.Resources()
hostname=(socket.gethostname())
date=time.time()
jsonout=cf.main_configuration['json_output']

def GetDisks():
	values=[]
	for k, v in cf.yamls['disks'].items():
		values.append(v)
	return values

def GetCpuAvg():
	interval=cf.yamls['cpu']['cpu_avg_interval']
	try:
		if interval==1:
			cpu_avg=x.LoadAvarage(0)
		elif interval==5:
			cpu_avg=x.LoadAvarage(1)
		elif interval==15:
			cpu_avg=x.LoadAvarage(2)
		return cpu_avg
	except:
		return 'cpu_avg_interval not configured well'

def CpuMsg():
	cpu=GetCpuAvg()
	critical=cf.yamls['cpu']['warning']		

	if cpu>=critical:
		danger=msg.CpuLoadAvg(str(cpu), hostname)
		return alert.Slack(danger, 'Alarm', 'danger', 'high', str(date))	
def MemoryMsg():
	memory=x.MemoryUsage()
	if memory['percent']>=90:
                danger=msg.MemoryPercent(memory['percent'], hostname)
                return alert.Slack(danger, 'Alarm', 'danger', 'high', str(date))

def SwapMsg():
	swap=x.Swap()
	if swap['percent']>=90:
                danger=msg.SwapPercent(swap['percent'], hostname)
                return alert.Slack(danger, 'Alarm', 'danger', 'high', str(date))
def DiskMsg():
        partitions=GetDisks()
        for partition in partitions:
                percent = x.MapDiskUsage()[partition][3]
                if percent >= 90:
                        health=partition
                        warn=msg.DiskPercent(partition, percent, hostname)
                        return alert.Slack(warn , 'Alarm', 'danger', 'high', str(date))

def JsonOut(filename, func, dictname):
	if jsonout=='enable':
		return jout.json_output(filename, func, dictname)
	elif jsonout=='disable':
		pass
	else:
		msg='json_out should be enable or disable'
		return 



def Main():
	CpuMsg()
	MemoryMsg()
	SwapMsg()
	DiskMsg()
	JsonOut('meminfo.json', x.MemoryUsage(), 'memory')
	es.Elastic()
if __name__ == '__main__':
	Main()
