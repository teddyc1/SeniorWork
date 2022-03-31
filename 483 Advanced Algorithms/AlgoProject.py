# Theodore Church G01127117
# Advanced Algorithms Project
import random
import math
import matplotlib.pyplot as plotter


def main():
    # i want 100 data points per set, a uniform and an increasing set
    # Adaptive Search Data
    AS10U = [0]*100
    AS10I = [0]*100
    AS100U = [0]*100
    AS100I = [0]*100
    # Interpolation Binary Search Data
    IBS10U = [0]*100
    IBS10I = [0]*100
    IBS100U = [0]*100
    IBS100I = [0]*100
    # Switch Binary / Interpolation Search Data
    S10U = [0]*100
    S10I = [0]*100
    S100U = [0]*100
    S100I = [0]*100
    i = 0
    #AS10k
    while i < 100:
        uniformTen = [1] * 10000
        increasingTen = [1] * 10000
        j = 1
        # uniform
        while j < 10000:
            uniformTen[j] = uniformTen[j - 1] + random.randrange(1, 10)
            j = j + 1
            # increasing
        j = 1
        while j < 10000:
            x = increasingTen[j - 1]
            if j != 1:
                increasingTen[j] = increasingTen[j] + random.randrange(1, x)
            else:
                increasingTen[j] = 2
            j = j + 1
        k = 0
        # uniform
        test = 0
        while k < 3:
            k = k+1
            key = random.randrange(1, uniformTen[-1])
            test = test + AS(key, uniformTen)
        test = test/3
        AS10U[i] = test
        k = 0
        # increasing
        itest = 0
        while k < 3:
            k = k + 1
            key = random.randrange(1, increasingTen[-1])
            itest = itest + AS(key, increasingTen)
        itest = itest/3
        AS10I[i] = itest
        i = i+1
    print(AS10U)
    print(AS10I)
    i = 0
    # AS100k
    while i < 100:
        uniformTen = [1] * 100000
        increasingTen = [1] * 100000
        j = 1
        # uniform
        while j < 100000:
            uniformTen[j] = uniformTen[j - 1] + random.randrange(1, 10)
            j = j + 1
            # increasing
        j = 1
        while j < 100000:
            x = increasingTen[j - 1]
            if j != 1:
                increasingTen[j] = increasingTen[j] + random.randrange(1, x)
            else:
                increasingTen[j] = 2
            j = j + 1
        k = 0
        # uniform
        test = 0
        while k < 3:
            k = k + 1
            key = random.randrange(1, uniformTen[-1])
            test = test + AS(key, uniformTen)
        test = test / 3
        AS100U[i] = test
        k = 0
        # increasing
        itest = 0
        while k < 3:
            k = k + 1
            key = random.randrange(1, increasingTen[-1])
            itest = itest + AS(key, increasingTen)
        itest = itest / 3
        AS100I[i] = itest
        i = i + 1
    print(AS100U)
    print(AS100I)
    i = 0
    # IBS10k
    while i < 100:
        uniformTen = [1] * 10000
        increasingTen = [1] * 10000
        j = 1
        # uniform
        while j < 10000:
            uniformTen[j] = uniformTen[j - 1] + random.randrange(1, 10)
            j = j + 1
            # increasing
        j = 1
        while j < 10000:
            x = increasingTen[j - 1]
            if j != 1:
                increasingTen[j] = increasingTen[j] + random.randrange(1, x)
            else:
                increasingTen[j] = 2
            j = j + 1
        k = 0
        # uniform
        test = 0
        while k < 3:
            k = k + 1
            key = random.randrange(1, uniformTen[-1])
            test = test + IBS(key, uniformTen)
        test = test / 3
        IBS10U[i] = test
        k = 0
        # increasing
        itest = 0
        while k < 3:
            k = k + 1
            key = random.randrange(1, increasingTen[-1])
            itest = itest + IBS(key, increasingTen)
        itest = itest / 3
        IBS10I[i] = itest
        i = i + 1
    print(IBS10U)
    print(IBS10I)
    i = 0
    # IBS100k
    while i < 100:
        uniformTen = [1] * 100000
        increasingTen = [1] * 100000
        j = 1
        # uniform
        while j < 100000:
            uniformTen[j] = uniformTen[j - 1] + random.randrange(1, 10)
            j = j + 1
            # increasing
        j = 1
        while j < 100000:
            x = increasingTen[j - 1]
            if j != 1:
                increasingTen[j] = increasingTen[j] + random.randrange(1, x)
            else:
                increasingTen[j] = 2
            j = j + 1
        k = 0
        # uniform
        test = 0
        while k < 3:
            k = k + 1
            key = random.randrange(1, uniformTen[-1])
            test = test + IBS(key, uniformTen)
        test = test / 3
        IBS100U[i] = test
        k = 0
        # increasing
        itest = 0
        while k < 3:
            k = k + 1
            key = random.randrange(1, increasingTen[-1])
            itest = itest + IBS(key, increasingTen)
        itest = itest / 3
        IBS100I[i] = itest
        i = i + 1
    print(IBS100U)
    print(IBS100I)
    i = 0
    # S10k
    plotter.plot(AS10U, label='AS10U')
    plotter.plot(AS10I, label='AS10I')
    plotter.plot(AS100U, label='AS100U')
    plotter.plot(AS100I, label='AS100I')
    plotter.plot(IBS10U, label='IBS10U')
    plotter.plot(IBS10I, label='IBS10I')
    plotter.plot(IBS100U, label='IBS100U')
    plotter.plot(IBS100I, label='IBS100I')
    plotter.legend()
    plotter.show()
    # This broke right before I was done when it was working before.
    while i < 100:
        uniformTen = [1] * 10000
        increasingTen = [1] * 10000
        j = 1
        # uniform
        while j < 10000:
            uniformTen[j] = uniformTen[j - 1] + random.randrange(1, 10)
            j = j + 1
            # increasing
        j = 1
        while j < 10000:
            x = increasingTen[j - 1]
            if j != 1:
                increasingTen[j] = increasingTen[j] + random.randrange(1, x)
            else:
                increasingTen[j] = 2
            j = j + 1
        k = 0
        # uniform
        test = 0
        while k < 3:
            k = k + 1
            key = random.randrange(1, uniformTen[-1])
            test = test + switch(key, uniformTen)
        test = test / 3
        S10U[i] = test
        k = 0
        # increasing
        itest = 0
        while k < 3:
            k = k + 1
            key = random.randrange(1, increasingTen[-1])
            itest = itest + switch(key, increasingTen)
        itest = itest / 3
        S10I[i] = itest
        i = i + 1
    print(S10U)
    print(S10I)
    i = 0
    # S100k
    while i < 100:
        uniformTen = [1] * 100000
        increasingTen = [1] * 100000
        j = 1
        # uniform
        while j < 100000:
            uniformTen[j] = uniformTen[j - 1] + random.randrange(1, 10)
            j = j + 1
            # increasing
        j = 1
        while j < 100000:
            x = increasingTen[j - 1]
            if j != 1:
                increasingTen[j] = increasingTen[j] + random.randrange(1, x)
            else:
                increasingTen[j] = 2
            j = j + 1
        k = 0
        # uniform
        test = 0
        while k < 3:
            k = k + 1
            key = random.randrange(1, uniformTen[-1])
            test = test + switch(key, uniformTen)
        test = test / 3
        S100U[i] = test
        k = 0
        # increasing
        itest = 0
        while k < 3:
            k = k + 1
            key = random.randrange(1, increasingTen[-1])
            itest = itest + switch(key, increasingTen)
        itest = itest / 3
        S100I[i] = itest
        i = i + 1
    print(S100U)
    print(S100I)



