import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

## Çağla ile Yeni Bir Gün oranları 84 adet pozitif cümle var 21 adet negatif cümle var 11 adet nötr cümle var 112 37 37
## Müge Anlı ile Tatlı Sert 77 (68) , 39 , 86(57 ) 41.46
## Gelinim Mutfakta 98 , 22 , 18
## Müge ve Gülşen ile 2. Sayfa 72 93 , 15 36  , 5 51
## seda sayan 103 , 37 , 63
objects = ('Pozitif Cümleler', 'Negatif Cümleler', 'Nötr Cümleler')
y_pos = np.arange(len(objects))
performance = [98,22,18]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Cümle Sayıları')
plt.title('Gelinim Mutfakta')

plt.show()