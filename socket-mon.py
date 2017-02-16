import psutil
import operator

dic = {}
conns = psutil.net_connections(kind='tcp')
for proc in conns:
    if len(proc.laddr) > 0 and len(proc.raddr) > 0:
        if not proc.pid in dic:
            dic[proc.pid] = 1
        else:
            dic[proc.pid] += 1
#print dic
noOfConns =[]
for key, val in dic.items():
    noOfConns.append((key,val))

noOfConns.sort(key=operator.itemgetter(1), reverse=True)

#print noOfConns

print '"pid",  "laddr",  "raddr",  "status"'

for i,e in enumerate(noOfConns):
    for proc in conns:
        if e[0] == proc.pid and len(proc.laddr) > 0 and len(proc.raddr) > 0:
            print '"'+str(proc.pid)+ '", "' + proc.laddr[0]+ '", "' + proc.raddr[0]+ '", "' + proc.status +'"'

