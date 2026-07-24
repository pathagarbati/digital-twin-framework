from src.knowledge.observation import Observation


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

            value=len(
                str(message.content).split()
            ),

            source=message.sender,

            conversation_id=message.conversation_id,

            timestamp=message.timestamp

        )

    )


    return observations
from src.preprocessor.loader import load_json


if __name__ == "__main__":

    messages = load_json("sample.json")


    for message in messages:

        observations = preprocess(message)

        print("\nMESSAGE")
        print(message)

        print("\nOBSERVATIONS")

        for observation in observations:

            print(observation)