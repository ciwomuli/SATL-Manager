import json


class DataTeamManager:
    def __init__(self, fileName):
        self.fileName = fileName
        with open(self.fileName, "r", encoding='utf8') as f:
            self.row_data = json.load(f)

    def getTeams(self):
        nameList = []
        for name in self.row_data:
            nameList.append(name)
            if "players" not in self.row_data[name]:
                self.row_data[name] = {"players": []}
        self.save()
        return nameList

    def addTeam(self, teamName):
        self.row_data[teamName] = {"players": []}
        self.save()

    def delTeam(self, teamName):
        del self.row_data[teamName]
        self.save()

    def editTeam(self, originalName, newName):
        self.row_data[newName] = self.row_data[originalName]
        del self.row_data[originalName]
        self.save()

    def getPlayers(self, teamName):
        return self.row_data[teamName]["players"]

    def save(self):
        with open(self.fileName, "w", encoding='utf8') as f:
            json.dump(self.row_data, f, indent=2)
