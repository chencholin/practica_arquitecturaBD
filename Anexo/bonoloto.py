
import collections
import statistics as stats
import feedparser


FEED_URL = "https://www.loteriasyapuestas.es/es/bonoloto/resultados/.formatoRSS"


def parse_feed(FEED_URL):
    feed = feedparser.parse(FEED_URL)
    raw_date = feed.entries[1]["title"]
    raw_text = feed.entries[1]["description"]
    return raw_date, raw_text


def parse_feed2(FEED_URL):
    feed = feedparser.parse(FEED_URL)
    raw_date = feed.entries[2]["title"]
    raw_text = feed.entries[2]["description"]
    return raw_date, raw_text


def parse_feed4(FEED_URL):
    feed = feedparser.parse(FEED_URL)
    raw_date = feed.entries[4]["title"]
    raw_text = feed.entries[4]["description"]
    return raw_date, raw_text


def parse_feed6(FEED_URL):
    feed = feedparser.parse(FEED_URL)
    raw_date = feed.entries[6]["title"]
    raw_text = feed.entries[6]["description"]
    return raw_date, raw_text


def parse_feed8(FEED_URL):
    feed = feedparser.parse(FEED_URL)
    raw_date = feed.entries[8]["title"]
    raw_text = feed.entries[8]["description"]
    return raw_date, raw_text


def parse_feed10(FEED_URL):
    feed = feedparser.parse(FEED_URL)
    raw_date = feed.entries[10]["title"]
    raw_text = feed.entries[10]["description"]
    return raw_date, raw_text


def parse_feed12(FEED_URL):
    feed = feedparser.parse(FEED_URL)
    raw_date = feed.entries[12]["title"]
    raw_text = feed.entries[12]["description"]
    return raw_date, raw_text


def combinacion():
    raw_text = parse_feed(FEED_URL)[1]
    start = raw_text.find("<b>") + 3
    stop = raw_text.find("</b>")
    raw_numbers = raw_text[start:stop]
    numbers = []
    string_numbers = raw_numbers.split(" - ")
    for number in string_numbers:
        numbers.append(int(number))
    return numbers


def combinacion2():
    raw_text = parse_feed2(FEED_URL)[1]
    start = raw_text.find("<b>") + 3
    stop = raw_text.find("</b>")
    raw_numbers = raw_text[start:stop]
    numbers = []
    string_numbers = raw_numbers.split(" - ")
    for number in string_numbers:
        numbers.append(int(number))
    return numbers
    numero = number


def combinacion4():
    raw_text = parse_feed4(FEED_URL)[1]
    start = raw_text.find("<b>") + 3
    stop = raw_text.find("</b>")
    raw_numbers = raw_text[start:stop]
    numbers = []
    string_numbers = raw_numbers.split(" - ")
    for number in string_numbers:
        numbers.append(int(number))
    return numbers


def combinacion6():
    raw_text = parse_feed6(FEED_URL)[1]
    start = raw_text.find("<b>") + 3
    stop = raw_text.find("</b>")
    raw_numbers = raw_text[start:stop]
    numbers = []
    string_numbers = raw_numbers.split(" - ")
    for number in string_numbers:
        numbers.append(int(number))
    return numbers


def combinacion8():
    raw_text = parse_feed8(FEED_URL)[1]
    start = raw_text.find("<b>") + 3
    stop = raw_text.find("</b>")
    raw_numbers = raw_text[start:stop]
    numbers = []
    string_numbers = raw_numbers.split(" - ")
    for number in string_numbers:
        numbers.append(int(number))
    return numbers


def combinacion10():
    raw_text = parse_feed10(FEED_URL)[1]
    start = raw_text.find("<b>") + 3
    stop = raw_text.find("</b>")
    raw_numbers = raw_text[start:stop]
    numbers = []
    string_numbers = raw_numbers.split(" - ")
    for number in string_numbers:
        numbers.append(int(number))
    return numbers


def combinacion12():
    raw_text = parse_feed12(FEED_URL)[1]
    start = raw_text.find("<b>") + 3
    stop = raw_text.find("</b>")
    raw_numbers = raw_text[start:stop]
    numbers = []
    string_numbers = raw_numbers.split(" - ")
    for number in string_numbers:
        numbers.append(int(number))
    return numbers


