import requests
# from pprint import pprint

class Hero():

    def __init__(self, name):
        self.name = name

    def search_intelligence(self):
        url = f"https://superheroapi.com/api/2619421814940190/search/{self.name}"
        data = requests.post(url, timeout=5)
        # print(data.json())
        return data.json()

    def ent_intel_hero(self):
        intelligence = int(self.search_intelligence()['results'][0]['powerstats']['intelligence'])
        # print(self.intelligence)
        return intelligence

    def __lt__(self, other):
        if not isinstance(other, Hero):
            print('Invalid data.')
            return
        elif self.ent_intel_hero() > other.ent_intel_hero():
            print(f'{self.name} intelligence = {self.ent_intel_hero()}.\nHe is smarter!')
        else:
            print(f'{other.name} intelligence = {self.ent_intel_hero()}.\nHe is smarter!')

Thanos = Hero('Thanos')
Hulk = Hero('Hulk')
Cap_America = Hero('Captain America')

Thanos.search_intelligence()
Hulk.search_intelligence()
Cap_America.search_intelligence()

Thanos.ent_intel_hero()
Hulk.ent_intel_hero()
Cap_America.ent_intel_hero()

Hulk > Cap_America
Thanos > Hulk
Cap_America > Thanos