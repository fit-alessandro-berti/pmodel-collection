# Generated from: 213b9271-7ebc-45cd-82c0-d2c039969bd8.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm on a commercial building. It includes site assessment for structural integrity and sunlight exposure, soil and water testing, regulatory compliance checks, selection of crop varieties suited for rooftop conditions, installation of hydroponic or soil-based systems, integration of automated irrigation and climate control technologies, recruitment and training of specialized farming staff, ongoing pest and disease management, periodic yield monitoring and data analysis, community engagement for educational purposes, and final evaluation of environmental impact and profitability to ensure long-term viability and scalability of the rooftop farm model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Assess = Transition(label='Site Assess')
Structural_Check = Transition(label='Structural Check')
Sunlight_Map = Transition(label='Sunlight Map')
Soil_Test = Transition(label='Soil Test')
Water_Quality = Transition(label='Water Quality')
Permit_Review = Transition(label='Permit Review')
Crop_Select = Transition(label='Crop Select')
System_Install = Transition(label='System Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Climate_Control = Transition(label='Climate Control')
Staff_Hire = Transition(label='Staff Hire')
Training_Run = Transition(label='Training Run')
Pest_Monitor = Transition(label='Pest Monitor')
Yield_Track = Transition(label='Yield Track')
Data_Analyze = Transition(label='Data Analyze')
Community_Meet = Transition(label='Community Meet')
Impact_Review = Transition(label='Impact Review')
Profit_Assess = Transition(label='Profit Assess')

# Site assessment partial order: Structural Check and Sunlight Map concurrent after Site Assess
site_assessment = StrictPartialOrder(
    nodes=[Site_Assess, Structural_Check, Sunlight_Map],
)
site_assessment.order.add_edge(Site_Assess, Structural_Check)
site_assessment.order.add_edge(Site_Assess, Sunlight_Map)

# Soil and water testing partial order concurrent
soil_water_testing = StrictPartialOrder(
    nodes=[Soil_Test, Water_Quality],
    # no order edges, fully concurrent
)

# Regulatory and crop selection sequential: Permit Review -> Crop Select
regulatory_crop = StrictPartialOrder(
    nodes=[Permit_Review, Crop_Select],
)
regulatory_crop.order.add_edge(Permit_Review, Crop_Select)

# Installation partial order: System Install, Irrigation Setup, Climate Control can be partially ordered
# Let's say System Install -> (Irrigation Setup and Climate Control concurrent, after System Install)

installation_irrigation_climate = StrictPartialOrder(
    nodes=[System_Install, Irrigation_Setup, Climate_Control],
)
installation_irrigation_climate.order.add_edge(System_Install, Irrigation_Setup)
installation_irrigation_climate.order.add_edge(System_Install, Climate_Control)

# Staff hiring and training sequential
staff_training = StrictPartialOrder(
    nodes=[Staff_Hire, Training_Run],
)
staff_training.order.add_edge(Staff_Hire, Training_Run)

# Monitoring activities: Pest Monitor and Yield Track concurrent
# Yield Track precedes Data Analyze
monitoring = StrictPartialOrder(
    nodes=[Pest_Monitor, Yield_Track, Data_Analyze]
)
monitoring.order.add_edge(Yield_Track, Data_Analyze)
# Pest Monitor concurrent with Yield Track and Data Analyze (no edges to or from Pest Monitor)

# Community Meet is after monitoring completes (after Data Analyze)
community_meet = Community_Meet

# Final evaluation sequential: Impact Review and Profit Assess
final_evaluation = StrictPartialOrder(
    nodes=[Impact_Review, Profit_Assess]
)
final_evaluation.order.add_edge(Impact_Review, Profit_Assess)

# Compose the big PO:
# Overall order sketch:
# site_assessment -> soil_water_testing
# soil_water_testing -> regulatory_crop
# regulatory_crop -> installation_irrigation_climate
# installation_irrigation_climate -> staff_training
# staff_training -> monitoring
# monitoring -> Community_Meet
# Community_Meet -> final_evaluation

# Build nodes list of the top-level partial order:
# all submodels plus Community_Meet (as a Transition)

root = StrictPartialOrder(
    nodes=[
        site_assessment,
        soil_water_testing,
        regulatory_crop,
        installation_irrigation_climate,
        staff_training,
        monitoring,
        Community_Meet,
        final_evaluation,
    ],
)

# Add edges defining the process flow as per above order
root.order.add_edge(site_assessment, soil_water_testing)
root.order.add_edge(soil_water_testing, regulatory_crop)
root.order.add_edge(regulatory_crop, installation_irrigation_climate)
root.order.add_edge(installation_irrigation_climate, staff_training)
root.order.add_edge(staff_training, monitoring)
root.order.add_edge(monitoring, Community_Meet)
root.order.add_edge(Community_Meet, final_evaluation)