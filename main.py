# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
   # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
import numpy as np
from scipy import sparse
file_path = '/Users/ruslan/Code/GeometricalFlow/octahedron.txt'
from faces import fases
Fases = []
with open(file_path) as fl_wth_fs:
    lines = fl_wth_fs.readlines()

for line in lines:
    ns_vx = line.rstrip('\n').split('\t') ## получили только числа из каждой строки
    a = int(ns_vx[0])
    b = int(ns_vx[1])
    c = int(ns_vx[2])
    Fases.append(fases(a,b,c))
row =[0,0,1,3,1,0,0]
col = [0,2,1,3,1,0,0]
data = []
# for fs in Fases:
#     row.append(fs[0])
#     col.append(fs[1])
#     row.append(fs[0])
#     col.append(fs[2])
#     row.append(fs[1])
#     col.append(fs[2])
#     break
[data.append(1) for i in range(len(row))]
spacerow = np.array(row)
spacecol = np.array(col)
sparcedata = np.array(data)
A = sparse.coo_matrix((sparcedata,(spacerow,spacecol)),shape=(4,4))
print(row)
print(col)
print(data)
print(A)