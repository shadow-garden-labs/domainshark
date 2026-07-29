import whois

# Perform the lookup
domain_info = whois.whois("google.com")

# Print the full parsed data
print(domain_info)

# Access specific attributes
print(f"Registrar: {domain_info.registrar}")
print(f"Creation Date: {domain_info.creation_date}")
print(f"Expiration Date: {domain_info.expiration_date}")
print(f"Name Servers: {domain_info.name_servers}")