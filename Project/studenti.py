studenti = {
    "RA 112/2021":{
        "ime": "Nikola",
        "prezime": "Jovanovic",
        "godina": 4,
        "ocene": None,
        "prosek": 0
        },
    "IN 142/2023":{
        "ime": "Boban",
        "prezime": "Misic",
        "godina": 2,
        "ocene": None,
        "prosek": 0
        },
    "LF 001/2021":{
        "ime": "Pavle",
        "prezime": "Andjelkovic",
        "godina": 3,
        "ocene": None,
        "prosek": 0
        }
    }
studenti["RA 112/2021"]["ime"] ="Nikola"
studenti["IN 142/2023"]["ime"]="Boban"
studenti["LF 001/2021"]["ime"]="Pavle"
studenti["RA 112/2021"]["prezime"] ="Jovanovic"
studenti["IN 142/2023"]["prezime"]= "Misic"
studenti["LF 001/2021"]["prezime"]="Andjelkovic"
studenti["RA 112/2021"]["godina"] = 2
studenti["IN 142/2023"]["godina"] = 3
studenti["LF 001/2021"]["godina"] = 4
studenti["RA 112/2021"]["ocene"] = [5, 6, 7, 10, 10, 10, 10, 10]
studenti["IN 142/2023"]["ocene"] = [5, 7, 8,5, 6]
studenti["LF 001/2021"]["ocene"] = [10, 9, 8, 9,7, 8]
def prosek(x):
    return(sum(x)/len(x))
studenti["RA 112/2021"]["prosek"] = [prosek(studenti["RA 112/2021"]["ocene"])]
studenti["IN 142/2023"]["prosek"] = [prosek(studenti["IN 142/2023"]["ocene"])]
studenti["LF 001/2021"]["prosek"] = [prosek(studenti["LF 001/2021"]["ocene"])]
print(studenti["RA 112/2021"]["prosek"],studenti["RA 112/2021"]["ocene"])
print(studenti["IN 142/2023"]["prosek"],studenti["IN 142/2023"]["ocene"])
print(studenti["LF 001/2021"]["prosek"],studenti["LF 001/2021"]["ocene"])
