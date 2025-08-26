# Created automatically by Cursor AI (2024-08-26)
"""
Sample item templates for AI Teacher's Lounge
Contains 10 templates per question type for the quiz builder
"""

MULTIPLE_CHOICE_TEMPLATES = [
    {
        "template_id": "mcq_energy_source_identification",
        "question_stem": "Which of the following is a {energy_type} energy source?",
        "options_pattern": [
            "Correct renewable source",
            "Fossil fuel option",
            "Nuclear option",
            "Another fossil fuel option"
        ],
        "difficulty_levels": ["easy", "medium", "hard"],
        "concepts": ["energy sources", "renewable vs non-renewable"],
        "example": {
            "question": "Which of the following is a renewable energy source?",
            "options": ["Solar power", "Coal", "Natural gas", "Oil"],
            "correct_answer": "Solar power",
            "explanation": "Solar power is renewable because the sun's energy is unlimited and naturally replenished."
        }
    },
    {
        "template_id": "mcq_energy_conversion",
        "question_stem": "What type of energy does a {device} convert {input_energy} into?",
        "options_pattern": [
            "Correct energy type",
            "Incorrect energy type",
            "Another incorrect type",
            "Unrelated energy type"
        ],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["energy conversion", "energy types"],
        "example": {
            "question": "What type of energy does a wind turbine convert wind energy into?",
            "options": ["Mechanical energy", "Chemical energy", "Nuclear energy", "Thermal energy"],
            "correct_answer": "Mechanical energy",
            "explanation": "Wind turbines convert wind energy into mechanical energy, which is then converted to electrical energy."
        }
    },
    {
        "template_id": "mcq_efficiency_calculation",
        "question_stem": "If a {device} has an efficiency of {efficiency}%, how much {output} does it produce from {input}?",
        "options_pattern": [
            "Correct calculation",
            "Calculation with wrong percentage",
            "Calculation with wrong operation",
            "Unrelated calculation"
        ],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["efficiency", "percentages", "calculations"],
        "example": {
            "question": "If a solar panel has an efficiency of 20%, how much electrical energy does it produce from 1000 watts of sunlight?",
            "options": ["200 watts", "20 watts", "100 watts", "1200 watts"],
            "correct_answer": "200 watts",
            "explanation": "Efficiency = (output/input) × 100%, so output = (20/100) × 1000 = 200 watts."
        }
    },
    {
        "template_id": "mcq_environmental_impact",
        "question_stem": "Which energy source has the {impact_type} environmental impact?",
        "options_pattern": [
            "Correct answer based on impact",
            "Energy source with moderate impact",
            "Energy source with high impact",
            "Energy source with mixed impact"
        ],
        "difficulty_levels": ["easy", "medium"],
        "concepts": ["environmental impact", "energy sources"],
        "example": {
            "question": "Which energy source has the lowest environmental impact?",
            "options": ["Solar power", "Coal", "Natural gas", "Nuclear"],
            "correct_answer": "Solar power",
            "explanation": "Solar power produces no air pollution or greenhouse gases during operation."
        }
    },
    {
        "template_id": "mcq_cost_comparison",
        "question_stem": "Which energy source typically has the {cost_type} cost per kilowatt-hour?",
        "options_pattern": [
            "Correct cost ranking",
            "Energy source with moderate cost",
            "Energy source with high cost",
            "Energy source with variable cost"
        ],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["cost analysis", "energy economics"],
        "example": {
            "question": "Which energy source typically has the lowest cost per kilowatt-hour?",
            "options": ["Wind power", "Nuclear power", "Solar power", "Coal"],
            "correct_answer": "Wind power",
            "explanation": "Wind power currently has the lowest levelized cost of electricity among major energy sources."
        }
    },
    {
        "template_id": "mcq_geographic_factors",
        "question_stem": "Which factor most affects the {energy_type} potential in a specific location?",
        "options_pattern": [
            "Primary geographic factor",
            "Secondary factor",
            "Unrelated factor",
            "Economic factor"
        ],
        "difficulty_levels": ["easy", "medium"],
        "concepts": ["geographic factors", "energy potential"],
        "example": {
            "question": "Which factor most affects the solar energy potential in a specific location?",
            "options": ["Sunlight hours", "Population density", "Local regulations", "Transportation access"],
            "correct_answer": "Sunlight hours",
            "explanation": "The amount of sunlight a location receives directly determines its solar energy potential."
        }
    },
    {
        "template_id": "mcq_technology_development",
        "question_stem": "When was the {technology} first developed for practical use?",
        "options_pattern": [
            "Correct historical date",
            "Date too early",
            "Date too late",
            "Unrelated historical period"
        ],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["history of technology", "energy development"],
        "example": {
            "question": "When was the first practical solar cell developed?",
            "options": ["1954", "1900", "1970", "1980"],
            "correct_answer": "1954",
            "explanation": "Bell Labs created the first practical silicon solar cell in 1954."
        }
    },
    {
        "template_id": "mcq_safety_considerations",
        "question_stem": "What is the primary safety concern when working with {energy_source}?",
        "options_pattern": [
            "Main safety hazard",
            "Secondary safety concern",
            "Minor consideration",
            "Unrelated safety issue"
        ],
        "difficulty_levels": ["easy", "medium"],
        "concepts": ["safety", "energy hazards"],
        "example": {
            "question": "What is the primary safety concern when working with solar panels?",
            "options": ["Electrical shock", "Falling from height", "Chemical exposure", "Radiation exposure"],
            "correct_answer": "Electrical shock",
            "explanation": "Solar panels produce electricity and can cause electrical shock if not handled properly."
        }
    },
    {
        "template_id": "mcq_energy_storage",
        "question_stem": "Which energy storage technology is best suited for {application}?",
        "options_pattern": [
            "Most appropriate technology",
            "Technology with some suitability",
            "Technology with limited suitability",
            "Inappropriate technology"
        ],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["energy storage", "technology selection"],
        "example": {
            "question": "Which energy storage technology is best suited for grid-scale storage?",
            "options": ["Pumped hydro", "Lithium-ion batteries", "Hydrogen storage", "Flywheels"],
            "correct_answer": "Pumped hydro",
            "explanation": "Pumped hydro provides large-scale, long-duration storage at relatively low cost."
        }
    },
    {
        "template_id": "mcq_future_trends",
        "question_stem": "Which renewable energy source is expected to grow the fastest in the next decade?",
        "options_pattern": [
            "Highest projected growth",
            "Moderate growth projection",
            "Stable growth projection",
            "Declining trend"
        ],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["future trends", "energy projections"],
        "example": {
            "question": "Which renewable energy source is expected to grow the fastest in the next decade?",
            "options": ["Solar power", "Wind power", "Geothermal", "Biomass"],
            "correct_answer": "Solar power",
            "explanation": "Solar power is expected to grow fastest due to decreasing costs and improving technology."
        }
    }
]

