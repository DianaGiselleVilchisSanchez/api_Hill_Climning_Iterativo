import math
import random

coord = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754472859146, -103.34625354877137),
    'Monterrey': (25.69161110159454, -100.321838480256),
    'QuintanaRoo': (21.163111924844458, -86.80231502121464),
    'Michohacan': (19.701400113725654, -101.20829680213464),
    'Aguascalientes': (21.87641043660486, -102.26438663286967),
    'CDMX': (19.432713075976878, -99.13318344772986),
    'QRO': (20.59719437542255, -100.38667040246602)
}

def distancia(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def evalua_ruta(ruta, coord):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(coord[ruta[i]], coord[ruta[i + 1]])
    total += distancia(coord[ruta[-1]], coord[ruta[0]])
    return total

def i_hill_climbing(coord, max_iteraciones=10):
    ciudades = list(coord.keys())
    mejor_ruta = None
    mejor_distancia = float('inf')

    for _ in range(max_iteraciones):
        ruta = ciudades[:]
        random.shuffle(ruta)

        mejora = True
        while mejora:
            mejora = False
            dist_actual = evalua_ruta(ruta, coord)

            for i in range(len(ruta)):
                for j in range(i + 1, len(ruta)):
                    ruta_tmp = ruta[:]
                    ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                    dist_tmp = evalua_ruta(ruta_tmp, coord)

                    if dist_tmp < dist_actual:
                        ruta = ruta_tmp
                        mejora = True
                        break
                if mejora:
                    break

        final_dist = evalua_ruta(ruta, coord)
        if final_dist < mejor_distancia:
            mejor_ruta = ruta[:]
            mejor_distancia = final_dist

    return mejor_ruta, mejor_distancia
