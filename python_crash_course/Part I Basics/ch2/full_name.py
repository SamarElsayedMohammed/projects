first_name ="samaR"
last_name  ="elsayeD"
full_name  =f"{first_name} {last_name}"
message    = f"welcome {first_name.title()} {last_name.title()} to our example"
print(full_name)
print(f"hello , {full_name.title()}")
print(f"hello , {full_name.lower()}")
print(f"hello , {full_name.upper()}")

print(message)
full_name = "{} {}   {}".format( last_name ,first_name,first_name)
print(full_name)
print("welcom to\tPython");print("***************************************")
print("Languages:\nPython\nC\nJavaScript");print("***************************************")
print("Languages:\n\tPython\n\tC\n\tJavaScript");print("***************************************")
print("***************************************")
favorite_languages = 'python & php  '
print(favorite_languages)
print(favorite_languages.rstrip())
print("***************************************")
favorite_languages = ' python & php'
print(favorite_languages)
print(favorite_languages.lstrip())
print("***************************************")
favorite_languages = '  python & php   '
print(favorite_languages)
print(favorite_languages.lstrip())
print(favorite_languages.rstrip())
print("***************************************")
print(favorite_languages)
print(favorite_languages.rstrip().lstrip())
print(favorite_languages.strip())