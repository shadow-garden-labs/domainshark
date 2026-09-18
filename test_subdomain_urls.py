from urllib.parse import urlparse
import requests

domain_name = 'google.com'


subdomain_list = [
    'mail', 'mail2', 'www', 'ns2', 'ns1', 'blog', 'localhost', 'm', 'ftp', 
    'mobile', 'ns3', 'smtp', 'search', 'api', 'dev', 'secure', 'webmail', 'admin', 'img',
    'news', 'sms', 'marketing', 'test', 'video', 'www2', 'media', 'static', 'ads', 'mail2',
    'beta', 'wap', 'blogs', 'download', 'dns1', 'www3', 'origin', 'shop', 'forum', 'chat',
    'www1', 'image', 'new', 'tv', 'dns', 'services', 'music', 'images', 'pay', 'ddrint',
    'conc'
    ]

url_lists = []


def update_subdomain_dict():

    for subdomain in subdomain_list:
        
        url = f'https://{subdomain}.{domain_name}'

        subdomain_dict["Subdomain URLs"].append(url)


def sublist3r():

    domain_name = 'google.com'

    for subdomain in subdomain_list:

        url = f'https://{subdomain}.{domain_name}'

        try:
            # sending get request to the url
            requests.get(url)

            url_lists.append(url)
        
            # if url is invalid then pass it
        except (requests.ConnectionError, requests.Timeout):

            pass



class Sublist3r:


    def __init__(self, domain_name):

        self.domain_name = domain_name
        
        self.url_list = []


    def get_subdomains(self):

        pass


    def set_subdomains(self):

        pass


    def valid_urls():

        self.domain_name = 'google.com'

        for subdomain in subdomain_list:

            url = f'https://{subdomain}.{self.domain_name}'

            try:
                # sending get request to the url
                requests.get(url)
            
                # if after putting subdomain one by one url 
                # is valid then printing the url
                self.url_list.append(url)
            
                # if url is invalid then pass it
            except (requests.ConnectionError, requests.Timeout):

                pass




sublist3r()

print(url_lists)