from dataclasses import dataclass


@dataclass
class Observation:

    category: str
    name: str
    value: object
    source: str
    conversation_id: str
    timestamp: str