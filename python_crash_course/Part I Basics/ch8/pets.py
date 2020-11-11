def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('hamster', 'harry')
# pet_type =input('enter yor pet type please')
# pet_name =input('enter your pet name please')
# describe_pet(pet_type,pet_name)
describe_pet(pet_name='harry',animal_type='hamster')