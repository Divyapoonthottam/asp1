from bs4 import BeautifulSoup
import requests

def get_html_for_url(url):
    response=requests.get(url)
    return response.text

def get_meta_tags_in_html(html):
    soup=BeautifulSoup (html,features="html.parser")
    meta_tags=soup.find_all("meta")
    named_meta_tags={}
    for meta_tag in meta_tags:
        if "name" in meta_tag.attrs:
            name=meta_tag.attrs["name"]
            content=meta_tag.attrs["content"]
            named_meta_tags[name]=content
    return named_meta_tags        

def search_for_meta_tags_in_url(url,meta_tag_name):
    html_content=get_html_for_url(url)
    named_meta_tags=get_meta_tags_in_html(html_content)
    if meta_tag_name in named_meta_tags:
        return named_meta_tags[meta_tag_name]