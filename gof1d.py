a=[0,0,0,0]
i=0
j=0

while(i<=len(a)-1):
	if(i==0):
		if(a[i+1]==1):
			a[i]=1
		else:
			a[i]=0	
		
		if(a[i-1]==a[i+1]):
			a[i]=0
		else:
			a[i]=1
		print a

		if(i==len(a)-1):
			if(a[i-1]==1):
				a[i]=1
			else:
				a[i]=0	
	else:
		i=i+1
print a
