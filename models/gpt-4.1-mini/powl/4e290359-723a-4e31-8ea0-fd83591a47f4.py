# Generated from: 4e290359-723a-4e31-8ea0-fd83591a47f4.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farm within a dense metropolitan area. It involves site analysis, environmental impact assessments, modular system design, multi-layer crop planning, automated nutrient delivery setup, energy optimization strategies, integration with local supply chains, community engagement, regulatory compliance, and ongoing maintenance protocols. The process demands coordination between agricultural experts, engineers, urban planners, and marketing teams to ensure sustainable production of fresh produce while minimizing ecological footprints and maximizing yield within limited urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Survey = Transition(label='Site Survey')
Impact_Study = Transition(label='Impact Study')
Modular_Design = Transition(label='Modular Design')
Crop_Mapping = Transition(label='Crop Mapping')
Sensor_Install = Transition(label='Sensor Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Energy_Audit = Transition(label='Energy Audit')
Waste_Plan = Transition(label='Waste Plan')
Permit_Filing = Transition(label='Permit Filing')
Supplier_Vetting = Transition(label='Supplier Vetting')
Community_Meet = Transition(label='Community Meet')
Tech_Integration = Transition(label='Tech Integration')
Trial_Harvest = Transition(label='Trial Harvest')
Market_Launch = Transition(label='Market Launch')
System_Tuning = Transition(label='System Tuning')
Maintenance_Check = Transition(label='Maintenance Check')

# Construct partial orders reflecting the process description and logical dependencies

# Phase 1: Site analysis and impact assessment
phase1 = StrictPartialOrder(nodes=[Site_Survey, Impact_Study])
phase1.order.add_edge(Site_Survey, Impact_Study)

# Phase 2: Modular design and crop planning
phase2 = StrictPartialOrder(nodes=[Modular_Design, Crop_Mapping])
phase2.order.add_edge(Modular_Design, Crop_Mapping)

# Phase 3: Installation setups (sensor, irrigation, nutrient)
setup_nodes = [Sensor_Install, Irrigation_Setup, Nutrient_Mix]
phase3 = StrictPartialOrder(nodes=setup_nodes)
# These three run concurrently, no order edges (concurrent)

# Phase 4: Energy audit and waste plan (can run concurrently with supplier vetting)
phase4 = StrictPartialOrder(nodes=[Energy_Audit, Waste_Plan])
phase4.order.add_edge(Energy_Audit, Waste_Plan)  # audit before waste plan

# Phase 5: Permit filing and supplier vetting (permit filing then supplier vetting)
phase5 = StrictPartialOrder(nodes=[Permit_Filing, Supplier_Vetting])
phase5.order.add_edge(Permit_Filing, Supplier_Vetting)

# Phase 6: Community meet and tech integration (can run concurrently)
phase6 = StrictPartialOrder(nodes=[Community_Meet, Tech_Integration])
# Concurrent: no edges

# Phase 7: Trial harvest, market launch, system tuning (trial harvest before market launch and tuning)
phase7 = StrictPartialOrder(nodes=[Trial_Harvest, Market_Launch, System_Tuning])
phase7.order.add_edge(Trial_Harvest, Market_Launch)
phase7.order.add_edge(Trial_Harvest, System_Tuning)

# Final phase: Maintenance check
maintenance = Maintenance_Check  # single activity

# Now define high-level ordering between phases according to logical dependencies:
# 1 -> 2 -> 3 -> (4 and 5 concurrent) -> 6 -> 7 -> maintenance

# Combine phase4 and phase5 in concurrent partial order
phase4_5 = StrictPartialOrder(nodes=[phase4, phase5])
phase4_5.order.add_edge(phase4, phase5)  # Energy audit+Waste plan before supplier vetting?

# Actually phase5 requires permit filing before supplier vetting; energy audit/waste plan separate.
# But based on description, they might be concurrent; so do not order phase4 and phase5.
phase4_5 = StrictPartialOrder(nodes=[phase4, phase5])
# no order edges: concurrent

# Now build the top-level partial order:

root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, phase4_5, phase6, phase7, maintenance]
)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4_5)
root.order.add_edge(phase4_5, phase6)
root.order.add_edge(phase6, phase7)
root.order.add_edge(phase7, maintenance)