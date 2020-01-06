true = "true"
false = "false"
mydict = {"return": [{"arch": "x86", "current": true, "props": {"core-id": 0, "thread-id": 0, "socket-id": 0}, "CPU": 0, "qom_path": "/machine/unattached/device[0]", "pc": -1646216725, "halted": true, "thread_id": 2903}, {"arch": "x86", "current": false, "props": {"core-id": 0, "thread-id": 0, "socket-id": 1}, "CPU": 1, "qom_path": "/machine/unattached/device[2]", "pc": -1646216725, "halted": true, "thread_id": 2904}, {"arch": "x86", "current": false, "props": {"core-id": 0, "thread-id": 0, "socket-id": 2}, "CPU": 2, "qom_path": "/machine/unattached/device[3]", "pc": -1646216725, "halted": true, "thread_id": 2905}, {"arch": "x86", "current": false, "props": {"core-id": 0, "thread-id": 0, "socket-id": 3}, "CPU": 3, "qom_path": "/machine/unattached/device[4]", "pc": -1646216725, "halted": true, "thread_id": 2906}, {"arch": "x86", "current": false, "props": {"core-id": 0, "thread-id": 0, "socket-id": 4}, "CPU": 4, "qom_path": "/machine/unattached/device[5]", "pc": -1646216725, "halted": true, "thread_id": 2907}, {"arch": "x86", "current": false, "props": {"core-id": 0, "thread-id": 0, "socket-id": 5}, "CPU": 5, "qom_path": "/machine/unattached/device[6]", "pc": -1646216725, "halted": true, "thread_id": 2908}]}

#print(type(mydict))
list =[]
value = mydict['return']
#print(type(value))
for i in value:
    data = i["thread_id"]
    list.append(data)
print(list)
   # print(i["thread_id"])


#print(type(i))
   # for key,value in i.items():
       # print(key,value)
       # if key == "thread-id":
           # print(value)


