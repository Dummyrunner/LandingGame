from src.scenario import Scenario
from src.scenario_results_struct import ScenarioState


class ScenarioTermination:
    def __init__(self, scenario: Scenario):
        self.termination_condition: bool = False
        self.termination_condition: callable = scenario.termination_condition
        self.result_dict: dict = {}

    def execute_termination(self):
        self.termination_stdout_message()

    def termination_stdout_message(self):
        print("---------------------- Scenario terminated -----------------------")
        print("Scenario result struct: \n", self.result_dict)

    def assign_values_to_scenario_result_struct(
        self, state: ScenarioState, elapsed_time: float, final_score: float
    ):
        self.result_dict["scenario_state"] = state
        self.result_dict["elapsed_time"] = elapsed_time
        self.result_dict["final_score"] = final_score