MULTI_SELECT_TEMPLATES = [
    {
        "template_id": "ms_renewable_sources",
        "question_stem": "Select all the renewable energy sources from the following list:",
        "options_pattern": [
            "Multiple renewable sources",
            "Some renewable, some non-renewable"
        ],
        "difficulty_levels": ["easy", "medium"],
        "concepts": ["renewable energy", "energy classification"],
        "example": {
            "question": "Select all the renewable energy sources:",
            "options": ["Solar power", "Wind power", "Coal", "Hydroelectric", "Natural gas"],
            "correct_answer": ["Solar power", "Wind power", "Hydroelectric"],
            "explanation": "Solar, wind, and hydroelectric are renewable because they use naturally replenished resources."
        }
    },
    {
        "template_id": "ms_energy_advantages",
        "question_stem": "Select all the advantages of {energy_source}:",
        "options_pattern": [
            "Multiple advantages",
            "Mix of advantages and disadvantages"
        ],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["energy advantages", "comparative analysis"],
        "example": {
            "question": "Select all the advantages of wind energy:",
            "options": ["Renewable", "No air pollution", "Low operating costs", "Requires no fuel", "Works at night"],
            "correct_answer": ["Renewable", "No air pollution", "Low operating costs", "Requires no fuel"],
            "explanation": "Wind energy is renewable, produces no air pollution, has low operating costs, and requires no fuel."
        }
    },
    {
        "template_id": "ms_safety_equipment",
        "question_stem": "Select all the safety equipment needed for {activity}:",
        "options_pattern": [
            "Multiple safety items",
            "Mix of safety and non-safety items"
        ],
        "difficulty_levels": ["easy", "medium"],
        "concepts": ["safety", "equipment"],
        "example": {
            "question": "Select all the safety equipment needed for building a solar oven:",
            "options": ["Safety goggles", "Gloves", "Scissors", "Tape", "Thermometer"],
            "correct_answer": ["Safety goggles", "Gloves"],
            "explanation": "Safety goggles protect eyes when using scissors, and gloves protect hands when handling materials."
        }
    },
    {
        "template_id": "ms_materials_needed",
        "question_stem": "Select all the materials needed to build a {device}:",
        "options_pattern": [
            "Essential materials",
            "Mix of essential and optional materials"
        ],
        "difficulty_levels": ["easy", "medium"],
        "concepts": ["materials", "construction"],
        "example": {
            "question": "Select all the materials needed to build a basic solar oven:",
            "options": ["Cardboard box", "Aluminum foil", "Black paper", "Glass", "Plastic wrap"],
            "correct_answer": ["Cardboard box", "Aluminum foil", "Black paper"],
            "explanation": "These three materials are essential for creating the basic structure and heat absorption."
        }
    },
    {
        "template_id": "ms_environmental_benefits",
        "question_stem": "Select all the environmental benefits of using {energy_source}:",
        "options_pattern": [
            "Multiple environmental benefits",
            "Mix of benefits and impacts"
        ],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["environmental benefits", "sustainability"],
        "example": {
            "question": "Select all the environmental benefits of using solar energy:",
            "options": ["Reduces greenhouse gases", "No air pollution", "Conserves water", "Reduces land use", "Creates jobs"],
            "correct_answer": ["Reduces greenhouse gases", "No air pollution", "Conserves water"],
            "explanation": "Solar energy reduces greenhouse gas emissions, produces no air pollution, and uses minimal water."
        }
    },
    {
        "template_id": "ms_energy_conversion_steps",
        "question_stem": "Select all the steps involved in converting {input_energy} to {output_energy}:",
        "options_pattern": [
            "Multiple conversion steps",
            "Mix of relevant and irrelevant steps"
        ],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["energy conversion", "process steps"],
        "example": {
            "question": "Select all the steps involved in converting sunlight to electricity:",
            "options": ["Light absorption", "Electron excitation", "Current flow", "Heat generation", "Water evaporation"],
            "correct_answer": ["Light absorption", "Electron excitation", "Current flow"],
            "explanation": "Solar panels absorb light, excite electrons, and generate electrical current."
        }
    },
    {
        "template_id": "ms_factors_affecting_efficiency",
        "question_stem": "Select all the factors that affect the efficiency of {device}:",
        "options_pattern": [
            "Multiple efficiency factors",
            "Mix of relevant and irrelevant factors"
        ],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["efficiency", "performance factors"],
        "example": {
            "question": "Select all the factors that affect the efficiency of a wind turbine:",
            "options": ["Wind speed", "Blade design", "Tower height", "Air temperature", "Local regulations"],
            "correct_answer": ["Wind speed", "Blade design", "Tower height"],
            "explanation": "Wind speed, blade design, and tower height directly affect wind turbine efficiency."
        }
    },
    {
        "template_id": "ms_energy_storage_methods",
        "question_stem": "Select all the methods used to store {energy_type} energy:",
        "options_pattern": [
            "Multiple storage methods",
            "Mix of storage and generation methods"
        ],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["energy storage", "technology"],
        "example": {
            "question": "Select all the methods used to store electrical energy:",
            "options": ["Batteries", "Pumped hydro", "Compressed air", "Solar panels", "Wind turbines"],
            "correct_answer": ["Batteries", "Pumped hydro", "Compressed air"],
            "explanation": "Batteries, pumped hydro, and compressed air are all methods of storing electrical energy."
        }
    },
    {
        "template_id": "ms_cleanup_procedures",
        "question_stem": "Select all the cleanup procedures required after {activity}:",
        "options_pattern": [
            "Multiple cleanup steps",
            "Mix of cleanup and setup steps"
        ],
        "difficulty_levels": ["easy", "medium"],
        "concepts": ["cleanup", "safety procedures"],
        "example": {
            "question": "Select all the cleanup procedures required after building a solar oven:",
            "options": ["Disassemble oven", "Return materials", "Wipe surfaces", "Wash hands", "Gather materials"],
            "correct_answer": ["Disassemble oven", "Return materials", "Wipe surfaces", "Wash hands"],
            "explanation": "These are all important cleanup steps to maintain safety and organization."
        }
    },
    {
        "template_id": "ms_energy_units",
        "question_stem": "Select all the units used to measure {energy_quantity}:",
        "options_pattern": [
            "Multiple relevant units",
            "Mix of energy and non-energy units"
        ],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["units of measurement", "energy quantities"],
        "example": {
            "question": "Select all the units used to measure electrical power:",
            "options": ["Watts", "Kilowatts", "Megawatts", "Joules", "Meters"],
            "correct_answer": ["Watts", "Kilowatts", "Megawatts"],
            "explanation": "Watts, kilowatts, and megawatts are all units of electrical power."
        }
    }
]

