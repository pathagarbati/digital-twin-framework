from src.preprocessor.loader import load_json
from src.preprocessor.preprocess import preprocess
from src.timeline.builder import TimelineBuilder

DATASET = "sample_taashi.json"

messages = load_json(DATASET)

observations = []

for message in messages:
    observations.extend(preprocess(message))

builder = TimelineBuilder()
timeline = builder.build(observations)

print("=" * 60)
print("TIMELINE EVENTS")
print("=" * 60)

for event in timeline.events:
    print(event)

print()
print(f"Total observations : {len(observations)}")
print(f"Total events       : {len(timeline.events)}")