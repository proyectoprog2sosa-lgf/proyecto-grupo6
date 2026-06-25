from proyecto import *

def manejar_archivo():
    """
    manejar_archivo() -> dict[int, tuple]
    Lee el archivo CSV y construye un diccionario donde la clave es el id del alojamiento
    y el valor es una tupla con toda la información del Airbnb.
    """
    dicc = {}
    with open('jola.csv') as listings:
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
