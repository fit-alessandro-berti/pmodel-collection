# Generated from: cca5d757-48f3-4719-b1cf-e039ac7f3d57.json
# Description: This process outlines the complex and multifaceted approach to establishing a sustainable urban rooftop farm in a densely populated cityscape. It involves site assessment for structural integrity, microclimate analysis, soil-less medium preparation, modular bed installation, automated irrigation setup, crop selection based on seasonal and local demand, pest management using integrated natural methods, community engagement for educational workshops, digital monitoring system deployment, waste recycling integration, seasonal yield forecasting, and finally distribution channel establishment through local markets and restaurants. This atypical yet realistic process requires cross-disciplinary coordination between architects, agronomists, technologists, and community organizers to ensure a productive, eco-friendly, and economically viable rooftop farming venture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Assess = Transition(label='Site Assess')
Load_Testing = Transition(label='Load Testing')
Climate_Study = Transition(label='Climate Study')
Medium_Prep = Transition(label='Medium Prep')
Bed_Install = Transition(label='Bed Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Crop_Select = Transition(label='Crop Select')
Pest_Control = Transition(label='Pest Control')
Community_Meet = Transition(label='Community Meet')
Monitor_Deploy = Transition(label='Monitor Deploy')
Waste_Cycle = Transition(label='Waste Cycle')
Yield_Forecast = Transition(label='Yield Forecast')
Market_Link = Transition(label='Market Link')
Workshop_Plan = Transition(label='Workshop Plan')
Tech_Integrate = Transition(label='Tech Integrate')

# The workflow:
# 1) Site Assess followed by Load Testing and Climate Study (these two concurrent after Load Testing)
so1 = StrictPartialOrder(nodes=[Site_Assess, Load_Testing, Climate_Study])
so1.order.add_edge(Site_Assess, Load_Testing)
so1.order.add_edge(Load_Testing, Climate_Study)

# 2) Medium Prep and Tech Integrate in parallel after Climate Study
so2 = StrictPartialOrder(nodes=[Medium_Prep, Tech_Integrate])
# no order edges - parallel

# 3) Bed Install (after Medium Prep)
so3 = StrictPartialOrder(nodes=[Medium_Prep, Bed_Install])
so3.order.add_edge(Medium_Prep, Bed_Install)

# 4) Irrigation Setup after Bed Install
so4 = StrictPartialOrder(nodes=[Bed_Install, Irrigation_Setup])
so4.order.add_edge(Bed_Install, Irrigation_Setup)

# 5) Crop Select after Irrigation Setup
so5 = StrictPartialOrder(nodes=[Irrigation_Setup, Crop_Select])
so5.order.add_edge(Irrigation_Setup, Crop_Select)

# 6) Pest Control after Crop Select
so6 = StrictPartialOrder(nodes=[Crop_Select, Pest_Control])
so6.order.add_edge(Crop_Select, Pest_Control)

# 7) Parallel after Pest Control: Community Meet, Workshop Plan, Waste Cycle, Monitor Deploy
# They all occur concurrently
so7 = StrictPartialOrder(
    nodes=[Community_Meet, Workshop_Plan, Waste_Cycle, Monitor_Deploy]
)
# no order edges

# 8) Yield Forecast after Waste Cycle and Monitor Deploy
so8 = StrictPartialOrder(
    nodes=[Waste_Cycle, Monitor_Deploy, Yield_Forecast]
)
so8.order.add_edge(Waste_Cycle, Yield_Forecast)
so8.order.add_edge(Monitor_Deploy, Yield_Forecast)

# 9) Market Link after Yield Forecast and Pest Control, and after Community Meet and Workshop Plan
# Pest Control already precedes so7, so link Pest Control to Market Link and Yield Forecast to Market Link
so9_nodes = [Pest_Control, Community_Meet, Workshop_Plan, Yield_Forecast, Market_Link]
so9 = StrictPartialOrder(nodes=so9_nodes)
so9.order.add_edge(Pest_Control, Market_Link)
so9.order.add_edge(Community_Meet, Market_Link)
so9.order.add_edge(Workshop_Plan, Market_Link)
so9.order.add_edge(Yield_Forecast, Market_Link)

# Now combine all parts into a global partial order

# Combine so1 and so2:

# so1 ends with Climate Study
# so2 includes Medium Prep and Tech Integrate in parallel - both start after Climate Study

root_nodes = [Site_Assess, Load_Testing, Climate_Study,
              Medium_Prep, Tech_Integrate,
              Bed_Install, Irrigation_Setup, Crop_Select, Pest_Control,
              Community_Meet, Workshop_Plan, Waste_Cycle, Monitor_Deploy,
              Yield_Forecast, Market_Link]

root = StrictPartialOrder(nodes=root_nodes)

# Add edges from all subparts
# so1 edges
root.order.add_edge(Site_Assess, Load_Testing)
root.order.add_edge(Load_Testing, Climate_Study)

# From so2: Climate Study --> Medium Prep and Climate Study --> Tech Integrate (start so2 after so1)
root.order.add_edge(Climate_Study, Medium_Prep)
root.order.add_edge(Climate_Study, Tech_Integrate)

# so3: Medium Prep --> Bed Install
root.order.add_edge(Medium_Prep, Bed_Install)

# so4: Bed Install --> Irrigation Setup
root.order.add_edge(Bed_Install, Irrigation_Setup)

# so5: Irrigation Setup --> Crop Select
root.order.add_edge(Irrigation_Setup, Crop_Select)

# so6: Crop Select --> Pest Control
root.order.add_edge(Crop_Select, Pest_Control)

# so7: Community Meet, Workshop Plan, Waste Cycle, Monitor Deploy are concurrent after Pest Control
root.order.add_edge(Pest_Control, Community_Meet)
root.order.add_edge(Pest_Control, Workshop_Plan)
root.order.add_edge(Pest_Control, Waste_Cycle)
root.order.add_edge(Pest_Control, Monitor_Deploy)

# so8: Waste Cycle and Monitor Deploy --> Yield Forecast
root.order.add_edge(Waste_Cycle, Yield_Forecast)
root.order.add_edge(Monitor_Deploy, Yield_Forecast)

# so9: Pest Control, Community Meet, Workshop Plan, Yield Forecast --> Market Link
root.order.add_edge(Pest_Control, Market_Link)
root.order.add_edge(Community_Meet, Market_Link)
root.order.add_edge(Workshop_Plan, Market_Link)
root.order.add_edge(Yield_Forecast, Market_Link)