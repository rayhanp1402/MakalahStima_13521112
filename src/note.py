class Note:
    def __init__(self, noteType):
        self.noteType = noteType
        self.parent = None

    def setParent(self, parent):
        self.parent = parent