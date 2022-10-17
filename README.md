# Trabajo de Programación 2
## Problema del Vendedor Viajero


1. Enunciado
<p stye="text-align: justify;">Se solicita desarrollar una aplicación que implemente el Problema del Vendedor Viajero a través del método de Sistema de Colonia de Hormigas utilizando el lenguajes de programación Python junto a las bibliotecas Numpy, Pandas, Sys y Time.

Primero se debe definir que estructura de datos se va a utilizar para modelar el problema con el objetivo de visitar de forma única un número N de ciudades. Por ejemplo, con grafos.

El código debe de tener al menos las siguientes funciones:</p>

- Generar un número real randómico entre [0, 1).
- Generar un número entero randómico entre [0, N].
- Inicializar una colonia de hormigas.
- Inicializar la feromona.
- Seleccionar el nuevo segmento de la ruta.
- Actualizar el nivel local de feromona.
Actualizar el nivel global de feromona.
- Evaluar la ruta generada por una hormiga.

Además, se debe ingresar y sintonizar los siguientes parámetros:

- Archivo de entrada.
- Valor semilla generador valores randómcos.
- Tamaño de la colonia o número de hormigas.
- Condición de término o número de iteraciones.
Factor de evaporación de la feromona ($\alpha$).
- El peso del valor de la heurística ($\beta$).
- Valor de probabilidad límite ($q_0$).

2. Programa

<p stye="text-align: justify;">El código debe ser desarrollado usando una metodología de programación modular, es decir,
debe haber un uso de funciones y/o métodos que implementen de forma genérica los principales
operadores, los cuales, serán usados en el programa principal.
El objetivo de esta implementación es poder crear una biblioteca de funciones y/o métodos que
puedan ser re-utilizados en cualquier otro programa que se pueda implementar en el futuro con
el correspondiente ahorro en tiempo y lineas de código.</p>