NUMERIC_TEMPLATES = [
    {
        "template_id": "numeric_efficiency_calculation",
        "question_stem": "If a {device} has an efficiency of {efficiency}% and receives {input} watts, how many watts does it produce?",
        "calculation_type": "percentage",
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["efficiency", "percentages", "calculations"],
        "example": {
            "question": "If a solar panel has an efficiency of 20% and receives 1000 watts of sunlight, how many watts does it produce?",
            "correct_answer": 200,
            "tolerance": 1,
            "explanation": "Efficiency = (output/input) × 100%, so output = (20/100) × 1000 = 200 watts."
        }
    },
    {
        "template_id": "numeric_energy_calculation",
        "question_stem": "If a {device} produces {power} watts for {time} hours, how much energy does it produce in kilowatt-hours?",
        "calculation_type": "energy",
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["energy", "power", "unit conversion"],
        "example": {
            "question": "If a wind turbine produces 2000 watts for 8 hours, how much energy does it produce in kilowatt-hours?",
            "correct_answer": 16,
            "tolerance": 0.1,
            "explanation": "Energy = Power × Time = 2000 watts × 8 hours = 16,000 watt-hours = 16 kWh."
        }
    },
    {
        "template_id": "numeric_cost_calculation",
        "question_stem": "If {energy_source} costs ${cost_per_kwh} per kilowatt-hour, how much does it cost to use {kwh} kilowatt-hours?",
        "calculation_type": "cost",
        "difficulty_levels": ["easy", "medium"],
        "concepts": ["cost", "multiplication"],
        "example": {
            "question": "If solar power costs $0.10 per kilowatt-hour, how much does it cost to use 50 kilowatt-hours?",
            "correct_answer": 5.0,
            "tolerance": 0.01,
            "explanation": "Cost = Rate × Usage = $0.10 × 50 = $5.00."
        }
    },
    {
        "template_id": "numeric_capacity_factor",
        "question_stem": "If a {device} operates at {capacity_factor}% capacity factor, how many hours per year does it operate at full capacity?",
        "calculation_type": "capacity_factor",
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["capacity factor", "percentages", "time"],
        "example": {
            "question": "If a wind turbine operates at 35% capacity factor, how many hours per year does it operate at full capacity?",
            "correct_answer": 3066,
            "tolerance": 10,
            "explanation": "Hours = Capacity factor × Total hours = 0.35 × 8760 = 3066 hours."
        }
    },
    {
        "template_id": "numeric_temperature_change",
        "question_stem": "If the temperature in a solar oven increases from {initial_temp}°F to {final_temp}°F in {time} minutes, what is the average temperature increase per minute?",
        "calculation_type": "rate",
        "difficulty_levels": ["easy", "medium"],
        "concepts": ["temperature", "rate calculation", "division"],
        "example": {
            "question": "If the temperature in a solar oven increases from 70°F to 150°F in 30 minutes, what is the average temperature increase per minute?",
            "correct_answer": 2.67,
            "tolerance": 0.1,
            "explanation": "Temperature increase = (150 - 70) = 80°F. Rate = 80°F ÷ 30 minutes = 2.67°F per minute."
        }
    },
    {
        "template_id": "numeric_area_calculation",
        "question_stem": "If a solar panel has an area of {area} square meters and produces {power} watts, what is its power density in watts per square meter?",
        "calculation_type": "density",
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["power density", "area", "division"],
        "example": {
            "question": "If a solar panel has an area of 2 square meters and produces 400 watts, what is its power density in watts per square meter?",
            "correct_answer": 200,
            "tolerance": 1,
            "explanation": "Power density = Power ÷ Area = 400 watts ÷ 2 m² = 200 W/m²."
        }
    },
    {
        "template_id": "numeric_percentage_calculation",
        "question_stem": "If {energy_source} produces {production} MW and this represents {percentage}% of total production, what is the total production in MW?",
        "calculation_type": "percentage_reverse",
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["percentages", "reverse calculation", "division"],
        "example": {
            "question": "If solar power produces 28,500 MW and this represents 34.2% of total renewable production, what is the total renewable production in MW?",
            "correct_answer": 83333,
            "tolerance": 100,
            "explanation": "Total = Production ÷ Percentage = 28,500 ÷ 0.342 = 83,333 MW."
        }
    },
    {
        "template_id": "numeric_annual_energy",
        "question_stem": "If a {device} produces {power} kW and operates at {capacity_factor}% capacity factor, how much energy does it produce in a year?",
        "calculation_type": "annual_energy",
        "difficulty_levels": ["hard"],
        "concepts": ["annual energy", "capacity factor", "unit conversion"],
        "example": {
            "question": "If a wind turbine produces 2 MW and operates at 35% capacity factor, how much energy does it produce in a year?",
            "correct_answer": 6132,
            "tolerance": 50,
            "explanation": "Annual energy = Power × Capacity factor × Hours = 2 × 0.35 × 8760 = 6,132 MWh."
        }
    },
    {
        "template_id": "numeric_cost_comparison",
        "question_stem": "If {energy_source1} costs ${cost1} per kWh and {energy_source2} costs ${cost2} per kWh, how much more expensive is {energy_source2} per kWh?",
        "calculation_type": "difference",
        "difficulty_levels": ["easy", "medium"],
        "concepts": ["cost comparison", "subtraction"],
        "example": {
            "question": "If wind power costs $0.032 per kWh and nuclear power costs $0.098 per kWh, how much more expensive is nuclear power per kWh?",
            "correct_answer": 0.066,
            "tolerance": 0.001,
            "explanation": "Difference = Nuclear cost - Wind cost = $0.098 - $0.032 = $0.066 per kWh."
        }
    },
    {
        "template_id": "numeric_revenue_calculation",
        "question_stem": "If a {device} produces {energy} MWh per year and electricity sells for ${price} per MWh, what is the annual revenue?",
        "calculation_type": "revenue",
        "difficulty_levels": ["hard"],
        "concepts": ["revenue", "multiplication", "money calculations"],
        "example": {
            "question": "If a wind farm produces 6,000 MWh per year and electricity sells for $50 per MWh, what is the annual revenue?",
            "correct_answer": 300000,
            "tolerance": 1000,
            "explanation": "Revenue = Energy × Price = 6,000 MWh × $50/MWh = $300,000."
        }
    }
]

