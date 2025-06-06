import asyncio
from pathlib import Path
import typer

from browser_use import Browser
from langchain_openai import ChatOpenAI
from patchright.async_api import async_playwright as patchright_async_playwright

from workflow_use.controller.service import WorkflowController
from workflow_use.workflow.service import Workflow

def main(workflow_path: str):
    async def _run_workflow():
        # Initialize LLMs
        llm_instance = ChatOpenAI(model='gpt-4o')
        page_extraction_llm = ChatOpenAI(model='gpt-4o-mini')

        # Start Playwright and browser
        playwright = await patchright_async_playwright().start()
        browser = Browser(playwright=playwright)
        controller_instance = WorkflowController()

        # Load workflow
        workflow_obj = Workflow.load_from_file(
            workflow_path,
            browser=browser,
            llm=llm_instance,
            controller=controller_instance,
            page_extraction_llm=page_extraction_llm,
        ) 

        # Prompt for inputs if needed 
        inputs = {}
        input_definitions = getattr(workflow_obj, "inputs_def", None)
        if input_definitions:
            for input_def in input_definitions:
                var_type = input_def.type.lower()
                is_required = input_def.required
                prompt_text = f"Enter value for '{input_def.name}' (type: {var_type}, {'required' if is_required else 'optional'}): "
                if var_type == "bool":
                    val = input(f"{prompt_text} [y/n]: ").strip().lower()
                    inputs[input_def.name] = val in ("y", "yes", "true", "1")
                elif var_type == "number":
                    val = input(prompt_text)
                    inputs[input_def.name] = float(val)
                else:
                    val = input(prompt_text)
                    inputs[input_def.name] = val

        print("\nRunning workflow...\n")
        result = await workflow_obj.run(inputs=inputs, close_browser_at_end=True)
        print("\nWorkflow execution completed!")
        print(f"Result: {len(result.step_results)} steps executed.")

    asyncio.run(_run_workflow())

if __name__ == "__main__":
    # file = "tmp/county_rec_1.json"
    file = "/Users/vikasrajpoot/Desktop/workflow-use/workflows/tmp/county_rec_1.json"
    main(file) 

