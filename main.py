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

def euclideanDistance(row1, row2, featureSet):
    total = 0.0
    for feature in featureSet:
        total += (row1[feature] - row2[feature]) ** 2
    return math.sqrt(total)

def nearestNeighbor(data, index, featureSet):
    bestDistance = float('inf')
    bestLabel = None

    for i in range(len(data)):
        if i == index:
            continue
        distance = euclideanDistance(data[index], data[i], featureSet)
        if distance < bestDistance:
            bestDistance = distance
            bestLabel = data[i][0]
    return bestLabel

def testAccuracy(data, featureSet):
    correct = 0
    for i in range(len(data)):
        predicted = nearestNeighbor(data, i, featureSet)
        actual = data[i][0]
        if predicted == actual:
            correct += 1
    return correct / len(data)

#Helper function to clean the trace
def formatFeatures(featureSet):
    return "{" + ", ".join(str(f) for f in featureSet) + "}"

def main():
    filename = "SanityCheckDataSet__2.txt"
    data = loadData(filename)
    nInstances = len(data)
    nFeatures = len(data[0]) - 1
    print(f"Number of instances: {nInstances}")
    print(f"Number of features: {nFeatures}")

    if nInstances >= 2:
        print("Distance test with features[1, 2]:", euclideanDistance(data[0], data[1], [1,2]))

    predicted = nearestNeighbor(data, 0, [1,2])
    actual = data[0][0]
    print(f"Predicted label: {predicted}, Actual label: {actual}")

    numberFeatures = list(range(1, nFeatures + 1))
    accuracy = testAccuracy(data, numberFeatures)
    print(f"Running nearest neighbor with features {numberFeatures}: Accuracy = {accuracy * 100:.1f}%")


    #test sanity before actual search
    sanityFeatures = [10, 8, 2]
    sanityAccuracy = testAccuracy(data, sanityFeatures)
    print(f"Sanity check accuracy with features {sanityFeatures}: Accuracy = {sanityAccuracy:.3f}")
    print(formatFeatures([1, 3, 5])) 

if __name__ == "__main__":
    main()