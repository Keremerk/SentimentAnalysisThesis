import csv
from textblob import TextBlob

#C:\Users\Kerem\Desktop\111\Transcripts_eng
infile = 'C:\\Users\\Kerem\\Desktop\\111\\abc.csv'
total_count = 0
count_positive = 0
count_negative = 0
count_neutral = 0

with open(infile, 'r', encoding="utf8") as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        sentence = row[0]
        total_count= total_count+1 
        blob1 = TextBlob(sentence)
        print(blob1.sentiment)
        if (blob1.sentiment.polarity) > 0:
            count_positive= count_positive + 1
        elif (blob1.sentiment.polarity) < 0:
            count_negative= count_negative + 1
        elif (blob1.sentiment.polarity) == 0.0:
            count_neutral= count_neutral + 1

print (count_positive, "adet pozitif cümle var")
print (count_negative, "adet negatif cümle var")
print (count_neutral, "adet nötr cümle var")
print ("Verinin pozitifilik yüzdesi =", (count_positive/total_count)*100 )