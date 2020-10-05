import matplotlib.pyplot as plt
import numpy as np

def get_data_values_from_file(experiment_number=1):
   f = open(f"Raw data\experiment{experiment_number}.txt", "r")
   ts, xs, ys, vs = np.array([]), np.array([]), np.array([]), np.array([])
   for i, line in enumerate(f):
      t, x, y, v = line.strip("\n").split("\t")
      ts = np.append(ts, float(t))
      xs = np.append(xs, float(x))
      ys = np.append(ys, float(y))
      vs = np.append(vs, float(v))
   return ts, xs, ys, vs

window = plt.figure('Plots',figsize=(12,3))
t, x, y, v = get_data_values_from_file(1)

def show_path():
   plt.plot(x,y)
   plt.title('Banens form')
   plt.xlabel('$x$ (m)',fontsize=20)
   plt.ylabel('$y$ (m)',fontsize=20)
   plt.grid()
   plt.show()

def show_velocity():
   plt.plot(x,v)
   plt.title('Fart')
   plt.xlabel('$x$ (m)',fontsize=20)
   plt.ylabel('$v$ (m/s)',fontsize=20)
   plt.grid()
   plt.show()

def show_x_by_time():
   plt.plot(t,x)
   plt.title('Posisjon')
   plt.xlabel('$t$ (s)',fontsize=20)
   plt.ylabel('$x$ (m)',fontsize=20)
   plt.grid()
   plt.show()

def show_v_by_time():
   plt.plot(t,v)
   plt.title('Fart')
   plt.xlabel('$t$ (s)',fontsize=20)
   plt.ylabel('$v$ (m/s)',fontsize=20)
   plt.grid()
   plt.show()

#show_path()
#show_velocity()
#show_x_by_time()
show_v_by_time()
