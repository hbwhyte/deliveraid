with open("PMNCH_partners_raw.txt") as f_in:
    lines = filter(None, (line.rstrip() for line in f_in))
lst = []
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
        del lst[:]
        addLast = False
