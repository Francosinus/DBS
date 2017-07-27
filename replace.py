import csv
from collections import Counter
from collections import OrderedDict
import re

in_file = open("C:/Users/topsen/Desktop/CSV/noduplicates.csv","r")
in_file2 = open("C:/Users/topsen/Desktop/CSV/cluster3.csv","r")  
out_file= open("C:/Users/topsen/Desktop/CSV/Idonerow.csv","wb" )

reader = csv.reader(in_file,delimiter=";")

reader2 = csv.reader(in_file2,delimiter=";")
writer = csv.writer(out_file,delimiter=";")
liste = []
liste2 = []
duplicates = set()

for row in reader2:
	liste2.append(row)
flattened  = [val for sublist in liste2 for val in sublist]
print flattened

laenge = []
laenge = list(range(len(flattened)))
#for i in flattened:#
#	laenge.append(len(i))

	
final = zip(flattened,laenge)
print final#print liste2

for word in final:
	writer.writerow([word])

ids = [x[1] for x in final]
j = []
for bla in liste2:
	j.append(len(bla)-1)
#	results = [(ids[j-1],num) for num in ids, ]

for x in j:
	zip(ids[y-x])
	y= x
	y+= y

print j
print results
#print results
#for word in final:
#	if word ==
#for i in liste2:
#	for i in liste2:


for row in reader:
	liste.append(row[0])
#print liste
liste = sorted(liste, key=len)
liste = list(reversed(liste))
#print liste
dictZ = OrderedDict(zip(liste,range(len(liste))))

print dictZ
#dictZ_sorted_keys = sorted(dictZ, key=dictZ.get, reverse=False)

#print dictZ_sorted_keys

#print dictZ
#nodups = list(reader)
#print nodups

#print dictZ

similiar = " VoterRegistrationDay NationalVoterRegistrationDay VoterRegistrationDay\
 MakeAmericaGreatAgain MakeAmericaGreatAgain MakeYoutubeGreatAgain makeamericagreatagain\
 debatenight DebateNight Debates2016 FallonTonight Srebrenica debatenight\
 TrumpPence16 TrumpCountry TrumpForPresident TrumpMovement TrumpPence16 TrumpPence2016\
 ImWithYou ImWithHer ImWithYou Statehood TrumpIsWithYou imwithher\
 MyTeacherIsWeird MyTeacherIsWeird\
 VoteTrump AlwaysTrump LoveTrumpsHate MeetTheTrumps TeamTrump VoteTrump VoteTrump2016 VoteTrumpNH VoteTrumpNV VoteTrumpNY VoteTrumpNYhttps VoteTrumpSC VoteTrumpWI VoterFraud VotersSpeak WeWantTrump Women4Ttump presidenttrump veterans\
 BlacksForTrump BikersForTrump BlackMenForBernie BlacksForTrump CaucusForTrump Teachers4Trump\
 Rio2016 2016 LeadRight2016 RTM2016 Rio2016 TRUMP2016\
 DemConvention DemConvention GOPConvention OpeningCeremony SecondAmendment TheTonightShow\
 MSM Bush ECONOMY GOP ICYMI ISIS LESM LSSC MAGA MSM NASCAR Pulse RIP WCS16\
 DemsInPhilly DemsInPhilly DemsinPhilly\
 StrongerTogether StandTogether StrongerTogether\
 RNCinCLE DNCinPHL GOPinCLE RNCinCLE ROGERAILES Racine\
 campaignfinance campaignfinance\
 FeelTheBern BuildTheWall DefendtheSecond FeelTheBern WeAreBernie\
 StoptheHate CripTheVote DisarmHate GOPDebate LoneStarState StoptheHate goodtrouble holdthefloor\
 Trump CA4Trump Cruz Enough Prince Rubio TeamUSA Trump Trump2016 TrumpNV TrumpTrain TrumpWaikiki TrumpWon Utah4Trump brexit trump trump2016\
 Clinton CBNNews ChangeAgents Clinton ClintonKaine CommonLaw ElectionDay Filibuster KenLangone LyingTed MaitnerStrong Orlando WashingtonDC Wisconsin sitin slipping\
 AsLongAsItTakes AsLongAsItTakes\
 EndGunViolence EndGunViolence NoMoreSilence gunviolence\
 OrlandoUnited CitizensUnited OrlandoUnited\
 CAPrimary AZPrimary ArizonaPrimary CAPrimary CTPrimary CrookedHillary DEPrimary INPrimary MDPrimary NHPrimary NYPrimary NebraskaPrimary NeverHillary ORPrimary ObamaCare PAPrimary PrimaryDay RIPrimary SCPrimary UtahPrimary WIPrimary primary\
 MothersoftheMovement MothersoftheMovement\
 HillaryOnGMA Hillary2016 HillaryClinton HillaryOnGMA\
 NeverCruz DivoDeJuarez NeilCavuto NeverCruz NeverDems NeverForget TedCruz jenniferrubin\
 UTCaucus IACaucus IowaCaucus KansasCaucus NevadaCaucus UTCaucus UtahCaucus\
 AmericanSamoa AmericaFirst AmericanSamoa\
 UT 1 2A ADA AZ LGBT NATO POTUS RNC SCOTUS TBT TPP UT Utah WH\
 SuperTuesday SuperBowlSunday SuperSaturday SuperTuesday WesternTuesday\
 EndCommonCore EndCommonCore StopCommonCore\
 Mahalo Benghazi DavidCameron EauClaire Elkhart GIBill JimmyFallon Mahalo MattSchlapp Mexico MichaelBrown MichaelMoore NaturalBorn Wausau smallbiz taxplan\
 MAKEAMERICAGREATAGAIN MAKEAMERICAGREATAGAIN\
 Ford FAIL FITN Ford Fox FoxNews Jobs Jonas Mormon Polls SB50 TheDonald enough iVoted\
 Carrier Carrier Colbert Hannity JuanGabriel LaborDay LaurenceTribe LawandOrder WattersWorld\
 NewYork NewDay NewHampshire NewYork NewYorkValues NoBillNoBreak\
 MaryBrigidMcManamon MaryBrigidMcManamon\
 IAPolitics IAPolitics NHPolitics Politician"
#count = 0
#tuples = tuple(similiar,)
#for i in nodups:
#	similiar = similiar.replace(istring.(count))
#	count += 1
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, str(j))
    return text

replace = replace_all(similiar, dictZ)
print replace
#similiar2 = similiar.split()
#for word in similiar2:
#	if word in dictZ:
#		similiar = similiar.replace(word,str(dictZ[word]))
#print similiar


in_file.close()
out_file.close()
