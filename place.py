import requests

class Test_new_location():
    #work with new location

    def test_create_new_location(self):

        base_url = "https://rahulshettyacademy.com"      #base url
        key = "?key=qaclick123"                         #parametr all requests

        #  create new loaction
        post_resource = "/maps/api/place/add/json"       # resource method Post

        post_url = base_url + post_resource + key
        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }

        result_post = requests.post(post_url, json=json_for_create_new_location) #отправляем запрос по методу пост
        print(result_post.text)
        print("Status code : " + str(result_post.status_code))
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Success! Create new location")
        else:
            print("Lose! Request bad")

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("Status code answer: " + check_info_post)
        assert check_info_post
        print("Status answer true")
        place_id = check_post.get("place_id")
        print("Place_id : " + place_id)

        #проверка создания новой локации

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)

        print("Status code : " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Success! Check create new location success")
        else:
            print("Lose! Request bad")

        """изменение новой локации"""

        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"

        }
        result_put = requests.put(put_url, json = json_for_update_new_location)
        print(result_put.text)
        print("Status code : " + str(result_put.status_code))
        assert 200 == result_put.status_code
        if result_put.status_code == 200:
            print("Success! Check changes new location success")
        else:
            print("Lose! Request bad")

        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        print("Message :" + check_put_info)
        assert check_put_info == "Address successfully updated"
        print("Message don't true")

        """Проверка изменения новой локации"""

        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!! Проверка изменения новой локации прошла успешно")
        else:
            print("Провал!!! Запрос ошибочный")
        check_address = result_get.json()
        check_address_info = check_address.get("address")
        print("Сообщение : " + check_address_info)
        assert check_address_info == "100 Lenina street, RU"
        print("Сообщение верно")

        """Удаление новой локации"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = requests.delete(delete_url, json = json_for_delete_new_location)
        print(result_delete.text)
        print("Статус код : " + str(result_delete.status_code))
        assert 200 == result_delete.status_code
        if result_delete.status_code == 200:
            print("Успешно!!! Удаление прошло успешно")
        else:
            print("Провал!!! Запрос ошибочный")
        check_status = result_delete.json()
        check_status_info = check_status.get("status")
        print("Сообщение : " + check_status_info)
        assert check_status_info == "OK"
        print("Сообщение верно")

        """Проверка удаления новой локации"""

        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 404 == result_get.status_code
        if result_get.status_code == 404:
            print("Успешно!!! Проверка удаления новой локации прошла успешно")
        else:
            print("Провал!!! Запрос ошибочный")
        check_msg = result_get.json()
        check_msg_info = check_msg.get("msg")
        print("Сообщение : " + check_msg_info)
        assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists"
        print("Сообщение верно") 

        print("Тестирование Twst_new_location завершено успешно")






new_place = Test_new_location()
new_place.test_create_new_location()