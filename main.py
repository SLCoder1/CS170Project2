import math
import time

def loadData(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = [float(x) for x in line.split()]
            data.append(row)
    return data

def euclideanDistance(row1, row2, feature_set):
    total = 0.0
    for feature in feature_set:
        total += (row1[feature] - row2[feature]) ** 2
    return math.sqrt(total)




def main():
    filename = "SanityCheckDataSet__2.txt"
    data = loadData(filename)
    nInstances = len(data)
    nFeatures = len(data[0]) - 1
    print(f"Number of instances: {nInstances}")
    print(f"Number of features: {nFeatures}")

    if nInstances >= 2:
        print("Distance test with features[1, 2]:", euclideanDistance(data[0], data[1], [1,2]))

if __name__ == "__main__":
    main()