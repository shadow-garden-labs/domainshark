from urllib.parse import urlparse

subdomain_list = ['mail', 'mail2', 'www', 'ns2', 'ns1', 'blog', 'localhost', 'm', 'ftp', 
    'mobile', 'ns3', 'smtp', 'search', 'api', 'dev', 'secure', 'webmail', 'admin', 'img',
    'news', 'sms', 'marketing', 'test', 'video', 'www2', 'media', 'static', 'ads', 'mail2',
    'beta', 'wap', 'blogs', 'download', 'dns1', 'www3', 'origin', 'shop', 'forum', 'chat',
    'www1', 'image', 'new', 'tv', 'dns', 'services', 'music', 'images', 'pay', 'ddrint', 'conc']

subdomain_dict = {"Subdomain URLs": []}

new_subdomain_dict = {"New Subdomain URLs": []}

def test_subdomain():

    domain_name = 'google.com'

    for subdomain in subdomain_list:
        
        url = f'https://{subdomain}.{domain_name}'

        subdomain_dict["Subdomain URLs"].append(url)

    print(subdomain_dict)


def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        # Verify both the scheme and host destination exist
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def new_dict():

    for url in subdomain_dict:

        if is_valid_url(url):

            new_subdomain_dict["New Subdomain URLs"].append(url)

    return new_subdomain_dict

test = {"New Subdomain URLs": []}

test["New Subdomain URLs"].append("Hello")

print(new_subdomain_dict)