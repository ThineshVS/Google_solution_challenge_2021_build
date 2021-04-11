def register_info(em, st, ar, co, pl, im):
    import json
    import requests
    import pyrebase
    from PIL import Image

    config = {
        "apiKey": "AIzaSyAG3rD_v048j8lz2QH8_ZfXDT0Cx8cdR_U",
        "authDomain": "grobage.firebaseapp.com",
        "databaseURL": "https://grobage-default-rtdb.firebaseio.com/",
        "projectId": "grobage",
        "storageBucket": "grobage.appspot.com",
        "messagingSenderId": "342165659797",
        "appId": "1:342165659797:web:0bc3271cae24a079547b9c",
        "measurementId": "G-S3TEHSRTM1"}

    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    # User information
    email_info = em
    stock_name = st
    area_name = ar
    contact_info = co
    plant_count = pl
    # end of user information

    # map_location
    send_url = "http://api.ipstack.com/check?access_key=716837ec670b004b7728dfe71a174afd"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    city = geo_json['city']
    location1 = "https://www.google.com/maps?q={},{}".format(
        latitude, longitude)
    # end of map location

    # image upload
    image_file = im
    email_info1 = email_info.rstrip("@gmail.com")
    name_of_the_file = "images/" + \
        str(email_info1) + str(plant_count) + ".jpg"
    path_on_cloud = name_of_the_file
    storage.child(path_on_cloud).put(image_file)

    def requestid_update():
        from firebase import firebase
        Firebase = firebase.FirebaseApplication(
            'https://grobage-default-rtdb.firebaseio.com/', None)
        request_id = Firebase.get("/Requests", "Request")
        request_id1 = int(request_id)
        request_id1 = request_id1 + 1
        request_id1 = request_id1
        Firebase.put("/Requests", "Request", request_id1)

    def upload_fire():
        from firebase import firebase
        Firebase = firebase.FirebaseApplication(
            'https://grobage-default-rtdb.firebaseio.com/', None)
        data = {'Service': stock_name,
                'Name': email_info1,
                'Area': area_name,
                'location': location1,
                'imageid': name_of_the_file
                }
        # + "User Request"  # + "/" + email_info1
        upload_string = "/" + stock_name + "/" + email_info1

        #data = {email_info1: data}
        result = Firebase.post(
            upload_string, data)  # data={email_info1: data})

    upload_fire()
    requestid_update()
