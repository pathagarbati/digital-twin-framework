from abc import ABC, abstractmethod

from src.knowledge.observation import Observation
from src.timeline.event import TimelineEvent


class TimelineRule(ABC):
    """
    Base class for every timeline rule.
    """

    @abstractmethod
    def apply(
        self,
        observations: list[Observation]
    ) -> list[TimelineEvent]:
        pass