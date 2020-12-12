import random
champs = ['Barcelona (ESP)', 'Bayern (GER)', 'Benfica (POR)', 'Chelsea (ENG)', 'Juventus (ITA)', 'Paris (FRA)', 'PSV (NED)', 'Zenit (RUS)']
other = ['Arsenal (ENG)', 'Astana (KAZ)', 'Atlético (ESP)', 'BATE (BLR)', 'CSKA Moskva (RUS)', 'Dinamo Zagreb (CRO)', 'Dynamo Kyiv (UKR)', 'Galatasaray (TUR)', 'Gent (BEL)', 'Leverkusen (GER)', 'Lyon (FRA)', 'M. Tel-Aviv (ISR)', 'Malmö (SWE)', 'Man. City (ENG)', 'Man. United (ENG)', 'Mönchengladbach (GER)', 'Olympiacos (GRE)', 'Porto (POR)', 'Real Madrid (ESP)', 'Roma (ITA)', 'Sevilla (ESP)', 'Shakhtar Donetsk (UKR)', 'Valencia (ESP)', 'Wolfsburg (GER)']

random.shuffle(champs)
random.shuffle(other)
allUsed = dict()
def dance():
	team = list()
	for place in champs:
		if place not in allUsed:
			team.append(place)
			allUsed[place] = 1
			break
	d = {team[0].split()[-1] : 1}
	for place in other:
		if place.split()[-1] not in d and place not in allUsed:
			d[place.split()[-1]] = 1
			allUsed[place] = 1
			team.append(place)
		if len(team) == 4:
			return team
for gp in 'ABCDEFGH':
	team = dance()
	print('Group',gp)
	print(team)
