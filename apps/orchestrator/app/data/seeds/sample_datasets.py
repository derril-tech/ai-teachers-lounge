# Created automatically by Cursor AI (2024-08-26)
"""
Sample datasets for AI Teacher's Lounge
Contains kWh costs and capacity factors for various energy sources
"""

ENERGY_COST_DATASET = {
    "title": "Energy Costs by Source (2024)",
    "description": "Average cost per kilowatt-hour for different energy sources in the United States",
    "source": "U.S. Energy Information Administration",
    "data": [
        {
            "energy_source": "Solar (Utility-scale)",
            "cost_per_kwh": 0.037,
            "unit": "dollars",
            "trend": "decreasing",
            "notes": "Costs have decreased significantly over the past decade"
        },
        {
            "energy_source": "Wind (Onshore)",
            "cost_per_kwh": 0.032,
            "unit": "dollars",
            "trend": "decreasing",
            "notes": "Most cost-effective renewable energy source"
        },
        {
            "energy_source": "Natural Gas",
            "cost_per_kwh": 0.045,
            "unit": "dollars",
            "trend": "increasing",
            "notes": "Costs vary with natural gas prices"
        },
        {
            "energy_source": "Coal",
            "cost_per_kwh": 0.042,
            "unit": "dollars",
            "trend": "stable",
            "notes": "Includes environmental compliance costs"
        },
        {
            "energy_source": "Nuclear",
            "cost_per_kwh": 0.098,
            "unit": "dollars",
            "trend": "increasing",
            "notes": "High initial construction costs"
        },
        {
            "energy_source": "Hydroelectric",
            "cost_per_kwh": 0.085,
            "unit": "dollars",
            "trend": "stable",
            "notes": "Low operating costs, high initial investment"
        },
        {
            "energy_source": "Geothermal",
            "cost_per_kwh": 0.075,
            "unit": "dollars",
            "trend": "stable",
            "notes": "Location-dependent resource"
        },
        {
            "energy_source": "Biomass",
            "cost_per_kwh": 0.089,
            "unit": "dollars",
            "trend": "stable",
            "notes": "Fuel costs can vary significantly"
        }
    ]
}

CAPACITY_FACTOR_DATASET = {
    "title": "Capacity Factors by Energy Source (2024)",
    "description": "Average capacity factor (percentage of time operating at full capacity) for different energy sources",
    "source": "U.S. Energy Information Administration",
    "data": [
        {
            "energy_source": "Nuclear",
            "capacity_factor": 92.5,
            "unit": "percent",
            "explanation": "Nuclear plants operate continuously except for maintenance"
        },
        {
            "energy_source": "Geothermal",
            "capacity_factor": 74.2,
            "unit": "percent",
            "explanation": "Geothermal plants can operate continuously"
        },
        {
            "energy_source": "Natural Gas (Combined Cycle)",
            "capacity_factor": 56.8,
            "unit": "percent",
            "explanation": "Used for both baseload and peak power"
        },
        {
            "energy_source": "Coal",
            "capacity_factor": 49.3,
            "unit": "percent",
            "explanation": "Traditionally used for baseload power"
        },
        {
            "energy_source": "Hydroelectric",
            "capacity_factor": 37.1,
            "unit": "percent",
            "explanation": "Depends on water availability and seasonal changes"
        },
        {
            "energy_source": "Wind (Onshore)",
            "capacity_factor": 35.4,
            "unit": "percent",
            "explanation": "Wind is intermittent and varies by location"
        },
        {
            "energy_source": "Solar (Utility-scale)",
            "capacity_factor": 24.9,
            "unit": "percent",
            "explanation": "Only produces power during daylight hours"
        },
        {
            "energy_source": "Biomass",
            "capacity_factor": 64.2,
            "unit": "percent",
            "explanation": "Can operate continuously with fuel supply"
        }
    ]
}

RENEWABLE_ENERGY_GROWTH_DATASET = {
    "title": "Renewable Energy Growth in the United States (2010-2024)",
    "description": "Annual renewable energy generation in terawatt-hours",
    "source": "U.S. Energy Information Administration",
    "data": [
        {"year": 2010, "solar": 1.2, "wind": 95.0, "hydroelectric": 260.2, "geothermal": 15.2, "biomass": 56.4},
        {"year": 2012, "solar": 4.3, "wind": 140.8, "hydroelectric": 276.2, "geothermal": 15.5, "biomass": 58.6},
        {"year": 2014, "solar": 18.3, "wind": 181.7, "hydroelectric": 259.4, "geothermal": 15.9, "biomass": 60.7},
        {"year": 2016, "solar": 36.1, "wind": 226.9, "hydroelectric": 265.5, "geothermal": 16.1, "biomass": 62.3},
        {"year": 2018, "solar": 63.8, "wind": 275.8, "hydroelectric": 292.5, "geothermal": 16.3, "biomass": 63.1},
        {"year": 2020, "solar": 91.0, "wind": 337.9, "hydroelectric": 291.1, "geothermal": 16.5, "biomass": 64.2},
        {"year": 2022, "solar": 143.2, "wind": 434.3, "hydroelectric": 262.0, "geothermal": 16.8, "biomass": 65.1},
        {"year": 2024, "solar": 185.5, "wind": 485.7, "hydroelectric": 275.3, "geothermal": 17.1, "biomass": 66.0}
    ]
}

