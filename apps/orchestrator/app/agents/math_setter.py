from crewai import Agent
from langchain_openai import ChatOpenAI
from app.core.config import settings

def create_math_setter_agent():
    """Create the math setter agent"""
    
    return Agent(
        role='Math Teacher',
        goal='Create engaging mathematical problem sets with real-world applications',
        backstory="""You are an experienced math teacher with 10 years of experience 
        in middle school mathematics. You excel at:
        - Creating word problems that connect to real-world scenarios
        - Developing problems at appropriate difficulty levels
        - Using data and statistics to make math relevant
        - Creating both core and challenge problems
        - Providing clear step-by-step solutions
        - Making abstract concepts concrete through examples
        - Connecting math to other subjects and current events""",
        verbose=True,
        allow_delegation=False,
        tools=[],
        llm=ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            openai_api_key=settings.OPENAI_API_KEY
        )
    )

def create_math_problems(topic: str, grade: str) -> dict:
    """Generate mathematical problem sets related to the lesson topic"""
    
    agent = create_math_setter_agent()
    
    task_description = f"""
    Create mathematical problem sets for a lesson on {topic} for grade {grade} students.
    
    Requirements:
    1. Create a dataset related to the lesson topic
    2. Develop 4-6 core problems (appropriate for most students)
    3. Create 2-3 challenge problems (for advanced students)
    4. Provide complete solutions with step-by-step explanations
    5. Include problems that use different mathematical concepts:
       - Proportional reasoning
       - Percentages and ratios
       - Basic algebra
       - Data analysis and graphs
       - Geometry (if applicable)
    
    For each problem, include:
    - Clear problem statement
    - Relevant data or context
    - Mathematical concepts being used
    - Step-by-step solution
    - Answer with units
    
    Return the results in this format:
    {{
        "dataset": {{
            "title": "Dataset Title",
            "description": "Description of the data",
            "data": [
                {{"category": "Category 1", "value": 100, "unit": "units"}},
                {{"category": "Category 2", "value": 150, "unit": "units"}}
            ]
        }},
        "core_problems": [
            {{
                "problem": "Problem statement",
                "concepts": ["concept1", "concept2"],
                "solution": "Step-by-step solution",
                "answer": "Final answer with units"
            }}
        ],
        "challenge_problems": [
            {{
                "problem": "Challenge problem statement",
                "concepts": ["concept1", "concept2"],
                "solution": "Step-by-step solution",
                "answer": "Final answer with units"
            }}
        ]
    }}
    """
    
    result = agent.execute(task_description)
    
    # TODO: Parse the result and return structured data
    return {
        "dataset": {
            "title": "Energy Production by Source (2023)",
            "description": "Data showing energy production from different sources in the United States",
            "data": [
                {"source": "Solar", "production": 164, "unit": "billion kWh", "percentage": 3.9},
                {"source": "Wind", "production": 425, "unit": "billion kWh", "percentage": 10.2},
                {"source": "Hydroelectric", "production": 240, "unit": "billion kWh", "percentage": 5.7},
                {"source": "Natural Gas", "production": 1800, "unit": "billion kWh", "percentage": 43.1},
                {"source": "Coal", "production": 675, "unit": "billion kWh", "percentage": 16.2},
                {"source": "Nuclear", "production": 775, "unit": "billion kWh", "percentage": 18.6}
            ]
        },
        "core_problems": [
            {
                "problem": "If a solar panel produces 400 watts of power and the sun shines for 6 hours, how much energy does it produce in kilowatt-hours?",
                "concepts": ["unit conversion", "multiplication"],
                "solution": "400 watts = 0.4 kilowatts\n0.4 kW × 6 hours = 2.4 kWh",
                "answer": "2.4 kilowatt-hours"
            },
            {
                "problem": "A wind turbine produces 2.5 megawatts of power. If it operates at 35% capacity factor, how much energy does it produce in one day?",
                "concepts": ["percentages", "multiplication", "time conversion"],
                "solution": "2.5 MW × 0.35 = 0.875 MW average\n0.875 MW × 24 hours = 21 MWh",
                "answer": "21 megawatt-hours"
            },
            {
                "problem": "If solar energy costs $0.12 per kWh and coal costs $0.08 per kWh, how much more expensive is solar energy as a percentage?",
                "concepts": ["percentages", "comparison"],
                "solution": "Difference = $0.12 - $0.08 = $0.04\nPercentage = ($0.04 ÷ $0.08) × 100 = 50%",
                "answer": "50% more expensive"
            }
        ],
        "challenge_problems": [
            {
                "problem": "A solar farm has 1000 panels, each producing 300W. If the farm operates at 25% capacity factor and electricity sells for $0.15/kWh, how much revenue does the farm generate in one year?",
                "concepts": ["multiplication", "percentages", "time conversion", "revenue calculation"],
                "solution": "Total power = 1000 × 300W = 300,000W = 300kW\nAverage power = 300kW × 0.25 = 75kW\nAnnual energy = 75kW × 8760 hours = 657,000 kWh\nRevenue = 657,000 kWh × $0.15 = $98,550",
                "answer": "$98,550 per year"
            },
            {
                "problem": "If renewable energy production increases by 8% each year, how many years will it take for production to double?",
                "concepts": ["exponential growth", "logarithms"],
                "solution": "Using the rule of 72: 72 ÷ 8 = 9 years\nOr using logarithms: log(2) ÷ log(1.08) ≈ 9 years",
                "answer": "9 years"
            }
        ]
    }
