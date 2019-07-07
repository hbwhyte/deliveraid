import csv

with open("PMNCH_partners_raw.txt") as f_in:
    lines = filter(None, (line.rstrip() for line in f_in))

lst = []
partners = []
addNext = False
addLast = False


class Partner:
    def __init__(self, name, constituency, focus, country, region):
        self.name = name
        self.constituency = constituency
        self.focus = focus
        self.country = country
        self.region = region

    def __getitem__(self, key):
        if isinstance(key, int):
            return key

    def partnerList(self):
        pl = [self.name, self.constituency, self.focus, self.country, self.region]
        return pl

    def countryList(self):
        cl = [self.name, self.country]
        return cl

    def choropleth(self):
        choro = [self.name, self.country]
        return choro


for line in lines:
    if 'orgchartBoxTitle' in line:
        line = line.split('orgchartBoxTitle">')
        name = line[1].replace('</font>', '').strip()
        if len(name) > 0: lst.append(name)
    elif 'Constituency' in line or 'Health focus' in line or 'Country' in line:
        addNext = True
    elif 'WHO region' in line:
        addLast = True
    elif addNext:
        value = line.replace('<br>', '').strip()
        lst.append(value)
        addNext = False
    elif addLast:
        region = line.replace('<br>', '').strip()
        name = lst[0]
        constituency = lst[1]
        focus = lst[2]
        country = lst[3]
        partner = Partner(name, constituency, focus, country, region)
        partners.append(partner)
        del lst[:]
        addLast = False

choro = {}
for partner in partners:
    if partner.country in choro:
        choro[partner.country] += 1
    else:
        choro[partner.country] = 1

with open('countries.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for partner in partners:
        wr.writerow(partner.countryList())

with open('countries_choro.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for ch in choro:
        concat = ch + "," + str(choro[ch])
        print concat
        wr.writerow([ch])
        wr.writerow([choro[ch]])
