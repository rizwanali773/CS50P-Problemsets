import requests, sys, json

try:
    if len(sys.argv) != 2:
        print("Missing command line arguments")
        sys.exit(1)
    else:
        sys.argv[1] = float(sys.argv[1])
except ValueError:
    print("Command line argument is not a number")
    sys.exit(1)

response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=4ca72c9c946442126a3790d988b3789ccf9641ee919b9ed0e43e8da3f994b1bf")

object = response.json()
# print(json.dumps(response.json(), indent = 2))

rate = object['data']['priceUsd']
rate = float(rate)

num = sys.argv[1]
amount = num * rate

print(f"${amount:,.4f}")

