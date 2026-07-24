import json

from pathlib import Path

from src.preprocessor.normalize import Message


DATASET_FOLDER = Path("datasets")


def load_json(filename):

    """
    Loads a JSON dataset and converts
    every message into Message objects.
    """

    file_path = DATASET_FOLDER / filename

    try:

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:

        print(f"{filename} was not found.")
        return []

    except json.JSONDecodeError:

        print(f"{filename} contains invalid JSON.")
        return []

    # Supports both:
    # [ {...}, {...} ]
    # and
    # { "messages":[ {...}, {...} ] }

    if isinstance(data, dict):
        data = data.get("messages", [])

    messages = []

    for item in data:

        message = Message(

            sender=item.get("sender", None),

            receiver=item.get("receiver", None),

            content=item.get("content", None),

            message_type=item.get(
                "message_type",
                "text"
            ),

            timestamp=item.get(
                "timestamp",
                None
            ),

            platform=item.get(
                "platform",
                None
            ),

            conversation_id=item.get(
                "conversation_id",
                None
            )

        )

        messages.append(message)

    return messages


def print_messages(messages):

    for message in messages:
        print(message)


if __name__ == "__main__":

    messages = load_json("sample.json")

    print_messages(messages)