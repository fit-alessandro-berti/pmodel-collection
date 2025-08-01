# Generated from: cbacbefb-0c7d-4b92-8e3e-fa461cba3574.json
# Description: This process encompasses the planning, development, and operational launch of a multi-level urban vertical farm designed to maximize limited space within city environments. It involves site analysis, modular infrastructure installation, climate control calibration, nutrient solution preparation, crop cycle scheduling, integrated pest management, and real-time sensor network deployment. The workflow ensures sustainable resource use, compliance with urban agricultural regulations, and continuous yield optimization through data-driven decisions, enabling efficient production of fresh produce for local markets and reducing transportation emissions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Design_Layout = Transition(label='Design Layout')
Module_Assembly = Transition(label='Module Assembly')
Climate_Setup = Transition(label='Climate Setup')
Sensor_Install = Transition(label='Sensor Install')
Water_Testing = Transition(label='Water Testing')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Selection = Transition(label='Seed Selection')
Planting_Phase = Transition(label='Planting Phase')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Yield_Audit = Transition(label='Yield Audit')
Packaging_Prep = Transition(label='Packaging Prep')
Market_Delivery = Transition(label='Market Delivery')
Waste_Recycling = Transition(label='Waste Recycling')

# Build partial order according to a reasonable flow based on description:
# Planning: Site Analysis -> Design Layout
# Development: Module Assembly -> Climate Setup
# Setup and Testing: Sensor Install, Water Testing, Nutrient Mix (concurrent after Climate Setup)
# Planting and growth: Seed Selection -> Planting Phase -> Growth Monitor
# Pest Control after Growth Monitor
# Harvest Plan after Pest Control
# Yield Audit after Harvest Plan
# Packaging Prep after Yield Audit
# Market Delivery after Packaging Prep
# Waste Recycling concurrent with Market Delivery (final step)

root = StrictPartialOrder(
    nodes=[
        Site_Analysis, Design_Layout,
        Module_Assembly, Climate_Setup,
        Sensor_Install, Water_Testing, Nutrient_Mix,
        Seed_Selection, Planting_Phase, Growth_Monitor,
        Pest_Control, Harvest_Plan, Yield_Audit,
        Packaging_Prep, Market_Delivery, Waste_Recycling
    ]
)

# Define order edges to model dependencies

# Planning phase
root.order.add_edge(Site_Analysis, Design_Layout)

# Development phase
root.order.add_edge(Design_Layout, Module_Assembly)
root.order.add_edge(Module_Assembly, Climate_Setup)

# Setup and Testing (concurrent after Climate_Setup)
root.order.add_edge(Climate_Setup, Sensor_Install)
root.order.add_edge(Climate_Setup, Water_Testing)
root.order.add_edge(Climate_Setup, Nutrient_Mix)

# Planting and Growth
root.order.add_edge(Nutrient_Mix, Seed_Selection)
root.order.add_edge(Water_Testing, Seed_Selection)
root.order.add_edge(Sensor_Install, Seed_Selection)

root.order.add_edge(Seed_Selection, Planting_Phase)
root.order.add_edge(Planting_Phase, Growth_Monitor)

# Pest management and harvest
root.order.add_edge(Growth_Monitor, Pest_Control)
root.order.add_edge(Pest_Control, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Yield_Audit)
root.order.add_edge(Yield_Audit, Packaging_Prep)

# Final delivery and recycling
root.order.add_edge(Packaging_Prep, Market_Delivery)

# Waste recycling concurrent with Market Delivery (no order between them)
# So no edge linking them

# End of model