from user import User

u = User("ab123", "Ada")                # create an object (calls __init__)
v = User("cd456", "Grace", "staff")     # role given instead of the default

print(u.name)                           # read an attribute
u.name = "Ada Lovelace"                 # change an attribute
print(u.email())                        # call a method that returns a value
print(u)                                # calls __str__
u.record_login("09:30")                 # call a method
print(u.logins)
