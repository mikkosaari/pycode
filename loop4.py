i=0 
l=0
k=0
A=[0,0,0,0]
while(i<=3):
	
	l=i
	while(l>=0):   
		if(l>0):		
			k=l-1
			A[3-l]=A[3-k]	
			A[3]=1
			print A
		else:		
			A[3-l]=A[3]	
			A[3]=1
			print A
		l=l-1
	i=i+1

