# Este es un programa para calcular la nota promedio de tres examenes. 

# Pedirle las notas de los tres examenes al estudiante.
primer_examen = float(input("Ingrese la nota del primer examen: "))
segundo_examen = float(input("Ingrese la nota del segundo examen: "))
tercer_examen = float(input("Ingrese la nota del tercer examen: "))

# Calcular la suma de las notas de los tres examenes.
suma = primer_examen + segundo_examen + tercer_examen

# Calcular el promedio
promedio = suma / 3

# Verificar si el estudiante esta aprobado y darle el resultado.
if promedio >= 5:
    print("Su promedio es: ", promedio, "y por lo tanto esta APROBADO")
else:
    print("Su promedio es: ", promedio, "y por lo tanto esta REPROBADO")
