from src.knowledge.observation import Observation
from src.timeline.event import TimelineEvent


class TimelineExtractor:
    """
    Extracts meaningful timeline events from observations.
    """

    def __init__(self):
        self._event_counter = 0
        self._seen_people = set()

    def extract(self, observations: list[Observation]) -> list[TimelineEvent]:

        events = []

        for observation in observations:

            person = observation.source

            # -----------------------------
            # Rule: First interaction
            # -----------------------------
            if person not in self._seen_people:

                events.append(
                    self._create_event(
                        observation,
                        "FIRST_INTERACTION",
                        f"First interaction with {person}",
                        f"First recorded interaction involving {person}."
                    )
                )

                self._seen_people.add(person)

            # Future rules go here

        return events

    def _create_event(
        self,
        observation: Observation,
        event_type: str,
        title: str,
        description: str,
    ) -> TimelineEvent:

        self._event_counter += 1

        return TimelineEvent(
            id=f"evt_{self._event_counter:06}",
            timestamp=observation.timestamp,
            event_type=event_type,
            title=title,
            description=description,
            people=[observation.source],
            observations=[observation],
        )