def switch(key, array):  # one step binary, one step interpolation
    bcomparisons = 1
    icomparisons = 1
    low = 0
    ilow = 0
    high = len(array)-1
    ihigh = len(array)-1
    median = 0
    imedian = 0
    barray = array.copy()
    iarray = array.copy()
    if len(array) == 1:
        if array[0] == key:
            return 1
        else:
            return 0
    while 1:
        #binary
        median = round((len(barray)) / 2)
        if key == barray[median]:
            bcomparisons = bcomparisons + 1
            return bcomparisons
        elif key > barray[median]:
            bcomparisons = bcomparisons + 2
            barray = array[median+1:high]
        elif key < barray[median]:
            bcomparisons = bcomparisons + 3
            barray = barray[low:median-1]
        #interpolation
        imedian = ilow + math.floor(((key - iarray[ilow])*(ihigh - ilow) / (iarray[ihigh] - iarray[ilow])))
        if iarray[imedian] == key:
            icomparisons = icomparisons + 1
            return icomparisons
        if iarray[imedian] < key:
            icomparisons = icomparisons + 2
            ilow = imedian + 1
            iarray = iarray[ilow:ihigh]
        elif iarray[imedian] > key:
            icomparisons = icomparisons + 3
            ihigh = imedian - 1
            iarray = iarray[ilow:ihigh]


