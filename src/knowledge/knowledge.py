class KnowledgeBase:

    def __init__(self):

        self.observations = []


    def add_observation(self, observation):

        self.observations.append(observation)


    def add_observations(self, observations):

        self.observations.extend(observations)


    def get_observations(self):

        return self.observations


    def total_observations(self):

        return len(self.observations)