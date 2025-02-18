from src.scenario_termination import ScenarioTermination
from src.scenario_results_struct import ScenarioState

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


def test_scenario_termination_execute_termination(capsys):
    """Check, whether a message is printed to stdout when termination is executed"""
    obj_with_true_condition = ScenarioTermination(mock_scenario_true)
    obj_with_true_condition.execute_termination()
    captured = capsys.readouterr()
    assert captured.out.strip() != ""


def test_result_struct_assignment():
    obj = ScenarioTermination(mock_scenario_true)
    result = obj.result_dict
    assert result == {}
    obj.assign_values_to_scenario_result_struct(ScenarioState.SUCCESS, 1.2, 3.4)
    assert result["scenario_state"] == ScenarioState.SUCCESS
    assert result["elapsed_time"] == 1.2
    assert result["final_score"] == 3.4
