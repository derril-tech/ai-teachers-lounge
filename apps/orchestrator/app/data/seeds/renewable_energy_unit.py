# Created automatically by Cursor AI (2024-08-26)
"""
Seed data for "Renewable Energy (Grade 6)" unit
Contains 2 complete lessons with all components
"""

RENEWABLE_ENERGY_UNIT = {
    "unit_id": "renewable_energy_grade6",
    "title": "Renewable Energy",
    "grade_level": "6",
    "subject": "Science",
    "description": "A comprehensive unit exploring renewable energy sources and their applications",
    "lessons": [
        {
            "lesson_id": "solar_energy_lesson",
            "title": "Solar Energy: Harnessing the Power of the Sun",
            "topic": "Solar Energy",
            "gradeBand": "6",
            "periodLength": 45,
            "days": 1,
            "classSize": 25,
            "equipment": ["cardboard", "aluminum_foil", "black_paper", "thermometers", "scissors", "tape"],
            "inclusionNotes": "Include students with visual impairments by providing tactile models and audio descriptions",
            "objectives": [
                {
                    "description": "Students will understand how solar energy can be converted to heat energy",
                    "success_criteria": [
                        "Can explain the basic principle of solar energy conversion",
                        "Can identify materials that absorb solar energy effectively",
                        "Can measure and record temperature changes"
                    ]
                },
                {
                    "description": "Students will apply engineering design principles to create a solar oven",
                    "success_criteria": [
                        "Can design a simple solar oven using available materials",
                        "Can explain the purpose of each component in their design",
                        "Can test and evaluate their design's effectiveness"
                    ]
                },
                {
                    "description": "Students will collect and analyze data to draw conclusions",
                    "success_criteria": [
                        "Can record temperature data accurately",
                        "Can create a simple graph of temperature over time",
                        "Can draw conclusions about their solar oven's performance"
                    ]
                }
            ],
            "sequence": {
                "sections": [
                    {
                        "title": "Introduction to Solar Energy",
                        "description": "Students learn about solar energy and its potential as a renewable resource",
                        "duration": 10,
                        "materials": ["projector", "slides"],
                        "formative_check": "Quick poll: How many students have seen solar panels?",
                        "transition": "Move to hands-on activity"
                    },
                    {
                        "title": "Solar Oven Construction",
                        "description": "Students build simple solar ovens using cardboard, foil, and black paper",
                        "duration": 20,
                        "materials": ["cardboard", "aluminum_foil", "black_paper", "scissors", "tape"],
                        "formative_check": "Check-in: Are students following safety procedures?",
                        "transition": "Prepare for testing phase"
                    },
                    {
                        "title": "Testing and Data Collection",
                        "description": "Students test their solar ovens and record temperature data",
                        "duration": 10,
                        "materials": ["thermometers", "data_sheets"],
                        "formative_check": "Exit ticket: What was the highest temperature reached?",
                        "transition": "Clean up and reflection"
                    },
                    {
                        "title": "Reflection and Discussion",
                        "description": "Students discuss their results and connect to real-world applications",
                        "duration": 5,
                        "materials": ["reflection_sheets"],
                        "formative_check": "Class discussion: How could this technology be used in real life?",
                        "transition": "Dismissal"
                    }
                ],
                "total_minutes": 45,
                "formative_checks": [
                    "Quick poll on solar panel awareness",
                    "Safety procedure check-in",
                    "Temperature data exit ticket",
                    "Real-world application discussion"
                ]
            },
            "quiz": {
                "quiz_items": [
                    {
                        "type": "mcq",
                        "question": "Which material is best for absorbing solar energy?",
                        "options": ["White paper", "Black paper", "Clear plastic", "Aluminum foil"],
                        "correct_answer": "Black paper",
                        "explanation": "Black materials absorb more light energy and convert it to heat",
                        "points": 2,
                        "difficulty": "easy"
                    },
                    {
                        "type": "mcq",
                        "question": "What happens to the temperature inside a solar oven when exposed to sunlight?",
                        "options": ["Stays the same", "Decreases", "Increases", "Becomes unpredictable"],
                        "correct_answer": "Increases",
                        "explanation": "Solar ovens trap and concentrate sunlight, converting it to heat energy",
                        "points": 2,
                        "difficulty": "medium"
                    },
                    {
                        "type": "multi_select",
                        "question": "Select all the materials needed to build a basic solar oven:",
                        "options": ["Cardboard box", "Aluminum foil", "Black paper", "Glass", "Plastic wrap"],
                        "correct_answer": ["Cardboard box", "Aluminum foil", "Black paper"],
                        "explanation": "These three materials are essential for creating the basic structure and heat absorption",
                        "points": 3,
                        "difficulty": "medium"
                    },
                    {
                        "type": "numeric",
                        "question": "If a solar oven reaches 150°F in 30 minutes, what is the average temperature increase per minute?",
                        "correct_answer": 5,
                        "tolerance": 0.5,
                        "explanation": "150°F ÷ 30 minutes = 5°F per minute",
                        "points": 3,
                        "difficulty": "hard"
                    },
                    {
                        "type": "short_answer",
                        "question": "Explain why black paper is used in solar ovens.",
                        "correct_answer": ["absorbs", "sunlight", "heat"],
                        "explanation": "Black surfaces absorb more light energy than light surfaces",
                        "points": 4,
                        "difficulty": "medium"
                    }
                ],
                "rubrics": [
                    {
                        "question_id": 4,
                        "criteria": [
                            {
                                "level": 4,
                                "description": "Complete explanation mentioning both absorption and heat conversion"
                            },
                            {
                                "level": 3,
                                "description": "Good explanation mentioning absorption or heat conversion"
                            },
                            {
                                "level": 2,
                                "description": "Basic explanation with some relevant information"
                            },
                            {
                                "level": 1,
                                "description": "Minimal or incorrect explanation"
                            }
                        ]
                    }
                ],
                "total_points": 14
            },
            "activity": {
                "activity": {
                    "title": "Solar Oven Construction and Testing",
                    "description": "Students build and test simple solar ovens to understand solar energy conversion",
                    "learning_objectives": [
                        "Understand how solar energy can be converted to heat",
                        "Apply engineering design principles",
                        "Collect and analyze temperature data"
                    ],
                    "materials": [
                        "Cardboard boxes (1 per group)",
                        "Aluminum foil",
                        "Black construction paper",
                        "Thermometers",
                        "Scissors",
                        "Tape",
                        "Rulers"
                    ],
                    "safety_equipment": [
                        "Safety goggles (if using scissors)",
                        "Gloves (optional for handling materials)"
                    ],
                    "safety_procedures": [
                        "Use scissors carefully and only when seated",
                        "Do not look directly at the sun",
                        "Handle thermometers gently",
                        "Wash hands after handling materials",
                        "Stay in designated work areas"
                    ],
                    "steps": [
                        {
                            "step": 1,
                            "description": "Students form groups of 3-4 and gather materials",
                            "time": 3,
                            "roles": ["Materials manager", "Recorder", "Builder", "Tester"]
                        },
                        {
                            "step": 2,
                            "description": "Line the inside of the box with aluminum foil",
                            "time": 5,
                            "roles": ["Builder", "Materials manager"]
                        },
                        {
                            "step": 3,
                            "description": "Place black paper at the bottom of the box",
                            "time": 2,
                            "roles": ["Builder"]
                        },
                        {
                            "step": 4,
                            "description": "Take initial temperature reading and place in sunlight",
                            "time": 3,
                            "roles": ["Tester", "Recorder"]
                        },
                        {
                            "step": 5,
                            "description": "Monitor temperature every 5 minutes for 20 minutes",
                            "time": 20,
                            "roles": ["Tester", "Recorder"]
                        },
                        {
                            "step": 6,
                            "description": "Record final temperature and clean up",
                            "time": 5,
                            "roles": ["All students"]
                        }
                    ],
                    "cleanup": [
                        "Disassemble solar ovens",
                        "Return materials to designated areas",
                        "Wipe down work surfaces",
                        "Wash hands thoroughly"
                    ],
                    "disposal": [
                        "Recycle cardboard boxes",
                        "Reuse aluminum foil if clean",
                        "Dispose of used black paper in regular trash"
                    ],
                    "differentiation": {
                        "support": "Provide pre-cut materials and simplified instructions for struggling students",
                        "extension": "Challenge advanced students to design more efficient ovens or test different materials",
                        "accommodations": "Provide larger materials for students with fine motor difficulties, assign partner for students who need support"
                    }
                }
            },
            "history": {
                "timeline": [
                    {
                        "date": "1839",
                        "location": "France",
                        "event": "Edmond Becquerel discovers the photovoltaic effect",
                        "relevance": "First scientific understanding of how light can generate electricity",
                        "modern_connection": "This discovery led to the development of solar panels",
                        "primary_source": "Becquerel's laboratory notes and publications"
                    },
                    {
                        "date": "1954",
                        "location": "United States",
                        "event": "Bell Labs creates the first practical solar cell",
                        "relevance": "First working solar cell that could power electrical devices",
                        "modern_connection": "Modern solar panels use the same basic technology",
                        "primary_source": "Bell Labs research papers and patents"
                    },
                    {
                        "date": "1977",
                        "location": "United States",
                        "event": "President Carter installs solar panels on the White House",
                        "relevance": "First major government adoption of solar energy",
                        "modern_connection": "Government buildings now commonly use solar power",
                        "primary_source": "White House photographs and official records"
                    }
                ],
                "discussion_questions": [
                    "How has our understanding of solar energy changed over time?",
                    "What role did government play in the development of solar technology?",
                    "How might solar energy use change in the next 50 years?"
                ],
                "key_themes": [
                    "Scientific discovery and innovation",
                    "Government support for renewable energy",
                    "Technological advancement over time"
                ]
            },
            "math": {
                "dataset": {
                    "title": "Solar Energy Production by State",
                    "description": "Data on solar energy production across different US states",
                    "data": [
                        {"state": "California", "production": 28500, "unit": "MW", "percentage": 34.2},
                        {"state": "Texas", "production": 12500, "unit": "MW", "percentage": 15.0},
                        {"state": "Florida", "production": 8500, "unit": "MW", "percentage": 10.2},
                        {"state": "North Carolina", "production": 7200, "unit": "MW", "percentage": 8.6},
                        {"state": "Arizona", "production": 6500, "unit": "MW", "percentage": 7.8}
                    ]
                },
                "core_problems": [
                    {
                        "problem": "If California produces 28,500 MW of solar energy and this represents 34.2% of the total US solar production, what is the total US solar energy production?",
                        "concepts": ["percentages", "proportions", "division"],
                        "solution": "28,500 ÷ 0.342 = 83,333 MW",
                        "answer": "83,333 MW"
                    },
                    {
                        "problem": "If a solar panel produces 300 watts and costs $200, what is the cost per watt?",
                        "concepts": ["unit rates", "division"],
                        "solution": "$200 ÷ 300 watts = $0.67 per watt",
                        "answer": "$0.67 per watt"
                    }
                ],
                "challenge_problems": [
                    {
                        "problem": "A solar farm has 1,000 panels, each producing 400 watts. If the farm operates at 75% capacity factor (meaning it produces 75% of its maximum output on average), how much energy does it produce in a day?",
                        "concepts": ["multiplication", "percentages", "unit conversion"],
                        "solution": "1,000 × 400 × 0.75 × 24 = 7,200,000 watt-hours = 7,200 kWh",
                        "answer": "7,200 kWh per day"
                    }
                ]
            },
            "udl": {
                "udl_flags": [
                    {
                        "type": "representation",
                        "severity": "medium",
                        "description": "Solar oven construction relies heavily on visual instructions",
                        "suggestion": "Add tactile models and audio descriptions for each step",
                        "principle": "representation"
                    },
                    {
                        "type": "action_expression",
                        "severity": "low",
                        "description": "Limited options for students to demonstrate understanding",
                        "suggestion": "Offer choice of written report, oral presentation, or visual diagram",
                        "principle": "expression"
                    },
                    {
                        "type": "engagement",
                        "severity": "low",
                        "description": "Activity may not engage students with different interests",
                        "suggestion": "Connect to students' personal experiences with energy use",
                        "principle": "engagement"
                    }
                ],
                "reading_level": {
                    "current_level": "Grade 6-7",
                    "recommendations": [
                        "Simplify technical terms like 'capacity factor'",
                        "Add more visual aids and diagrams",
                        "Break complex sentences into shorter ones"
                    ]
                },
                "vocabulary": [
                    {
                        "complex_word": "capacity factor",
                        "simpler_alternative": "how much of the time it works",
                        "context": "wind turbine problem"
                    },
                    {
                        "complex_word": "kilowatt-hours",
                        "simpler_alternative": "units of electricity",
                        "context": "energy calculations"
                    }
                ],
                "scaffolds": [
                    "Provide sentence starters for written responses",
                    "Use graphic organizers for data analysis",
                    "Offer peer support during group activities",
                    "Provide step-by-step checklists for complex tasks"
                ],
                "overall_score": "85% UDL compliant"
            },
            "exports": {
                "files": {
                    "pack_pdf": "Complete lesson pack with all components",
                    "slides_mdx": "Presentation slides in MDX format",
                    "worksheets_docx": "Student worksheets and activities",
                    "quiz_pdf": "Assessment with answer key",
                    "csv_grades": "Gradebook template",
                    "bundle_zip": "Complete lesson bundle"
                },
                "metadata": {
                    "lesson_id": "solar_energy_lesson",
                    "topic": "Solar Energy",
                    "generated_at": "2024-08-26T03:15:00Z",
                    "version": "1.0",
                    "file_count": 6,
                    "total_size_estimate": 2048576,
                    "expires_at": "2024-09-25T03:15:00Z"
                },
                "status": "completed"
            }
        },
        {
            "lesson_id": "wind_energy_lesson",
            "title": "Wind Energy: Capturing the Power of Moving Air",
            "topic": "Wind Energy",
            "gradeBand": "6",
            "periodLength": 45,
            "days": 1,
            "classSize": 25,
            "equipment": ["paper", "cardboard", "straws", "pins", "fans", "anemometers"],
            "inclusionNotes": "Include students with hearing impairments by providing visual cues and written instructions",
            "objectives": [
                {
                    "description": "Students will understand how wind energy can be converted to mechanical energy",
                    "success_criteria": [
                        "Can explain how wind turbines work",
                        "Can identify factors that affect wind energy production",
                        "Can design a simple wind turbine model"
                    ]
                },
                {
                    "description": "Students will investigate the relationship between wind speed and energy production",
                    "success_criteria": [
                        "Can measure wind speed using an anemometer",
                        "Can record data accurately",
                        "Can identify patterns in their data"
                    ]
                },
                {
                    "description": "Students will evaluate the advantages and disadvantages of wind energy",
                    "success_criteria": [
                        "Can list at least 3 advantages of wind energy",
                        "Can list at least 2 disadvantages of wind energy",
                        "Can compare wind energy to other energy sources"
                    ]
                }
            ],
            "sequence": {
                "sections": [
                    {
                        "title": "Introduction to Wind Energy",
                        "description": "Students learn about wind energy and how wind turbines work",
                        "duration": 10,
                        "materials": ["projector", "slides", "wind_turbine_model"],
                        "formative_check": "Think-pair-share: What do you know about wind turbines?",
                        "transition": "Move to hands-on investigation"
                    },
                    {
                        "title": "Wind Speed Investigation",
                        "description": "Students measure wind speed in different locations and conditions",
                        "duration": 15,
                        "materials": ["anemometers", "data_sheets", "fans"],
                        "formative_check": "Check-in: What factors affect wind speed?",
                        "transition": "Design and build wind turbine models"
                    },
                    {
                        "title": "Wind Turbine Model Construction",
                        "description": "Students design and build simple wind turbine models",
                        "duration": 15,
                        "materials": ["paper", "cardboard", "straws", "pins"],
                        "formative_check": "Gallery walk: Which designs look most effective?",
                        "transition": "Test and evaluate models"
                    },
                    {
                        "title": "Testing and Evaluation",
                        "description": "Students test their wind turbine models and discuss results",
                        "duration": 5,
                        "materials": ["fans", "evaluation_sheets"],
                        "formative_check": "Exit ticket: What was the most effective design feature?",
                        "transition": "Dismissal"
                    }
                ],
                "total_minutes": 45,
                "formative_checks": [
                    "Think-pair-share on wind turbines",
                    "Wind speed factor discussion",
                    "Design gallery walk",
                    "Effectiveness exit ticket"
                ]
            },
            "quiz": {
                "quiz_items": [
                    {
                        "type": "mcq",
                        "question": "What type of energy does a wind turbine convert wind energy into?",
                        "options": ["Chemical energy", "Mechanical energy", "Nuclear energy", "Thermal energy"],
                        "correct_answer": "Mechanical energy",
                        "explanation": "Wind turbines convert wind energy into mechanical energy, which is then converted to electrical energy",
                        "points": 2,
                        "difficulty": "easy"
                    },
                    {
                        "type": "mcq",
                        "question": "Which of the following factors most affects wind energy production?",
                        "options": ["Wind speed", "Air temperature", "Humidity", "Air pressure"],
                        "correct_answer": "Wind speed",
                        "explanation": "Wind speed is the primary factor affecting energy production in wind turbines",
                        "points": 2,
                        "difficulty": "medium"
                    },
                    {
                        "type": "multi_select",
                        "question": "Select all the advantages of wind energy:",
                        "options": ["Renewable", "No air pollution", "Low operating costs", "Requires no fuel", "Works at night"],
                        "correct_answer": ["Renewable", "No air pollution", "Low operating costs", "Requires no fuel"],
                        "explanation": "Wind energy is renewable, produces no air pollution, has low operating costs, and requires no fuel",
                        "points": 3,
                        "difficulty": "medium"
                    },
                    {
                        "type": "numeric",
                        "question": "If a wind turbine produces 2,000 kWh in 8 hours, what is its average power output in kW?",
                        "correct_answer": 250,
                        "tolerance": 1,
                        "explanation": "2,000 kWh ÷ 8 hours = 250 kW",
                        "points": 3,
                        "difficulty": "hard"
                    },
                    {
                        "type": "short_answer",
                        "question": "Explain why wind turbines are often placed on hills or near coastlines.",
                        "correct_answer": ["wind", "speed", "higher", "elevation"],
                        "explanation": "Wind speed is typically higher at higher elevations and near coastlines",
                        "points": 4,
                        "difficulty": "medium"
                    }
                ],
                "rubrics": [
                    {
                        "question_id": 4,
                        "criteria": [
                            {
                                "level": 4,
                                "description": "Complete explanation mentioning both elevation and wind speed relationship"
                            },
                            {
                                "level": 3,
                                "description": "Good explanation mentioning elevation or wind speed"
                            },
                            {
                                "level": 2,
                                "description": "Basic explanation with some relevant information"
                            },
                            {
                                "level": 1,
                                "description": "Minimal or incorrect explanation"
                            }
                        ]
                    }
                ],
                "total_points": 14
            },
            "activity": {
                "activity": {
                    "title": "Wind Turbine Design Challenge",
                    "description": "Students design and test simple wind turbine models to understand wind energy conversion",
                    "learning_objectives": [
                        "Understand how wind energy is converted to mechanical energy",
                        "Apply engineering design principles",
                        "Investigate factors affecting wind energy production"
                    ],
                    "materials": [
                        "Paper (various sizes)",
                        "Cardboard",
                        "Plastic straws",
                        "Straight pins",
                        "Small electric fans",
                        "Anemometers",
                        "Scissors",
                        "Tape"
                    ],
                    "safety_equipment": [
                        "Safety goggles (if using scissors)",
                        "Gloves (optional)"
                    ],
                    "safety_procedures": [
                        "Use scissors carefully and only when seated",
                        "Keep fingers away from moving parts",
                        "Do not touch fan blades while running",
                        "Handle pins carefully",
                        "Stay in designated work areas"
                    ],
                    "steps": [
                        {
                            "step": 1,
                            "description": "Students form groups and gather materials",
                            "time": 3,
                            "roles": ["Materials manager", "Designer", "Builder", "Tester"]
                        },
                        {
                            "step": 2,
                            "description": "Measure wind speed in different locations",
                            "time": 5,
                            "roles": ["Tester", "Recorder"]
                        },
                        {
                            "step": 3,
                            "description": "Design wind turbine blades on paper",
                            "time": 5,
                            "roles": ["Designer", "Builder"]
                        },
                        {
                            "step": 4,
                            "description": "Construct wind turbine model",
                            "time": 10,
                            "roles": ["Builder", "Materials manager"]
                        },
                        {
                            "step": 5,
                            "description": "Test wind turbine with fan",
                            "time": 7,
                            "roles": ["Tester", "Recorder"]
                        },
                        {
                            "step": 6,
                            "description": "Record observations and clean up",
                            "time": 5,
                            "roles": ["All students"]
                        }
                    ],
                    "cleanup": [
                        "Disassemble wind turbine models",
                        "Return materials to designated areas",
                        "Wipe down work surfaces",
                        "Wash hands thoroughly"
                    ],
                    "disposal": [
                        "Recycle paper and cardboard",
                        "Reuse straws and pins if possible",
                        "Dispose of damaged materials in regular trash"
                    ],
                    "differentiation": {
                        "support": "Provide pre-cut materials and templates for struggling students",
                        "extension": "Challenge advanced students to design more efficient turbines or test different blade shapes",
                        "accommodations": "Provide larger materials for students with fine motor difficulties, assign partner for students who need support"
                    }
                }
            },
            "history": {
                "timeline": [
                    {
                        "date": "1887",
                        "location": "Scotland",
                        "event": "First wind turbine to generate electricity",
                        "relevance": "First practical use of wind energy for electricity generation",
                        "modern_connection": "Modern wind turbines use the same basic principle",
                        "primary_source": "James Blyth's patent and laboratory notes"
                    },
                    {
                        "date": "1941",
                        "location": "United States",
                        "event": "First megawatt-scale wind turbine",
                        "relevance": "First large-scale wind energy project",
                        "modern_connection": "Today's wind turbines can generate 10+ megawatts",
                        "primary_source": "Smith-Putnam wind turbine documentation"
                    },
                    {
                        "date": "1980",
                        "location": "United States",
                        "event": "First wind farm in California",
                        "relevance": "First commercial wind farm in the US",
                        "modern_connection": "Wind farms are now common across the country",
                        "primary_source": "Altamont Pass wind farm records"
                    }
                ],
                "discussion_questions": [
                    "How has wind turbine technology changed over time?",
                    "What role did government policies play in wind energy development?",
                    "How might wind energy technology evolve in the future?"
                ],
                "key_themes": [
                    "Technological innovation",
                    "Government support for renewable energy",
                    "Scale and efficiency improvements"
                ]
            },
            "math": {
                "dataset": {
                    "title": "Wind Energy Production by State",
                    "description": "Data on wind energy production across different US states",
                    "data": [
                        {"state": "Texas", "production": 40000, "unit": "MW", "percentage": 25.8},
                        {"state": "Iowa", "production": 12000, "unit": "MW", "percentage": 7.7},
                        {"state": "Oklahoma", "production": 10000, "unit": "MW", "percentage": 6.5},
                        {"state": "Kansas", "production": 7500, "unit": "MW", "percentage": 4.8},
                        {"state": "Illinois", "production": 6500, "unit": "MW", "percentage": 4.2}
                    ]
                },
                "core_problems": [
                    {
                        "problem": "If Texas produces 40,000 MW of wind energy and this represents 25.8% of the total US wind production, what is the total US wind energy production?",
                        "concepts": ["percentages", "proportions", "division"],
                        "solution": "40,000 ÷ 0.258 = 155,039 MW",
                        "answer": "155,039 MW"
                    },
                    {
                        "problem": "If a wind turbine produces 2 MW and operates at 35% capacity factor, how much energy does it produce in a year?",
                        "concepts": ["multiplication", "percentages", "unit conversion"],
                        "solution": "2 × 0.35 × 8760 = 6,132 MWh",
                        "answer": "6,132 MWh per year"
                    }
                ],
                "challenge_problems": [
                    {
                        "problem": "A wind farm has 50 turbines, each producing 3 MW. If the farm operates at 40% capacity factor and electricity sells for $50 per MWh, what is the annual revenue?",
                        "concepts": ["multiplication", "percentages", "unit conversion", "money calculations"],
                        "solution": "50 × 3 × 0.4 × 8760 × $50 = $26,280,000",
                        "answer": "$26,280,000 per year"
                    }
                ]
            },
            "udl": {
                "udl_flags": [
                    {
                        "type": "representation",
                        "severity": "low",
                        "description": "Wind turbine models provide good visual and tactile learning",
                        "suggestion": "Add audio descriptions for students with visual impairments",
                        "principle": "representation"
                    },
                    {
                        "type": "action_expression",
                        "severity": "low",
                        "description": "Students can demonstrate learning through multiple means",
                        "suggestion": "Offer choice of written report, oral presentation, or model demonstration",
                        "principle": "expression"
                    },
                    {
                        "type": "engagement",
                        "severity": "low",
                        "description": "Hands-on activity engages most students",
                        "suggestion": "Connect to local wind energy projects or student interests",
                        "principle": "engagement"
                    }
                ],
                "reading_level": {
                    "current_level": "Grade 6",
                    "recommendations": [
                        "Use clear, simple language",
                        "Add diagrams for complex concepts",
                        "Provide vocabulary support"
                    ]
                },
                "vocabulary": [
                    {
                        "complex_word": "anemometer",
                        "simpler_alternative": "wind speed meter",
                        "context": "measuring wind speed"
                    },
                    {
                        "complex_word": "capacity factor",
                        "simpler_alternative": "how much of the time it works",
                        "context": "wind turbine efficiency"
                    }
                ],
                "scaffolds": [
                    "Provide step-by-step instructions with pictures",
                    "Use graphic organizers for data collection",
                    "Offer peer support during group work",
                    "Provide templates for wind turbine designs"
                ],
                "overall_score": "90% UDL compliant"
            },
            "exports": {
                "files": {
                    "pack_pdf": "Complete lesson pack with all components",
                    "slides_mdx": "Presentation slides in MDX format",
                    "worksheets_docx": "Student worksheets and activities",
                    "quiz_pdf": "Assessment with answer key",
                    "csv_grades": "Gradebook template",
                    "bundle_zip": "Complete lesson bundle"
                },
                "metadata": {
                    "lesson_id": "wind_energy_lesson",
                    "topic": "Wind Energy",
                    "generated_at": "2024-08-26T03:20:00Z",
                    "version": "1.0",
                    "file_count": 6,
                    "total_size_estimate": 2150400,
                    "expires_at": "2024-09-25T03:20:00Z"
                },
                "status": "completed"
            }
        }
    ]
}
