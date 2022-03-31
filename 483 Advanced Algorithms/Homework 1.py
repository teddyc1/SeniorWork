# Theodore Church G01127117
# a) Pick a positive integer, call it n.
# (b) If n is even, divide it by 2.
# (c) Otherwise, multiply it by 3 and add 1.
# (d) Repeat steps 2-4 with the new number
i = 0


# This is collatz, except specifically tailored to return steps taken instead of the answer.
def steps(n):
    global i
    if n == 1:
        return i
    if n % 2 == 0:
        i += 1
        return steps(n/2)
    else:
        i += 1
        return steps((n*3)+1)


# I don't feel like this is complicated enough to be worth commenting
def collatz(n):
    print(n)
    if n == 1:
        return
    if n % 2 == 0:
        return collatz(n/2)
    else:
        return collatz((n*3)+1)


# I've seen a few different implementations for this. The recommended implementation is to use
# '@functools.lru_cache(maxsize=n)' because this will memoize at function definition instead of run time
# to my understanding. I used this blog https://dbader.org/blog/python-memoization as well as the wikipedia
# article linked in the assignment https://en.wikipedia.org/wiki/Memoization, and the python library
# https://docs.python.org/3/library/, as well as a youtube video https://www.youtube.com/watch?v=Qk0zUZW-U_M. To try and
# better understand memoization.
# I'm specifically commenting this function to prove I have understanding of memoization and didn't just copy code
# as this function is very similar to the function listed on the blog. The key difference is the change of *args to n
# since we are not required to make sure this function works for all args for our assignment. For my own personal
# implementation in the future I won't wrap functions like this. Instead I'll be using the previously recommended line
# @functools.lru..... because of it's better runtime on initial run.
def memoizer(function, dictionary):
    cache = dictionary  # makes our cache

    def new_function(n):  # we use a wrapper that calls the original function and adds a few steps
        if n in cache:  # Check if the answer is in the cache first
            return cache[n]
        result = function(n)  # answer isn't in cache, run the function normally
        cache[n] = result  # return the result to our cache. The most recent results are kept
        return result  # return result of the function
    return new_function  # return the new wrapped function, nicely memoized


def max_collatz_steps(n):
    global i
    i = 0
    stepsD = dict()
    new_steps = memoizer(steps, stepsD)
    stepsTaken = []
    for number in range(1, n+1):
        stepsTaken.append(new_steps(number))
        i = 0  # resetting global variable
    return stepsTaken


def max_collatz_num(n):
    stepCount = max_collatz_steps(n)
    j = max(stepCount)
    k = stepCount.index(j)
    collatzD = dict()
    new_collatz = memoizer(collatz, collatzD)
    print(j, " is the largest number of steps taken from 1 to your specified input.")
    print("The collatz conjecture for ", (k+1), " is:")
    new_collatz(k+1)
    print("")


def main():
    global i
    i = 0
    k = 100
    print("steps taken for each number 1 to ", k, ": ", max_collatz_steps(k))
    max_collatz_num(k)
    # note: I wasn't quite sure about how to do 5. You can change K to whatever you'd like.


if __name__ == '__main__':
    main()
