nodes = [1,2,3,4,5]
    
left =1
right = 2
nodes[left-1:right] = nodes[right-1::-1]
print(nodes)