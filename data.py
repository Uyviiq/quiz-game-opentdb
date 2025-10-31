import requests
proxies = {
    "https":"10.156.167.122:8080",
    "http":"10.156.167.122:8080"
}
url = "https://opentdb.com/api.php"
cate = {
    "Any Category":"any",
    "General Knowledge":9,
    "Video Games":15,
    "Computers":18
    }
remove_category_from_payload = False
question_data = None
def questions():
    global remove_category_from_payload,question_data
    number = int(input("how many question do you want?: ").strip())
    while True:
        category = input("what Category type 's' to show all categories: ").strip().title()
        if category == "":
            category = "Any Category"
            remove_category_from_payload = True
            break
        elif category == 'S':
            for item in cate:
                print(item)
        elif category in cate:
            break
    difficulty = input("Choose the difficulty easy/medium/hard : ").strip()
    payload = {
        "amount":number,
        "category":cate[category],
        "difficulty": difficulty
    }
    if remove_category_from_payload:
        payload.pop("category")
    try:
        response = requests.get(url,params=payload,headers={"Accept":"application/json"},proxies=proxies).json()
        response.pop("response_code")
        question_data = list(response["results"][:])
    except Exception as e:
        print("Error fetching data:",e)
    return question_data