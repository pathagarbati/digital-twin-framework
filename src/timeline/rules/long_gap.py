from datetime import datetime

from src.knowledge.observation import Observation
from src.timeline.event import TimelineEvent
from src.timeline.rules.base import TimelineRule


class LongGapRule(TimelineRule):

    def __init__(self):
        self._counter = 100000

    def apply(
        self,
        observations: list[Observation]
    ) -> list[TimelineEvent]:

        events = []

        previous = None

        for observation in observations:

            if previous is None:
                previous = observation
                continue

            previous_time = datetime.fromisoformat(
                str(previous.timestamp)
            )

            current_time = datetime.fromisoformat(
                str(observation.timestamp)
            )

            gap = (current_time - previous_time).days

            if gap >= 30:

                self._counter += 1

                events.append(

                    TimelineEvent(

                        id=f"evt_{self._counter}",

                        timestamp=observation.timestamp,

                        event_type="LONG_GAP",

                        title=f"{gap}-day conversation gap",

                        description=f"No interaction for {gap} days.",

                        people=[observation.source],

                        observations=[previous, observation]

                    )

                )

            previous = observation

        return events