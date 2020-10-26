# TFY4104/4107/4115 Fysikk hÃ¸sten 2020.
#
# Programmet bestemmer hÃ¸yden til de 8 festepunktene ved Ã¥ trekke
# tilfeldige heltall mellom 50 og 300 (mm). NÃ¥r festepunktene er
# akseptable, beregnes baneformen med mm som enhet. 
# Etter dette regnes hÃ¸ydeverdiene om til meter som enhet.
# Hele banens form y(x) beregnes
# ved hjelp av 7 ulike tredjegradspolynomer, pÃ¥ en slik mÃ¥te
# at bÃ¥de banen y, dens stigningstall dy/dx og dens andrederiverte
# d2y/dx2 er kontinuerlige i alle 6 indre festepunkter.
# I tillegg velges null krumning (andrederivert) 
# i banens to ytterste festepunkter (med bc_type='natural' nedenfor).
# Dette gir i alt 28 ligninger som fastlegger de 28 koeffisientene
# i de i alt 7 tredjegradspolynomene.

# Programmet aksepterer de 8 festepunktene fÃ¸rst nÃ¥r
# fÃ¸lgende betingelser er oppfylt:
#
# 1. StarthÃ¸yden er stor nok og en del hÃ¸yere enn i de Ã¸vrige 7 festepunktene.
# 2. Helningsvinkelen i startposisjonen er ikke for liten.
# 3. Banens maksimale helningsvinkel er ikke for stor.
#
# Med disse betingelsene oppfylt vil 
# (1) objektet (kula/skiva/ringen) fullfÃ¸re hele banen selv om det taper noe 
#     mekanisk energi underveis;
# (2) objektet fÃ¥ en fin start, uten Ã¥ bruke for lang tid i nÃ¦rheten av
#     startposisjonen; 
# (3) objektet forhÃ¥pentlig rulle rent, uten Ã¥ gli/slure.

# Vi importerer nÃ¸dvendige biblioteker:
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
# Horisontal avstand mellom festepunktene er 200 mm
h = 200
xfast=np.asarray([0,h,2*h,3*h,4*h,5*h,6*h,7*h])
# Vi begrenser starthÃ¸yden (og samtidig den maksimale hÃ¸yden) til
# Ã¥ ligge mellom 250 og 300 mm
ymax = 300
# yfast: tabell med 8 heltall mellom 50 og 300 (mm); representerer
# hÃ¸yden i de 8 festepunktene
RANDOM_Y_VALUES = True
#yfast = np.asarray(np.random.randint(50, ymax, size=8))
yfast = np.array([294,233,232,164,212,169,172,221])
# inttan: tabell med 7 verdier for (yfast[n+1]-yfast[n])/h (n=0..7); dvs
# banens stigningstall beregnet med utgangspunkt i de 8 festepunktene.
inttan = np.diff(yfast)/h
attempts=1
# while-lÃ¸kken sjekker om en eller flere av de 3 betingelsene ovenfor
# ikke er tilfredsstilt; i sÃ¥ fall velges nye festepunkter inntil
# de 3 betingelsene er oppfylt
while (yfast[0] < yfast[1]*1.04 or
       yfast[0] < yfast[2]*1.08 or
       yfast[0] < yfast[3]*1.12 or
       yfast[0] < yfast[4]*1.16 or
       yfast[0] < yfast[5]*1.20 or
       yfast[0] < yfast[6]*1.24 or
       yfast[0] < yfast[7]*1.28 or
       yfast[0] < 250 or
       np.max(np.abs(inttan)) > 0.4 or
       inttan[0] > -0.2):
          yfast=np.asarray(np.random.randint(0, ymax, size=8))
          inttan = np.diff(yfast)/h
          attempts=attempts+1

# NÃ¥r programmet her har avsluttet while-lÃ¸kka, betyr det at
# tallverdiene i tabellen yfast vil resultere i en tilfredsstillende bane. 

# Omregning fra mm til m:
xfast = xfast/1000
yfast = yfast/1000



#Programmet beregner deretter de 7 tredjegradspolynomene, et
#for hvert intervall mellom to nabofestepunkter.

#Med scipy.interpolate-funksjonen CubicSpline:
cs = CubicSpline(xfast, yfast, bc_type='natural')
xmin = 0.000
xmax = 1.401
dx = 0.001
x = np.arange(xmin, xmax, dx)
Nx = len(x)
y = cs(x)
dy = cs(x,1)
d2y = cs(x,2)

