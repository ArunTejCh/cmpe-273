import psutil


for proc in psutil.net_connections(kind='inet4'):
    print(proc)