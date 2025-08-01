# Generated from: ec48dcf3-82ab-497c-90e3-2096670fb435.json
# Description: This process details the complex setup of an urban vertical farm, integrating sustainable agriculture within limited city spaces. It involves site analysis, modular structure assembly, hydroponic system installation, climate control calibration, nutrient solution formulation, seed selection and germination, automated monitoring integration, pest management planning, workforce training, yield forecasting, and community engagement initiatives, all designed to optimize crop production while minimizing environmental impact and ensuring scalability in dense urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Structure_Build = Transition(label='Structure Build')
System_Install = Transition(label='System Install')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Prep = Transition(label='Nutrient Prep')
Seed_Germinate = Transition(label='Seed Germinate')
Planting_Phase = Transition(label='Planting Phase')
Sensor_Deploy = Transition(label='Sensor Deploy')
Pest_Control = Transition(label='Pest Control')
Water_Monitor = Transition(label='Water Monitor')
Data_Analyze = Transition(label='Data Analyze')
Staff_Train = Transition(label='Staff Train')
Yield_Forecast = Transition(label='Yield Forecast')
Community_Meet = Transition(label='Community Meet')

# Partial order reflecting a reasonable complex process order based on description
# Site Survey -> Design Layout -> Structure Build -> System Install -> Climate Setup
# Nutrient Prep and Seed Germinate are preparatory, but Seed Germinate must precede Planting Phase
# Sensor Deploy, Pest Control, Water Monitor, Data Analyze can be concurrent after Planting Phase
# Staff Train and Yield Forecast come after Data Analyze and Pest Control
# Community Meet happens finally for engagement initiatives

root = StrictPartialOrder(nodes=[
    Site_Survey,
    Design_Layout,
    Structure_Build,
    System_Install,
    Climate_Setup,
    Nutrient_Prep,
    Seed_Germinate,
    Planting_Phase,
    Sensor_Deploy,
    Pest_Control,
    Water_Monitor,
    Data_Analyze,
    Staff_Train,
    Yield_Forecast,
    Community_Meet
])

# Define edges (partial order dependencies)
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Structure_Build)
root.order.add_edge(Structure_Build, System_Install)
root.order.add_edge(System_Install, Climate_Setup)

# Nutrient Prep can happen after Climate Setup
root.order.add_edge(Climate_Setup, Nutrient_Prep)

# Seed Germinate depends on Nutrient Prep (formulation) presumably
root.order.add_edge(Nutrient_Prep, Seed_Germinate)

# Planting Phase depends on Seed Germinate and Structure Build finished
root.order.add_edge(Seed_Germinate, Planting_Phase)
root.order.add_edge(Structure_Build, Planting_Phase)

# Sensor Deploy, Pest Control, Water Monitor start after Planting Phase (concurrent)
root.order.add_edge(Planting_Phase, Sensor_Deploy)
root.order.add_edge(Planting_Phase, Pest_Control)
root.order.add_edge(Planting_Phase, Water_Monitor)

# Data Analyze depends on Sensor Deploy and Water Monitor (analysis after monitoring)
root.order.add_edge(Sensor_Deploy, Data_Analyze)
root.order.add_edge(Water_Monitor, Data_Analyze)

# Staff Train depends on Pest Control (training workforce for pest mgmt)
root.order.add_edge(Pest_Control, Staff_Train)

# Yield Forecast depends on Data Analyze
root.order.add_edge(Data_Analyze, Yield_Forecast)

# Community Meet happens after Staff Train and Yield Forecast
root.order.add_edge(Staff_Train, Community_Meet)
root.order.add_edge(Yield_Forecast, Community_Meet)