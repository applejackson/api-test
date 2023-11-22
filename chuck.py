import requests

class Test_new_joke():
    # create new jokes
    def __init__(self):
        pass

    def test_create_new_random_categories_joke(self):
        #create rendom joke on opr theme
        category = "spor"

        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print("Status code : " + str(result.status_code))
        assert 404 == result.status_code
        if result.status_code == 404:
            print("Success! We get new joke")
        else:
            print("Lose! Request bad")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ["spor"]
        print("Categories true")
        # check_info_value  = check.get("value")
        # print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print("Chuck yes")
        # else:
        #     print("Chuck no")


sport_joke = Test_new_joke()
sport_joke.test_create_new_random_categories_joke()