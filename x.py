import googletrans
from googletrans import Translator

#print(googletrans.LANGUAGES)

translator=Translator()

text="ਆਸਟਿਨ ਟਾਊਨ, ਬੰਗਲੌਰ, ਬੰਗਲੌਰ ਈਸਟ, 560095"
y=translator.detect(text)
print(y.lang)
x=translator.translate(text,src='en',dest='hi')
print(x.text)
