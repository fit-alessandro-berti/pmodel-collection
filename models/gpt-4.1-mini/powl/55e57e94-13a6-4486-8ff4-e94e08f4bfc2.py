# Generated from: 55e57e94-13a6-4486-8ff4-e94e08f4bfc2.json
# Description: This process outlines the steps involved in establishing an urban vertical farming system within a repurposed warehouse. It encompasses site evaluation, structural modification, installation of hydroponic systems, climate control setup, nutrient cycling design, crop selection, automation integration, labor training, and ongoing maintenance protocols. The process aims to optimize space utilization, maximize yield per square meter, and ensure sustainable resource management while meeting urban agricultural demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Structure_Audit = Transition(label='Structure Audit')
Layout_Design = Transition(label='Layout Design')
Hydroponic_Install = Transition(label='Hydroponic Install')
Climate_Setup = Transition(label='Climate Setup')
Lighting_Config = Transition(label='Lighting Config')
Nutrient_Plan = Transition(label='Nutrient Plan')
Crop_Selection = Transition(label='Crop Selection')
Automation_Install = Transition(label='Automation Install')
Water_Recycling = Transition(label='Water Recycling')
Pest_Control = Transition(label='Pest Control')
Staff_Training = Transition(label='Staff Training')
Trial_Cultivation = Transition(label='Trial Cultivation')
System_Calibration = Transition(label='System Calibration')
Yield_Monitoring = Transition(label='Yield Monitoring')
Maintenance_Check = Transition(label='Maintenance Check')
Waste_Disposal = Transition(label='Waste Disposal')

# Phase 1: Site evaluation and structural prep
phase1 = StrictPartialOrder(nodes=[Site_Survey, Structure_Audit])
phase1.order.add_edge(Site_Survey, Structure_Audit)

# Phase 2: Layout and system install - partial order
phase2_nodes = [Layout_Design, Hydroponic_Install, Climate_Setup, Lighting_Config]
phase2 = StrictPartialOrder(nodes=phase2_nodes)
phase2.order.add_edge(Layout_Design, Hydroponic_Install)  # layout before install
phase2.order.add_edge(Layout_Design, Climate_Setup)
phase2.order.add_edge(Layout_Design, Lighting_Config)
# Hydroponic, Climate, and Lighting installs can run in parallel after Layout Design

# Phase 3: Nutrient plan and crop selection, then automation install
phase3 = StrictPartialOrder(nodes=[Nutrient_Plan, Crop_Selection, Automation_Install])
phase3.order.add_edge(Nutrient_Plan, Automation_Install)
phase3.order.add_edge(Crop_Selection, Automation_Install)

# Phase 4: Water recycling and pest control (concurrent)
phase4 = StrictPartialOrder(nodes=[Water_Recycling, Pest_Control])

# Phase 5: Staff training before trial cultivation
phase5 = StrictPartialOrder(nodes=[Staff_Training, Trial_Cultivation])
phase5.order.add_edge(Staff_Training, Trial_Cultivation)

# Phase 6: System calibration before yield monitoring
phase6 = StrictPartialOrder(nodes=[System_Calibration, Yield_Monitoring])
phase6.order.add_edge(System_Calibration, Yield_Monitoring)

# Phase 7: Maintenance check followed by waste disposal
phase7 = StrictPartialOrder(nodes=[Maintenance_Check, Waste_Disposal])
phase7.order.add_edge(Maintenance_Check, Waste_Disposal)

# Combine phases 4 and 5 into parallel (Water/Pest controls concurrent with Training)
phase45 = StrictPartialOrder(nodes=[phase4, phase5])

# Combine all phases with strict order:
# Phase 1 -> Phase 2 -> Phase 3 -> Phase 4&5 -> Phase 6 -> Phase 7
root = StrictPartialOrder(nodes=[phase1, phase2, phase3, phase45, phase6, phase7])
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase45)
root.order.add_edge(phase45, phase6)
root.order.add_edge(phase6, phase7)