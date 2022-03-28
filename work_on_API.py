import requests

class Hero:

    def __init__(self, name):
        self.name = name

    def search_intelligence(self):
        url = f"https://superheroapi.com/api/2619421814940190/search/{self.name}"
        data = requests.post(url, timeout=5)
        return data.json()

    def ent_intel_hero(self):
        self.intelligence = int(self.search_intelligence()['results'][0]['powerstats']['intelligence'])
        # print(self.intelligence)
        return self.intelligence

Thanos = Hero('Thanos')
Hulk = Hero('Hulk')
Cap_America = Hero('Captain America')

def very_smartest(first=Thanos, second=Hulk, third=Cap_America):
    very_smart = max(first.ent_intel_hero(), second.ent_intel_hero(), third.ent_intel_hero())
    for i in first,second, third:
        if i.ent_intel_hero() == very_smart:
            name = i.name
    return f"Smartest hero {name}. IQ = {very_smart}"

print(very_smartest())