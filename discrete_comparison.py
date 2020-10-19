import matplotlib.pyplot as plt
import numpy as np
from import_experiments import get_data_values_from_file

dic = {}
end_velocities = np.array([])
end_times = np.array([])

for i in range(1,10):
    t, x, y, v = get_data_values_from_file(i)
    end_velocities = np.append(end_velocities, v[-1])
    end_times = np.append(end_times, t[-1])

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

show_end_speeds()



