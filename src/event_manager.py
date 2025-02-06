class EventManager:
    def __init__(self):
        self.events = {}

    def add_event(self, event_name):
        """Adds a new event if not already present."""
        if event_name not in self.events:
            self.events[event_name] = []

    def add_participant(self, event_name, participant):
        """Adds a participant to the specified event."""
        if event_name in self.events:
            self.events[event_name].append(participant)

    def display_participants(self, event_name):
        """Returns a list of participants for a given event."""
        return self.events.get(event_name, [])

    def search_participant(self, participant_name):
        """Finds a participant and returns their event and details."""
        for event_name, participants in self.events.items():
            for participant in participants:
                if participant[0] == participant_name:
                    return event_name, participant
        return None

    def mark_participation(self, participant_name, status):
        """Updates a participant's attendance status."""
        for event_name, participants in self.events.items():
            for i, participant in enumerate(participants):
                if participant[0] == participant_name:
                    participants[i] = (
                        participant[0], participant[1], participant[2], status)
                    return True
        return False

    def generate_summary(self):
        """Generates a summary of total participants in each event."""
        return {event: len(participants) for event, participants in self.events.items()}
