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