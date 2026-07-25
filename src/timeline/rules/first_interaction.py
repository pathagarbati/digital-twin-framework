from src.knowledge.observation import Observation
from src.timeline.event import TimelineEvent
from src.timeline.rules.base import TimelineRule


class FirstInteractionRule(TimelineRule):

    def __init__(self):
        self._counter = 0

    def apply(
        self,
        observations: list[Observation]
    ) -> list[TimelineEvent]:

        events = []
        seen_people = set()

        for observation in observations:

            person = observation.source

            if person in seen_people:
                continue

            seen_people.add(person)

            self._counter += 1

            events.append(

                TimelineEvent(

                    id=f"evt_{self._counter:06}",

                    timestamp=observation.timestamp,

                    event_type="FIRST_INTERACTION",

                    title=f"First interaction with {person}",

                    description=f"First recorded interaction involving {person}.",

                    people=[person],

                    observations=[observation]

                )

            )

        return events