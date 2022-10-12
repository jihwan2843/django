import googletrans
from googletrans import Translator

print(googletrans.LANGUAGES)

text1 = "안녕하세요"

translator = Translator()

print(translator.detect(text1))

trans1 = translator.translate(text1, src='ko', dest='ja')

print("English to Japanese: ", trans1.text)