def reintegro():
    raw_text = parse_feed(FEED_URL)[1]
    start = raw_text.find("R(") + 2
    stop = raw_text.find(")</b>", start)
    raw_reintegro = raw_text[start:stop]
    return raw_reintegro


def complementario():
    raw_text = parse_feed(FEED_URL)[1]
    start = raw_text.find("C(") + 2
    stop = raw_text.find(")</b>", start)
    raw_complementario = raw_text[start:stop]
    return raw_complementario


def joker():
    raw_text = parse_feed(FEED_URL)[1]
    start = raw_text.find("J(") + 2
    stop = raw_text.find(")</b>", start)
    raw_joker = raw_text[start:stop]
    return raw_joker


def fecha():
    raw_date = parse_feed(FEED_URL)[0]
    return raw_date


def is_updated():
    if ultimo_sorteo.count() >= 1:
        ultimo_sorteo_en_db = ultimo_sorteo.distinct("fecha")[0]
        if ultimo_sorteo_en_db == fecha():
            return False
        return True
    else:
        return True

# Definicion variables


uno = combinacion()
dos = combinacion2()
tres = combinacion4()
cuatro = combinacion6()
cinco = combinacion8()
seis = combinacion10()
siete = combinacion12()
suma_todas = uno+dos+tres+cuatro+cinco+seis+siete
# modificado

repetido_uno = combinacion()+combinacion2()
repetido_dos = combinacion()+combinacion2()+(combinacion4())
repetido_tres = combinacion()+combinacion2()+(combinacion4())+(combinacion6())
repetido_cuatro = combinacion()+combinacion2()+(combinacion4()) + \
    (combinacion6())+(combinacion8())
repetido_cinco = combinacion()+combinacion2()+(combinacion4()) + \
    (combinacion6())+(combinacion8())+(combinacion10())
repetido_seis = combinacion()+combinacion2()+(combinacion4())+(combinacion6()) + \
    (combinacion8())+(combinacion10())+(combinacion12())

# Funcion para sacar la media de 7 sorteos

suma_aritmetica_siete = stats.mean(combinacion()) + \
    stats.mean(combinacion2())+stats.mean(combinacion4()) + \
    stats.mean(combinacion6())+stats.mean(combinacion8()) + \
    stats.mean(combinacion10())+stats.mean(combinacion12())

suma_aritmetica_seis = stats.mean(combinacion()) + \
    stats.mean(combinacion2())+stats.mean(combinacion4()) + \
    stats.mean(combinacion6())+stats.mean(combinacion8()) + \
    stats.mean(combinacion10())

ari_siete = stats.mean(combinacion()+combinacion2()+combinacion4() +
                       combinacion6()+combinacion8()+combinacion10()+combinacion12())
ari_seis = stats.mean(combinacion()+combinacion2()+combinacion4() +
                      combinacion6()+combinacion8()+combinacion10())


# OPCION 1: Extraer numeros


def extraer_combinaciones():
    fecha2 = str(fecha())
    salida = str(combinacion())
    salida2 = str(combinacion2())
    salida3 = str(combinacion4())
    salida4 = str(combinacion6())
    salida5 = str(combinacion8())
    salida6 = str(combinacion10())
    salida7 = str(combinacion12())

    return "COMBINACIONES: \n{0} : {1} \n{2} \n{3} \n{4} \n{5} \n{6} \n{7}".format(salida, fecha2, salida2, salida3, salida4, salida5, salida6, salida7)


# OPCION 2: OBTENER REPETIDOS

lista = combinacion()
lista2 = combinacion2()
lista4 = combinacion4()
lista6 = combinacion6()
lista8 = combinacion8()
lista10 = combinacion10()
lista12 = combinacion12()


def listas(a, b):
    lista_final = []
    for i in a:
        if (i not in lista_final) and (i in b):
            lista_final.append(i)
    return lista_final


