RELATIONSHIPS = {

    "Taashi": {

        "relationship": "Romantic Interest",
        "importance": 98,
        "comfort": 96,
        "communication": "Very Expressive"

    },

    "EX": {

        "relationship": "Ex",
        "importance": 95,
        "comfort": 85,
        "communication": "Very Expressive"

    }

}


def who_is(person):

    if person not in RELATIONSHIPS:
        return "Unknown Person."

    return RELATIONSHIPS[person]


if __name__ == "__main__":

    print(who_is("Taashi"))