from deep_translator import GoogleTranslator

def to_fa(textfa):
    translated = GoogleTranslator(source='en', target='fa').translate(textfa)
    return (translated)

def to_en(textfa):
    translated = GoogleTranslator(source='fa', target='en').translate(textfa)
    return (translated)


print( to_en("....سلام من به انگلیسی ترجمه شدم "))
print( to_fa("hi i am python .... "))
