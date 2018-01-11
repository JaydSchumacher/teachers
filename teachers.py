teachers = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
 'Kenneth Love': ['Python Basics', 'Python Collections', 'Django Basics']}

def num_teachers(teachers):
    count = 0
    for teacher in teachers:
        count += 1
    return count

def num_courses(list):
    count = 0
    for x,y in list.items():
        for x in y:
            count += 1
    return count

def courses(list):
    course_list = []
    for x,y in list.items():
        for x in y:
            course_list.append(x)
    return course_list

def most_courses(list):
    max_count = 0
    top_teacher = ''
    for x,y in list.items():
        if len(y) > max_count:
            max_count = len(y)
            top_teacher = x
    return top_teacher

def stats(list):
    stat_list = []
    count = 0
    for x,y in list.items():
        count = len(y)
        stat_list.append([x, count])
    return stat_list
print(stats(teachers))