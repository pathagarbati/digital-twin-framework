class KnowledgeBase:

    def __init__(self):

        self.observations = []

    # Add one observation
    def add_observation(self, observation):

        self.observations.append(observation)

    # Add multiple observations
    def add_observations(self, observations):

        self.observations.extend(observations)

    # Get all observations
    def get_observations(self):

        return self.observations

    # Total number of observations
    def total_observations(self):

        return len(self.observations)

    # Get observations by sender
    def get_by_sender(self, sender):

        return [

            observation

            for observation in self.observations

            if observation.source == sender

        ]

    # Get observations by conversation
    def get_by_conversation(self, conversation_id):

        return [

            observation

            for observation in self.observations

            if observation.conversation_id == conversation_id

        ]


if __name__ == "__main__":

    from src.preprocessor.loader import load_json
    from src.preprocessor.preprocess import preprocess

    # Create our brain
    brain = KnowledgeBase()

    # Load the dataset
    messages = load_json("sample.json")

    # Convert every message into observations
    for message in messages:

        observations = preprocess(message)

        brain.add_observations(
            observations
        )

    # Total observations
    print("\nTOTAL OBSERVATIONS")
    print(brain.total_observations())

    # All observations made by Parth
    print("\nPARTH'S OBSERVATIONS")
    print(
        brain.get_by_sender(
            "Parth"
        )
    )

    # All observations from Taashi's conversation
    print("\nTAASHI'S OBSERVATIONS")
    print(
        brain.get_by_conversation(
            "taashi"
        )
    )