#Plotting

window = plt.figure('Plots',figsize=(12,3))


#baneform.savefig("baneform.pdf", bbox_inches='tight')
#baneform.savefig("baneform.png", bbox_inches='tight')


#print('Antall forsÃ¸k',attempts)
#print('FestepunkthÃ¸yder (m)',yfast)
#print('Banens hÃ¸yeste punkt (m)',np.max(y))

#print('NB: SKRIV NED festepunkthÃ¸ydene nÃ¥r du/dere er fornÃ¸yd med banen.')
#print('Eller kjÃ¸r programmet pÃ¥ nytt inntil en attraktiv baneform vises.')

g = 9.81
c = 2/5
m = 0.048

curviture = d2y / (1 + dy**2)**(3/2)

velocity = np.sqrt((2*g*(y[0]-y))/(1+c))

centripal_acceleration = velocity**2 * curviture

beta_in_radians = np.arctan(dy)

normal_force = m * (g *np.cos(beta_in_radians)+centripal_acceleration)

friction_force = np.abs((c * m * g * np.sin(beta_in_radians))/(1+c))

velocity_x = velocity * np.cos(beta_in_radians)
velocity_x_average = np.array([])

time_from_start = 0
time_array = np.array([time_from_start])

for i in range(1,len(velocity_x)):
   average = 0.5 * (velocity_x[i] + velocity_x[i-1])
   velocity_x_average = np.append(velocity_x_average,average)
   time_from_start += dx/average
   time_array = np.append(time_array, time_from_start)


def show_path():
   plt.plot(x,y,xfast,yfast,'*')
   plt.title('Banens form')
   plt.xlabel('$x$ (m)',fontsize=20)
   plt.ylabel('$y(x)$ (m)',fontsize=20)
   plt.ylim(0,0.350)
   plt.grid()
   plt.show()

def show_curviture():
   plt.plot(x,curviture)
   plt.title('Krumning')
   plt.xlabel('$x$ (m)',fontsize=20)
   plt.ylabel('$K(x)$ (1/m)',fontsize=20)
   plt.grid()
   plt.show()

def show_velocity():
   plt.plot(x,velocity)
   plt.title('Fart')
   plt.xlabel('$x$ (m)',fontsize=20)
   plt.ylabel('$v(x)$ (m/s)',fontsize=20)
   plt.grid()
   plt.show()

def show_centripal_acceleration():
   plt.plot(x,centripal_acceleration)
   plt.title('Sentripetalakselerasjon')
   plt.xlabel('$x$ (m)',fontsize=20)
   plt.ylabel('$ca(x)$ (m/s^2)',fontsize=20)
   plt.grid()
   plt.show()


def show_beta():
   plt.plot(x,np.rad2deg(beta_in_radians))
   plt.title('Helningsvinkel')
   plt.xlabel('$x$ (m)',fontsize=20)
   plt.ylabel('$\u03B2(x)$ (grader)',fontsize=20)
   plt.grid()
   plt.show()
   
def show_normal_force():
   plt.plot(x,normal_force)
   plt.title('Normalkraft')
   plt.xlabel('$x$ (m)',fontsize=20)
   plt.ylabel('$N$ (N)',fontsize=20)
   plt.grid()
   plt.show()

def show_friction_force():
   plt.plot(x,friction_force)
   plt.title('Friksjonskraft')
   plt.xlabel('$x$ (m)',fontsize=20)
   plt.ylabel('$f$ (N)',fontsize=20)
   plt.grid()
   plt.show()

def show_x_by_time():
   plt.plot(time_array,x)
   plt.title('Posisjon')
   plt.xlabel('$t$ (s)',fontsize=20)
   plt.ylabel('$x$ (m)',fontsize=20)
   plt.grid()
   plt.show()

def show_v_by_time():
   plt.plot(time_array,velocity)
   plt.title('Fart')
   plt.xlabel('$t$ (s)',fontsize=20)
   plt.ylabel('$v$ (m/s)',fontsize=20)
   plt.grid()
   plt.show()

#show_path()
#show_velocity()
#show_curviture()
#show_centripal_acceleration()
#show_beta()
#show_normal_force()
#show_friction_force()
#show_x_by_time()
#show_v_by_time()

