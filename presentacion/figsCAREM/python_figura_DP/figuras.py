import numpy as np
import matplotlib.pyplot as plt
import time
plt.rcParams['mathtext.fontset']= 'cm'
plt.ion()
plt.cla()
plt.close('all')

# DATOS  ==================================================================================================
pf= [394.69] #, 9.450, 12.888] # Valores de presiones para cada caso
# Q=[0.9e-3, 1.72e-3, 2.10e-3] # Valores de caudales para cada caso [Q2 Q4 Q5]
# Q_name=[2,4,5]
rho=997.62  # Valor de densidad a 23 grados
# #nro_caso=[5, 6, 4]; # numero de caso original en directorios OpenFOAM para [Q2 Q4 Q5] 


# LECTURA DE MEDICIONES Y RESULTADOS  =====================================================================
datos=[];  datos1=[]; M=997;  z=np.zeros([M,2]); p=np.zeros([M,2]); #gg=np.zeros([M*2,len(pf)])
# Nota: los archivos de resultados tienen 998 lineas cada mitad (para hacerlo genérico abrir uno y extraer
# el tamaño de los datos)

for i in range(1):  # dos lineas de datos  NO, SEPARADAS XQ TIENEN DISTINTO Z
    # Resultados
    file_name='resultados/p_linea_' + "{}".format(i+1) + ".dat"
    fi = open(file_name,'r')  # abro archivo para lectura
    lineas=fi.readlines()
    fi.close()
    for j,k in enumerate(lineas):
        datos.append(k.split('\t'))  # limpio datos de archivo original
        datos1.append(datos[j][0].split('   '))
        print(datos1[j][3])
        z[j,i]=float(datos1[j][2])       # extraigo valor de z (es el mismo para todos los casos)
        # p[j,i]=(float(datos1[j][3])-(pf[0]*z[j,i]))*rho  # extraigo p y hago la conversion
        p[j,i]=float( datos1[j][3] )  # extraigo p y hago la conversion
        
    datos=[]; datos1=[]
        
datos=[];  datos1=[]; M=999;  z2=np.zeros([M,2]); p2=np.zeros([M,2]);
for i in range(1,2):  #  NO, SEPARADAS XQ TIENEN DISTINTO Z
    # Resultados
    file_name='resultados/p_linea_' + "{}".format(i+1) + ".dat"
    fi = open(file_name,'r')  # abro archivo para lectura
    lineas=fi.readlines()
    fi.close()
    for j,k in enumerate(lineas):
        datos.append(k.split('\t'))  # limpio datos de archivo original
        datos1.append(datos[j][0].split('   '))
        z2[j,i]=float(datos1[j][2])       # extraigo valor de z (es el mismo para todos los casos)
        # p2[j,i]=(float(datos1[j][3])-(pf[0]*z2[j,i]))*rho  # extraigo p y hago la conversion
        p2[j,i] = float( datos1[j][3] )
    datos=[]; datos1=[]


# CÁLCULO DE LINEAS DE FITEO  =============================================================================
# Resultados
s1=7; # Datos desde z=-0.0732
s2=146; # Datos hasta  z=-0.0417
p_DS=900#954; # Punto de fiteo DS z = 0.1404
h=np.zeros([1,2]); lineal_US=np.zeros([len(z),1]); lineal_DS=np.zeros([len(z),1]);
DP=np.zeros([1]); coef_corr=np.zeros([2,2,1]);
for i in range(1):   # todo es "(1)" porque viene copiado de otro loop
    h[i,:]=np.polyfit(z[s1:s2,i],p[s1:s2,i],1); # pendiente (h[0]) y ordenada al origen (h[1])
    lineal_US[:,i] = z[:,0]*h[i,0] + h[i,1]; # función lineal US
    lineal_DS[:,i] = z[:,0]*h[i,0] + (p[p_DS,i]-h[i,0]*z[p_DS,0]);
    DP[i] = h[i,1] - (p[p_DS,i] - h[i,0]*z[p_DS,0]); # delta p = ordenada al orig US - ord al orig DS
    coef_corr[:,:,i]= np.corrcoef(np.polyval(h[i,:],z[s1:s2,i]), p[s1:s2,i]) # correlation coeff


    
# GRAFICOS ================================================================================================
line_width=0.75; mark_size=0.25;
font_size_legend= 7; font_size_labels=9; font_size_ticks=6

# US Y DS
plt.figure(1,figsize=(5.5,3.5),dpi=300)

plt.plot(z2,p2, 'b^', markersize=mark_size, label='Línea 2', lw=line_width)
plt.plot(z,p, 'ro', markersize=mark_size, label='Línea 1', lw=line_width)


# fiteos
plt.plot(z[:380,0],lineal_US[:380,0], 'k--', markersize=mark_size, lw=0.5)
plt.plot(z[290:,0],lineal_DS[290:,0], 'k--', markersize=mark_size, lw=0.5)

plt.show(); plt.tight_layout()
plt.gcf().subplots_adjust(left=0.17)   # me cortaba el ylabel
#plt.legend( loc="best", fontsize=font_size_legend)
plt.xlabel('$z \ (m)$', fontsize=font_size_labels);
plt.ylabel('$\Delta P \ (u.a)$', fontsize=font_size_labels)
plt.xlim((-0.08,0.16));
# plt.ylim((-75000,125000))
plt.xticks(np.arange(-0.08,0.17,0.02), fontsize=font_size_ticks);
# plt.yticks(np.arange(-40000,110000,20000), fontsize=font_size_ticks);
plt.grid()

# # Separador 
plt.axvline(x=-0.005,  color='k', lw=1); plt.axvline(x=0.005,  color='k', lw=1);
plt.axvline(x=0, color='k', linestyle='dashed',lw=1)

####plt.axvline(x=-0.0417, color='k', linestyle='dashed',lw=1)

plt.savefig('US_DS.png', dpi=300)
plt.savefig('US_DS.pdf')


# #plt.close('all')
