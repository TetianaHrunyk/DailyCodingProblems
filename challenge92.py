"""We're given a hashmap associating each courseId key with a list of courseIds values, 
which represents that the prerequisites of courseId are courseIds.
 Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'],
 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
"""

def available_courses(hmap: dict, courses = list(), courses_count = 0):
    for key,value in hmap.items():
        value_set = set(value)
        courses_set = set(courses)
        if (value_set & courses_set) == value_set:
            if key not in courses:
                courses.append(key)
    if len(courses) > courses_count:
        courses_count = len(courses)
        available_courses(hmap, courses, courses_count)
    return courses

if __name__ == "__main__":
    hmap = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
    assert available_courses(hmap) == ['CSC100', 'CSC200', 'CSC300']