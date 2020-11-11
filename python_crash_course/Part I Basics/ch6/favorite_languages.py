favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned.')
# #point_value = alien_0.get('points') o/p none
# print(point_value)

# print('+'*30)

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in favorite_languages.keys():
#     print(name.title())

# for name in favorite_languages.values():
#     print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    # print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
languages = {'python', 'ruby', 'python', 'c'}
print(languages)