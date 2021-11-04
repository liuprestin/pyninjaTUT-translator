from translate import Translator 

translator = Translator(to_lang="zh")
try:
    with open('./example.md', mode='r') as in_file:
        text = in_file.read()
    
    with open('./example-tranlated.md', mode='w') as trans_file:
        trans_file.write(translator.translate(text))
        

except FileNotFoundError as e:
    print('check your file path')