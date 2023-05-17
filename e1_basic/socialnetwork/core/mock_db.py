from core.models import Profile

#Mock bases creation
lastID = 0
ProfileBase = {}
ConnectionBase = {}

#Mock profiles creation and registration
mockProfile1 = Profile(id= lastID+1, email = "1@email.com")
lastID = lastID + 1
ProfileBase[mockProfile1.id] = mockProfile1
ConnectionBase[mockProfile1.id] = []

mockProfile2 = Profile(id= lastID+1, email = "2@email.com")
lastID = lastID + 1
ProfileBase[mockProfile2.id] = mockProfile2
ConnectionBase[mockProfile2.id] = []

mockProfile3 = Profile(id= lastID+1, email = "3@email.com")
lastID = lastID + 1
ConnectionBase[mockProfile3.id] = []
ProfileBase[mockProfile3.id] = mockProfile3

#Conection creation (1<>2)
ConnectionBase[mockProfile1.id].append(mockProfile2.id)
ConnectionBase[mockProfile2.id].append(mockProfile3.id)