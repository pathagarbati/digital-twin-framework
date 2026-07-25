from src.preprocessor.loader import load_json
from src.preprocessor.preprocess import preprocess
from src.timeline.builder import TimelineBuilder

messages = load_json("sample.json")

# Collect observations from every message
observations = []

for message in messages:
    observations.extend(preprocess(message))

builder = TimelineBuilder()
timeline = builder.build(observations)

print("=" * 60)
print("TIMELINE")
print("=" * 60)

for event in timeline.events:
    print(f"[{event.timestamp}]")
    print(f"Type : {event.event_type}")
    print(f"Title: {event.title}")
    print(f"People: {event.people}")
    print(f"Description: {event.description}")
    print("-" * 60)

print(f"\nTotal Events: {len(timeline.events)}")