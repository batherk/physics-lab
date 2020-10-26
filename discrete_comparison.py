import matplotlib.pyplot as plt
import numpy as np
from import_experiments import get_data_values_from_file
from cubicspline import time_array, velocity, x

dic = {}
end_velocities = np.array([])
end_times = np.array([])

times = np.array([])
velocities = np.array([])

for i in range(1,10):
    ts, xs, ys, vs = get_data_values_from_file(i)
    times = np.append(times, ts)
    velocities = np.append(velocities, vs)
    end_velocities = np.append(end_velocities, vs[-1])
    end_times = np.append(end_times, ts[-1])

average = sum(end_velocities)/len(end_velocities)
std = np.std(end_velocities)
default_error = std/np.sqrt(len(end_velocities))

print(f"Average: {average}")
print(f"Standard deviation {std}")
print(f"Default error: {default_error}")

print(f"\nAverage: {average} +/- {default_error}")

window = plt.figure('Plots',figsize=(12,3))

def show_end_speeds():
   plt.plot(end_times,end_velocities, "o")
   plt.title('Sluttfart')
   plt.xlabel('$t$ (s)',fontsize=20)
   plt.ylabel('$v$ (m/s)',fontsize=20)
   plt.ylim(0,1.5)
   plt.xlim(0,2)
   plt.grid()
   plt.show()

def show_speeds():
    plt.plot(times,velocities, ".")
    plt.title('Fart')
    plt.xlabel('$t$ (s)',fontsize=20)
    plt.ylabel('$v$ (m/s)',fontsize=20)
    plt.ylim(0,1.75)
    plt.xlim(0,1.6)
    plt.grid()
    plt.show()

def show_speeds_compared_to_theory():
    plt.plot( times,velocities, ".", time_array, velocity,)
    plt.title('Fart')
    plt.xlabel('$t$ (s)',fontsize=20)
    plt.ylabel('$v$ (m/s)',fontsize=20)
    plt.ylim(0,1.75)
    plt.xlim(0,1.6)
    plt.grid()
    plt.show()

#show_end_speeds()
show_speeds()
show_speeds_compared_to_theory()


