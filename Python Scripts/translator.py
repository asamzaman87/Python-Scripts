from translate import Translator

with open("../translate.txt", mode = "r+") as my_file:
	my_file.truncate()
	my_file.write("My name is Asad Zaman")
	lang = input("Enter translator language: ")
	translator = Translator(to_lang=lang) 
	my_file.seek(0)
	original_txt = my_file.readline()

with open("../translate.txt", mode = "w") as my_file:
	translation = translator.translate(original_txt)
	my_file.write(f"{translation}")
