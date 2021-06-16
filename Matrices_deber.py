print('Ingresa el orden de su Matriz 1')
filas1,columnas1 = int(input()),int(input())
print('Ingresa el orden de su Matriz 2')
filas2,columnas2 = int(input()),int(input())

if (columnas1==filas2):

	matriz1 = []
	for i in range(filas1):
		matriz1.append( [0] * columnas1 )

	matriz2 = []
	for i in range(filas2):
		matriz2.append( [0] * columnas2 )

	print ("Ingrese su Matriz 1")
	for i in range(filas1):
		for j in range(columnas1):
			matriz1[i][j] = float(input('Elemento (%d,%d): ' % (i, j)))
	print ('Ingrese su Matriz 2')
	for i in range(filas2):
		for j in range(columnas2):
			matriz2[i][j] = float(input('Elemento (%d,%d): ' % (i, j)))

	matriz3 = []
	for i in range(filas1):
		matriz3.append( [0] * columnas2 )

	for i in range(filas1):
		for j in range(columnas2):
			for k in range(filas2):
				matriz3[i][j] += matriz1[i][k] * matriz2[k][j]
	print ('Su matriz resultante es',matriz3)
	
else:
	print ('Recurda la multiplicacion entre matrices debe ser mxn * nxp')