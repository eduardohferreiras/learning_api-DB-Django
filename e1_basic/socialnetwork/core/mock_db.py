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

def create_new_connection(id1, id2):
    global ConnectionBase
    #creating connection 1->2
    try:
        ConnectionBase[id1].index(Connection(id1, id2)) 
    except ValueError:
        ConnectionBase[id1].append(Connection(id1, id2))    
    
    #creating connection 2->1
    try:
        ConnectionBase[id2].index(Connection(id2, id1)) 
    except ValueError:
        ConnectionBase[id2].append(Connection(id2, id1))    

#Mock profiles creation and registration
mockProfile1 = create_new_profile(email = "1@email.com")
mockProfile2 = create_new_profile(email = "2@email.com")
mockProfile3 = create_new_profile(email = "3@email.com")


#Conection creation (1<>2)
create_new_connection(1, 2)
create_new_connection(1, 3)
#print(ConnectionBase)