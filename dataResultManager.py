import json


class DataResultManager:
    def __init__(self, fileName):
        self.fileName = fileName
        with open(self.fileName, "r", encoding='utf8') as f:
            self.row_data = json.load(f)

    def getRoundList(self):
        roundList = []
        for round in self.row_data:
            roundList.append(round)
        return roundList

    def getResultList(self, roundName):
        resultList = []
        for result in self.row_data[roundName]:
            resultList.append(result["home"] + " vs " + result["away"])
        return resultList

    def getDetail(self, roundName, index):
        detailList = []
        for detail in self.row_data[roundName][index]["details"]:
            detailList.append(detail)
        return detailList
