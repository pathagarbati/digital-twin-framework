from src.knowledge.observation import Observation
from src.timeline.event import TimelineEvent

from src.timeline.rules.first_interaction import FirstInteractionRule
from src.timeline.rules.long_gap import LongGapRule


class TimelineExtractor:
    """
    Extracts meaningful timeline events from observations.
    """

    def __init__(self):

        self.rules = [

            FirstInteractionRule(),
            LongGapRule(),

        ]

    def extract(
        self,
        observations: list[Observation]
    ) -> list[TimelineEvent]:

        events = []

        for rule in self.rules:

            events.extend(
                rule.apply(observations)
            )

        events.sort(
            key=lambda event: event.timestamp
        )

        return events