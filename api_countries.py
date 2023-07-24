import requests

def listar_nombre_paises(url):
    paises = requests.get(url)
    paises = paises.json()

    for pais in paises:
        print(f"Nombre Oficial:{pais['name']['official']}")
        print(f"La capital es: {pais['capital'][0]}")

        #print(f"La moneda es: {pais['currencies']}")

        diccionario_monedas = pais['currencies']
        for clave_moneda, datos_moneda in diccionario_monedas.items():
            nombre_moneda = datos_moneda['name']
            print(f"Nombre de la moneda {clave_moneda}: {nombre_moneda}")

        #print(f"El codigo telefonico es: {pais['idd']['root']}")
        codigo_telefono = pais['idd']['root']
        sufijos = pais['idd']['suffixes']
        # Unimos el código telefónico con los sufijos
        codigo_completo = codigo_telefono + "".join(sufijos)
        # Imprimimos el resultado
        print(f"Código telefónico completo: {codigo_completo}")

        print()
url = "https://restcountries.com/v3.1/independent?status=true"
listar_nombre_paises(url)