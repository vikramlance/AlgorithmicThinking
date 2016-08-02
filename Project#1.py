'''
Coursera course "Algorithmic Thinking Part 1"
Taught by professors of Rice University.

Week 1 - Project#1

Graph Basics and Random Digraphs
Degree Distributions for graphs

Author: Vikramsinh Jadhav
'''

"""
EX_GRAPH0, EX_GRAPH1, EX_GRAPH2 - Define three constants whose values are dictionaries corresponding to the three directed graphs shown in
these linked diagrams: EX_GRAPH0, EX_GRAPH1, and EX_GRAPH2.
"""
#directed graphs 
EX_GRAPH0 = {0:[1,2],
             1:[],
             2:[]}

print EX_GRAPH0


EX_GRAPH1={0:[1,4,5],
           1:[2,6],
           2:[3],
           3:[0],
           4:[1],
           5:[2],
           6:[]}

print EX_GRAPH1


EX_GRAPH2 = {0: [1,4,5], 
          1: [2,6],
          2: [3,7],
          3: [7],
          4: [1],
          5: [2],
          6: [],
          7: [3],
          8: [1,2],
          9: [0,3,4,5,6,7]}
print EX_GRAPH2

num_nodes= int(raw_input().strip())

for i in range():
print n

if n<=0:
	result_graph=
