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

def main():
    filename = "SanityCheckDataSet__2.txt"
    data = loadData(filename)
    nInstances = len(data)
    nFeatures = len(data[0]) - 1
    print(f"Number of instances: {nInstances}")
    print(f"Number of features: {nFeatures}")

if __name__ == "__main__":
    main()