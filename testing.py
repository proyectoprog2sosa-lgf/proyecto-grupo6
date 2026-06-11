import pytest
from proyecto import *

# tests de la funcion mayor
# caso 1
def test_mayor_medio():
    lista = [("a",10), ("b", 50), ("c", 20)]
    assert mayor(lista)==("b", 50)

# caso 2 y 3 (principio y unico elemento)
def test_mayor_principio():
    lista=[("a", 100), ("b",50), ("c", 20)]
    assert mayor(lista) == ("a", 100)

def test_mayor_unico():
    lista = [("a",10)]
    assert mayor(lista) == ("a", 10)

# caso 4
def test_mayor_negativos():
    lista = [("a",-10),("b",-5),("c", -20)]
    assert mayor(lista) == ("b", -5)


# pruebas para disponibilidades_anuales
def test_disp_anuales_varios():
    # armo tuplas falopas de 18 elementos para q no rompa
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
        t[15]= str(i*10) # tira 0, 10, 20...
        listings[f"id{i}"] = tuple(t)
        
    res = mayores10(listings)
    
    assert len(res) == 10
    assert res[0] == ("id9", 90) # chequeo el mayor
    assert res[-1]== ("id0",0)

def test_mayores10_pasado():
    # le mandamos mas de 10 a ver q onda
    listings = {}
    for i in range(15):
        t=["x"] * 18
        t[15] = str(i)
        listings[f"id{i}"] = tuple(t)
        
    res = mayores10(listings)
    assert len(res) == 10
    assert res[0] == ("id14", 14)


# test para alojamientos_mayor_disp
def test_alojamientos_extraccion():
    # armamos uno de 10 para q no crashee mayores10
    listings = {}
    for i in range(10):
        t = [str(j) for j in range(18)]
        t[0] = f"ID_{i}"
        t[3]=f"Nom_{i}"
        t[5] = f"Var5_{i}"
        t[8] = f"Var8_{i}"
        t[15]= str(i*10)
        listings[f"id{i}"] = tuple(t)
        
    resultado= alojamientos_mayor_disp(listings)
    
    assert len(resultado)==10
    # tiene q traer el indice 9 q es el mas grande, con los campos q pide
    assert resultado[0] == ["ID_9", "Nom_9", "Var5_9", "Var8_9", "90"]