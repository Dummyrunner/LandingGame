from src.scenario_termination import ScenarioTermination


def test_scenario_termination():
    some_variable = "hi"
    condition_true = lambda: some_variable == "hi"
    condition_false = lambda: some_variable == "bye"
    obj_with_true_condition = ScenarioTermination(condition_true)
    obj_with_false_condition = ScenarioTermination(condition_false)

    assert obj_with_true_condition.termination_condition() == True
    assert obj_with_false_condition.termination_condition() == False
