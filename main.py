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
        diff = row1[feature] - row2[feature]
        total += diff * diff
    return math.sqrt(total)

def nearestNeighbor(data, index, featureSet):
    bestDistance = float('inf')
    bestLabel = None
    targetRow = data[index]

    for i in range(len(data)):
        if i == index:
            continue
        otherRow = data[i]
        distance = euclideanDistance(targetRow, otherRow, featureSet)
        if distance < bestDistance:
            bestDistance = distance
            bestLabel = otherRow[0]
    return bestLabel

def testAccuracy(data, featureSet, bestSoFar = None):
    correct = 0
    total = len(data)

    for i in range(total):
        predicted = nearestNeighbor(data, i, featureSet)
        actual = data[i][0]
        if predicted == actual:
            correct += 1
        if bestSoFar is not None:
            maxPossible = correct + (total - i - 1)
            maxAccuracy = maxPossible / total
            if maxAccuracy <= bestSoFar:
                return maxAccuracy
    return correct / total

#Helper function to clean the trace
def formatFeatures(featureSet):
    return "{" + ", ".join(str(f) for f in featureSet) + "}"

def forwardSelection(data, nFeatures):
    curSet = []
    bestSet = []
    bestAccuracy = 0.0
    print("Beginning search")
    for i in range(nFeatures):
        featureToAdd = None
        curAccuracy = 0.0
        for feature in range(1, nFeatures + 1):
            if feature in curSet:
                continue
            tempSet = curSet + [feature]
            accuracy = testAccuracy(data, tempSet, curAccuracy)
            print(f"Using feature(s) {formatFeatures(tempSet)} accuracy is {accuracy * 100:.1f}%")
            if accuracy > curAccuracy:
                curAccuracy = accuracy
                featureToAdd = feature
        if featureToAdd is not None:
            curSet.append(featureToAdd)
            print(f"Feature set {formatFeatures(curSet)} was best, accuracy = {curAccuracy * 100:.1f}%  ")
            if curAccuracy > bestAccuracy:
                bestAccuracy = curAccuracy
                bestSet = curSet.copy()
    print(f"Finished search! Best feature subset is {formatFeatures(bestSet)}, which has an accuracy of {bestAccuracy * 100:.1f}%")
    return bestSet, bestAccuracy

def backwardElimination(data, nFeatures):
    curSet = list(range(1, nFeatures + 1))
    bestSet = curSet.copy()
    bestAccuracy = testAccuracy(data, curSet)

    print("Beginning search.")

    while len(curSet) > 1:
        featureToRemove = None
        curAccuracy = 0.0
        bestCandidate = None

        for feature in curSet:
            tempSet = [f for f in curSet if f != feature]
            accuracy = testAccuracy(data, tempSet)
            print(f"Using feature(s) {formatFeatures(tempSet)} accuracy is {accuracy * 100:.1f}%")

            if accuracy > curAccuracy:
                curAccuracy = accuracy
                featureToRemove = feature
                bestCandidate = tempSet

        curSet = bestCandidate
        print(f"Feature set {formatFeatures(curSet)} was best, accuracy is {curAccuracy * 100:.1f}%")

        if curAccuracy > bestAccuracy:
            bestAccuracy = curAccuracy
            bestSet = curSet.copy()

    print(f"Finished search!! The best feature subset is {formatFeatures(bestSet)}, which has an accuracy of {bestAccuracy * 100:.1f}%")
    return bestSet, bestAccuracy

def main():
    
    # print(f"Number of instances: {nInstances}")
    # print(f"Number of features: {nFeatures}")

    # if nInstances >= 2:
    #     print("Distance test with features[1, 2]:", euclideanDistance(data[0], data[1], [1,2]))

    # predicted = nearestNeighbor(data, 0, [1,2])
    # actual = data[0][0]
    # print(f"Predicted label: {predicted}, Actual label: {actual}")

    # numberFeatures = list(range(1, nFeatures + 1))
    # accuracy = testAccuracy(data, numberFeatures)
    # print(f"Running nearest neighbor with features {numberFeatures}: Accuracy = {accuracy * 100:.1f}%")


    # #test sanity before actual search
    # sanityFeatures = [10, 8, 2]
    # sanityAccuracy = testAccuracy(data, sanityFeatures)
    # print(f"Sanity check accuracy with features {sanityFeatures}: Accuracy = {sanityAccuracy:.3f}")
    # print(formatFeatures([1, 3, 5])) 
    print("Welcome to Sathvik's Feature Selection Algorithm.")
    filename = input("Type in the name of the file to test: ")
    data = loadData(filename)

    nInstances = len(data)
    nFeatures = len(data[0]) - 1

    print("Type the number of the algorithm you want to run.")
    print("1) Forward Selection")
    print("2) Backward Elimination")
    choice = input()

    print(f"This dataset has {nFeatures} features (not including the class attribute), with {nInstances} instances.")

    allFeatures = list(range(1, nFeatures + 1))
    accuracy = testAccuracy(data, allFeatures)
    print(f"Running nearest neighbor with all {nFeatures} features, using \"leaving-one-out\" evaluation, I get an accuracy of {accuracy * 100:.1f}%")

    start = time.time()

    if choice == "1":
        forwardSelection(data, nFeatures)
    elif choice == "2":
        backwardElimination(data, nFeatures)
    else:
        print("Invalid choice.")

    end = time.time()
    print(f"Runtime: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()