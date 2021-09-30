array1 = [4,-2,6]
array2 = [8,0,1]

array3 = [[0,1],[5,9]]
array4 = [[5,6],[8,11]]

def dotProductVectors(A, B):
	resultado = 0
	if len(A)== len(B):
		print ("Same lenght on rows")
		for item in range (0,len(A)):
			resultado += A[item]* B[item]
		print(resultado)
	else:
		print("Not the same lenght")


def matrixMultiplication(A, B):
	# structure :   A(mxn) ,B(nxp) reuslting in AB(mxp)
	# first rows then columns

	# dot product of rows and collums

dotProduct(array1, array2)
