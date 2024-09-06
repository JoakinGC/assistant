import re

patron_url = re.compile(
    r'((http|https):\/\/)?(www\.)?([a-zA-Z0-9-_]+\.[a-zA-Z]+)(\/[a-zA-Z0-9-_#]+\/?)*'
)
