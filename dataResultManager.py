import json


class DataResultManager:
    def __init__(self, fileName):
        self.fileName = fileName
        with open(self.fileName, "r", encoding='utf8') as f:
            self.row_data = json.load(f)

    def save(self):
        with open(self.fileName, "w", encoding='utf8') as f:
            json.dump(self.row_data, f, indent=2)

    def getRoundList(self):
        roundList = []
        for round in self.row_data:
            roundList.append(round)
        return roundList

    def addRound(self, roundName):
        self.row_data[roundName] = []
        self.save()

    def delRound(self, roundName):
        del self.row_data[roundName]
        self.save()

    def getResultList(self, roundName):
        resultList = []
        for result in self.row_data[roundName]:
            resultList.append(result["home"] + " vs " + result["away"])
        return resultList

    def getResult(self, roundName, index):
        return self.row_data[roundName][index]

    def getDetail(self, roundName, index):
        detailList = []
        for detail in self.row_data[roundName][index]["details"]:
            detailList.append(detail)
        return detailList

    def addResult(self, roundName, home, away):
        self.row_data[roundName].append({"home": home, "away": away, "details": []})
        self.save()

    def delResult(self, roundName, index):
        del self.row_data[roundName][index]
        self.save()

    def editResult(self, roundName, index, home, away):
        self.row_data[roundName][index]["home"] = home
        self.row_data[roundName][index]["away"] = away
        self.save()

    def delDetail(self, roundName, index, index2):
        del self.row_data[roundName][index]["details"][index2]
        self.save()

    def addDetail(self, roundName, index, player1, player2, mapName, winner):
        self.row_data[roundName][index]["details"].append({
            "player1": player1,
            "player2": player2,
            "map": mapName,
            "winner": winner
        })
        self.save()

    def editDetail(self, roundName, index, index2, player1, player2, mapName, winner):
        self.row_data[roundName][index]["details"][index2] = {
            "player1": player1,
            "player2": player2,
            "map": mapName,
            "winner": winner
        }
        self.save()

    def exportResult(self, roundName, index, date):
        result = self.row_data[roundName][index]
        ret = "|M" + str(index + 1) + "={{Match"
        if index == 0:
            ret += "|dateheader=true|bestof=6|matchsection=" + roundName + "\n"
        else:
            ret += "\n"
        ret += "\t|date=" + date + "{{abbr/CST}}\n"
        ret += "\t|opponent1={{TeamOpponent|" + result["home"] + "}}\n"
        ret += "\t|opponent2={{TeamOpponent|" + result["away"] + "}}\n"
        for i in range(0, 6):
            detail = result["details"][i]
            ret += "\t|map" + str(i + 1) + "={{Map|map=" + detail["map"] + "|winner=" + str(detail["winner"]) + "|t1p1=" + \
                   detail["player1"] + "|t2p1=" + detail["player2"] + "|subgroup=" + str(i // 2 + 1) + "}}\n"
        ret += "}}\n"
        return ret
