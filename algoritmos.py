# 1)
# Lista de calificaciones de Ana
calificaciones = [4.3, 2.1, 1.5, 4, 3.9, 3.2]

promedio = sum(calificaciones) / len(calificaciones)
if promedio >= 3.0:
    resultado = "Aprobado"
else:
    resultado = "No Aprobado"

print(f"Promedio: {promedio}")
print(f"Resultado: {resultado}")


# 4)

# Lista de velocidades en km/h y tiempos en minutos
registros = [
    (80, 10),
    (66, 20),
    (110, 8),
    (40, 5),
    (70, 30)
]
distancia_total = 0
for velocidad, tiempo in registros:
    tiempo_horas = tiempo / 60
    distancia = velocidad * tiempo_horas
    distancia_total += distancia

print(f"Distancia total recorrida: {distancia_total} km")


# 6)


# Lista de fechas de nacimiento (día, mes, año)
fechas_nacimiento = [
    (20, 10, 2000),
    (11, 2, 2017),
    (25, 9, 1998),
    (30, 3, 2005),
    (30, 12, 1976)
]

# Ingresar la fecha actual
dia_actual = int(input("Ingrese el día actual: "))
mes_actual = int(input("Ingrese el mes actual: "))
año_actual = int(input("Ingrese el año actual: "))

# Función para calcular edad y verificar cumpleaños


def calcular_edad(dia, mes, año):
    edad_años = año_actual - año
    edad_meses = mes_actual - mes
    edad_dias = dia_actual - dia

    # Ajuste de meses y días si el cumpleaños aún no ha pasado en el año actual
    if edad_dias < 0:
        edad_meses -= 1
        # Asumimos 30 días en el mes anterior para ajustar
        edad_dias += 30

    if edad_meses < 0:
        edad_años -= 1
        edad_meses += 12

    # Verifica si ya cumplió años este año
    ya_cumplio_este_año = (mes < mes_actual) or (
        mes == mes_actual and dia <= dia_actual)

    # Verifica si hoy es su cumpleaños
    hoy_cumple_años = (dia == dia_actual and mes == mes_actual)

    return edad_años, edad_meses, edad_dias, ya_cumplio_este_año, hoy_cumple_años


for dia, mes, año in fechas_nacimiento:
    edad_años, edad_meses, edad_dias, ya_cumplio_este_año, hoy_cumple_años = calcular_edad(
        dia, mes, año)
    print(f"Fecha de nacimiento: {dia}/{mes}/{año}")
    print(f"Edad: {edad_años} años, {edad_meses} meses, {edad_dias} días")
    print(f"Ya cumplió años este año: {'Sí' if ya_cumplio_este_año else 'No'}")
    print(f"Hoy es su cumpleaños: {
          'Sí, ¡feliz cumpleaños!' if hoy_cumple_años else 'No'}")