def listas2():
    a = "Primer sorteo comparado con el segundo :", listas(a=lista, b=lista2)
    b = "Primer sorteo comparado con el tercero :", listas(a=lista, b=lista4)
    c = "Primer sorteo comparado con el cuarto :", listas(a=lista, b=lista6)
    d = "Primer sorteo comparado con el quinto :", listas(a=lista, b=lista8)
    e = "Primer sorteo comparado con el sexto :", listas(a=lista, b=lista10)
    f = "Primer sorteo comparado con el septimo :", listas(a=lista, b=lista12)
    return "REPETIDOS comparacion con el primer sorteo: \n{0}  \n{1} \n{2} \n{3} \n{4} \n{5} ".format(a, b, c, d, e, f)


def obtener_repetidos():
    a = "Repetidos en Dos Sorteos : ", [
        x for x, y in collections.Counter(repetido_uno).items() if y > 1]
    b = "Repetidos en Tres Sorteos : ", [
        x for x, y in collections.Counter(repetido_dos).items() if y > 1]
    c = "Repetidos en Cuatro Sorteos : ", [
        x for x, y in collections.Counter(repetido_tres).items() if y > 1]
    d = "Repetidos en Cinco Sorteos : ", [
        x for x, y in collections.Counter(repetido_cuatro).items() if y > 1]
    e = "Repetidos en Seis Sorteos : ", [
        x for x, y in collections.Counter(repetido_cinco).items() if y > 1]
    f = "Repetidos en Siete Sorteos : ", [
        x for x, y in collections.Counter(repetido_seis).items() if y > 1]
    
    
    return "REPETIDOS en 7 sorteos: \n{0} \n{1} \n{2} \n{3} \n{4} \n{5} ".format(a, b, c, d, e, f)


# .........................


# OPCION 3: Funcion para sacar los que han salido una vez en los ultimos 7 sorteos

def salen_uno():
    suma_todas = uno+dos+tres+cuatro+cinco+seis+siete
    suma_todas = set(suma_todas)
    numeros_repetidos = [
        x for x, y in collections.Counter(repetido_seis).items() if y > 1]
    numeros_repetidos = set(numeros_repetidos)
    salen_uno1 = suma_todas-numeros_repetidos
    salen_uno2 = (list(salen_uno1))
    salen_uno2.sort()
    a = salen_uno2
    return "NUMEROS salen una sola vez en 7 sorteos: \n \n{0}".format(a)

# OPCION 4: menu media


def espacio():
    return str("                                                                        ")


def espacio2():
    return str("Hecho")


def media():
    media_repetido_uno = combinacion()
    media_repetido_dos = combinacion2()
    media_repetido_tres = combinacion4()
    media_repetido_cuatro = combinacion6()
    media_repetido_cinco = combinacion8()
    media_repetido_seis = combinacion10()
    media_repetido_siete = combinacion12()
    a = "media  primer sorteo", stats.mean(combinacion())
    b = "media  segundo sorteo", stats.mean(combinacion2())
    c = "media  tercero sorteo", stats.mean(combinacion4())
    d = "media  cuarto sorteo", stats.mean(combinacion6())
    e = "media  quinto sorteo", stats.mean(combinacion8())
    f = "media  sexto sorteo", stats.mean(combinacion10())
    g = "media  septimo sorteo", stats.mean(combinacion12())
    return "MEDIA: \n{0}  \n{1} \n{2} \n{3} \n{4} \n{5} \n{6} ".format(a, b, c, d, e, f, g)


def media2():
    a = "media  de la media aritmetica de 7 sorteos", ari_siete
    b = "suma de la media aritmetica 7 sorteos :", suma_aritmetica_siete
    c = "media de la media aritmetica de seis sorteos", ari_seis
    d = "suma de la media aritmetica 6 sorteos :", suma_aritmetica_seis
    return "SUMA DE LA MEDIA: \n{0}  \n{1} \n{2} \n{3} ".format(a, b, c, d)


def media3():
    salida = stats.mean(combinacion()), espacio(), predi_arriba()
    mensaje = "El rango hacia arriba estimado de la media aritmetica es de {0} hasta \n {2} \n{1}".format(
        salida[0], salida[1], salida[2])
    salida2 = stats.mean(combinacion()), predi_abajo()
    mensaje2 = "El rango hacia abajo estimado de la media aritmetica es de {0} hasta {1} ".format(
        salida2[0], salida2[1])
    return "PREDICCION MEDIA: \n{0}  \n{1}  ".format(mensaje, mensaje2)


