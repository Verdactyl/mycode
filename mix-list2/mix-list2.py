#!/usr/bin/env python3
#proto = ['ssh', 'http', 'https']
#print(proto)
#print(proto[1])
#proto.extend('dns')
#print(proto)


proto = ['ssh', 'http', 'https']

protoa = ['ssh', 'http', 'https']

print(proto)

proto.append('dns')

protoa.append('dns')


print(proto)

print(protoa)

proto2 = [ 22, 80, 443, 53 ]

proto.extend(proto2)
print("\nThis is what list.extend() did to our list.\nExtend iterated through proto2, and added each element to the end of our list (fancy way of saying it combined the lists).")
print (proto)

protoa.append(proto2)
print("\nThis is what list.append() did to our list.\nAppend opens up a SINGLE slot at the end of the list.")
print (protoa)

print(proto[4])

print(protoa[4][0])

