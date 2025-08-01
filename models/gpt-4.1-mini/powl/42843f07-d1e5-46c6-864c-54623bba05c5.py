# Generated from: 42843f07-d1e5-46c6-864c-54623bba05c5.json
# Description: This process outlines the comprehensive steps required to establish a fully operational urban vertical farm within a metropolitan environment. It involves site assessment, modular infrastructure design, climate system integration, nutrient cycling optimization, IoT sensor deployment, and automation setup. The process continues with seed selection, germination protocols, growth monitoring, pest control, harvesting schedules, packaging logistics, waste recycling, energy management, and continuous yield analysis. Each phase is critical to ensure sustainable production, minimize environmental impact, and maximize crop output in limited urban spaces while adapting to fluctuating demand and technological advancements.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Survey = Transition(label='Site Survey')
Modular_Design = Transition(label='Modular Design')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Deploy = Transition(label='Sensor Deploy')
Automation_Init = Transition(label='Automation Init')
Seed_Selection = Transition(label='Seed Selection')
Germination = Transition(label='Germination')
Growth_Check = Transition(label='Growth Check')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Pack_Logistics = Transition(label='Pack Logistics')
Waste_Sorting = Transition(label='Waste Sorting')
Energy_Audit = Transition(label='Energy Audit')
Yield_Review = Transition(label='Yield Review')

# Create a StrictPartialOrder representing the linear sequence of all activities
root = StrictPartialOrder(nodes=[
    Site_Survey,
    Modular_Design,
    Climate_Setup,
    Nutrient_Mix,
    Sensor_Deploy,
    Automation_Init,
    Seed_Selection,
    Germination,
    Growth_Check,
    Pest_Control,
    Harvest_Plan,
    Pack_Logistics,
    Waste_Sorting,
    Energy_Audit,
    Yield_Review
])

# Add edges to represent the order of execution
root.order.add_edge(Site_Survey, Modular_Design)
root.order.add_edge(Modular_Design, Climate_Setup)
root.order.add_edge(Climate_Setup, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Sensor_Deploy)
root.order.add_edge(Sensor_Deploy, Automation_Init)
root.order.add_edge(Automation_Init, Seed_Selection)
root.order.add_edge(Seed_Selection, Germination)
root.order.add_edge(Germination, Growth_Check)
root.order.add_edge(Growth_Check, Pest_Control)
root.order.add_edge(Pest_Control, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Pack_Logistics)
root.order.add_edge(Pack_Logistics, Waste_Sorting)
root.order.add_edge(Waste_Sorting, Energy_Audit)
root.order.add_edge(Energy_Audit, Yield_Review)