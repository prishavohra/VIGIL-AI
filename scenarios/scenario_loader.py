from scenarios.configs import SCENARIOS

def load_scenario(filename):
    name = filename.lower().strip()
    return SCENARIOS.get(name, {
        "title": "Uploaded Video",
        "risk": "UNKNOWN",
        "events": []
    })