
import pandas as pd
import os

from bcch import BancoCentralDeChile

# Por seguridad, es mejor guardar las contraseñas y usuarios en las variables de entorno
bcch_user = os.environ['BCCH_USER']
bcch_pwd = os.environ['BBCH_PWD']

# Creación de la instancia
client = BancoCentralDeChile(bcch_user, bcch_pwd)

# Verificar que series son de frequencia trimestral
resp = pd.DataFrame(
    client.get_busqueda(frecuencia='quarterly')
    )

# Solicitar la Deuda pública en relación al PIB (porcentaje del PIB)
resp = pd.DataFrame(
    client.get_macro(serie='F012.PPCP.FLU.N.7.AME.CL.USD.FMI.Z.0.A')
    )

print(resp.head())

resp.to_csv('/Users/rosario/Downloads/bcch_scrapped.csv', index=False)