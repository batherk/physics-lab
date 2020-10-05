def get_data_values_from_file(experiment_number):
    f = open(f"Raw data\experiment{experiment_number}.txt", "r")
    output_lists = []
    for i, line in enumerate(f):
        t, x, y, v = line.strip("\n").split("\t")
        if i == 0:
            output_lists.append([float(t),float(x),float(y),0])
        elif v == '':
            last_v = output_lists[-1][3]
            output_lists.append([float(t),float(x),float(y),last_v])
        else:
             output_lists.append([float(t),float(x),float(y),float(v)])
    return output_lists


