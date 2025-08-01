# Generated from: 46e56213-1042-4e2b-b3d1-8c326aba60e2.json
# Description: This process outlines the complex and atypical steps involved in establishing a sustainable urban rooftop farm. It begins with site analysis to assess structural integrity and sunlight exposure, followed by securing permits and community engagement to ensure regulatory compliance and local support. Next, soil testing and hydroponic system design are tailored to urban constraints. Procurement involves sourcing lightweight, eco-friendly materials and heirloom seeds. Installation includes modular bed assembly, irrigation setup, and sensor integration for climate control. Subsequent activities focus on planting, pest management using organic methods, and continuous monitoring via IoT devices. Harvesting is scheduled in phases to optimize yield, followed by distribution through local markets and restaurants. The process concludes with seasonal evaluation and planning for crop rotation to maintain soil health and sustainability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Analysis = Transition(label='Site Analysis')
Permit_Filing = Transition(label='Permit Filing')
Community_Meet = Transition(label='Community Meet')
Soil_Testing = Transition(label='Soil Testing')
System_Design = Transition(label='System Design')
Material_Sourcing = Transition(label='Material Sourcing')
Seed_Selection = Transition(label='Seed Selection')
Bed_Assembly = Transition(label='Bed Assembly')
Irrigation_Setup = Transition(label='Irrigation Setup')
Sensor_Install = Transition(label='Sensor Install')
Planting_Phase = Transition(label='Planting Phase')
Pest_Control = Transition(label='Pest Control')
Climate_Monitor = Transition(label='Climate Monitor')
Harvesting_Plan = Transition(label='Harvesting Plan')
Yield_Distribution = Transition(label='Yield Distribution')
Season_Review = Transition(label='Season Review')
Crop_Rotation = Transition(label='Crop Rotation')

# Construct partial orders where appropriate

# Parallel start of Permit Filing and Community Meet after Site Analysis
start_PO = StrictPartialOrder(nodes=[Site_Analysis, Permit_Filing, Community_Meet])
start_PO.order.add_edge(Site_Analysis, Permit_Filing)
start_PO.order.add_edge(Site_Analysis, Community_Meet)

# Soil Testing and System Design can proceed in parallel after permit and meet
prep_PO = StrictPartialOrder(nodes=[Permit_Filing, Community_Meet, Soil_Testing, System_Design])
prep_PO.order.add_edge(Permit_Filing, Soil_Testing)
prep_PO.order.add_edge(Permit_Filing, System_Design)
prep_PO.order.add_edge(Community_Meet, Soil_Testing)
prep_PO.order.add_edge(Community_Meet, System_Design)

# Material Sourcing and Seed Selection in parallel after Soil Testing and System Design
procurement_PO = StrictPartialOrder(nodes=[Soil_Testing, System_Design, Material_Sourcing, Seed_Selection])
procurement_PO.order.add_edge(Soil_Testing, Material_Sourcing)
procurement_PO.order.add_edge(Soil_Testing, Seed_Selection)
procurement_PO.order.add_edge(System_Design, Material_Sourcing)
procurement_PO.order.add_edge(System_Design, Seed_Selection)

# Installation steps: Bed Assembly, Irrigation Setup, Sensor Install in parallel after Material and Seed Procurements
installation_PO = StrictPartialOrder(
    nodes=[Material_Sourcing, Seed_Selection, Bed_Assembly, Irrigation_Setup, Sensor_Install]
)
installation_PO.order.add_edge(Material_Sourcing, Bed_Assembly)
installation_PO.order.add_edge(Material_Sourcing, Irrigation_Setup)
installation_PO.order.add_edge(Material_Sourcing, Sensor_Install)
installation_PO.order.add_edge(Seed_Selection, Bed_Assembly)
installation_PO.order.add_edge(Seed_Selection, Irrigation_Setup)
installation_PO.order.add_edge(Seed_Selection, Sensor_Install)

# Planting Phase must wait until Bed Assembly done
planting = StrictPartialOrder(nodes=[Bed_Assembly, Planting_Phase])
planting.order.add_edge(Bed_Assembly, Planting_Phase)

# Pest Control and Climate Monitor are concurrent but start after Planting Phase
monitor_PO = StrictPartialOrder(nodes=[Planting_Phase, Pest_Control, Climate_Monitor])
monitor_PO.order.add_edge(Planting_Phase, Pest_Control)
monitor_PO.order.add_edge(Planting_Phase, Climate_Monitor)

# Harvesting Plan after Pest Control and Climate Monitor
harvest_plan = StrictPartialOrder(nodes=[Pest_Control, Climate_Monitor, Harvesting_Plan])
harvest_plan.order.add_edge(Pest_Control, Harvesting_Plan)
harvest_plan.order.add_edge(Climate_Monitor, Harvesting_Plan)

# Yield Distribution after Harvesting Plan
distribute = StrictPartialOrder(nodes=[Harvesting_Plan, Yield_Distribution])
distribute.order.add_edge(Harvesting_Plan, Yield_Distribution)

# Season Review then Crop Rotation after Distribution
final_PO = StrictPartialOrder(nodes=[Yield_Distribution, Season_Review, Crop_Rotation])
final_PO.order.add_edge(Yield_Distribution, Season_Review)
final_PO.order.add_edge(Season_Review, Crop_Rotation)

# Compose the overall order:
# Start -> preparation -> procurement -> installation -> planting -> monitoring -> harvesting -> distribution -> final

root = StrictPartialOrder(
    nodes=[
        start_PO,
        prep_PO,
        procurement_PO,
        installation_PO,
        planting,
        monitor_PO,
        harvest_plan,
        distribute,
        final_PO,
    ]
)

root.order.add_edge(start_PO, prep_PO)
root.order.add_edge(prep_PO, procurement_PO)
root.order.add_edge(procurement_PO, installation_PO)
root.order.add_edge(installation_PO, planting)
root.order.add_edge(planting, monitor_PO)
root.order.add_edge(monitor_PO, harvest_plan)
root.order.add_edge(harvest_plan, distribute)
root.order.add_edge(distribute, final_PO)