###############################################
import pandas as pd
from os import path

df = pd.read_csv('muge.csv')

def trans(s):
  from googletrans import Translator
  translator = Translator()
  return (translator.translate(s).text)

df.transcript = df.transcript.apply(trans)
print(df.transcript)
df.transcript.to_csv('transcript_muge_eng.csv', index=False)

#################################################

#with open('transcript_cagla_ile_yeni_gun_eng.csv', 'w', newline='') as file:
# writer = csv.writer(file)
# writer.writerows(df.transcript)

