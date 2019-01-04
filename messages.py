from blessings import Terminal

def DiskPercent(partition, percent, hostname):
	warn =  partition +' has reached '+ str(percent)+ '%'+' on '+ hostname
	return warn

def MemoryPercent(percent, hostname):
	percent=percent
	hostname=hostname
	danger="The memory usage has reached "+str(percent)+"% on "+hostname 
	return danger

def SwapPercent(percent, hostname):
	danger="The swap usage has reached "+str(percent)+"% on "+hostname
	return danger

def CpuLoadAvg(avarage, hostname):
	danger="average cpu load is "+str(avarage)+" on "+hostname
	return danger

#print CpuLoadAvg("20", "backup.remal.com")
