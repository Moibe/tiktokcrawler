url = "https://www.google.com/search?q=hola"
segments = url.split("/")

last_segment = segments.pop()

print(last_segment)