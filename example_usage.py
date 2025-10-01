#!/usr/bin/env python3
"""
Example usage of Parallel_client.py for company research.
This file demonstrates how to call the run_task function with specific input data.
"""

from Parallel_client_Twitter_handles import run_task_twitter_handles, InputModel
from Parallel_client_Other_handles import run_task_other_handles, InputModel
from Parallel_client_company_stage import run_task_company_stage, InputModel
from Paralllel_client_Nexus_investment import run_task_nexus_investment, InputModel

def main():
    """
    Example usage of the Parallel client for company research.
    """
    
    # Example 1: Research for a well-known company
    print("=== Example 1: Tesla Research ===")
    tesla_input = InputModel(
        company_website="https://www.tesla.com",
        company_name="Tesla",
        founder_name="Elon Musk"
    )
    
    print(f"Researching: {tesla_input.company_name}")
    print(f"Website: {tesla_input.company_website}")
    print(f"Founder: {tesla_input.founder_name}")
    print("\nRunning task...")
    
    try:
        run_result_twitter_handles = run_task_twitter_handles(tesla_input)
        run_result_other_handles = run_task_other_handles(tesla_input)
        run_result_company_stage = run_task_company_stage(tesla_input)
        run_result_nexus_investment = run_task_nexus_investment(tesla_input)
        output_data = run_result_twitter_handles.output.content
        output_data_other = run_result_other_handles.output.content
        output_data_company_stage = run_result_company_stage.output.content
        output_data_nexus_investment = run_result_nexus_investment.output.content
        print(f"\n📱 Founder X Profile: {output_data['founder_twitter_url']}")
        print(f"🏢 Company X Profile: {output_data['company_twitter_url']}")
        print(f"🔗 LinkedIn: {output_data_other['linkedin_url']}")
        print(f"🔗 Medium: {output_data_other['medium_url']}")
        print(f"🔗 YouTube: {output_data_other['youtube_url']}")
        print(f"🔗 Substack: {output_data_other['substack_url']}")
        print(f"💰 Company Stage: {output_data_company_stage['company_stage']}")
        print(f"💰 First Nexus Investment: {output_data_nexus_investment['first_investment_round']}")
    except Exception as e:
        print(f"Error occurred: {e}")
    
    print("\n" + "="*50 + "\n")
    


if __name__ == "__main__":
    # Run the main examples
    main()
    
    # You can also run individual research by calling run_single_research
    # Uncomment the line below to test with your own data:
    # run_single_research("https://example.com", "Example Corp", "John Doe")
