import json
from datetime import datetime
from pathlib import Path

from src.preprocessor.normalize import Message

DATASET_FOLDER = Path("datasets")


def load_json(filename):
    """
    Loads either:
    1. Internal sample datasets
    2. Instagram exports
    """

    file_path = DATASET_FOLDER / filename

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            raw = json.load(file)

    except FileNotFoundError:
        print(f"{filename} was not found.")
        return []

    except json.JSONDecodeError:
        print(f"{filename} contains invalid JSON.")
        return []

    participants = []

    if isinstance(raw, dict):

        participants = [
            person["name"]
            for person in raw.get("participants", [])
        ]

        data = raw.get("messages", [])

    else:
        data = raw

    messages = []

    for item in data:

        # -------------------------------------------------
        # Instagram Export
        # -------------------------------------------------

        if "sender_name" in item:

            sender = item.get("sender_name")

            receiver = None

            for person in participants:
                if person != sender:
                    receiver = person
                    break

            timestamp_ms = item.get("timestamp_ms")

            timestamp = None

            if timestamp_ms is not None:
                timestamp = datetime.fromtimestamp(
                    timestamp_ms / 1000
                )

            message = Message(
                sender=sender,
                receiver=receiver,
                content=item.get("content", ""),
                message_type="text",
                timestamp=timestamp,
                platform="Instagram",
                conversation_id=filename
            )

        # -------------------------------------------------
        # Internal Sample Dataset
        # -------------------------------------------------

        else:

            message = Message(
                sender=item.get("sender"),
                receiver=item.get("receiver"),
                content=item.get("content"),
                message_type=item.get(
                    "message_type",
                    "text"
                ),
                timestamp=item.get("timestamp"),
                platform=item.get(
                    "platform",
                    "Internal"
                ),
                conversation_id=item.get(
                    "conversation_id",
                    filename
                )
            )

        messages.append(message)

    return messages


def print_messages(messages):

    for message in messages:
        print(message)


if __name__ == "__main__":

    messages = load_json("sample_taashi.json")

    print_messages(messages[:5])