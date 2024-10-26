import string
import datetime
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Define the conditions
conditions = [
    (lambda x: len(x) >= 5, "Password must be at least 5 characters long."),
    (lambda x: any(char.isdigit() for char in x), "Password must contain at least one digit."),
    (lambda x: any(char.isupper() for char in x), "Password must contain at least one uppercase letter."),
    (lambda x: any(char in string.punctuation for char in x), "Password must contain at least one special character."),
    (lambda x: sum(int(char) for char in x if char.isdigit()) == 25, "The sum of digits in the password must be 25."),
    (lambda x: any(month in x.lower() for month in ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]), "Password must contain the name of a month."),
    (lambda x: any(roman in x for roman in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]), "Password must contain a Roman numeral."),
    (lambda x: any(word in x.lower() for word in ["pepsi", "starbucks", "shell"]), "Password must contain one of the specified words. - 'pesi or starbucks or shell'"),
    (lambda x: any(roman in x for roman in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]) and any(roman in x for roman in ["V", "X", "L", "C", "D", "M"]) and any(roman in x for roman in ["V", "X", "L", "C", "D", "M"]) == 35, "Password must meet specific Roman numeral conditions."),
    (lambda x: any(symbol in x for symbol in ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]), "Password must contain a chemical element symbol."),
    (lambda x: any(phase in x for phase in ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"]), "Password must contain a moon phase emoji."),
    (lambda x: any(country in x.lower() for country in ["united states", "china", "japan", "germany", "india", "united kingdom", "france", "brazil", "italy", "canada", "south korea", "russia", "australia", "spain", "mexico", "indonesia", "netherlands", "saudi arabia", "turkey", "switzerland", "argentina", "sweden", "poland", "belgium", "iran", "thailand", "austria", "norway", "united arab emirates", "israel", "denmark", "egypt", "ireland", "philippines", "malaysia", "singapore", "south africa", "finland", "greece", "portugal", "new zealand", "vietnam", "czech republic", "romania", "chile", "hungary", "ukraine", "algeria", "peru", "nigeria", "north korea", "morocco", "bangladesh", "colombia", "venezuela", "kenya", "sudan", "tanzania", "myanmar", "ethiopia", "uzbekistan", "iraq", "afghanistan", "yemen", "mozambique", "ghana", "nepal", "angola", "madagascar", "cameroon", "ivory coast", "australia", "niger", "sri lanka", "burkina faso", "mali", "malawi", "zambia", "senegal", "chad", "somalia", "zimbabwe", "guinea", "rwanda", "benin", "burundi", "tunisia", "south sudan", "togo", "sierra leone", "libya", "congo", "liberia", "central african republic", "mauritania", "eritrea", "namibia", "gambia", "botswana", "gabon", "lesotho", "guinea-bissau", "mauritius", "eswatini", "djibouti", "comoros", "cape verde", "sao tome and principe", "seychelles", "maldives", "brunei", "bahamas", "belize", "barbados", "vanuatu", "samoa", "saint lucia", "kiribati", "micronesia", "grenada", "tonga", "saint vincent and the grenadines", "antigua and barbuda", "seychelles", "andorra", "marshall islands", "saint kitts and nevis", "liechtenstein", "monaco", "san marino", "tuvalu", "nauru", "palau", "vatican city"]), "Password must contain the name of a country."),
    (lambda x: datetime.datetime.now().year % 4 == 0, "Password must be entered in a leap year."),
    (lambda x: any(move in x for move in ["e4", "d4", "Nf3", "Nc3", "Bc4", "Bb5", "O-O", "O-O-O", "d3", "d4", "c3", "c4", "Nc3", "Nf3", "Nxe"]), "Password must contain a chess move.")
]

# Main game loop
def password_game(conditions):
    print("Welcome to the Password Game!")
    print("Create a password that meets the following conditions:\n")
    while True:
        password = input("Enter Password: ")
        past_rules = []
        failed_conditions = []
        for i, condition in enumerate(conditions, start=1):
            if not condition[0](password):
                failed_conditions.append(condition[1])
            else:
                past_rules.append(condition[1])
        if not failed_conditions:
            print("\nCongratulations! Password meets all conditions.")
            break
        else:
            print("\nPassword does not meet the following conditions:")

            for condition in failed_conditions:
                print(condition)
            if past_rules:
                print("\nRules you have met in previous attempts:")
                for rule in past_rules:
                    print(rule)


# Run the game
password_game(conditions)
