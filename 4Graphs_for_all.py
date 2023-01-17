import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

## Çağla ile yeni bir gün oranları 112 37 37
## Müge anlı 77 , 44 , 86 41.46
## gelinim mutfakta 98 , 22 , 18
## Müge ve gülşen 72 , 15 , 5
## seda sayan 103 , 37 , 63


objects = ('Çağla ile Yeni Bir Gün', 'Sabahın Sultanı Seda Sayan',
 'Müge Anlı ile Tatlı Sert', 'Müge ve Gülşen ile 2. Sayfa', 'Gelinim Mutfakta')
y_pos = np.arange(len(objects))
performance = [60.21,50.73,41.46,51.66,71]

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Pozitiflik Yüzdesi')
plt.title('Programlar')

plt.show()