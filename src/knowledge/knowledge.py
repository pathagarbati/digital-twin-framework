class KnowledgeBase:

    def __init__(self):

        self.observations = []

    # ----------------------------------
    # ADD OBSERVATIONS
    # ----------------------------------

    def add_observation(self, observation):

        self.observations.append(observation)

    def add_observations(self, observations):

        self.observations.extend(observations)

    # ----------------------------------
    # BASIC QUERIES
    # ----------------------------------

    def get_observations(self):

        return self.observations

    def total_observations(self):

        return len(self.observations)

    # ----------------------------------
    # FILTERS
    # ----------------------------------

    def get_by_sender(self, sender):

        return [

            observation

            for observation in self.observations

            if observation.source == sender

        ]

    def get_by_conversation(self, conversation_id):

        return [

            observation

            for observation in self.observations

            if observation.conversation_id == conversation_id

        ]

    def get_by_name(self, name):

        return [

            observation

            for observation in self.observations

            if observation.name == name

        ]

    def get_by_category(self, category):

        return [

            observation

            for observation in self.observations

            if observation.category == category

        ]

    def get_by_origin(self, origin):

        return [

            observation

            for observation in self.observations

            if observation.origin == origin

        ]

    def get_by_timestamp(self, timestamp):

        return [

            observation

            for observation in self.observations

            if observation.timestamp == timestamp

        ]

    # ----------------------------------
    # BOOLEAN QUERIES
    # ----------------------------------

    def get_true_observations(self, name):

        return [

            observation

            for observation in self.observations

            if observation.name == name
            and observation.value is True

        ]

    def get_false_observations(self, name):

        return [

            observation

            for observation in self.observations

            if observation.name == name
            and observation.value is False

        ]

    # ----------------------------------
    # STATISTICS
    # ----------------------------------

    def get_statistics(self):

        statistics = {

            "total_observations":
            len(self.observations),

            "metadata_observations":
            len(
                self.get_by_category(
                    "metadata"
                )
            ),

            "content_observations":
            len(
                self.get_by_category(
                    "content"
                )
            )

        }

        # Count observations
        # from each platform

        origins = set(

            observation.origin

            for observation

            in self.observations

        )

        for origin in origins:

            statistics[
                f"{origin.lower()}_observations"
            ] = len(

                self.get_by_origin(
                    origin
                )

            )

        return statistics


# --------------------------------------------------
# TESTING
# --------------------------------------------------

if __name__ == "__main__":

    from src.preprocessor.loader import load_json
    from src.preprocessor.preprocess import preprocess

    brain = KnowledgeBase()

    messages = load_json("sample.json")

    for message in messages:

        observations = preprocess(message)

        brain.add_observations(
            observations
        )

    print("\nTOTAL OBSERVATIONS")
    print(
        brain.total_observations()
    )

    print("\nGOODNIGHT = TRUE")
    print(

        brain.get_true_observations(
            "contains_goodnight"
        )

    )

    print("\nGOODNIGHT = FALSE")
    print(

        brain.get_false_observations(
            "contains_goodnight"
        )

    )

    print("\nSTATISTICS")
    print(

        brain.get_statistics()

    )