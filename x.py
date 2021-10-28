import googletrans
from googletrans import Translator

#print(googletrans.LANGUAGES)

translator=Translator()

text="ઓસ્ટિન ટાઉન, બેંગલોર, બેંગલોર ઈસ્ટ, 560095"
y=translator.detect(text)
print(y.lang)
x=translator.translate(text,src='en',dest='hi')
print(x.text)
