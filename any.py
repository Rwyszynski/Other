
def zwracanie(person, skills):
    return all( skill in person['skills'] for skill in skills)



john = {
    'name': 'John Doe',
    'age': 30,
    'skills': ['Python', 'JavaScript', 'C++']
}
 
jane = {
    'name': 'Jane Smith',
    'age': 25,
    'skills': ['Python', 'Java']
}




programy = ['Python', 'JavaScript']

print(zwracanie(john, programy))




