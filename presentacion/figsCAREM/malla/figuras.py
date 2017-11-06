import numpy as np
import matplotlib.pyplot as plt
import time
plt.rcParams['mathtext.fontset']= 'cm'
plt.ion()
plt.cla()
plt.close('all')


# GRAFICOS ================================================================================================

line_width=0.75; mark_size=0.25;

font_size_legend= 7; font_size_labels=9; font_size_ticks=6

data = np.loadtxt('gradP.dat')


plt.figure(1,figsize=(5.5,3.5),dpi=300)

plt.plot(data[:,1]/1e+06, data[:,2] / np.max(data[:,2]), marker = 'o', lw=line_width)

# plt.show();

plt.tight_layout()

plt.gcf().subplots_adjust(left=0.12)   # me cortaba el ylabel

plt.gcf().subplots_adjust(bottom=0.13)   # me cortaba el ylabel

plt.xlabel('Millones de celdas', fontsize=font_size_labels);

plt.ylabel('$\Delta P_{norm}$', fontsize=font_size_labels)

# plt.xlim((-0.08,0.16));

plt.ylim((0.955,1.005))

# plt.xticks(np.arange(-0.08,0.17,0.02), fontsize=font_size_ticks);

# plt.yticks(np.arange(-40000,110000,20000), fontsize=font_size_ticks);

plt.grid()

# # # Separador 
# plt.axvline(x=-0.005,  color='k', lw=1); plt.axvline(x=0.005,  color='k', lw=1);
# plt.axvline(x=0, color='k', linestyle='dashed',lw=1)

# ####plt.axvline(x=-0.0417, color='k', linestyle='dashed',lw=1)

plt.savefig('malla.png', dpi=300)
plt.savefig('malla.pdf')


# #plt.close('all')
