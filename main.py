from workflow_use import Workflow

workflow = Workflow.load_from_file("example.workflow.json")
result = asyncio.run(workflow.run_as_tool("I want to search for 'workflow use'"))