def AS(key, array):  # adaptive search
    comparisons = 0
    median = 0
    bot = 0
    nextI = 0
    top = len(array)-1
    s = array[bot:top+1]
    sprime = s
    keynotfound = True
    # print("Adaptive Search: Pre While: Bot: ", array[bot], " Top: ", array[top], "Key: ", key)
    if key > array[len(array)-1]:
        comparisons = comparisons + 1
        return comparisons  # array is sorted, key is bigger than array
    comparisons = comparisons + 1
    # while():
    while keynotfound:
        # next =  bot + abs(((key - A[bot])/(A[top] - [bot]))*(top-bot))
        nextI = bot + math.ceil(((key - array[bot]) / (array[top] - array[bot])) * (top - bot))
        # if bot <= key <= next:
        #     top = next
        #     S' = A[bot]...A[next]
        if array[bot] <= key <= array[nextI]:
            comparisons = comparisons + 2
            top = nextI
            sprime = s[bot:nextI+1]
        # else
        #     bot = next
        #     S' = A[next]...A[top]
        else:
            comparisons = comparisons + 2
            bot = nextI
            sprime = s[nextI:top+1]
        # if S' > abs(Len(S)/2) next = med = bot + ((Top-bot)/2)
        if len(sprime) > (len(array)/2):
            nextI = bot + math.ceil(((top - bot) / 2))
            median = bot + math.floor((top-bot)/2)
        # else if key = A[next]
        #       return key
        if key == array[nextI]:
            comparisons = comparisons + 1
            keynotfound = False
            return comparisons
        # else if key > A[next] then bot = next+1
        elif key > array[nextI]:
            comparisons = comparisons + 2  # 2 elif comparisons = + 2
            bot = nextI + 1
        # else (key < A[next]) top = next -1
        else:
            comparisons = comparisons + 3
            top = nextI - 1
        # finally; if bot <= key <= next:
        # recursive call on S'
        # I have been having issues with recursion working, so Im just using a loop
        #  else terminate, key is not in S'
        if array[bot] <= key <= array[top]:
            comparisons = comparisons + 2
        else:
            comparisons = comparisons + 2
            return comparisons # 0 = key not found


def IBS(alpha, array):  # Interpolation binary search
    # H = high, L = Low
    # (1) : L = 0, H = n, XsL = 0, y = alpha, N=n
    comparisons = 0
    theta = 2
    S = 2
    L = 0
    H = len(array)-1
    N = len(array)-1
    y = (alpha-array[L])/(array[H]-array[L]) # email
    # (2) : If N < S go to (4) Otherwise: Lhat =
    #       Max{L+[Ny-theta(Ny(1-y))^(!/2)], L+1},
    #       H = Min{L+[Ny + theta(Ny(1-y))^(1/2)], H-1}
    if alpha > array[len(array)-1]:
        comparisons = comparisons+1
        return comparisons  # Key is too big
    comparisons = comparisons + 1
    while 1:
        if N > S:
            Lhat = max((L + (math.ceil(N*y - theta * ((N*y*(1-y))**(1/2))))), L+1)
            Hhat = min((L + (math.floor(N*y + theta * ((N*y*(1-y))**(1/2))))), H-1)
            # (3) : If XsLhat = Alpha or XsHhat = alpha stop Otherwise
            if array[Lhat] == alpha:
                comparisons = comparisons + 1
                return comparisons
            else:
                comparisons = comparisons + 1
            if array[Hhat] == alpha:
                comparisons = comparisons + 1
                return comparisons
            else:
                comparisons = comparisons + 1
            #       a. if alpha < XsLhat set H = Lhat;
            if alpha < array[Lhat]:
                comparisons = comparisons + 1
                H = Lhat
            #       else if XsLhat < alpha < XsHhat, set L = Lhat H=Hhat
            elif array[Lhat] < alpha < array[Hhat]:
                comparisons = comparisons + 3
                L = Lhat
                H = Hhat
            #       else if XsHhat < alpha set L = Hhat;
            elif array[Hhat] < alpha:
                comparisons = comparisons + 4
                L = Hhat
            #       b. y = (alpha - XsL)/(XsH - XsL)
            y = (alpha - array[L])/(array[H] - array[L])
        # (4) : M = [1/2 * (L+H)]
        M = math.ceil((1/2) * (L+H))
        # (5) : If XsM = alpha stop, Otherwise
        #       a. if alpha < XsubM set H = M
        #       else L = M
        #       b. N = H - L - 1; Y = (alpha - XsL)/(XsH - XsL)
        #       c. if N = 0 stop (Alpha is not in X) otherwise go to (2)
        if array[M] == alpha:
            comparisons = comparisons + 1
            return comparisons
        else:
            if alpha < array[M]:
                comparisons = comparisons + 2
                H = M
            else:
                comparisons = comparisons + 3
                L = M
            N = H - L - 1
            y = round((alpha - array[L])/(array[H] - array[L]))
            if N == 0:
                # print("Not Found. Comparisons done:")
                return comparisons  # alpha not in X
            else:
                continue


if __name__ == '__main__':
    main()
