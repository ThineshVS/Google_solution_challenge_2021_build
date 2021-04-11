from firebase import firebase
Firebase = firebase.FirebaseApplication(
    'https://grobage-default-rtdb.firebaseio.com/', None)
'''def requestid_update():
    request_id = Firebase.get("/Requests", "Request")
    request_id1 = int(request_id)
    request_id1 += 1
    request_id1 = request_id1
    Firebase.put("/Requests", "Request", request_id1)'''


'''def user_requestid():
    try:
        user_request = Firebase.get("/thineshtes", "Request")
        user_request += 1
        Firebase.put("/thineshtes", "Request", request_id1)
    except:
        #Firebase.put("/thineshtes", {"Request": 1})
        Firebase.put("/thineshtes", "Request", 1)


user_requestid()'''

'''def requestid_update():
    request_id = Firebase.get("/Requests", "Request")
    request_id1 = int(request_id)
    request_id1 = request_id1 + 1
    request_id1 = request_id1
    Firebase.put("/Requests", "Request", request_id1)'''

'''result2 = Firebase.get("/plantation/", "thineshtes")
key1 = tuple(result2.keys())[0]
key3 = tuple(result2.keys())[1]
key2 = tuple(result2[key1].keys())[0]
# print(result2)
print(key1)
print(key3)'''
