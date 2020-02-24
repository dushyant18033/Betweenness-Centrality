#SBC_2018033.py
#Date: 30-10-2018

#Name: DUSHYANT PANCHAL
#Roll No.: 2018033
#Section: A    Group: 1


from itertools import permutations


def genBFS(s,V,E):
	"""Returns Breadth First Search starting from s given
	the Vertices in a list V and Edges in a list E.

	Returned BFS is a slight variation of the actual BFS."""

	Ver=V[:]	#Creating a copy
	Ver.remove(s)
	#Ver will be used for marking the vertices as used.

	#BFS algorithm implementation
	bfs=list()
	start=[s]
	bfs.append(start)

	c=0
	while(len(Ver)>0):
		level=list()
		for i in bfs[c]:
			#print(c,i,level,bfs,'   ',Ver)
			for j in E:
				if(j[0]==i and (j[1] in Ver)):
					level.append(j[1])
					Ver.remove(j[1])
				elif(j[1]==i and (j[0] in Ver)):
					level.append(j[0])
					Ver.remove(j[0])
			#print(c,i,level,bfs,'   ',Ver)
			#print("")
		bfs.append(level)
		c+=1

	return bfs


def minDist(bfs,s,e):
	"""Returns the minimum distance
	(no. of hops) between s and e."""

	level=-1
	for i in range(len(bfs)):
		if(e in bfs[i]):
			level=i
	return level


def shortestPaths(V,E,bfs,s,e):
	"""Returns a list of shortest paths
	which are in the form of lists."""

	lev=minDist(bfs,s,e)
	#Getting min distance
	
	#Getting all the shortest paths
	BFS=bfs[1:lev]
	Ver=V[:]
	Ver.remove(s)
	Ver.remove(e)
	k=lev-1
	paths=list(permutations(Ver,k))
	validPaths=list()
	for j in paths:
		valid=True
		for i in range(k):
			if(j[i] not in BFS[i]):
				valid=False
				break
		if(valid):
			validPaths.append([s]+list(j)+[e])

	del paths

	possiblePaths=list()
	for i in validPaths:
		valid=True
		for j in range(k+1):
			if( not (([i[j],i[j+1]] in E) or ([i[j+1],i[j]] in E))):
				valid=False
				break
		if(valid):
			possiblePaths.append(i)

	del validPaths

	return possiblePaths


def bwCentrality(V,E,v):
	"""Returns the standard betweenness
	centrality of node v."""

	n=len(V)

	gv=0
	for s in range(n):
		if(V[s]!=v):
			bfs=genBFS(V[s],V,E)
			for e in range(s+1,n):
				if(V[e]!=v):
					P=shortestPaths(V,E,bfs,V[s],V[e])
					sig=len(P)
					sig_v=0
					for i in P:
						if(v in i):
							sig_v+=1
					#print(V[s],V[e],":",P,":",(sig_v,sig))
					gv+=(sig_v/sig)

	std_gv=(2*gv)/((n-1)*(n-2))

	return std_gv


def top_k(V,E):
	"""Returns top k nodes
	with max and equal SBC."""

	stanBWC=list()
	n=len(V)
	for i in range(n):
		stanBWC.append(bwCentrality(V,E,V[i]))
	M=max(stanBWC)	#Max SBC

	top=list()
	for i in range(n):
		if(stanBWC[i]==M):	#Check vertices having SBC=max SBC
			top.append(V[i])

	return top


if(__name__=="__main__"):	#If program is run
	V=list(map(int,input("Enter Vertices: ").split()))
	n=int(input("Enter number of edges: "))
	E=list()
	print("Now enter the edges:")
	for i in range(n):
		a,b=map(int,input().split())
		E.append([a,b])
	#Getting the inputs

	topk=top_k(V,E)
	print("Here are the top Vertices with equal BWC: ",topk)
	#Printing the Outputs