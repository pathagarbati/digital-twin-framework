from src.knowledge.observation import Observation
from src.preprocessor.loader import load_json


def preprocess(message):

    observations = []

    # Word count
    word_count = len(str(message.content).split())

    # Message length
    if word_count <= 5:
        length = "short"

    elif word_count <= 20:
        length = "medium"

    else:
        length = "long"

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
            value=len(str(message.content)),
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