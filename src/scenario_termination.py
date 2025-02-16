from src.scenario_results_struct import ScenarioResultStruct, ScenarioState


class ScenarioTermination:
    def __init__(self, termination_condition: callable):
        self.termination_condition: bool = False
        self.termination_condition: callable = termination_condition
        self.result_struct: dict = {}

    def execute_termination_if_needed(self):
        self.termination_stdout_message()

    def termination_stdout_message(self):
        print("---------------------- Scenario terminated -----------------------")
        print("Scenario result struct: \n", self.result_struct)

    def assign_values_to_scenario_result_struct(
        self, state: ScenarioState, elapsed_time: float, final_score: float
    ):
        self.result_struct["scenario_state"] = state
        self.result_struct["elapsed_time"] = elapsed_time
        self.result_struct["final_score"] = final_score

    def result_struct(self):
        return ScenarioResultStruct(
            scenraio_state=ScenarioState.FAILED,
            elapsed_time=0.0,
            final_score=0.0,
        )
