from urllib.parse import urlparse

url = "142.251.34.238"

# Extract the network location (hostname)
netloc = urlparse(url).netloc
print(netloc)  # Output: www.example.com

# Strip 'www.' manually for a cleaner look
if netloc.startswith("www."):
    human_readable_domain = netloc[4:]
else:
    human_readable_domain = netloc

print(human_readable_domain)  # Output: example.com