SOLAR_PANEL_EFFICIENCY_DATASET = {
    "title": "Solar Panel Efficiency by Technology (2024)",
    "description": "Average efficiency of different solar panel technologies",
    "source": "National Renewable Energy Laboratory",
    "data": [
        {
            "technology": "Monocrystalline Silicon",
            "efficiency": 20.0,
            "unit": "percent",
            "cost_per_watt": 0.85,
            "lifespan": 25,
            "notes": "Most efficient commercial technology"
        },
        {
            "technology": "Polycrystalline Silicon",
            "efficiency": 15.5,
            "unit": "percent",
            "cost_per_watt": 0.65,
            "lifespan": 25,
            "notes": "Good balance of efficiency and cost"
        },
        {
            "technology": "Thin Film (CdTe)",
            "efficiency": 11.0,
            "unit": "percent",
            "cost_per_watt": 0.45,
            "lifespan": 20,
            "notes": "Lower efficiency but very low cost"
        },
        {
            "technology": "Thin Film (CIGS)",
            "efficiency": 12.5,
            "unit": "percent",
            "cost_per_watt": 0.55,
            "lifespan": 20,
            "notes": "Flexible panels, good for curved surfaces"
        },
        {
            "technology": "Perovskite",
            "efficiency": 25.7,
            "unit": "percent",
            "cost_per_watt": 1.20,
            "lifespan": 15,
            "notes": "Emerging technology, highest efficiency"
        }
    ]
}

WIND_TURBINE_CAPACITY_DATASET = {
    "title": "Wind Turbine Capacity by Size (2024)",
    "description": "Typical capacity and specifications for different wind turbine sizes",
    "source": "American Wind Energy Association",
    "data": [
        {
            "turbine_size": "Small (Residential)",
            "capacity": 10,
            "unit": "kW",
            "rotor_diameter": 7,
            "hub_height": 20,
            "annual_output": 12000,
            "notes": "Suitable for homes and small businesses"
        },
        {
            "turbine_size": "Medium (Commercial)",
            "capacity": 100,
            "unit": "kW",
            "rotor_diameter": 21,
            "hub_height": 30,
            "annual_output": 120000,
            "notes": "Used for schools, farms, and small communities"
        },
        {
            "turbine_size": "Large (Utility)",
            "capacity": 2000,
            "unit": "kW",
            "rotor_diameter": 90,
            "hub_height": 80,
            "annual_output": 2400000,
            "notes": "Standard size for wind farms"
        },
        {
            "turbine_size": "Offshore",
            "capacity": 8000,
            "unit": "kW",
            "rotor_diameter": 120,
            "hub_height": 100,
            "annual_output": 9600000,
            "notes": "Largest turbines, highest capacity factors"
        }
    ]
}

ENERGY_STORAGE_DATASET = {
    "title": "Energy Storage Technologies Comparison (2024)",
    "description": "Comparison of different energy storage technologies",
    "source": "U.S. Department of Energy",
    "data": [
        {
            "technology": "Lithium-Ion Batteries",
            "energy_density": 150,
            "unit": "Wh/kg",
            "cost_per_kwh": 137,
            "efficiency": 85,
            "lifespan": 10,
            "notes": "Most common for grid storage and electric vehicles"
        },
        {
            "technology": "Pumped Hydro",
            "energy_density": 0.5,
            "unit": "Wh/kg",
            "cost_per_kwh": 165,
            "efficiency": 80,
            "lifespan": 50,
            "notes": "Large-scale storage, requires specific geography"
        },
        {
            "technology": "Compressed Air",
            "energy_density": 0.1,
            "unit": "Wh/kg",
            "cost_per_kwh": 105,
            "efficiency": 70,
            "lifespan": 30,
            "notes": "Large-scale storage, underground caverns required"
        },
        {
            "technology": "Flow Batteries",
            "energy_density": 25,
            "unit": "Wh/kg",
            "cost_per_kwh": 300,
            "efficiency": 75,
            "lifespan": 20,
            "notes": "Long-duration storage, scalable capacity"
        },
        {
            "technology": "Hydrogen Storage",
            "energy_density": 120,
            "unit": "Wh/kg",
            "cost_per_kwh": 500,
            "efficiency": 40,
            "lifespan": 15,
            "notes": "Very long-duration storage, low efficiency"
        }
    ]
}
