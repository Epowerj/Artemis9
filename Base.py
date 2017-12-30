
class Base:
    name = str()
    ownername = str()
    ownerid = int()

    units = []
    buildings = []

    def __init__(self, userid, ownername, name):
        self.ownerid = userid
        self.ownername = ownername
        self.name = name

    def get_status(self):
        return "Base " + self.name + "\n" \
                                     "Owner " + self.ownername + "\n"
