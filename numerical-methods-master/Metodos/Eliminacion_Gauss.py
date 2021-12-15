import time
import matplotlib.pyplot
import sympy
import numpy

class Eliminacion_Gauss():

	def gauss():
		print ('')
		print ('			ELIMINACIÓN GAUSS')
		print ('')
		m=int(input('Valor de filas:'))

		n=int(input('Valor de columnas:'))

		matrix = numpy.zeros((m,n))

		vector= numpy.zeros((n))
		x=numpy.zeros((m))

		con=0
		

		print ('Introduce la matriz de coeficientes y el vector solución')
		print ('')
		for r in range(0,m):
			con=con+1
			print('')
			print('ECUACION',con)
			for c in range(0,n):
				matrix[(r),(c)]=(input("Elemento a["+str(r+1)+","+str(c+1)+"] "))   
			vector[(r)]=(input('b['+str(r+1)+']: '))
		print(matrix)

		for k in range(0,m):
			print(k)
			for r in range(k+1,m):
				factor=(matrix[r,k]/matrix[k,k])
				print(factor)
				vector[r]=vector[r]-(factor*vector[k])
				print(vector)
				for c in range(0,n):
					matrix[r,c]=matrix[r,c]-(factor*matrix[k,c])
					print(matrix)
		
		
		
		#sustitución hacia atrás
		x[m-1]=vector[m-1]/matrix[m-1,m-1]
		print (x[m-1])
		print ("Valor antiguo")
		print (x)

		for r in range(m-2, -1,-1):
			suma=0
			for c in range(0,n):
				suma=suma+matrix[r,c]*x[c]
				print("suma:")
				print(suma)
			x[r]=(vector[r]-suma)/matrix[r,r]
			print("valor x registrado")
			print(x)
		print ('')
		print ('Resultado matriz')
		print(matrix)

		print ('')
		print ('Resultado del vector')
		print(vector)

		print ('')
		print ('Resultados:')
		print(x)
        
        