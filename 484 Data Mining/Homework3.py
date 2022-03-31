import numpy as np
import random
from sklearn.preprocessing import normalize


def preprocess(text):
    # "K means has problems with outliers"

    # This block is old, kept to show some preprocessing that can be useful
    # We will look into outliers later, for now we're removing \n from each line
    # newtext = []
    # for line in text:
    #     x = line[:-1]
    #     newtext.append(x)

    # normalize the numbers, take a standard distribution and kick out outliers
    # first we normalize to [0,1]
    text = normalize(text)
    # removing outliers can be done a few ways, I'm removing everything
    #   that doesn't fall within 3 standard deviations of mean
    # print("Start outlier test:")
    # print("These are the rows and columns that do not fall within three standard deviations,")
    # print("note: there may be no data points outside the range :")
    # Data Note: For the Iris new data set, there are only 2 points outside of 2 SD, everything else falls
    # within 3 SD. The following code doesn't work with the new_test4 data set because of the 0 values
    # No values should be removed from the iris_new_data set.
    # sd = np.std(text, axis=0)
    # mean = np.mean(text, axis=0)
    # rows, columns = text.shape
    # j = 0
    # while j < rows:
    #     i = 0
    #     while i < columns:
    #         if text[j, i] > (mean[i] + (3 * sd[i])):
    #             print("Above allowed range")
    #             print("Row: ", j, " Column: ", i, " Mean: ", mean[i], " Standard Deviation: ", sd[i])
    #             print(text[j])
    #         if text[j, i] < (mean[i] - (3 * sd[i])):
    #             print("Lower than allowed range")
    #             print("Row: ", j, " Column: ", i, " Mean: ", mean[i], " Standard Deviation: ", sd[i])
    #             print(text[j])
    #         i = i+1
    #     j = j+1
    # print("End Outlier test.")
    return text


def pick_c(array, k):
    # pick K centroids from array
    centroidArray = []
    # this is our first centroid
    rows, columns = array.shape
    x = random.randint(0, rows)
    centroidArray.append(array[x, :])
    for i in range(k-1):  # K-1 because we picked 1 centroid already
        if len(centroidArray) > 1:
            # can't take a mean if there's only 1 entry
            x = np.mean(centroidArray, axis=0)
        else:
            # when there's only 1 entry we just use that entry
            x = centroidArray[0]
        y = calculate_farthest(array, x)
        centroidArray.append(y)
    return centroidArray


def calculate_farthest(array, x):
    # returns the location in the array of farthest point from location x in the array
    # centroids is our current list of centroids, we don't want duplicates
    rows = array.shape[0]
    i = 0
    distance = 0  # we want the farthest away
    pos = 0  # position in the array of that point
    while i < rows:
        dist = np.linalg.norm(x - array[i])
        if dist > distance:
            distance = dist
            pos = i
        i = i+1
    return array[pos]


def cluster_array(array, centroids):
    clusters = []
    for line in range(array.shape[0]):
        dist = []
        # this could've been rewritten with np.argsort
        for i in range(len(centroids)):
            x = np.linalg.norm(array[line]-centroids[i])
            dist.append(x)
        # sort into order, then assign the cluster the nearest centroid
        mindist = dist[0]
        appendnumber = 0
        for i in range(len(dist)):
            if mindist > dist[i]:
                mindist = dist[i]
                appendnumber = i
        clusters.append(appendnumber+1)  # clusters 1 / 2 / 3 ... x
    return clusters


def repick(data, centroids, clusters):
    # my clusters array is just the cluster each data piece belongs to, it's just an integer
    newCentroids = []
    # add every piece from data to new cluster cross referencing clusters(the array), calculate new center
    for i in range(len(centroids)):
        thisCluster = []
        for j in range(len(data)):
            if clusters[j] == (i+1):
                thisCluster.append(data[j])
        # now thisCluster has every data point that's in that cluster, recalculate the middle
        newAverage = np.mean(thisCluster, axis=0)
        distances = []
        for j in range(len(thisCluster)):
            dist = np.linalg.norm(newAverage[i] - thisCluster[j])
            distances.append(dist)
        # this sorts the list by value but returns the index, IE: if 11 is first, 11 is the shortest
        distances = np.argsort(distances)
        newCentroids.append(thisCluster[distances[0]])
    return newCentroids


def main():
    # training = np.genfromtxt("1616505271_4922109_iris_new_data.txt", dtype=str)
    test = np.genfromtxt("1616506692_795991_new_test4.txt", delimiter=',', dtype=str)
    # data = preprocess(training)
    data = preprocess(test)

    # pick x random centroids
    # for
    #   assign each point it's centroid
    #   recompute the center of each cluster
    # do this until centroids don't change

    centroids = pick_c(data, 10)  # 3 for iris, 10 for image
    # now we group everything into a centroid, just assign it a number
    clusters = cluster_array(data, centroids)
    # repick centroids, repick clutsers
    newCentroids = []
    oldCentroids = centroids
    nca = 0  # new centroid average
    oca = np.mean(centroids)  # old centroid average
    # k = 0 used to track this comparison
    # i'm using mean to compare, run until the means are the same
    while oca != nca:
        newCentroids = repick(data, centroids, clusters)
        oca = np.mean(centroids)
        nca = np.mean(newCentroids)
        centroids = newCentroids
        clusters = cluster_array(data, centroids) # new clusters
        # k = k+1
        # print(k)
    # answers = open("answers.txt", "w")  # used for iris data, on average ran 5 times
    #  used for image data, ran for 30 minutes, didn't stop oer 2600 iterations I ran less times and was getting weird
    # line write errors. One time I'd run and the file would have 10740 answers then another it wouldn't, it would have
    # more or less.
    answers = open("testanswers.txt", "w")
    for line in clusters:
        answers.write('%d\n' % line)


if __name__ == '__main__':
    main()
