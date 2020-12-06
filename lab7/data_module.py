import numpy as np
np.set_printoptions(suppress=True)


def read_csv(filename):
    with open(filename, "r") as csv_file:
        data = []
        for line in csv_file:
            numbers = line.replace("\n","").split(";")
            data.append(numbers)
    number_of_col = len(data[0])
    data = [float(number) for row in data for number in row]
    data = np.asarray(data)

    return data.reshape(-1, number_of_col)


def normalize_column(data, which_col):
    col = data[:, which_col]
    mean = np.mean(col)
    std = np.std(col)
    for ind, x in enumerate(col):
        col[ind] = (col[ind] - mean)/std

    return data


def center_column(data, which_col):
    col = data[:, which_col]
    mean = np.mean(col)
    for ind, x in enumerate(col):
        col[ind] = col[ind] - mean

    return data


def normalize_rows(data):
    for i, row in enumerate(data):
        mean = np.mean(row)
        std = np.std(row)
        for ind, x in enumerate(row):
            row[ind] = (x - mean)/std

    return data


def choose_label(data, which_col):
    label = data[:, which_col]
    x = data[:, :-1]
    return x, label


if __name__ == "__main__":
    sample_data = read_csv('sample2.csv')
    label, x = choose_label(sample_data, 16)
