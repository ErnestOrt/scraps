import requests
from bs4 import BeautifulSoup

CSV_SEPARATOR = '|'

def getGithubInfo(name, link):
    github = BeautifulSoup(requests.get(link).content, 'html.parser')
    socialCounts = github.find_all('a', class_='social-count')
    csvLine = name;
    for socialCount in socialCounts:
        csvLine = csvLine+ CSV_SEPARATOR + socialCount.getText().strip()
    
    print(csvLine.replace('\r', '').replace('\n', '').replace(',', '.'))


getGithubInfo('Trampoline', 'https://github.com/ErnestOrt/Trampoline')
getGithubInfo('Spring AMQP', 'https://github.com/spring-projects/spring-amqp')

soupSpringProjects = BeautifulSoup(requests.get("https://spring.io/projects/spring-boot").content, 'html.parser')
projectLis = soupSpringProjects.find_all('li', class_='sidebar_project')

for projectLi in projectLis:
    projectName = projectLi.find_all('a')[0].getText();
   
    soupSpringProject = BeautifulSoup(requests.get(projectLi.find_all('a')[0]['href']).content, 'html.parser')

    anchorsGithub = soupSpringProject.find_all('a', class_='link--github')
    
    if anchorsGithub:
        getGithubInfo(projectName, anchorsGithub[0]['href'])
    else:
        anchorsGithub = soupSpringProject.find_all('a', class_='project-link')
        
        if anchorsGithub:
            getGithubInfo(projectName, anchorsGithub[0]['href'])            


