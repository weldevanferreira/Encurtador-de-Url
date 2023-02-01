import pyshorteners

url = input('Qual seria o link: ')

s = pyshorteners.Shortener(api_key='Sua API Bitly')

shortUrl = s.bitly.short(url)

print(f" Url encurtada: {shortUrl}")

