# Generated from: fb83cb7b-cc38-403b-8ae3-39ec0c658194.json
# Description: This process outlines the complex steps involved in establishing an urban rooftop farming system. It begins with site assessment and structural analysis to ensure the roof can support the load. Next, permits and zoning approvals are secured, followed by sourcing sustainable materials and soil mixtures tailored for rooftop environments. Installation involves waterproofing, irrigation setup, and modular planting bed assembly. Ongoing activities include crop planning, pest monitoring using integrated pest management techniques, and automated nutrient delivery calibration. The process concludes with harvest scheduling, community engagement for education, and data collection for yield optimization and environmental impact assessment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Assess = Transition(label='Site Assess')
Structure_Check = Transition(label='Structure Check')
Permit_Obtain = Transition(label='Permit Obtain')
Material_Source = Transition(label='Material Source')
Soil_Prepare = Transition(label='Soil Prepare')
Waterproof_Roof = Transition(label='Waterproof Roof')
Irrigation_Setup = Transition(label='Irrigation Setup')
Bed_Assemble = Transition(label='Bed Assemble')
Crop_Plan = Transition(label='Crop Plan')
Pest_Monitor = Transition(label='Pest Monitor')
Nutrient_Calibrate = Transition(label='Nutrient Calibrate')
Harvest_Schedule = Transition(label='Harvest Schedule')
Community_Train = Transition(label='Community Train')
Yield_Record = Transition(label='Yield Record')
Impact_Review = Transition(label='Impact Review')

# Phase 1: Site assessment and structural analysis
phase1 = StrictPartialOrder(nodes=[Site_Assess, Structure_Check])
phase1.order.add_edge(Site_Assess, Structure_Check)

# Phase 2: Permits and zoning approvals
phase2 = Permit_Obtain

# Phase 3: Sourcing sustainable materials and soil mixtures
phase3 = StrictPartialOrder(nodes=[Material_Source, Soil_Prepare])
phase3.order.add_edge(Material_Source, Soil_Prepare)

# Phase 4: Installation: waterproofing, irrigation setup, and modular bed assembly - sequential
install = StrictPartialOrder(nodes=[Waterproof_Roof, Irrigation_Setup, Bed_Assemble])
install.order.add_edge(Waterproof_Roof, Irrigation_Setup)
install.order.add_edge(Irrigation_Setup, Bed_Assemble)

# Merge phases 3 and 4 sequentially
mat_soil_install = StrictPartialOrder(nodes=[phase3, install])
mat_soil_install.order.add_edge(phase3, install)

# Phase 5: Ongoing activities: crop planning, pest monitoring, nutrient calibration (concurrent)
ongoing = StrictPartialOrder(nodes=[Crop_Plan, Pest_Monitor, Nutrient_Calibrate])
# no order edges => concurrent

# Phase 6: Conclusion: harvest scheduling, community engagement, data collection (3 activities),
# The description orders them as: harvest scheduling, community engagement, data collection,
# interpret this as sequential.

data_collection = StrictPartialOrder(nodes=[Yield_Record, Impact_Review])
data_collection.order.add_edge(Yield_Record, Impact_Review)

conclusion = StrictPartialOrder(nodes=[Harvest_Schedule, Community_Train, data_collection])
conclusion.order.add_edge(Harvest_Schedule, Community_Train)
conclusion.order.add_edge(Community_Train, data_collection)

# Now combine all phases in order:
# phase1 --> phase2 --> (phase3 --> phase4) --> ongoing --> conclusion

root = StrictPartialOrder(nodes=[phase1, phase2, mat_soil_install, ongoing, conclusion])
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, mat_soil_install)
root.order.add_edge(mat_soil_install, ongoing)
root.order.add_edge(ongoing, conclusion)