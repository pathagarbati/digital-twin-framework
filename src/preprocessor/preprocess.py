import re
import unicodedata

from src.knowledge.observation import Observation
from src.preprocessor.loader import load_json


def preprocess(message):

    observations = []

    content = str(message.content)
    lower_content = content.lower()

    # -------------------
    # Metadata
    # -------------------

    word_count = len(content.split())

    if word_count <= 5:
        length = "short"

    elif word_count <= 20:
        length = "medium"

    else:
        length = "long"

    # -------------------
    # Content Analysis
    # -------------------

    contains_uppercase = any(
        character.isupper()
        for character in content
    )

    contains_question = "?" in content

    contains_exclamation = "!" in content

    contains_number = any(
        character.isdigit()
        for character in content
    )

    contains_url = bool(

        re.search(
            r"https?://|www\.",
            content
        )

    )

    # laughter detection

    laughter_words = [

        "haha",
        "hehe",
        "lol",
        "lmao",
        "lmfao",
        "rofl",
        "xd"

    ]

    contains_laughter = any(

        word in lower_content

        for word in laughter_words

    )

    # emoji detection

    contains_emoji = any(

        unicodedata.category(character)
        == "So"

        for character in content

    )

    # attachment detection

    attachment_extensions = [

        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".webp",
        ".pdf",
        ".doc",
        ".docx",
        ".mp4",
        ".mp3",
        ".zip"

    ]

    contains_attachment = any(

        extension in lower_content

        for extension in attachment_extensions

    )

    # goodnight detection

    goodnight_words = [

        "goodnight",
        "good night",
        "gn",
        "gnn"

    ]

    contains_goodnight = any(

        word in lower_content

        for word in goodnight_words

    )

    # goodmorning detection

    goodmorning_words = [

        "goodmorning",
        "good morning",
        "gm",
        "gmm"

    ]

    contains_goodmorning = any(

        word in lower_content

        for word in goodmorning_words

    )

    # profanity detection

    profanity_words = [

        "fuck",
        "fucking",
        "shit",
        "bitch",
        "asshole",
        "mc",
        "bc",
        "madarchod",
        "behenchod",
        "lund",
        "chutiya",
        "bsdk"

    ]

    contains_profanity = any(

        word in lower_content

        for word in profanity_words

    )

    # -------------------
    # OBSERVATIONS
    # -------------------

    observation_data = [

        ("metadata", "sender", message.sender),
        ("metadata", "receiver", message.receiver),
        ("metadata", "word_count", word_count),
        ("metadata", "message_length", length),
        ("metadata", "content_length", len(content)),
        ("metadata", "message_type", message.message_type),
        ("metadata", "platform", message.platform),

        ("content", "contains_uppercase", contains_uppercase),
        ("content", "contains_question", contains_question),
        ("content", "contains_exclamation", contains_exclamation),
        ("content", "contains_number", contains_number),
        ("content", "contains_url", contains_url),
        ("content", "contains_laughter", contains_laughter),
        ("content", "contains_emoji", contains_emoji),
        ("content", "contains_attachment", contains_attachment),
        ("content", "contains_goodnight", contains_goodnight),
        ("content", "contains_goodmorning", contains_goodmorning),
        ("content", "contains_profanity", contains_profanity),

    ]

    for category, name, value in observation_data:

        observations.append(

            Observation(

                category=category,
                name=name,
                value=value,
                source=message.sender,
                origin=message.platform,
                conversation_id=message.conversation_id,
                timestamp=message.timestamp

            )

        )

    return observations


if __name__ == "__main__":

    messages = load_json("sample.json")

    for message in messages:

        observations = preprocess(message)

        print("\nMESSAGE")
        print(message)

        print("\nOBSERVATIONS")

        for observation in observations:

            print(observation)