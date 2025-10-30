import psutil

threshold = 80

cpu = psutil.cpu_percent()
mem = psutil.virtual_memory().percent
disk = psutil.disk_usage('C:\\')

print(f'{cpu}')
print(f'{mem}')
print(f'{disk.percent}')


if  cpu > threshold:
    print( "cpu is greater then 80")

if  mem > threshold:
    print( "mem is greater then 80")

if  disk.percent > threshold:
    print( "disk is greater then 80")
