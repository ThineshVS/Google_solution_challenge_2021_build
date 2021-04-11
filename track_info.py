from firebase import firebase

Firebase = firebase.FirebaseApplication(
    'https://grobage-default-rtdb.firebaseio.com/', None)


def user_request_list():
    l = []
    result2 = Firebase.get("/", "plantation")
    for i in result2.keys():
        for j in result2[i].keys():
            z = result2[i][j]
            l.append(z)
    # # print(result2)
    # for i in range(100):

    #     try:
    #         key1 = tuple(result2.keys())[i]
    #         print(key1)
    #         try:
    #             for j in range(100):
    #                 key2 = tuple(result2[key1].keys())[j]
    #                 key3 = tuple(result2[key2].keys())[j]
    #                 l.append(key2)
    #                 area = result2[key3]['Area']
    #                 name_final = result2[key3]['Name']
    #                 service_of = result2[key3]['Service']
    #                 imageid_of = result2[key3]['imageid']
    #                 location_info = result2[key3]['location']
    #                 print(key2)
    #                 print(area)
    #                 print(name_final)
    #                 print(service_of)

    #         except:
    #             continue

    #         #key2 = tuple(result2[key1].keys())[i]
    #         #key3 = tuple(result2[key2].keys())[0]
    #         '''area = result2[key1]['Area']
    #         name_final = result2[key1]['Name']
    #         service_of = result2[key1]['Service']
    #         imageid_of = result2[key1]['imageid']
    #         location_info = result2[key1]['location']
    #         # key3 = tuple(result2.keys())[1]

    #         print(key1)
    #         print(area)
    #         print(name_final)
    #         print(service_of)
    #         print(imageid_of)
    #         print(location_info)
    #         #j = j+1'''
    #     except:
    #         print("exit")
    #         exit()
    return l


print(user_request_list())
