#librerias
import numpy as np
import spiceypy as spy
spy.furnsh("naif0012.tls") #Cargar Kernel de datos 
import numpy as np 
import datetime
import pandas as pd
from astropy import units as u
from astropy.coordinates import SkyCoord
from sbpy.data import Ephem
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, EarthLocation
from astropy.coordinates import get_body_barycentric, get_body, get_moon


#constantes
deg=np.pi/180 # para pasar los alfa y delta a radianes
rad=1/deg
au=149597870.693 # km, fuente: https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/de-403-masses.tpc
mu=132712440023.31

#tiempo astronómico
def tiempo_astronomico(fecha):
    tu=spy.str2et(fecha) 
    dt=spy.deltet(tu,"ET") 
    t=tu-dt
    return (t)

fecha1="2020-07-15"
fecha2="2020-08-15" 
fecha3="2020-09-15"

t1=tiempo_astronomico(fecha1)
t2=tiempo_astronomico(fecha2)
t3=tiempo_astronomico(fecha3)

#posición de la Tierra
def posicion_tierra(Ra):
    t = Time(Ra)
    P=get_body_barycentric('earth',t,ephemeris='de432s')
    return P

#Posición para fecha uno de observación
R1=posicion_tierra(fecha1)

#Posición para fecha dos de observación
R2=posicion_tierra(fecha2)

#Posición para fecha tres de observación
R3=posicion_tierra(fecha3)


P1=[-R1.x/u.km,-R1.y/u.km,-R1.z/u.km]
P2=[-R2.x/u.km,-R2.y/u.km,-R2.z/u.km]
P3=[-R3.x/u.km,-R3.y/u.km,-R3.z/u.km]


