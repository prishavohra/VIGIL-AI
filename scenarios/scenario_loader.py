from scenarios.configs import SCENARIOS

def load_scenario(filename):
    return SCENARIOS.get(filename, None)