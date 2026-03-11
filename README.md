# reto01_calculadora_sumas

Programa en Python que lee lineas de texto con numeros separados por comas desde la entrada estandar, limpia los valores y retorna la suma de los enteros truncados por cada linea.

---

## Como ejecutar

### Ejecucion basica con archivo de texto

```bash
python3 main.py < tests/entrada1.txt
```

### Guardar el resultado en un archivo de salida

```bash
python3 main.py < tests/entrada1.txt > tests/salida1.txt
```

### Ingresar datos manualmente desde la terminal

```bash
python3 main.py
```
Escribe cada linea y presiona Enter. Al terminar presiona `Ctrl + D`.

---

## Reglas de limpieza

- Los valores se separan por comas
- Se eliminan espacios en blanco
- Se eliminan letras y caracteres especiales (`$`, `%`, `#`, etc.)
- Los numeros decimales se truncan a entero (no se redondean)
- Los valores vacios o con solo letras cuentan como `0`
- Se suman todos los enteros de cada linea y se imprime el resultado

---

## Ejemplo de entrada y salida

**Entrada** (`tests/entrada1.txt`):
```
1,2,3
1.9,2.1,3.7
1a2,3b,4
-5,10,3
  5 , 10 , 15  
abc,def
,1,2,
100
```

**Salida** (`tests/salida1.txt`):
```
6
6
19
8
30
0
3
100
```

---

## Estructura del proyecto

```
reto-semana-01/
├── README.md           # Documentacion del proyecto
├── main.py             # Solucion principal
├── .gitignore          # Archivos a ignorar
└── tests/
    ├── entrada1.txt    # Archivo de prueba basico
    ├── salida1.txt     # Salida esperada basica
    ├── entrada2.txt    # Archivo de prueba con datos sucios
    └── salida2.txt     # Salida esperada datos sucios
```

---

## Autor

**Diego Jehu Bustamante Villanueva**