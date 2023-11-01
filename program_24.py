sentence_1=input("Enter sentence 1\n").lower()
sentence_2=input("Enter sentence 2\n").lower()
most_letter_1=(len(sentence_1))
most_letter_2=(len(sentence_2))

a1=sentence_1.count("a")
e1=sentence_1.count("e")
i1=sentence_1.count("i")
o1=sentence_1.count("o")
u1=sentence_1.count("u")
a2=sentence_2.count("a")
e2=sentence_2.count("e")
i2=sentence_2.count("i")
o2=sentence_2.count("o")
u2=sentence_2.count("u")
most_vowels_2=a2+e2+i2+o2+u2
most_vowels_1=a1+e1+i1+o1+u1

print(f"The percentage of vowels in sentence 1 is: {round(100/most_letter_1*most_vowels_1,2)}")
print(f"The percentage of vowels in sentence 2 is: {round(100/most_letter_2*most_vowels_2,2)}")
print(f"Sentence 1 has {most_vowels_1} vowels.")
print(f"Sentence 2 has {most_vowels_2} vowels.")

if most_vowels_1>most_letter_2:
    print("Sentence 1 has more vowels.")
elif most_vowels_1<most_letter_2:
    print("Sentence 2 has more vowels.")
else:
    print("Sentence 1 and 2 have the same number of vowels.")