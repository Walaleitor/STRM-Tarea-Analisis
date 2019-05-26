from gmalthgtparser import HgtParser
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LightSource
from tqdm import tqdm




#Obtiene las elevaciones desde el archivo .htg, con esto no ahorramos lidiar con los big endians
def get_array():
    with HgtParser('S34W071.hgt') as parser:
        for elev_value in parser.get_sample_iterator(1201, 1201):
            return np.array(elev_value[4]) #En la posicion 4 se encuentra el array con las elevaciones, automaticamente los parseamos a un array de numpy




#Dibuja el mapa y le aplica un shade con las sombras
def plot_map(e):
    azimut_angle = 100 
    elevation_angle = 20 
    fig = plt.figure(figsize=(7,7))
    strm_map = fig.add_subplot(1,1,1)
    light_source = LightSource(azimut_angle, elevation_angle)
    map_with_shadows = light_source.hillshade(e, vert_exag=10)
    strm_map.imshow(map_with_shadows, cmap='gray')
    plt.suptitle("STRM", fontsize=20)
    plt.show()


        
#Main de la aplicacion
array = get_array()
plot_map(array)










        
        


