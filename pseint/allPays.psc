Algoritmo allPays
    Definir nameProduct Como Cadena
    Definir priceUnit, allPay Como Real
    Definir cant Como Entero
    
    Escribir "Ingrese el nombre del producto:"
    Leer nameProduct
    
    Escribir "Ingrese el precio unitario:"
    Leer priceUnit
    
    Escribir "Ingrese la cantidad comprada:"
    Leer cant
    
    allPay = priceUnit * cant
    
    Escribir "Producto: ", nameProduct
    Escribir "Total a pagar: $", allPay
FinAlgoritmo
