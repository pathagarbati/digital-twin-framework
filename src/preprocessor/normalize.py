from dataclasses import dataclass


@dataclass
class Message:

    sender: str
    receiver: str
    content: object
    message_type: str
    timestamp: str
    platform: str
    conversation_id: str


if __name__ == "__main__":

    message = Message(

        sender="Parth",
        receiver="Taashi",
        content="hehe goodnight idiot",
        message_type="text",
        timestamp="2026-07-26",
        platform="Instagram",
        conversation_id="taashi"

    )

    print(message)