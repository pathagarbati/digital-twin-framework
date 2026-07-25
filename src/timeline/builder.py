from src.knowledge.observation import Observation
from src.timeline.extractor import TimelineExtractor
from src.timeline.timeline import Timeline


class TimelineBuilder:
    """
    Builds a Timeline from a collection of Observations.
    """

    def __init__(self):
        self.extractor = TimelineExtractor()

    def build(self, observations: list[Observation]) -> Timeline:

        timeline = Timeline()

        observations = sorted(
            observations,
            key=lambda observation: observation.timestamp
        )

        events = self.extractor.extract(observations)

        for event in events:

            timeline.add_event(event)

            # Person index
            for person in event.people:
                timeline.by_person.setdefault(person, []).append(event)

            # Event type index
            timeline.by_type.setdefault(event.event_type, []).append(event)

            # Date index
            day = str(event.timestamp)[:10]
            timeline.by_date.setdefault(day, []).append(event)

        timeline.sort()

        return timeline