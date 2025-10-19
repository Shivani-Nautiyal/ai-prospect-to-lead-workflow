import json
import importlib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class WorkflowExecutor:
    """
    LangGraph-style workflow executor that dynamically loads and runs agents
    based on workflow.json configuration
    """
    
    def __init__(self, workflow_file='workflow.json'):
        self.workflow_file = workflow_file
        self.workflow_config = None
        self.state = {}  # Stores outputs from each step
        
    def load_workflow(self):
        """Load workflow configuration from JSON file"""
        print(f"📖 Loading workflow from {self.workflow_file}...")
        with open(self.workflow_file, 'r') as f:
            self.workflow_config = json.load(f)
        print(f"✅ Loaded workflow: {self.workflow_config['workflow_name']}\n")
        
    def load_agent(self, agent_class):
        """Dynamically import and instantiate an agent"""
        module_name = f"agents.{self._class_to_module(agent_class)}"
        module = importlib.import_module(module_name)
        agent_cls = getattr(module, agent_class)
        return agent_cls()
    
    def _class_to_module(self, class_name):
        """Convert ProspectSearchAgent -> prospect_search_agent"""
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', class_name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    def resolve_inputs(self, inputs):
        """
        Resolve input variables like {{prospect_search.output}}
        with actual values from previous steps
        """
        resolved = {}
        for key, value in inputs.items():
            if isinstance(value, str) and value.startswith('{{') and value.endswith('}}'):
                # Extract reference like "prospect_search.output"
                ref = value[2:-2].strip()
                step_id, output_key = ref.split('.')
                resolved[key] = self.state[step_id][output_key]
            else:
                resolved[key] = value
        return resolved
    
    def execute(self):
        """Execute all workflow steps in sequence"""
        if not self.workflow_config:
            self.load_workflow()
        
        steps = self.workflow_config['steps']
        
        print(f"🚀 Starting workflow execution with {len(steps)} steps\n")
        print("=" * 70)
        
        for idx, step in enumerate(steps, 1):
            step_id = step['id']
            agent_class = step['agent_class']
            description = step['description']
            
            print(f"\n📍 STEP {idx}/{len(steps)}: {step_id.upper()}")
            print(f"   Agent: {agent_class}")
            print(f"   Description: {description}")
            print("-" * 70)
            
            # Load the agent
            agent = self.load_agent(agent_class)
            
            # Resolve inputs from previous steps
            inputs = self.resolve_inputs(step['inputs'])
            
            print(f"⚙️  Running {agent_class}...")
            
            # Execute agent
            output = agent.run(inputs)
            
            # Store output in state
            self.state[step_id] = {'output': output}
            
            # Display output
            print(f"✅ {agent_class} completed successfully!")
            print(f"📊 Output preview:")
            self._display_output(output)
            print("=" * 70)
        
        print(f"\n🎉 Workflow completed successfully!")
        return self.state
    
    def _display_output(self, output, max_items=3):
        """Pretty print output with truncation for large lists"""
        if isinstance(output, list):
            print(f"   → Returned {len(output)} items")
            for i, item in enumerate(output[:max_items], 1):
                print(f"   [{i}] {item}")
            if len(output) > max_items:
                print(f"   ... and {len(output) - max_items} more items")
        elif isinstance(output, dict):
            for key, value in list(output.items())[:5]:
                print(f"   → {key}: {value}")
        else:
            print(f"   → {output}")


def main():
    """Main entry point for the workflow"""
    print("\n" + "="*70)
    print("🤖 AI PROSPECT-TO-LEAD WORKFLOW SYSTEM")
    print("="*70 + "\n")
    
    executor = WorkflowExecutor('workflow.json')
    
    try:
        result = executor.execute()
        
        # Display final summary
        print("\n" + "="*70)
        print("📋 WORKFLOW SUMMARY")
        print("="*70)
        
        if 'outreach_content' in result:
            emails = result['outreach_content']['output']
            print(f"\n✉️  Generated {len(emails)} personalized outreach emails:")
            for i, email in enumerate(emails, 1):
                print(f"\n--- Email #{i} ---")
                print(f"To: {email['contact_name']} at {email['company_name']}")
                print(f"Subject: {email['subject']}")
                print(f"Preview: {email['message'][:100]}...")
        
        print("\n" + "="*70)
        print("✅ All tasks completed successfully!")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error executing workflow: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()