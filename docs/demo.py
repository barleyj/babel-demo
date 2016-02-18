import urllib2
import json

def get_repos_for(user):
    results = urllib2.urlopen('https://api.github.com/users/barleyj/repos')
    content = results.read()
    repos = json.loads(content)
    return [repo['name'] for repo in repos]
