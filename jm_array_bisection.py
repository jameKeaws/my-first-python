import bisect

values = [5, 7, 13, 20, 25, 31, 36, 43, 47, 49, 50, 75]

# TODO Exercise the left and right bisection routines
# bisect and bisect_right gives the index to the right of the existing value
print(bisect.bisect(values,26))
print(bisect.bisect_right(values,26))
# bisect_left gives the index of the value
print(bisect.bisect_left(values,26))


# TODO Use insort to insert new items
# bisect.insort_right(values, 25)
print(values)
bisect.insort_right(values, 26)
print(values)

# bisect can be used as an array lookup using breakpoints
breakpoints = [60, 70, 80, 90]
gradeLetters = "FDCBA"
scores = [81, 68, 53, 91, 90, 82, 71, 76, 84]

def calc_grade(score):
    # TODO Use the bisect function to identify cutoff points for the letter grades
    i = bisect.bisect(breakpoints, score)
    print(score)
    print(gradeLetters[i])
    print("\n")
    return gradeLetters[i]

results = [calc_grade(score) for score in scores]