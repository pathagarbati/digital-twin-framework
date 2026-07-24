class KnowledgeBase:

    def __init__(self):

        self.observations = []



    def add_observation(self, observation):

        self.observations.append(observation)



    def get_observations(self):

        return self.observations



if __name__=="__main__":

    brain = KnowledgeBase()


    brain.add_observation(

        "Parth usually communicates casually."

    )


    print(brain.get_observations())