classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]

# V
def index_of_student(name):
    for i, student in enumerate(classroom):
        if student['name'] == name:
           return i
    #return classroom.index(name)[name]

# V
def add_student(name, email=None):
    if(email==None):
        classroom.append({'name': name,'email':f'{name.lower()}@example.com','grades':[]})
    else:
        classroom.append({'name': name,'email':email,'grades':[]})
    """Add a new student to the classroom
    with the following keys:
    'name': the given name
    'email': if email is given use it otherwise use <name>@example.com
             in lowercase, you can use the `s.lower()` method
    'grade': initialize with empty list
    """
    pass

# V
def delete_student(name):
    index=index_of_student(name)
    classroom.remove(classroom[index])
    """Delete a student from the classroom"""
    pass

# V
def set_email(name, email):
    classroom[index_of_student(name)]['email']=email
    #classroom[index_of_student(name)].get('email')
    """Sets the email of the student"""
    pass

# V
def add_grade(name, profession, grade):
    classroom[index_of_student(name)]['grades'].append((profession,grade))
    """Adds a new grade to the student grades"""
    pass

# V
def avg_grade(name, profession):
    sum_of_grades=0
    num_of_grades=0
    for g in classroom[index_of_student(name)]['grades']:
        if(g[0]==profession):
            sum_of_grades+=g[1]
            num_of_grades+=1
    return sum_of_grades/num_of_grades
    """Returns the average of grades of the student
    in the specified profession
    """
    pass

# V
def get_professions(name):
    l=[]
    for g in classroom[index_of_student(name)]['grades']:
        if(g[0] not in l):
            l.append(g[0])
    return l
    """Returns a list of unique professions that student has grades in"""
    pass

#print(index_of_student('Charlie'))
#delete_student('Bob')
#set_email('Charlie','charlie2@example.com')
#add_grade('Bob','physics',100)
#print(avg_grade('Charlie','english'))
#print(get_professions('Charlie'))
#add_student('Abc','abc@gmail.com')
#add_student('Def')
#print(classroom)