SHORT_ANSWER_TEMPLATES = [
    {
        "template_id": "sa_energy_explanation",
        "question_stem": "Explain how {energy_source} works to produce electricity.",
        "key_concepts": ["energy conversion", "process explanation"],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["energy processes", "explanation"],
        "example": {
            "question": "Explain how solar panels work to produce electricity.",
            "correct_answer": ["photovoltaic effect", "sunlight", "electrons", "electrical current"],
            "explanation": "Solar panels use the photovoltaic effect to convert sunlight into electricity by exciting electrons."
        }
    },
    {
        "template_id": "sa_efficiency_factors",
        "question_stem": "What factors affect the efficiency of {device}?",
        "key_concepts": ["efficiency factors", "performance variables"],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["efficiency", "performance factors"],
        "example": {
            "question": "What factors affect the efficiency of a wind turbine?",
            "correct_answer": ["wind speed", "blade design", "tower height", "air density"],
            "explanation": "Wind speed, blade design, tower height, and air density all affect wind turbine efficiency."
        }
    },
    {
        "template_id": "sa_environmental_impact",
        "question_stem": "What are the environmental impacts of using {energy_source}?",
        "key_concepts": ["environmental effects", "positive and negative impacts"],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["environmental impact", "sustainability"],
        "example": {
            "question": "What are the environmental impacts of using solar energy?",
            "correct_answer": ["no air pollution", "reduces greenhouse gases", "land use", "manufacturing impact"],
            "explanation": "Solar energy has no air pollution during operation but requires land and has manufacturing impacts."
        }
    },
    {
        "template_id": "sa_safety_procedures",
        "question_stem": "What safety procedures should be followed when working with {energy_source}?",
        "key_concepts": ["safety protocols", "hazard prevention"],
        "difficulty_levels": ["easy", "medium"],
        "concepts": ["safety", "procedures"],
        "example": {
            "question": "What safety procedures should be followed when working with solar panels?",
            "correct_answer": ["electrical safety", "fall protection", "proper tools", "qualified personnel"],
            "explanation": "Electrical safety, fall protection, proper tools, and qualified personnel are essential."
        }
    },
    {
        "template_id": "sa_energy_storage",
        "question_stem": "How can {energy_source} energy be stored for later use?",
        "key_concepts": ["storage methods", "energy conversion"],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["energy storage", "technology"],
        "example": {
            "question": "How can solar energy be stored for later use?",
            "correct_answer": ["batteries", "pumped hydro", "thermal storage", "hydrogen"],
            "explanation": "Solar energy can be stored in batteries, pumped hydro, thermal storage, or converted to hydrogen."
        }
    },
    {
        "template_id": "sa_cost_analysis",
        "question_stem": "What are the main costs associated with {energy_source}?",
        "key_concepts": ["cost components", "economic factors"],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["cost analysis", "economics"],
        "example": {
            "question": "What are the main costs associated with wind energy?",
            "correct_answer": ["initial investment", "maintenance", "transmission", "land lease"],
            "explanation": "Wind energy costs include initial investment, maintenance, transmission, and land lease."
        }
    },
    {
        "template_id": "sa_geographic_factors",
        "question_stem": "What geographic factors make a location suitable for {energy_source}?",
        "key_concepts": ["geographic requirements", "site selection"],
        "difficulty_levels": ["medium", "hard"],
        "concepts": ["geography", "site selection"],
        "example": {
            "question": "What geographic factors make a location suitable for wind energy?",
            "correct_answer": ["wind speed", "elevation", "terrain", "access to grid"],
            "explanation": "High wind speed, elevation, open terrain, and grid access make locations suitable for wind energy."
        }
    },
    {
        "template_id": "sa_technology_comparison",
        "question_stem": "Compare {energy_source1} and {energy_source2} in terms of efficiency and cost.",
        "key_concepts": ["comparative analysis", "multiple factors"],
        "difficulty_levels": ["hard"],
        "concepts": ["comparison", "analysis"],
        "example": {
            "question": "Compare solar and wind energy in terms of efficiency and cost.",
            "correct_answer": ["solar efficiency", "wind efficiency", "solar cost", "wind cost"],
            "explanation": "Solar has lower efficiency but decreasing costs, while wind has higher efficiency and lowest costs."
        }
    },
    {
        "template_id": "sa_future_development",
        "question_stem": "How might {energy_source} technology develop in the future?",
        "key_concepts": ["future trends", "technology advancement"],
        "difficulty_levels": ["hard"],
        "concepts": ["future trends", "technology"],
        "example": {
            "question": "How might solar energy technology develop in the future?",
            "correct_answer": ["higher efficiency", "lower costs", "new materials", "integration"],
            "explanation": "Future developments include higher efficiency, lower costs, new materials, and better integration."
        }
    },
    {
        "template_id": "sa_energy_policy",
        "question_stem": "What policies could encourage the adoption of {energy_source}?",
        "key_concepts": ["policy measures", "incentives"],
        "difficulty_levels": ["hard"],
        "concepts": ["policy", "incentives"],
        "example": {
            "question": "What policies could encourage the adoption of renewable energy?",
            "correct_answer": ["tax credits", "renewable standards", "carbon pricing", "research funding"],
            "explanation": "Policies include tax credits, renewable portfolio standards, carbon pricing, and research funding."
        }
    }
]
