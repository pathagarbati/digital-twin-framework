from src.knowledge.observation import Observation
from src.preprocessor.loader import load_json


def preprocess(message):

    observations = []

    # sender
    observations.append(

        Observation(

            category="metadata",
            name="sender",
            value=message.sender,
            source=message.sender,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp

        )

    )

    # receiver
    observations.append(

        Observation(

            category="metadata",
            name="receiver",
            value=message.receiver,
            source=message.sender,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp

        )

    )

    # word count
    observations.append(

        Observation(

            category="metadata",
            name="word_count",
            value=len(str(message.content).split()),
            source=message.sender,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp

        )

    )

    # message length (short/medium/long)
    word_count = len(str(message.content).split())

    if word_count <= 5:
        length = "short"

    elif word_count <= 20:
        length = "medium"

    else:
        length = "long"

    observations.append(

        Observation(

            category="metadata",
            name="message_length",
            value=length,
            source=message.sender,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp

        )

    )

    # content length
    observations.append(

        Observation(

            category="metadata",
            name="content_length",
            value=len(str(message.content)),
            source=message.sender,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp

        )

    )

    # message type
    observations.append(

        Observation(

            category="metadata",
            name="message_type",
            value=message.message_type,
            source=message.sender,
            conversation_id=message.conversation_id,
            timestamp=message.timestamp

        )

    )

    # platform
    observations.append(

        Observation(

            category="metadata",
            name="platform",
            value=message.platform,
            source=message.sender,
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