# Traductron

<a href="url"><img src="https://user-images.githubusercontent.com/57665176/170719939-f24a5a6c-30c8-458a-a3c1-5ee5665f3a2b.jpeg" align="right" height="284" width="220" ></a>

**Tabla de contenidos**
- [¿Qué es esto?](#id0)
- [Objetivo](#id8)
- [Componentes](#id1)
- [Circuito Hardware](#id9)
- [Arquitectura Sofware](#id10)
- [Requisitos](#id11)
- [Documentación](#id2)
- [Modo de empleo](#id3)
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

<a href="url"><img src="https://user-images.githubusercontent.com/57665176/170707822-0ee75ba9-1f03-48e8-b06b-94847864b0e3.PNG" height="358" width="471" ></a>


## Arquitectura Sofware<a name="id10"></a>
Así es como funciona nuesto robot traductron. Esta dividido en los siguientes módulos:

<a href="url"><img src="https://user-images.githubusercontent.com/104013393/170675185-498d200d-2c50-49bb-8465-f29e686f25ff.png" height="132" width="727" ></a>


## Requisitos <a name="id11"></a>
- [NumPy](https://numpy.org/)
- [Pandas](https://aprendeconalf.es/docencia/python/manual/pandas/)
- [gTTs](https://pypi.org/project/gTTS/)
- [playSound](https://pypi.org/project/playsound/)
- [cv2](https://pypi.org/project/cv2-tools/)
- [MediaPipe](https://pypi.org/project/mediapipe/)
- [Pickle](https://docs.python.org/es/3/library/pickle.html)
- [sklearn](https://scikit-learn.org/stable/install.html)
- [Math](https://docs.python.org/es/3.10/library/math.html)
- [Copy](https://docs.python.org/es/3/library/copy.html)
- [Time](https://docs.python.org/es/3/library/time.html)

## Documentación <a name="id2"></a>
Traductron, de momento, solo realiza la traducción del abecedario del Lenguaje de Signos Español.

<a href="url"><img src="https://user-images.githubusercontent.com/57665176/170559218-840539d5-3058-4434-80e0-c771af3a1851.jpg" height="268" width="524" ></a>


Para poder hacer esto de manera correcta, tuvimos que hacer algunos cambios.

1. Hacer las letras sin movimiento, ya que no pudimos procesarlo.
2. Eliminamos las letras no necesárias, como: 'LL', 'RR', 'Ñ' y 'CH'.
3. Modificamos los signos de letras las letras que se confundian con otras.
4. Así ha quedado el abecedario que traduce Traductron.

<a href="url"><img src="https://user-images.githubusercontent.com/57665176/170559192-c9fcc1f4-8eb7-46c4-975d-41c1d67e6dec.jpg" height="268" width="524" ></a>



## Modo de empleo <a name="id3"></a>

En el caso de ejecutarlo en ordenador: 

1. Clonar  repositorio
2. Instalar librerias necesarias
3. Ejecutar los archivos en el siguiente orden:

  - 3.1.  Ejecutamos archivo "pythonPrueba2.py
    > Utilizamos este archivo par crear el DataSet, utilizando el findDetector.
  - 3.2. Ejecutamos el archivo "concatenarTablas.py"
    > Creamos un únicho archivo con todos los valores de las letras que hemos generado anteriormente.
  - 3.3. Ejecutamos el archivo  "redNeuronal.py"
    > Nos devuelve un valor de Accuracy para poder analizar la precisión de nuestro detector.
  - 3.4. Ejecutamos el archivo  "altavoz.py"
  - 3.5. Ejecutamos el archivo "intentoTraductorFinal.py"
    > Utilizamos el de nuevo el handDetector para en el momento detectar los puntos y comparmos con los valores que tenemos en el dataSet y reproducimos por audio.
  
Una vez ejecutados estos archivos con el último de ellos podemos empezar a traducir


## Autores <a name="id6"></a>

- Àlex Pedrola González
- Susana Sánchez Ropero
- Paula Martín Merino
- Pablo Ezequiel Britos

## Bibliografía <a name="id7"></a>
This project has been inspired by the following Internet projects:

- [https://www.xataka.com/aplicaciones/asi-showleap-traductor-lengua-signos-a-texto-voz-tiempo-real-esta-cada-vez-cerca ](https://www.xataka.com/aplicaciones/asi-showleap-traductor-lengua-signos-a-texto-voz-tiempo-real-esta-cada-vez-cerca )


