class User:
    """A user of a system."""

    def __init__(self, uid, name, role="student"):
        self.uid = uid          # data attributes
        self.name = name
        self.role = role
        self.logins = []        # start with an empty list

    def email(self):
        # a method that builds a value from the attributes and returns it
        return f"{self.uid}@example.ac.uk"

    def __str__(self):
        info_str = f"User {self.uid}: {self.name}\n"
        info_str += f"role: {self.role}\n"
        info_str += f"email: {self.email()}"
        return info_str

    def record_login(self, when):
        self.logins.append(when)
        print(f"{self.name} logged in at {when}")