def media4():
    a = "Media en RANGO"
    b = "Suma media Aritmetica en RANGO"
    c = "ATENCION MEDIA ARITMETICA FUERA DE RANGO¡: Posibilidad de salir numeros Altos"
    d = "ATENCION MEDIA ARITMETICA FUERA DE RANGO¡: Posibilidad de salir numeros Bajos"
    e = "Rango de la suma de la media aritmetica: 163-193"
    f = "Rango de la media de la media aritmetica: 23,27-27,57"
    if suma_aritmetica_siete > 162.9 and suma_aritmetica_siete < 193.6:
        print(a)
    if ari_siete > 23.27 and ari_siete < 27.57:
        print(b)
    if suma_aritmetica_siete < 162.9 and ari_siete < 23.27:
        print(c)
    if suma_aritmetica_siete > 193.6 and ari_siete > 27.57:
        print(d)

    else:
        print(e)
        print(f)


def prediccion_media_arriba():

    a1 = ari_siete
    a2 = (ari_siete)+1
    a3 = suma_aritmetica_siete
    return a1*a3/a2


def prediccion_media_abajo():
    a1 = ari_siete
    a2 = (ari_siete)-1
    a3 = suma_aritmetica_siete
    return a1*a3/a2


predicccionar = prediccion_media_arriba()
predicccionab = prediccion_media_abajo()


def predi_abajo():
    a1 = suma_aritmetica_seis
    a2 = predicccionar
    return a2-a1


def predi_arriba():
    a1 = suma_aritmetica_seis
    a2 = predicccionab
    return a2-a1
# ......................................


# OPCION 5: anteriores posteriores

def anadir_uno(x):
    return x+1


uno = combinacion()
result = list(map(anadir_uno, uno))


def anadir_dos(x):
    return x+2


result2 = list(map(anadir_dos, uno))


def quitar_uno(x):
    return x-1


result3 = list(map(quitar_uno, uno))


def quitar_dos(x):
    return x-2


result4 = list(map(quitar_dos, uno))


def anteriores_posteriores():
    anteriores_posteriores = result+result2+result3+result4
    anteriores_posteriores2 = set(anteriores_posteriores)
    suma_todas = uno+dos+tres+cuatro+cinco+seis+siete
    suma_todas2 = set(suma_todas)
    combinacion_anteriores_posteriores = anteriores_posteriores2-suma_todas2
    combinacion_anteriores_posteriores2 = list(
        combinacion_anteriores_posteriores)
    combinacion_anteriores_posteriores3 = sorted(
        combinacion_anteriores_posteriores2)
    if 50 in combinacion_anteriores_posteriores3:
        combinacion_anteriores_posteriores3.remove(50)
    if 51 in combinacion_anteriores_posteriores3:
        combinacion_anteriores_posteriores3.remove(51)
    if 0 in combinacion_anteriores_posteriores3:
        combinacion_anteriores_posteriores3.remove(0)
    if -1 in combinacion_anteriores_posteriores3:
        combinacion_anteriores_posteriores3.remove(-1)
        

    return "Anteriores y Posteriores: \n{0}  ".format(combinacion_anteriores_posteriores3)


# ...........................................
# OPCION6.....RESTO

# repetidos
def resto_repetidos():
    f = [x for x, y in collections.Counter(repetido_seis).items() if y > 1]
    return f


# salen1
def resto_salen1():
    suma_todas = uno+dos+tres+cuatro+cinco+seis+siete
    suma_todas = set(suma_todas)
    numeros_repetidos = [
        x for x, y in collections.Counter(repetido_seis).items() if y > 1]
    numeros_repetidos = set(numeros_repetidos)
    salen_uno1 = suma_todas-numeros_repetidos
    salen_uno2 = (list(salen_uno1))
    salen_uno2.sort()
    a = salen_uno2
    
    return a


# salen1
# anterioresyposteriores


