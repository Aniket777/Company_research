# pip install parallel-web
from pydantic import BaseModel, Field

from parallel import Parallel
from parallel.types import TaskSpecParam
from typing import Literal

def build_task_spec_param(
    input_schema: type[BaseModel], output_schema: type[BaseModel]
) -> TaskSpecParam:
    """Build a TaskSpecParam from an input and output schema."""
    return {
        "input_schema": {
            "type": "json",
            "json_schema": input_schema.model_json_schema(),
        },
        "output_schema": {
            "type": "json",
            "json_schema": output_schema.model_json_schema(),
        },
    }


class InputModel(BaseModel):
    company_website: str = Field(
        description="The website of the company to find funding information."
    )
    company_name: str = Field(
        description="The name of the company to look up the investment round for."
    )
    founder_name: str = Field(
        description="The name of the founder to gather funding details."
    )

class OutputModel(BaseModel):
    first_investment_round: Literal["seed", "series A", "series B", "series C", "series D", "Undetermined"] = Field(
        description="The first round of investment by Nexus Venture Partners in the specified company. The round should be identified based on the order of precedence: seed over series A over series B over series C over series D. If Nexus Venture Partners has not invested in the company, return 'Not available'. If the specific round cannot be determined, return the earliest possible round based on available data."
    )


def run_task_nexus_investment(input_data: BaseModel):
    client = Parallel(api_key="fc0WB2L0EqFE-p0CBslkMZ4UlDLzjPf21lxxFQPD")

    task_spec = build_task_spec_param(InputModel, OutputModel)
    task_run = client.task_run.create(
        input=input_data.model_dump(),
        task_spec=task_spec,
        processor="base"
    )
    print(f"Run id: {task_run.run_id}")

    # Wait for the task run to complete.
    run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
    print(run_result.output)
    return run_result
