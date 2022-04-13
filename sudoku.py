# Autor: Luis Corbacho Flores
# Nombre del fichero: sudoku.py
# Bloque: 09

# Colocar aquí el código:
import matrices

def sudoku_legal(archivo):
    #utiliza las funciones que definiremos posteriormente para comprobar si el sudoku funciona
    sudoku=leer_sudoku(archivo)
    if comprobar_sudoku(sudoku)==True:
        if submatrices(sudoku)==True:
            #le he puesto print porque al escribirlo sobre el .txt el sudoku queda INUTIL 
            print ('Es valido')

def comprobar_sudoku(matriz):
    #comprueba las filas y las columnas del sudoku
    contador=0
    lineas=0
    columnas=0
    #comprueba las filas
    for linea in range(len(matriz)):
        for numero in range(0,10):
            if matriz[linea].count(numero)==1:
                contador=contador+1
        if contador==9:
            lineas=1
    #comprueba las columnas
    contador=0
    matriz_transpuesta=matrices.transpuesta_matriz(matriz)
    for linea in range(len(matriz_transpuesta)):
        for numero in range(0,10):
            if matriz_transpuesta[linea].count(numero)==1:
                contador=contador+1
        if contador==9:
            columnas=1
    #si las filas y columnas no tienen nigun fallo lo devuelve como TRUE
    if lineas==1 and columnas==1:
        return True
    else:
        return False

def leer_sudoku(archivo):
        #funcion para obtener el sudoku, creando una matriz nueva a partir de la lectura del archivo
	file=open(archivo)
	sudoku_letras=file.readlines()
	sudoku_numeros=[]
	sudoku_letras[0]=sudoku_letras[0].replace('\ufeff','')

	#sustituir caracteres vacios, dejar solo numeros en string
	for i in range((len(sudoku_letras))):
		for j in range(len(sudoku_letras[i])-1):
                    #esta linea de debajo es para evitar fallos del tipo 'out of range'
			if j>=len(sudoku_letras[i]):
				pass
			elif sudoku_letras[i][j] not in '123456789':
				sudoku_letras[i]=sudoku_letras[i].replace(sudoku_letras[i][j],'')
				
	#sudoku en forma de matriz
	for i in range((len(sudoku_letras))):
		sudoku_numeros.append([])
		for j in range((len(sudoku_letras[i]))):
			sudoku_numeros[i].append(int(sudoku_letras[i][j]))
	return sudoku_numeros

def submatrices(sudoku):
    #para buscar repeticiones en grupos de 3x3 en el sudoku
	submatriz=[]
	contador=0
	contador2=0
	#Para obtener las submatrices de 3x3 procedemos
	for linea in range(0,3):
		for columnas in range(0,3):
			submatriz=submatriz+sudoku[linea*3][columnas*3:columnas*3+3]+sudoku[linea*3+1][columnas*3:columnas*3+3]+sudoku[linea*3+2][columnas*3:columnas*3+3]
			for num in [1,2,3,4,5,6,7,8,9]:
				if submatriz.count(num)==1:
					contador=contador+1
			submatriz=[]
	if contador==81:
	    return True
	else:
		return False

    
# Comprobación del código

if __name__ == '__main__':
    sudoku_legal('sudoku_1.txt')
    sud = [[3, 2, 9, 6, 1, 5, 7, 8, 4], [4, 8, 5, 2, 3, 7, 1, 6, 9], [1, 6, 7, 9, 8, 4, 2, 5, 3],
              [6, 3, 2, 4, 9, 1, 5, 7, 8], [5, 9, 1, 8, 7, 6, 4, 3, 2], [7, 4, 8, 5, 2, 3, 9, 1, 6],
              [8, 5, 4, 7, 6, 2, 3, 9, 1], [9, 7, 3, 1, 4, 8, 6, 2, 5], [2, 1, 6, 3, 5, 9, 8, 4, 7]]
    sudoku_legal('sudoku_2.txt')
