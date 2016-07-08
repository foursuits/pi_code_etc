# this code is not mine; taken from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

def mergeSort(L):

	print("Splitting ",L)
	if len(L)>1:
		mid = len(L)//2
		lefthalf = L[:mid]
		righthalf = L[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

	i=0
	j=0
	k=0
	'''
	while i < len(lefthalf) and j < len(righthalf):
	    if lefthalf[i] < righthalf[j]:
		L[k]=lefthalf[i]
		i=i+1
	    else:
		L[k]=righthalf[j]
		j=j+1
	    k=k+1

	while i < len(lefthalf):
	    L[k]=lefthalf[i]
	    i=i+1
	    k=k+1

	while j < len(righthalf):
	    L[k]=righthalf[j]
	    j=j+1
	    k=k+1
	'''
	while i < len(L)-1:
		if lefthalf[j] < righthalf[k]:
			L[i] = lefthalf[j]
			j += 1 		
			i += 1 
	   	if lefthalf[j] >= righthalf[k]:
			L[i] = righthalf[k]
			k += 1 		 
			i += 1 
	print("Merging ",L)

L = [54,26,93,17,77,31,44,55,20]
mergeSort(L)
print(L)

