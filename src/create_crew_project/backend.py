import sys
import warnings
from create_crew_project.crew import CreateCrewProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run(input):
    """
    Run the crew.
    """
    inputs = {
        'definicao_do_sistema': input,
    }
    
    try:
        CreateCrewProject().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
