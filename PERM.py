A=[0,0,0,0]
B=[1,2]
k=3
j=0
l=1
def f(A,B,k,j,l):
	while(j<=1):	
		if(j==0):
			while(l<=3):		
				A[3]=B[j]
				A[3-l]=A[3]
				l=l+1
				print A
		
				f(A,B,k,j,l)
		elif(j==0):
			while(l<=3):		
			
				A[3]=B[j]
				A[3-l]=A[3]
				l=l+1
				print A

				f(A,B,k,j,l)
		j=j+1
f(A,B,k,j,l)















	
