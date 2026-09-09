Algoritmo students_grades
	Definir  note1, note2, note3, result Como Real
	Definir  fullname Como Caracter
	fullname = ""
	note1 = 0
	note2 = 0
	note3= 0
	Escribir "enter her fullname"
	Leer fullname
	Escribir "Enter the firth note of the cort"
	Leer note1 
	Escribir "Enter the second note of the cort"
	Leer note2
	Escribir "Enter the third note of the cort"
	Leer note3
	result <- note1 * 0.3 + note2 * 0.3 + note3 * 0.4 
	Escribir "Buenas querido estudiante:" fullname "su nota total es de: " result
	Escribir "Grades Avereges is " , (note1 + note2 + note3) / 3
 	

FinAlgoritmo
