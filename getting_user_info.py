from firebase import firebase

Firebase = firebase.FirebaseApplication(
    'https://grobage-default-rtdb.firebaseio.com/', None)


def user_request_list():
    result2 = Firebase.get("/plantation/", "thineshtes")
    for i in range(100):

        try:
            key1 = tuple(result2.keys())[i]
            #key2 = tuple(result2[key1].keys())[i]
            #key3 = tuple(result2[key2].keys())[0]
            area = result2[key1]['Area']
            name_final = result2[key1]['Name']
            service_of = result2[key1]['Service']
            imageid_of = result2[key1]['imageid']
            location_info = result2[key1]['location']
            # key3 = tuple(result2.keys())[1]'''

            print(key1)
            print(area)
            print(name_final)
            print(service_of)
            print(imageid_of)
            print(location_info)
            #j = j+1
        except:
            print("exit")
            exit()


user_request_list()
