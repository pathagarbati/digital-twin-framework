import re

from src.knowledge.observation import Observation
from src.preprocessor.loader import load_json


def preprocess(message):

    observations = []

    content = str(message.content)

    # Word count
    word_count = len(content.split())

    # Message length
    if word_count <= 5:
        length = "short"

    elif word_count <= 20:
        length = "medium"

    else:
        length = "long"

    # Uppercase detection
    contains_uppercase = any(
        character.isupper()
        for character in content
    )

    # Question detection
    contains_question = "?" in content

    # Number detection
    contains_number = any(
        character.isdigit()
        for character in content
    )

    # URL detection
    contains_url = bool(

        re.search(
            r"https?://|www\.",
            content
        )

    )

    # Sender
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

    # Receiver
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

    # Word Count
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

    # Message Length
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

    # Content Length
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

    # Message Type
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

    # Platform
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

    # Contains Uppercase
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

    # Contains Question
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

    # Contains Number
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

    # Contains URL
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