def resto_anteriores_posteriores():
    anteriores_posteriores = result+result2+result3+result4
    anteriores_posteriores2 = set(anteriores_posteriores)
    suma_todas = uno+dos+tres+cuatro+cinco+seis+siete
    suma_todas2 = set(suma_todas)
    combinacion_anteriores_posteriores = anteriores_posteriores2-suma_todas2
    combinacion_anteriores_posteriores2 = list(
        combinacion_anteriores_posteriores)
    combinacion_anteriores_posteriores3 = sorted(
        combinacion_anteriores_posteriores2)
    if 50 in combinacion_anteriores_posteriores3:
        combinacion_anteriores_posteriores3.remove(50)
    if 51 in combinacion_anteriores_posteriores3:
        combinacion_anteriores_posteriores3.remove(51)
    if 0 in combinacion_anteriores_posteriores3:
        combinacion_anteriores_posteriores3.remove(0)
    if -1 in combinacion_anteriores_posteriores3:
        combinacion_anteriores_posteriores3.remove(-1)
    return combinacion_anteriores_posteriores3


resto_de_numeros = resto_anteriores_posteriores()+resto_salen1() + \
    resto_repetidos()
resto_de_numeros.sort()


def opcion_seis():
    a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
         26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49}
    b = set(resto_de_numeros)
    resto = a - b
    resto2 = list(resto)
    resto2.sort()
    return "Resto de numeros \n{0}". format(str(resto2))


# opcion6


def Selecciona_opcion():

    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Selecciona una opcion: "))
            correcto = True
        except ValueError:
            print('Error, introduce una opcion valida')

    return num


salir = False

opcion = 0


while not salir:
    print("")
    print("1. Actualizar sorteos:")
    print("2. Obtener Numeros repetidos:")
    print("3. Numeros que ha salido una sola vez en 7 sorteos:")
    print("4. Media aritmetica:")
    print("5. Anteriores y posteriores :")
    print("6. Resto de Numeros ")
    print("7. Grabar informacion: ")
    print("8. Salir")
    print("")

    opcion = Selecciona_opcion()

    if opcion == 1:
        print("Opcion 1")
        print("  ")
        print(extraer_combinaciones())
        print("  ")

    elif opcion == 2:
        print("Opcion 2")
        print("  ")
        print(obtener_repetidos())
        print("  ")
        print(listas2())
        print("  ")

    elif opcion == 3:
        print("Opcion 3")
        print("  ")
        print(salen_uno())
        print("  ")

    elif opcion == 4:
        print("Opcion 4")
        print("")
        print(media())
        print("")
        print(media2())
        print("")
        print(media3())
        print("")
        print(media4())

    elif opcion == 5:
        print("Opcion 5")
        print("")
        print(anteriores_posteriores())
        print("  ")
    elif opcion == 6:
        print("opcion 6")
        print("")
        print(opcion_seis())
        print("  ")

    elif opcion == 7:
        print("opcion 7")

        while True:  # Creamos un bucle infinito
            try:  # Intentamos abrirlo
                # Abrimos el fichero a modo de Reescribir (r+)
                with open("bonoloto_apuestas.txt", "+a") as f:
                    contenido = f.read()  # <-Lo abrimos utilizando el método read
                    f.write(extraer_combinaciones())
                    f.write('\n')
                    f.write('\n')
                    f.write(obtener_repetidos())
                    f.write('\n')
                    f.write('\n')
                    f.write(listas2())
                    f.write('\n')
                    f.write('\n')
                    f.write(salen_uno())
                    f.write('\n')
                    f.write('\n')
                    f.write(media())
                    f.write('\n')
                    f.write('\n')
                    f.write(media2())
                    f.write('\n')
                    f.write('\n')
                    f.write(media3())
                    f.write('\n')
                    f.write('\n')
                    f.write(anteriores_posteriores())
                    f.write('\n')
                    f.write('\n')
                    f.write(opcion_seis())
                    f.write('\n')
                    f.write(
                        '-------------------------------------------------------------')
                    f.write('\n')

                # Imprimimos el texto que almacenamos en la variable contenido

                break  # Rompemos el bucle
            except:
                print("Error al intentar abrir")
                break  # Rompemos el bucle

    elif opcion == 8:
        salir = True
    else:
        print("Elige una opcion")

print("Fin")
