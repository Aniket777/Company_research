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
        description="The website of the company to search for funding announcements."
    )
    company_name: str = Field(
        description="The name of the company to analyze for its funding stage."
    )
    founder_name: str = Field(
        description="The name of the founder to cross-reference with funding information."
    )

class OutputModel(BaseModel):
    company_stage: Literal["Seed", "Series A", "Series B", "Series C", "Series D", "Series E", "Series F", "Series G", "Series H", "Series I", "Series J","Acquired", "Public Company", "Undetermined"] = Field(
        description="The funding stage of the company based on its most recent public fundraising announcements. Possible values are Seed, Series A, Series B, Series C, Series D, Series E, Series F, Series G, Series H, Series I, Series J, Acquired, Public Company, or Undetermined if the stage cannot be determined. Classification is based on the latest available data, prioritizing the most recent stage if multiple stages are found."
    )


def run_task_company_stage(input_data: BaseModel):
    client = Parallel(api_key="fc0WB2L0EqFE-p0CBslkMZ4UlDLzjPf21lxxFQPD")

    task_spec = build_task_spec_param(InputModel, OutputModel)
    task_run = client.task_run.create(
        input=input_data.model_dump(),
        task_spec=task_spec,
        processor="pro"
    )
    print(f"Run id: {task_run.run_id}")

    # Wait for the task run to complete.
    run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
    return run_result
