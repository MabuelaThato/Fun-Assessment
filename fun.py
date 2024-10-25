def dog_years():
    years = 0
    while True:
        try:
            n = int(input("Input a dog's age in human years: "))
            if n < 1:
                print("The years have to be atleast 1..")
            elif n > 20:
                print("The years have to be maximum 20 years..")
            else:
                years = n
            break
        except ValueError:
            pass
    new = 0
    count = 0
    while count < 2 and years > 0:
        years -= 1
        new += 10.5
        count += 1

    while years > 0:
        years -= 1
        new += 4
    
    print(f"The dog's age in dog's years is {round(new)}")

def fizzbuzz(num):
    string = ""
    for i in range(1,num + 1):
        if i % 3 == 0:
            word = "Fizz "
            if i % 5 == 0:
                word = "FizzBuzz "
            if i ==  num:
                string += word.strip()
            else:
                string += word
        elif i % 5 == 0:
            word = "Buzz "
            if i ==  num:
                string += word.strip()
            else:
                string += word
        else:
            number = f"{i} "
            if i ==  num:
                string += number.strip()
            else:
                string += number
    
    return string

def word_lengths(sentence):
    sentence = str(sentence)
    if sentence.isdigit():
        raise ValueError("Sentence has to be a string not numbers")
    words = sentence.split()
    dictionary = {}
    for word in words:
        if sentence.count(word) == 1:
            dictionary[word] = len(word)
    
    return dictionary


def cube_sum(number):
    nums = list(str(number))
    sum = 0
    for num in nums:
        sum += (int(num) ** 3) 

    return sum
    