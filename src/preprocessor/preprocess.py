import re
import unicodedata

from src.knowledge.observation import Observation
from src.preprocessor.loader import load_json


def preprocess(message):

    observations = []

    content = str(message.content)

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

    lower_content = content.lower()

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

    # -------------------
    # OBSERVATIONS
    # -------------------

    observations.append(

        Observation(
            category="metadata",
            name="sender",
            value=message.sender,
            source=message.sender,
            origin=message.platform,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp
        )

    )

    observations.append(

        Observation(
            category="metadata",
            name="receiver",
            value=message.receiver,
            source=message.sender,
            origin=message.platform,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp
        )

    )

    observations.append(

        Observation(
            category="metadata",
            name="word_count",
            value=word_count,
            source=message.sender,
            origin=message.platform,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp
        )

    )

    observations.append(

        Observation(
            category="metadata",
            name="message_length",
            value=length,
            source=message.sender,
            origin=message.platform,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp
        )

    )

    observations.append(

        Observation(
            category="metadata",
            name="content_length",
            value=len(content),
            source=message.sender,
            origin=message.platform,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp
        )

    )

    observations.append(

        Observation(
            category="metadata",
            name="message_type",
            value=message.message_type,
            source=message.sender,
            origin=message.platform,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp
        )

    )

    observations.append(

        Observation(
            category="metadata",
            name="platform",
            value=message.platform,
            source=message.sender,
            origin=message.platform,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp
        )

    )

    observations.append(

        Observation(
            category="content",
            name="contains_uppercase",
            value=contains_uppercase,
            source=message.sender,
            origin=message.platform,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp
        )

    )

    observations.append(

        Observation(
            category="content",
            name="contains_question",
            value=contains_question,
            source=message.sender,
            origin=message.platform,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp
        )

    )

    observations.append(

        Observation(
            category="content",
            name="contains_number",
            value=contains_number,
            source=message.sender,
            origin=message.platform,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp
        )

    )

    observations.append(

        Observation(
            category="content",
            name="contains_url",
            value=contains_url,
            source=message.sender,
            origin=message.platform,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp
        )

    )

    observations.append(

        Observation(
            category="content",
            name="contains_laughter",
            value=contains_laughter,
            source=message.sender,
            origin=message.platform,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp
        )

    )

    observations.append(

        Observation(
            category="content",
            name="contains_emoji",
            value=contains_emoji,
            source=message.sender,
            origin=message.platform,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp
        )

    )

    observations.append(

        Observation(
            category="content",
            name="contains_attachment",
            value=contains_attachment,
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