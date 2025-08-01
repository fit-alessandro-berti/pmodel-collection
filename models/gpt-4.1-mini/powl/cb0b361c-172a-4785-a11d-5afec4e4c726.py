# Generated from: cb0b361c-172a-4785-a11d-5afec4e4c726.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility within a repurposed warehouse. It involves site analysis, structural modifications, installation of hydroponic systems, climate control integration, and automation setup. The process also covers nutrient solution formulation, seed selection, growth monitoring, pest management, and harvesting protocols. Additionally, it includes packaging, distribution logistics, and sustainability reporting to ensure environmental compliance and economic viability in an urban agriculture context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Structural_Audit = Transition(label='Structural Audit')
Layout_Design = Transition(label='Layout Design')
System_Install = Transition(label='System Install')
Climate_Setup = Transition(label='Climate Setup')
Water_Testing = Transition(label='Water Testing')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Selection = Transition(label='Seed Selection')
Planting_Prep = Transition(label='Planting Prep')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Inspect = Transition(label='Pest Inspect')
Harvest_Plan = Transition(label='Harvest Plan')
Packaging_Prep = Transition(label='Packaging Prep')
Distribution = Transition(label='Distribution')
Sustainability = Transition(label='Sustainability')

# Define nodes and partial order edges respecting the process description and logical flow

# Phase 1: Preparation phase
# Site Survey -> Structural Audit -> Layout Design
# These are strictly ordered
# Phase 2: Facility modification and system setup
# Layout Design -> System Install -> Climate Setup
# Concurrent with Climate Setup: Water Testing (can be parallel with Climate Setup)
# Phase 3: Production preparation
# After System Install and Climate Setup+Water Testing
# Nutrient Mix -> Seed Selection -> Planting Prep
# Phase 4: Production process monitoring
# Planting Prep -> Growth Monitor -> Pest Inspect -> Harvest Plan
# Phase 5: Post-harvest and distribution
# Harvest Plan -> Packaging Prep -> Distribution
# Final: Sustainability reporting after Distribution

nodes = [
    Site_Survey, Structural_Audit, Layout_Design,
    System_Install, Climate_Setup, Water_Testing,
    Nutrient_Mix, Seed_Selection, Planting_Prep,
    Growth_Monitor, Pest_Inspect, Harvest_Plan,
    Packaging_Prep, Distribution, Sustainability
]

root = StrictPartialOrder(nodes=nodes)

# Site Survey -> Structural Audit -> Layout Design
root.order.add_edge(Site_Survey, Structural_Audit)
root.order.add_edge(Structural_Audit, Layout_Design)

# Layout Design -> System Install
root.order.add_edge(Layout_Design, System_Install)

# System Install -> Climate Setup and System Install -> Water Testing
root.order.add_edge(System_Install, Climate_Setup)
root.order.add_edge(System_Install, Water_Testing)

# Climate Setup and Water Testing can run concurrently - no edge between them

# Climate Setup and Water Testing must finish before Nutrient Mix
root.order.add_edge(Climate_Setup, Nutrient_Mix)
root.order.add_edge(Water_Testing, Nutrient_Mix)

# Nutrient Mix -> Seed Selection -> Planting Prep
root.order.add_edge(Nutrient_Mix, Seed_Selection)
root.order.add_edge(Seed_Selection, Planting_Prep)

# Planting Prep -> Growth Monitor -> Pest Inspect -> Harvest Plan
root.order.add_edge(Planting_Prep, Growth_Monitor)
root.order.add_edge(Growth_Monitor, Pest_Inspect)
root.order.add_edge(Pest_Inspect, Harvest_Plan)

# Harvest Plan -> Packaging Prep -> Distribution
root.order.add_edge(Harvest_Plan, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Distribution)

# Distribution -> Sustainability reporting
root.order.add_edge(Distribution, Sustainability)