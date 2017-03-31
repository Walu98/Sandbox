"""
Walu
"""
def main(): #
    name = get_name(0)
    frequency = number_of_letters(name)


def get_name(name):
    nameIsBlank = True
    while ~nameIsBlank:
        getName = input("Enter your name:")
        if getName is "":
            pass
        else:
            print(getName[0::2])
            return getName

def number_of_letters(name):
    #print(a)
    freqs = {}
    for line in name:
        for char in line:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1

    print(freqs)
    """
    character_frequency = {i: name.count(i) for i in set(name)}
    print(character_frequency)
    """

main()