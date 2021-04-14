import requests
import time

# Ler as Msgs
resultados_save = ''
while True:
 token = 
  '1715148022:AAHrWIgTdOfLIq4-AENGPlgRncxm9sBFLlE'
  url_base = f'https://api.telegram.org/bot{token}/getUpdates'
  resultados = requests.get(url_base)
  if resultados_save != resultados:
    print(resultado.json())
    resultados_save = resultados
  time.sleep (2)
  
