import json

def storedata(name, score):
    int(score)
    with open('scoredata.txt') as datafile:
        data = json.load(datafile)

    if score > data["5"]["score"]:
        data["5"]["name"] = name
        data["5"]["score"] = score
        if score > data["4"]["score"]:
            data["5"]["name"] = data["4"]["name"]
            data["5"]["score"] = data["4"]["score"]
            data["4"]["name"] = name
            data["4"]["score"] = score
            if score > data["3"]["score"]:
                data["4"]["name"] = data["3"]["name"]
                data["4"]["score"] = data["3"]["score"]
                data["3"]["name"] = name
                data["3"]["score"] = score
                if score > data["2"]["score"]:
                    data["3"]["name"] = data["2"]["name"]
                    data["3"]["score"] = data["2"]["score"]
                    data["2"]["name"] = name
                    data["2"]["score"] = score
                    if score > data["1"]["score"]:
                        data["2"]["name"] = data["1"]["name"]
                        data["2"]["score"] = data["1"]["score"]
                        data["1"]["name"] = name
                        data["1"]["score"] = score 

'''
    with open('scoredata.txt', 'w') as datafile:
        json.dump(data,datafile)
        print(data["1"]["name"])
'''