# Generated from: 6ec63f82-ee19-4b5b-b81c-900cbb778f50.json
# Description: This process outlines the detailed steps involved in establishing an urban vertical farm within a repurposed industrial building. It begins with site analysis and environmental assessment, followed by modular system design and nutrient sourcing. The process includes installation of hydroponic towers, automated climate control calibration, and integration of renewable energy sources. Subsequent activities cover seed selection, germination monitoring, pest management without chemicals, and continuous growth optimization through AI analytics. Finally, the process addresses harvest scheduling, packaging automation, quality verification, and distribution logistics to local retailers, ensuring sustainability and minimal waste throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition, SilentTransition, OperatorPOWL
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Analysis = Transition(label='Site Analysis')
Env_Assessment = Transition(label='Env Assessment')
Modular_Design = Transition(label='Modular Design')
Nutrient_Sourcing = Transition(label='Nutrient Sourcing')
Tower_Install = Transition(label='Tower Install')
Climate_Setup = Transition(label='Climate Setup')
Energy_Integrate = Transition(label='Energy Integrate')
Seed_Selection = Transition(label='Seed Selection')
Germination_Check = Transition(label='Germination Check')
Pest_Control = Transition(label='Pest Control')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Packaging_Auto = Transition(label='Packaging Auto')
Quality_Check = Transition(label='Quality Check')
Distribution = Transition(label='Distribution')

# Build partial orders based on described dependencies

# Phase 1: Site Analysis -> Env Assessment
# Site Analysis and Env Assessment are sequential
phase1 = StrictPartialOrder(nodes=[Site_Analysis, Env_Assessment])
phase1.order.add_edge(Site_Analysis, Env_Assessment)

# Phase 2: Modular Design and Nutrient Sourcing can be done after Env Assessment, possibly concurrent
# Modular Design and Nutrient Sourcing have no order between them (concurrent),
# both depend on Env Assessment
phase2 = StrictPartialOrder(nodes=[Env_Assessment, Modular_Design, Nutrient_Sourcing])
phase2.order.add_edge(Env_Assessment, Modular_Design)
phase2.order.add_edge(Env_Assessment, Nutrient_Sourcing)

# Phase 3: Installation: Tower Install, Climate Setup, Energy Integrate
# All follow Phase2 and can be done concurrently
phase3 = StrictPartialOrder(
    nodes=[Modular_Design, Nutrient_Sourcing, Tower_Install, Climate_Setup, Energy_Integrate]
)
phase3.order.add_edge(Modular_Design, Tower_Install)
phase3.order.add_edge(Modular_Design, Climate_Setup)
phase3.order.add_edge(Modular_Design, Energy_Integrate)
phase3.order.add_edge(Nutrient_Sourcing, Tower_Install)
phase3.order.add_edge(Nutrient_Sourcing, Climate_Setup)
phase3.order.add_edge(Nutrient_Sourcing, Energy_Integrate)

# Phase 4: Seed Selection -> Germination Check -> Pest Control (without chemicals)
phase4 = StrictPartialOrder(nodes=[Tower_Install, Climate_Setup, Energy_Integrate, Seed_Selection, Germination_Check, Pest_Control])
# Installation must finish before Seed Selection
phase4.order.add_edge(Tower_Install, Seed_Selection)
phase4.order.add_edge(Climate_Setup, Seed_Selection)
phase4.order.add_edge(Energy_Integrate, Seed_Selection)
# Sequential steps Seed Selection -> Germination Check -> Pest Control
phase4.order.add_edge(Seed_Selection, Germination_Check)
phase4.order.add_edge(Germination_Check, Pest_Control)

# Phase 5: Growth Monitor after Pest Control (continuous optimization)
phase5 = StrictPartialOrder(nodes=[Pest_Control, Growth_Monitor])
phase5.order.add_edge(Pest_Control, Growth_Monitor)

# Phase 6: Harvest Plan -> Packaging Auto -> Quality Check -> Distribution
phase6 = StrictPartialOrder(nodes=[Growth_Monitor, Harvest_Plan, Packaging_Auto, Quality_Check, Distribution])
phase6.order.add_edge(Growth_Monitor, Harvest_Plan)
phase6.order.add_edge(Harvest_Plan, Packaging_Auto)
phase6.order.add_edge(Packaging_Auto, Quality_Check)
phase6.order.add_edge(Quality_Check, Distribution)

# Combine all phases into a global process
root = StrictPartialOrder(nodes=[
    Site_Analysis, Env_Assessment, Modular_Design, Nutrient_Sourcing,
    Tower_Install, Climate_Setup, Energy_Integrate, Seed_Selection,
    Germination_Check, Pest_Control, Growth_Monitor, Harvest_Plan,
    Packaging_Auto, Quality_Check, Distribution
])

# Add edges that cover all dependencies
# Phase 1 and 2
root.order.add_edge(Site_Analysis, Env_Assessment)
root.order.add_edge(Env_Assessment, Modular_Design)
root.order.add_edge(Env_Assessment, Nutrient_Sourcing)

# Phase 2 to 3
root.order.add_edge(Modular_Design, Tower_Install)
root.order.add_edge(Modular_Design, Climate_Setup)
root.order.add_edge(Modular_Design, Energy_Integrate)
root.order.add_edge(Nutrient_Sourcing, Tower_Install)
root.order.add_edge(Nutrient_Sourcing, Climate_Setup)
root.order.add_edge(Nutrient_Sourcing, Energy_Integrate)

# Phase 3 to 4
root.order.add_edge(Tower_Install, Seed_Selection)
root.order.add_edge(Climate_Setup, Seed_Selection)
root.order.add_edge(Energy_Integrate, Seed_Selection)

# Phase 4 sequence
root.order.add_edge(Seed_Selection, Germination_Check)
root.order.add_edge(Germination_Check, Pest_Control)

# Phase 4 to 5
root.order.add_edge(Pest_Control, Growth_Monitor)

# Phase 5 to 6
root.order.add_edge(Growth_Monitor, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Packaging_Auto)
root.order.add_edge(Packaging_Auto, Quality_Check)
root.order.add_edge(Quality_Check, Distribution)