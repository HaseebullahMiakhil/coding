full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # Validate character name
    if not isinstance(name, str): 
        return "The character name should be a string."
    if len(name) > 10:
        return "The character name is too long."
    if ' ' in name:
        return "The character name should not contain spaces."

    # Store stats in a dictionary
    stats = {'STR': strength, 'INT': intelligence, 'CHA': charisma}
    
    # Validate stats
    for stat in stats.values():
        if not isinstance(stat, int):
            return "All stats should be integers."
    for stat in stats.values():
        if stat < 1:
            return "All stats should be no less than 1."
    for stat in stats.values():
        if stat > 4:
            return "All stats should be no more than 4."
    if sum(stats.values()) != 7:
        return "The character should start with 7 points."

    # Construct the character representation
    character_string = name
    for key in ['STR', 'INT', 'CHA']:
        stat = stats[key]
        character_string += f'\n{key} {full_dot * stat}{empty_dot * (10 - stat)}'

    return character_string  

# Example usage
print(create_character("ren", 4, 2, 1))

# Expected string for verification
test_str = 'ren\nSTR ●●●●○○○○○○\nINT ●●○○○○○○○○\nCHA ●○○○○○○○○○'

# Print the expected string for comparison
print(f"{test_str}")