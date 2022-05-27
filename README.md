# Traductron

**Tabla de contenidos**
- [¿Qué es esto?](#id0)
- [Objetivo](#id8)
- [Componentes](#id1)
- [Circuito Hardware](#id9)
- [Arquitectura Sofware](#id10)
- [Documentación](#id2)
- [Modo de empleo](#id3)
- [Planificación de rutas](#id4)
- [Seguimiento de rutas](#id5)
- [Autores](#id6)
- [Bibliografía](#id7)


## ¿Qué es esto? <a name="id0"></a>
Traductron es un robot móvil que dispone de un brazo con cámara. Este gira sobre si mismo hasta localizar a una persona, cuando lo hace, procede a hacer la traducción del Lenguaje de Signos Español y emitirlo en audio. 

## Objetivo <a name="id8"></a>
Nuestro objetivo es facilitar a las personas que se comunican mediante Lenguaje de Signos a mantener conversaciones con otras que no conozcan el lenguaje.

Buscamos que este colectivo gane independencia y que no tenga que disponer de un intérprete o de un familiar para poder hacer tareas cuotidianas como por ejemplo, ir a hacer una transacción a un banco. 

## Componentes <a name="id1"></a>
El hardware que hemos usado para nuestro robot prototipo son los siguientes:

- 2 Motores Micro Metal LP
- 2 Ruedas base 
- Controlador de motores L289n
- Motor paso a paso 28BYJ-48
- Raspberry pi zero
- Cámara raspberry pi 
- Altavoz
- Amplificador
- Power Bank
- Pilas 9V
- Rueda loca metálica 
- Piezas 3D

No son los ideales, ya que tuvimos que escogerlos al principio del proyecto y no sabíamos bien bien cuáles iban mejor con nuestro software. También teníamos que adaptarnos a un presupuesto de 100 € proporcionado por la universidad.

Cabe destacar que, como usamos Mediapipe, la raspberry pi zero no es aconsejable usarla, por el hecho de que no se puede instalar esta librería en ella.

## Circuito Hardware <a name="id9"></a>
Este es un circuito orientativo con nuestros componentes.
![HW traductron](https://user-images.githubusercontent.com/57665176/170707822-0ee75ba9-1f03-48e8-b06b-94847864b0e3.PNG)

## Arquitectura Sofware<a name="id10"></a>
Así es como funciona nuesto robot traductron. Esta dividido en los siguientes módulos:
![image](https://user-images.githubusercontent.com/104013393/170675185-498d200d-2c50-49bb-8465-f29e686f25ff.png)

## Librerías usadas<a name="id10"></a>
- numpy
- pandas
- gTTs
- playSound
- cv2
- mediapipe
- pickle
- sklearn
- math
- copy
- time

## Documentación <a name="id2"></a>
Traductron, de momento, solo realiza la traducción del abecedario del Lenguaje de Signos Español.

![LENGUAJE SIGNOS](https://user-images.githubusercontent.com/57665176/170559218-840539d5-3058-4434-80e0-c771af3a1851.jpg)

Para poder hacer esto de manera correcta, tuvimos que hacer algunos cambios.

1. Hacer las letras sin movimiento, ya que no pudimos procesarlo.
2. Eliminamos las letras no necesárias, como: 'LL' y 'CH'.
3. Modificamos los signos de letras las letras que se confundian con otras.
4. Así ha quedado el abecedario que traduce Traductron.

![LENGUAJE SIGNOS FINAL](https://user-images.githubusercontent.com/57665176/170559192-c9fcc1f4-8eb7-46c4-975d-41c1d67e6dec.jpg)

## Modo de empleo <a name="id3"></a
En el caso de ejecutarlo en ordenador: 
1. Clonar  repositorio
2. Instalar librerias necesarias
3. Ejecutar los archivos en el siguiente orden
  3.1  Ejecutamos archivo "pythonPrueba2.py"
  3.2 Ejecutamos el archivo "concatenarTablas.py"
  3.3 Ejecutamos el archivo  "redNeuronal.py"
  3.4 Ejecutamos el archivo  "altavoz.py"
  3.5 Ejecutamos el archivo "intentoTraductorFinal.py"
Una vez ejecutados estos archivos con el último de ellos podemos empezar a traducir

## Planificación de rutas <a name="id4"></a>
como esta organozado el codigo

## Seguimiento de rutas <a name="id5"></a>

## Autores <a name="id6"></a>

Àlex Pedrola González
Susana Sánchez Ropero
Paula Martín Merino
Pablo Ezequiel Britos

## Bibliografía <a name="id7"></a>

