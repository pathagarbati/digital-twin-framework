def parse_message(person, text):

    message={

        "person":person,
        "text":text,
        "words":len(text.split()),
        "length":len(text)

    }

    return message



if __name__=="__main__":

    sample=parse_message(

        "Taashi",
        "goodnight idiot lol"

    )

    print(sample)