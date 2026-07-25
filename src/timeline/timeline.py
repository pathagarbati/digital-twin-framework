from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List

from src.timeline.event import TimelineEvent


@dataclass
class Timeline:
    """
    Represents the complete chronological timeline.
    """

    events: List[TimelineEvent] = field(default_factory=list)

    by_person: Dict[str, List[TimelineEvent]] = field(default_factory=dict)
    by_type: Dict[str, List[TimelineEvent]] = field(default_factory=dict)
    by_date: Dict[date, List[TimelineEvent]] = field(default_factory=dict)

    def add_event(self, event: TimelineEvent) -> None:
        self.events.append(event)

    def sort(self) -> None:
        self.events.sort(key=lambda event: event.timestamp)

    def get_events(self) -> List[TimelineEvent]:
        return self.events

    def get_events_by_person(self, person: str) -> List[TimelineEvent]:
        return self.by_person.get(person, [])

    def get_events_by_type(self, event_type: str) -> List[TimelineEvent]:
        return self.by_type.get(event_type, [])

    def get_events_by_date(self, day: date) -> List[TimelineEvent]:
        return self.by_date.get(day, [])