from dataclasses import dataclass
from datetime import datetime
from typing import List

from src.knowledge.observation import Observation


@dataclass(frozen=True)
class TimelineEvent:
    """
    Represents a meaningful event in the user's timeline.

    Timeline events are generated from one or more observations and
    describe what happened at a specific point in time.
    """

    id: str
    timestamp: datetime

    event_type: str

    title: str
    description: str

    people: List[str]

    observations: List[Observation]