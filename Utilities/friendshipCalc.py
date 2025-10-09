
def friendship_score(name_a, name_b):
    name_a.lower()
    name_b.lower()
    score = 0
    shared_letters = set(name_a) & set(name_b)
    vowels = set('aeiou')

    score += len(shared_letters) * 5 
    score += len(vowels & shared_letters) * 10 
    
    return min(score, 100)

name_a = input("Name of first friend.")
name_b = input("Name of seond friend.")

print(f"Your score is {friendship_score(name_a, name_b)}")
