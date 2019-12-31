from translate import Translator

translator = Translator(to_lang="ja")
#ja = Japanese


try:
    with open('textToTranslate.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('./test-ja.txt', mode='w') as my_file_2:
            my_file_2.write(translation)
except FileNotFoundError as e:
        print('check your file path')