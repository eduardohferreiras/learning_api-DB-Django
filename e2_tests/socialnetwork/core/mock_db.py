from core.models import Profile, Connection

#Mock bases creation
lastID = 0
ProfileBase = {}
ConnectionBase = {}

def create_new_profile(email, isHidden = False):
    global lastID
    global ProfileBase
    global ConnectionBase

    profile = Profile(id = lastID + 1, email = email, isHidden = isHidden)
    lastID = lastID + 1
    ProfileBase[profile.id] = profile
    ConnectionBase[profile.id] = []
    return profile

def create_new_connection_unilateral(id1, id2):
    global ConnectionBase
    connAlreadyExist = False
    for connectionOfId in ConnectionBase[id1]:
        if(connectionOfId.id2 == id2):
            connAlreadyExist = True
            break
    if(not connAlreadyExist):
        ConnectionBase[id1].append(Connection(id1, id2))

def create_new_connection(id1, id2):
    create_new_connection_unilateral(id1, id2)
    create_new_connection_unilateral(id2, id1)
    
#Mock profiles creation and registration
mockProfile1 = create_new_profile(email = "1@email.com")
mockProfile2 = create_new_profile(email = "2@email.com")
mockProfile3 = create_new_profile(email = "3@email.com")
mockProfile3 = create_new_profile(email = "4@email.com")
mockProfile3 = create_new_profile(email = "5@email.com")
mockProfile3 = create_new_profile(email = "6@email.com")
mockProfile3 = create_new_profile(email = "7@email.com")
mockProfile3 = create_new_profile(email = "8@email.com")

#Conection creation (1<>2)
create_new_connection(1, 2)
create_new_connection(1, 3)
create_new_connection(1, 4)
create_new_connection(5, 2)
create_new_connection(5, 3)
create_new_connection(5, 4)
create_new_connection(5, 6)
create_new_connection(6, 7)
create_new_connection(7, 2)
