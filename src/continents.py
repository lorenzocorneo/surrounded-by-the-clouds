_countries = dict()

dataset_path = "./data/continents.csv"

with open(dataset_path) as f:
    _countries = {
        l.split(",")[0]: l.rstrip("\n").split(",")[1]
        for l in f.readlines()[1:]
    }

with open("./data/iso2-iso3.csv") as f:
    _iso3_to_iso2 = {
        l.split(",")[2]: l.rstrip("\n").split(",")[1]
        for l in f.readlines()[1:]
    }


def get_continent(isocode):
    return _countries.get(isocode)


def get_countries(continent):
    return [
        country for country, cont in _countries.items()
        if continent.upper() == cont
    ]

def iso3_to_iso2(iso3: str) -> str:
    return _iso3_to_iso2.get(iso3)


def get_all_countries():
    return [country for country, _ in _countries.items()]
