import requests

def send_request():
    # url = "http://localhost:5000/predict"
    url = "https://abitur.pythonanywhere.com/predict"

    for i in range(1, 13):
        x_json = {
            "year":2021,
            "month":i
        }

        r = requests.post(url, json = x_json)

        print(r.text.strip())

if __name__ == "__main__":
    send_request()