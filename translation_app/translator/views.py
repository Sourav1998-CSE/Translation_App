from django.shortcuts import render
from googletrans import Translator

def translate(request):
    if request.method == 'POST':
        text_to_translate = request.POST.get('text_to_translate', '')
        target_language = request.POST.get('target_language', '')

        translator = Translator()
        translation = translator.translate(text_to_translate, dest=target_language)

        return render(request, 'translator/translate.html', {'translation': translation.text})

    return render(request, 'translator/translate.html')

