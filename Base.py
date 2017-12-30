
class Base:
    name = str()
    ownerid = int()

    units = []
    buildings = []

    def __init__(self, userid, name):
        self.ownerid = userid
        self.name = name

    def get_status(self):
        return "Base " + self.name + "\n" \
                                     "Owner " + str(self.ownerid) + "\n"
