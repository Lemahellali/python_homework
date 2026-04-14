# Write your code here.
def hello():
    return "Hello!"


def greet(name):
    return f ("Hello, Lema!")


def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b

    except ZeroDivisionError:
        return "You can't divide by 0!"

    except TypeError:
        return "You can't multiply those values!"


def data_type_conversion(value, type_name):
    try:
        if type_name == "int":
            return int(value)
        elif type_name == "float":
            return float(value)
        elif type_name == "str":
            return str(value)

    except (ValueError, TypeError):
        return f"You can't convert {value} into a {type_name}."


def grade(*args):
    try:
        avg = sum(args) / len(args)

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    except:
        return "Invalid data was provided."


def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result


def student_scores(mode, **kwargs):
    if mode == "best":
        return max(kwargs, key=kwargs.get)

    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)


def titleize(sentence):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = sentence.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        elif word in little_words:
            words[i] = word
        else:
            words[i] = word.capitalize()

    return " ".join(words)


def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result


def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")

        elif word.startswith("qu"):
            result.append(word[2:] + "quay")

        else:
            i = 0
            while i < len(word) and word[i] not in vowels:
                if word[i:i+2] == "qu":
                    i += 2
                    break
                i += 1

            result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)