import requests
import time
from bs4 import BeautifulSoup

def getGithubLocation(link):
    xml = BeautifulSoup(requests.get("https://github.com"+ link).content, 'html.parser')
    detail = xml.find('li', itemprop='homeLocation')
    if detail is not None:
        print(detail.getText())
       

def getGithubProfiles(link):
    xml = BeautifulSoup(requests.get(link).content, 'html.parser')
    followers = xml.find_all('li', class_='follow-list-item')

    for follower in followers:
        getGithubLocation(follower.find_all('a')[0]['href'])
    

getGithubProfiles("https://github.com/ErnestOrt/Trampoline/stargazers")
getGithubProfiles("https://github.com/ErnestOrt/Trampoline/stargazers?page=2")
getGithubProfiles("https://github.com/ErnestOrt/Trampoline/stargazers?page=3")
getGithubProfiles("https://github.com/ErnestOrt/Trampoline/stargazers?page=4")
getGithubProfiles("https://github.com/ErnestOrt/Trampoline/stargazers?page=5")
getGithubProfiles("https://github.com/ErnestOrt/Trampoline/stargazers?page=6")

"""
        List<String> urls = new ArrayList<>();
        urls.add("https://nominatim.openstreetmap.org/search?q=Barcelona&format=json");
        urls.add("https://nominatim.openstreetmap.org/search?q=Leipzig&format=json");
        
        List<String> out = new ArrayList<>();

        urls.forEach(url -> {
            try {
                String result = new RestTemplate().getForObject(url, String.class);
                out.add(result.split("\"lat\":\"")[1].split("\",")[0] + ","+result.split("\"lon\":\"")[1].split("\",")[0]);
            }catch (Exception e){
                System.out.println("ERROR");
            }

        });

        out.forEach(System.out::println);

        http://www.copypastemap.com/map.php
"""