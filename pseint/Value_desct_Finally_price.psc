Algoritmo Value_desct_Finally_price
	Definir price_origin, desct, price_desct, price_finally Como Real
	Escribir "cuanto vale el producto originalmente?"
	Leer price_origin
	Escribir "Cuanto es el procentaje del descuento?"
	Leer desct
	price_desct <- price_origin * desct / 100
	price_finally <- price_origin - price_desct
	Escribir "el descuento del producto es de:  $" price_desct
	Escribir "El total que tiene que pagar el cliente es de: $" price_finally
FinAlgoritmo
