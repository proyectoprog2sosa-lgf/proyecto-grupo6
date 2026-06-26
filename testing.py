from proyecto import *

def manejar_archivo2():
    """
    manejar_archivo() -> dict[int, tuple]
    Lee el archivo CSV y construye un diccionario donde la clave es el id del alojamiento
    y el valor es una tupla con toda la información del Airbnb.
    """
    dicc = {}
    with open('dataset2.csv') as listings:
        lector = csv.reader(listings)
        next(lector)
        for linea in lector:
            datos = linea
            dicc[datos[0]] = (datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10],datos[11],datos[12],datos[13],datos[14],datos[15],datos[16],datos[17],datos[18])
    return dicc


def test_menor ():
    pass

# pruebas para disponibilidades_anuales
def test_disp_anuales_varios():
    t1 = ["x"]*18
    t1[15] = "365"
    t2 = ["x"] * 18
    t2[15]="120"
    
    listings = {
        "id1": tuple(t1),
        "id2":tuple(t2)
    }
    
    res = disponibilidades_anuales(listings)
    assert res == [("id1", 365), ("id2", 120)]

# caso diccionario vacio
def test_disp_anuales_vacio():
    assert disponibilidades_anuales({})==[]


# test mayores10
# caso 1: justo 10 elementos
def test_mayores10_exacto():
    listings={}
    for i in range(10):
        t = ["x"] * 18
        t[15]= str(i*10) # tira 0, 10, 20 etc
        listings[f"id{i}"] = tuple(t)
        
    res = mayores10(listings)
    
    assert len(res) == 10
    assert res[0] == ("id9", 90) # chequeo el mayor
    assert res[-1]== ("id0",0)

def test_mayores10_pasado():
    #elementos de mas
    listings = {}
    for i in range(15):
        t=["x"] * 18
        t[15] = str(i)
        listings[f"id {i}"] = tuple(t)
        
    res = mayores10(listings)
    assert len(res) == 10
    assert res
#testing buscar alojamiento por nombre
def test_buscar_alojamiento():
    listings = {
        1: ("Casa Azul", 0, 0, "Juan", "", "Palermo", 0, 0, "", 0, 0, 5),
        2: ("Depto Azul", 0, 0, "Ana", "", "Recoleta", 0, 0, "", 0, 0, 10)
    }

    resultado = buscar_alojamiento("Casa Azul", listings)

    assert resultado == [["Nombre", "Anfitrión", "Barrio", "Reseñas"],["Casa Azul","Juan","Palermo",5]]

def test_alojamientos_minimo_noches():
    listings = manejar_archivo2()
    lista_resultado = [(-34.59381206465798,-58.414331541691794),
                       (-34.59976681720103,-58.42649866037633),
                       (-34.58604,-58.39537),
                       (-34.62284436910694,-58.39210310422973),
                       (-34.59026,-58.40117),
                       (-34.6153174,-58.36287300000001),
                       (-34.6110957,-58.40255639999999),
                       (-34.582348,-58.4349066),
                       (-34.58855417184091,-58.3916275575757),
                       (-34.62114416204078,-58.402598587937945),
                       (-34.55769,-58.46924)]
    assert alojamientos_minimo_noches(1,listings) == lista_resultado
    assert alojamientos_minimo_noches(0,listings) == []
    
def test_contar_aloj_barrio():
    listings = manejar_archivo2()
    dicc_resultado = {"Belgrano": 1,
                      "Palermo": 6,
                      "Almagro": 1,
                      "Recoleta": 3,
                      "San Cristobal": 2,
                      "Puerto Madero": 1,
                      "San Nicolas": 1,
                      "Balvanera": 1,
                      "Retiro": 1,
                      "Barracas": 1,
                      "Nuñez": 1}
    assert contar_aloj_barrio(listings) == dicc_resultado
