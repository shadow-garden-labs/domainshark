from urllib.parse import urlparse
import requests

domain_name = 'google.com'


subdomain_list = ['mail', 'mail2', 'www', 'ns2', 'ns1', 'blog', 'localhost', 'm', 'ftp', 
    'mobile', 'ns3', 'smtp', 'search', 'api', 'dev', 'secure', 'webmail', 'admin', 'img',
    'news', 'sms', 'marketing', 'test', 'video', 'www2', 'media', 'static', 'ads', 'mail2',
    'beta', 'wap', 'blogs', 'download', 'dns1', 'www3', 'origin', 'shop', 'forum', 'chat',
    'www1', 'image', 'new', 'tv', 'dns', 'services', 'music', 'images', 'pay', 'ddrint', 'conc']

subdomain_dict = {"Subdomain URLs": []}

new_subdomain_dict = {"New Subdomain URLs": []}

def update_subdomain_dict():

    for subdomain in subdomain_list:
        
        url = f'https://{subdomain}.{domain_name}'

        subdomain_dict["Subdomain URLs"].append(url)



def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        # Verify both the scheme and host destination exist
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def sublist3r():

    domain_name = 'google.com'

    for subdomain in subdomain_list:

        url = f'https://{subdomain}.{domain_name}'

        try:
            # sending get request to the url
            requests.get(url)
        
            # if after putting subdomain one by one url 
            # is valid then printing the url
            subdomain_dict["Subdomain URLs"].append(url)
        
            # if url is invalid then pass it
        except (requests.ConnectionError, requests.Timeout):

            pass


update_subdomain_dict()

sublist3r()

print(subdomain_dict)