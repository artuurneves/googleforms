import requests
import random
import dicts
import config
count = 1
while True:
    firstname = f"{dicts.fname[random.randint(0,len(dicts.fname)-1)]}"
    lastname = f"{dicts.lname[random.randint(0,len(dicts.lname)-1)]}"
    fullname = f"{firstname} {lastname}"
    email = f"{firstname}.{lastname}{dicts.domain[random.randint(0,len(dicts.domain)-1)]}"
    endereco = f"{dicts.endereco[random.randint(0,len(dicts.endereco)-1)]}"
    presidente = f"{dicts.presidentes[random.randint(0, len(dicts.presidentes)-1)]}"
    ano = random.randint(1940, 2002)
    idade = 2018 - ano

    post = f"{config.url}entry.2005620554={fullname}" \
           f"&entry.1045781291={email}" \
           f"&entry.1065046570={endereco}" \
           f"&entry.1166974658={presidente}" \
           f"&entry.839337160={idade}"

    result = requests.post(post)
    # print(result.status_code)
    if result.status_code != 200:
        print(f"""
            Nome: {fullname}
            E-mail: {email}
            Endereço: {endereco}
            Presidente: {presidente}
            Idade: {idade}
            """)
    count = count + 1
