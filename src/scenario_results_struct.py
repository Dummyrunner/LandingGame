from dataclasses import dataclass
from enum import Enum


class ScenarioState(Enum):
    SUCCESS = "success"
    ERROR = "error"
    FAILURE = "failure"
    RUNNING = "running"
    PENDING = "pending"


@dataclass
class ScenarioResultStruct:
    scenraio_state: ScenarioState = ScenarioState.PENDING
    elapsed_time: float = 0.0
    final_score: float = 0.0
