from core.models import Profile

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

#Mock profiles creation and registration
mockProfile1 = create_new_profile(email = "1@email.com")
mockProfile2 = create_new_profile(email = "2@email.com")
mockProfile3 = create_new_profile(email = "3@email.com")


#Conection creation (1<>2)
ConnectionBase[mockProfile1.id].append(mockProfile2.id)
ConnectionBase[mockProfile2.id].append(mockProfile3.id)