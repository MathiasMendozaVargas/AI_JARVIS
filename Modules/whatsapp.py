###################
# CHECK PERSON
###################
def checkPerson(person):
    global isOk
    isOk = False

    contacts = {'mamita': '+59162221110', 'myself': '+59177099432'}
    for key in contacts:
        if key == person:
            isOk = True
            number = contacts[key]

    if isOk == True:
        return number
    else:
        number = False
        return number


def checkGroup(group):
    global isOk
    isOk = False

    groups = {'mamita y yo': 'Enf18KzKfvcCF1Ojv8oCde', 'another group': 'FpaSX3UfBHzDVO8aITz5XV'}
    for key in groups:
        if key == group:
            isOk = True
            group_id = groups[key]

    if isOk == True:
        return group_id
    else:
        group_id = False
        return group_id
