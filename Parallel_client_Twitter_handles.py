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
        description="The website of the company to assist in finding the Twitter URLs."
    )
    company_name: str = Field(
        description="The name of the company to find the Twitter URLs for."
    )
    founder_name: str = Field(
        description="The name of the founder to find their Twitter URL."
    )

class OutputModel(BaseModel):
    founder_twitter_url: str = Field(
        description="Twitter (x.com) profile URL of the founder. If the founder's Twitter URL cannot be found, return 'URL not found.' The URL should be in the format 'https://x.com/[username]'."
    )
    company_twitter_url: str = Field(
        description="Twitter (x.com) page URL of the company. If the company's Twitter URL cannot be found, return 'URL not found.' The URL should be in the format 'https://x.com/[companyhandle]'."
    )


def run_task_twitter_handles(input_data: BaseModel):
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
