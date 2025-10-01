# pip install parallel-web
from pydantic import BaseModel, Field

from parallel import Parallel
from parallel.types import TaskSpecParam

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
        description="The website of the company to assist in finding company urls for different social media platforms."
    )
    company_name: str = Field(
        description="The name of the company to find company urls for different social media platforms."
    )
    founder_name: str = Field(
        description="The name of the founder to find their company urls for different social media platforms."
    )

class OutputModel(BaseModel):
    linkedin_url: str = Field(
        description="URL of the company's official LinkedIn page. If LinkedIn page is unavailable, return 'URL unavailable.'"
    )
    medium_url: str = Field(
        description="URL of the company's official Medium page. If Medium page is unavailable, return 'URL unavailable.'"
    )
    youtube_url: str = Field(
        description="URL of the company's official YouTube channel. If YouTube channel is unavailable, return 'URL unavailable.'"
    )
    substack_url: str = Field(
        description="URL of the company's official Substack page. If Substack page is unavailable, return 'URL unavailable.'"
    )


def run_task_other_handles(input_data: BaseModel):
    client = Parallel(api_key="fc0WB2L0EqFE-p0CBslkMZ4UlDLzjPf21lxxFQPD")

    task_spec = build_task_spec_param(InputModel, OutputModel)
    task_run = client.task_run.create(
        input=input_data.model_dump(),
        task_spec = task_spec,
        processor="base"
    )
    print(f"Run id: {task_run.run_id}")

    # Wait for the task run to complete.
    run_result = client.task_run.result(task_run.run_id, api_timeout=3600)
    return run_result
