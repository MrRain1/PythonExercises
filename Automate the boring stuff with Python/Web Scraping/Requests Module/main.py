import requests

# to download a file we can use the request.get() method

response = requests.get("https://automatetheboringstuff.com/files/rj.txt")
response.status_code
len(response.text)
print(response.text[:500])

# another way to see if the download was successful or nots is rising an exception

response.raise_for_status()
# badRes = requests.get("https://automatetheboringstuff.com/files/asdaqg")
# badRes.raise_for_status()

# to save the downloaded text into a file we do:

with open("./R&J.txt", "wb") as txt_file:
    for chunk in response.iter_content(100000):
        txt_file.write(chunk)