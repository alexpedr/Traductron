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
Traductron, como su propio nombre indica, traduce el Lenguaje de Signos Español a audio mediante una cámara.

El robot tiene la cámara en un brazo móvil. Este brazo baja y sube en función de la posición que capta del tronco superior (utilizando MediaPipe). Traductron también gira a la derecha o a la izquierda sobre sí mismo, así nunca perderá a la persona.

Si cuando el robot se enciende no encuentra a la persona, gira sobre sí mismo hasta encontrarla y realiza el procedimiento anterior para no perderla. Una vez encontrada, hace la traducción detectando la mano mediante MediPipe y la emite por el altavoz y repite el proceso en bucle.  


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

<a href="url"><img src="https://user-images.githubusercontent.com/57665176/171011130-dd06c393-af70-4386-a4d5-11338f93fd95.PNG" align="center" height="115" width="419" ></a>

No son los ideales, ya que tuvimos que escogerlos al principio del proyecto y no sabíamos bien bien cuáles iban mejor con nuestro software. También teníamos que adaptarnos a un presupuesto de 100 € proporcionado por la universidad.

Cabe destacar que, como usamos Mediapipe, la raspberry pi zero no es aconsejable usarla, por el hecho de que no se puede instalar esta librería en ella.

## Circuito Hardware <a name="id9"></a>
Este es un circuito orientativo con nuestros componentes.

<a href="url"><img src="https://user-images.githubusercontent.com/57665176/170707822-0ee75ba9-1f03-48e8-b06b-94847864b0e3.PNG" align="center" height="358" width="471" ></a>


## Arquitectura Sofware<a name="id10"></a>
Así es como funciona nuesto robot traductron. Está dividido en los siguientes módulos:

<a href="url"><img src="https://user-images.githubusercontent.com/57665176/171006682-3404a4f9-b8d8-4c44-bbd7-9720db8c90f6.PNG" align="center" height="245" width="677" ></a>

1. Camara
Cada 1,5 segundos aproximadamente la camara toma fotos y estas se pasan al módulo de detector de tronco superior.

2. Detector tronco superior

<a href="url"><img src="https://user-images.githubusercontent.com/57665176/171008763-ee81b8cc-e71a-47a1-8d8e-13ab42bcea85.png" align="right" height="291" width="407" ></a>

Para realizar el movimiento de desplazamiento del robot y el de subir y bajar el brazo con la cámara, usamos también la librería MediaPipe, en este caso la opción de detectar solo el tronco superior.

De esta manera, creamos un documento de texto en el cual escribiremos 8 movimientos:


- Left - Up
- Left- Down
- Left
- Up
- Down
- Right - Up
- Right - Down
- Right

Este documento se pasa al módulo de movimiento.

3. Movimiento

A partir de los valores del documento, el robot se moverá de manera correspondiente. Una vez posicionado, se accede al módulo de detector de manos y traducción. Y se repite el procedimiento en bucle.

4. Detector de manos
<a href="url"><img src="https://user-images.githubusercontent.com/57665176/171010112-c993ec96-3af0-47db-855d-b3464167c791.PNG" align="right" height="210" width="219" ></a>

A partir de la librería “MediaPipe”, detectamos los puntos de control de la mano y concretamente las coordenadas X e Y de cada uno de los puntos. Con este detector creamos de 0 nuestro dataset para poder entrenar posteriormente la Red Neuronal. 



5. Red Neuronal

A través de la librería sklearn podemos entrenar una red neuronal con la función MLPclassifier() donde le pasamos el Dataset con todas las letras y sus respectivas etiquetas. 

6. Salida de audio 

A través de las librerías gtts y playsound podemos reproducir, mediante audio, las letras en signos que le vayamos enseñando a la cámara. 
Creamos una función que, pasada la etiqueta de la letra, la pase al código ASCII y después la convierta a tipo char. Una vez hecho esto, le pasamos la letra a la función gTTS(), que grabará el audio en español. Guardamos el resultado en un archivo .mp3 y después con la función playsound() reproducimos el audio. 


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
    > Utilizamos este archivo para crear el DataSet, utilizando el findDetector.
  - 3.2. Ejecutamos el archivo "concatenarTablas.py"
    > Creamos un único archivo con todos los valores de las letras que hemos generado anteriormente.
  - 3.3. Ejecutamos el archivo  "redNeuronal.py"
    > Nos devuelve un valor de Accuracy para poder analizar la precisión de nuestro detector y generar un archivo sav que será la red neuronal que se utilizará.
  - 3.4. Ejecutamos el archivo "intentoTraductorFinal.py"
    > Utilizamos de nuevo el handDetector para el momento de detectar los puntos y comparamos con los valores que tenemos en el dataSet y reproducimos por audio.
 
 Una vez ejecutados estos archivos con el último de ellos podemos empezar a traducir
 
 (Los puntos 3.1, 3.2 y 3.3 no son necesarios de ejecutar, ya que proporcionamos una red neuronal y un dataset).

  4. En el caso de no disponer de una raspberry pi 3 o 4, como en nuestro caso, puedes usar las carpetas CLIENTE y SERVIDOR. El cliente se guardará en la raspberry y el servidor en tu ordenador. 
 
El cliente coje una fotografía creada por la cámara, la guarda y la envía al ordenador mediante sockets. El ordenador usará MediaPipe sobre esa foto recibida, clasifica ese signo y envía el resultado al altavoz. Una vez hecho esto, detecta el tronco superior y dependiendo de la posición de la persona, enviará un documento de texto u otro al módulo de movimiento, que se encuentra en la raspberry.
    


## Autores <a name="id6"></a>

- Àlex Pedrola González
- Susana Sánchez Ropero
- Paula Martín Merino
- Pablo Ezequiel Britos

## Bibliografía <a name="id7"></a>
This project has been inspired by the following Internet projects:

- [https://www.xataka.com/aplicaciones/asi-showleap-traductor-lengua-signos-a-texto-voz-tiempo-real-esta-cada-vez-cerca ](https://www.xataka.com/aplicaciones/asi-showleap-traductor-lengua-signos-a-texto-voz-tiempo-real-esta-cada-vez-cerca )


