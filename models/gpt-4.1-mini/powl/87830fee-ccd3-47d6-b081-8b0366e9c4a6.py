# Generated from: 87830fee-ccd3-47d6-b081-8b0366e9c4a6.json
# Description: This process outlines the intricate steps required to establish a fully operational urban vertical farm within a repurposed industrial building. It involves site analysis, structural modifications, environmental controls, hydroponic system installation, nutrient management, automated monitoring integration, crop selection and rotation planning, pest management without chemicals, energy optimization, waste recycling, and community engagement to ensure sustainable urban agriculture that maximizes yield in limited city spaces while minimizing ecological footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Survey = Transition(label='Site Survey')
Structural_Check = Transition(label='Structural Check')
Layout_Design = Transition(label='Layout Design')
Lighting_Setup = Transition(label='Lighting Setup')
Climate_Control = Transition(label='Climate Control')
Hydroponic_Install = Transition(label='Hydroponic Install')
Nutrient_Mix = Transition(label='Nutrient Mix')
Crop_Planning = Transition(label='Crop Planning')
Pest_Monitoring = Transition(label='Pest Monitoring')
Water_Recycling = Transition(label='Water Recycling')
Energy_Audit = Transition(label='Energy Audit')
Automation_Setup = Transition(label='Automation Setup')
Waste_Sorting = Transition(label='Waste Sorting')
Harvest_Schedule = Transition(label='Harvest Schedule')
Community_Outreach = Transition(label='Community Outreach')
Market_Analysis = Transition(label='Market Analysis')

# Build partial orders reflecting dependencies and partial concurrency

# Phase 1: Site Survey -> Structural Check -> Layout Design
phase1 = StrictPartialOrder(nodes=[Site_Survey, Structural_Check, Layout_Design])
phase1.order.add_edge(Site_Survey, Structural_Check)
phase1.order.add_edge(Structural_Check, Layout_Design)

# Phase 2: Environmental controls, hydroponic installation, nutrient management and lighting/web:
# Lighting Setup and Climate Control can be done concurrently after Layout Design
# Hydroponic Install after Layout Design
phase2 = StrictPartialOrder(nodes=[Layout_Design, Lighting_Setup, Climate_Control, Hydroponic_Install, Nutrient_Mix])
phase2.order.add_edge(Layout_Design, Lighting_Setup)
phase2.order.add_edge(Layout_Design, Climate_Control)
phase2.order.add_edge(Layout_Design, Hydroponic_Install)

# Nutrient Mix depends on Hydroponic Install
phase2.order.add_edge(Hydroponic_Install, Nutrient_Mix)

# Phase 3: Crop planning and pest monitoring
# Crop Planning after Nutrient Mix
# Pest Monitoring after Crop Planning; no chemicals used, so just monitoring
phase3 = StrictPartialOrder(nodes=[Nutrient_Mix, Crop_Planning, Pest_Monitoring])
phase3.order.add_edge(Nutrient_Mix, Crop_Planning)
phase3.order.add_edge(Crop_Planning, Pest_Monitoring)

# Phase 4: Water recycling, Energy audit and Waste sorting run concurrently
phase4 = StrictPartialOrder(nodes=[Water_Recycling, Energy_Audit, Waste_Sorting])

# Phase 5: Automation Setup after Climate Control and Hydroponic Install (both needed)
phase5 = StrictPartialOrder(nodes=[Climate_Control, Hydroponic_Install, Automation_Setup])
phase5.order.add_edge(Climate_Control, Automation_Setup)
phase5.order.add_edge(Hydroponic_Install, Automation_Setup)

# Phase 6: Harvest Schedule after Crop Planning and Nutrient Mix (both needed)
phase6 = StrictPartialOrder(nodes=[Crop_Planning, Nutrient_Mix, Harvest_Schedule])
phase6.order.add_edge(Crop_Planning, Harvest_Schedule)
phase6.order.add_edge(Nutrient_Mix, Harvest_Schedule)

# Phase 7: Community Outreach and Market Analysis can be done concurrently after Harvest Schedule
phase7 = StrictPartialOrder(nodes=[Harvest_Schedule, Community_Outreach, Market_Analysis])
phase7.order.add_edge(Harvest_Schedule, Community_Outreach)
phase7.order.add_edge(Harvest_Schedule, Market_Analysis)

# Now combine the phases into a top-level partial order with proper causal relations

# Start with phase1
# phase2 and phase5 start after phase1 and layout design
# phase3 after phase2 (Nutrient Mix)
# phase6 after phase3 (Crop Planning, Nutrient Mix)
# phase4 independent concurrency - starts after layout design
# phase7 after phase6 (Harvest Schedule)


root = StrictPartialOrder(nodes=[
    phase1,
    phase2,
    phase3,
    phase4,
    phase5,
    phase6,
    phase7
])

# Add order edges reflecting causal dependencies between phases
# phase1 -> phase2 (via Layout Design)
root.order.add_edge(phase1, phase2)
# phase1 -> phase4 (Water recycling, energy audit, waste sorting after layout design for infrastructure)
root.order.add_edge(phase1, phase4)
# phase2 -> phase3 (Nutrient Mix -> Crop Planning)
root.order.add_edge(phase2, phase3)
# phase2 -> phase5 (Climate Control and Hydroponic Install needed for Automation Setup)
root.order.add_edge(phase2, phase5)
# phase3 -> phase6 (Crop Planning and Nutrient Mix before Harvest Schedule)
root.order.add_edge(phase3, phase6)
# Also enforce Nutrient Mix from phase2 for phase6
root.order.add_edge(phase2, phase6)
# phase6 -> phase7 (Harvest Schedule before Community Outreach and Market Analysis)
root.order.add_edge(phase6, phase7)