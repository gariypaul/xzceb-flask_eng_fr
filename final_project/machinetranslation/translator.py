from deep_translator import MyMemoryTranslator

def english_to_french(englishText):
    '''This function translates text from english to french'''
    frenchText = MyMemoryTranslator(source='english', target='french').translate(englishText)
    return frenchText

def french_to_english(frenchText):
    '''This function translates text from english to french'''
    englishText = MyMemoryTranslator(source='french', target='english').translate(frenchText)
    return englishText