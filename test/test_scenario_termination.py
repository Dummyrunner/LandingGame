from src.scenario_termination import ScenarioTermination

some_variable = "hi"


class MockScenario:
    def __init__(self, termination_condition):
        self.termination_condition = termination_condition


mock_scenario_true = MockScenario(lambda: some_variable == "hi")
mock_scenario_false = MockScenario(lambda: some_variable == "bye")


def test_scenario_termination():
    obj_with_true_condition = ScenarioTermination(mock_scenario_true)
    obj_with_false_condition = ScenarioTermination(mock_scenario_false)

    assert obj_with_true_condition.termination_condition() == True
    assert obj_with_false_condition.termination_condition() == False
