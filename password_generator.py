import random
import string
u = random.choice(string.ascii_uppercase)
l = random.choice(string.ascii_lowercase)
d= random.choice(string.ascii_lowercase)
s= random.choice(string.punctuation)
n = int(input("Enter your desired length"))
characters = string.ascii_letters +string.digits+string.punctuation
random_s= random.choices(characters,k=(n-4))
final_list = [u,l,d,s]+ random_s
random.shuffle(final_list)
final_string = "".join(final_list)
print("Your password:",final_string)
print("EXIT")