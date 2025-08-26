from crewai import Agent
from langchain_openai import ChatOpenAI
from app.core.config import settings

def create_timeline_historian_agent():
    """Create the timeline historian agent"""
    
    return Agent(
        role='History Teacher',
        goal='Create engaging historical timelines and primary source connections',
        backstory="""You are a passionate history teacher with 12 years of experience 
        in middle school education. You excel at:
        - Making historical connections relevant to modern topics
        - Creating engaging timelines that students can relate to
        - Finding primary sources that bring history to life
        - Connecting historical events to current issues
        - Making complex historical concepts accessible to young learners
        - Using storytelling to make history memorable""",
        verbose=True,
        allow_delegation=False,
        tools=[],
        llm=ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            openai_api_key=settings.OPENAI_API_KEY
        )
    )

def create_history_timeline(topic: str, grade: str) -> dict:
    """Generate historical timeline and connections for a topic"""
    
    agent = create_timeline_historian_agent()
    
    task_description = f"""
    Create a historical timeline and connections for a lesson on {topic} for grade {grade} students.
    
    Requirements:
    1. Create a timeline of 6-10 key historical events related to the topic
    2. Include events that span different time periods and regions
    3. Make connections to current events and modern relevance
    4. Provide engaging primary source prompts
    5. Include discussion questions that connect history to the lesson topic
    
    For each historical event, include:
    - Date and location
    - Brief description of what happened
    - Why it's relevant to the lesson topic
    - Connection to modern times
    - Primary source suggestion (document, image, artifact, etc.)
    
    Return the results in this format:
    {{
        "timeline": [
            {{
                "date": "Year",
                "location": "Place",
                "event": "What happened",
                "relevance": "Why it matters to the lesson",
                "modern_connection": "How it connects to today",
                "primary_source": "Suggested primary source"
            }}
        ],
        "discussion_questions": [
            "Question 1",
            "Question 2",
            "Question 3"
        ],
        "key_themes": [
            "Theme 1",
            "Theme 2",
            "Theme 3"
        ]
    }}
    """
    
    result = agent.execute(task_description)
    
    # TODO: Parse the result and return structured data
    return {
        "timeline": [
            {
                "date": "1769",
                "location": "France",
                "event": "Nicolas-Joseph Cugnot builds the first steam-powered vehicle",
                "relevance": "Shows early attempts to move away from animal power",
                "modern_connection": "Today we're still working on alternative fuel vehicles",
                "primary_source": "Engraving of Cugnot's steam carriage"
            },
            {
                "date": "1882",
                "location": "New York, USA",
                "event": "Thomas Edison opens the first commercial power plant",
                "relevance": "Beginning of widespread electricity generation",
                "modern_connection": "We still use power plants, but now have renewable options",
                "primary_source": "Photograph of Edison's Pearl Street Station"
            },
            {
                "date": "1954",
                "location": "Bell Labs, USA",
                "event": "First practical solar cell is developed",
                "relevance": "Beginning of solar energy technology",
                "modern_connection": "Solar panels are now common on homes and buildings",
                "primary_source": "Patent drawing of the first solar cell"
            },
            {
                "date": "1973",
                "location": "Global",
                "event": "OPEC oil embargo causes energy crisis",
                "relevance": "Showed the world's dependence on fossil fuels",
                "modern_connection": "We're still working to reduce fossil fuel dependence",
                "primary_source": "Newspaper headlines from 1973"
            },
            {
                "date": "2000",
                "location": "Germany",
                "event": "Renewable Energy Act passed",
                "relevance": "First major country to prioritize renewable energy",
                "modern_connection": "Many countries now have similar policies",
                "primary_source": "German government document from 2000"
            },
            {
                "date": "2015",
                "location": "Paris, France",
                "event": "Paris Climate Agreement signed",
                "relevance": "Global commitment to reduce fossil fuel use",
                "modern_connection": "Countries are still working to meet these goals",
                "primary_source": "Photo of world leaders signing the agreement"
            }
        ],
        "discussion_questions": [
            "How has our relationship with energy changed over time?",
            "What historical events led to our current energy situation?",
            "How might future historians look back on our energy choices today?"
        ],
        "key_themes": [
            "Innovation and invention",
            "Global cooperation",
            "Environmental awareness"
        ]
    }
