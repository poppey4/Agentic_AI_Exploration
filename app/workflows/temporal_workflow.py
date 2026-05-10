from temporalio import workflow


@workflow.defn
class EnterpriseWorkflow:

    @workflow.run
    async def run(self):
        return "Workflow Executed Successfully"