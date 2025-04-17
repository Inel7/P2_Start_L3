def is_good_or_bad_bot(json):
    is_good_bot = json["botProps"]["isGoodBot"]
    is_suspected_bad_bot = json["botProps"]["isSuspectedBadBot"]
    print(f"Is good bot? {is_good_bot}")
    print(f"Is suspected bad bot? {is_suspected_bad_bot}")

# ...

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(response.status_code)
    data = None

if data is None:
    print('no data received')
else:
    is_good_or_bad_bot(data)
