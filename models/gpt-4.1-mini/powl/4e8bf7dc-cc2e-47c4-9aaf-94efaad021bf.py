# Generated from: 4e8bf7dc-cc2e-47c4-9aaf-94efaad021bf.json
# Description: This process outlines the intricate steps required to establish a fully operational urban vertical farm within a repurposed industrial building. It begins with site analysis and environmental impact assessment, followed by modular structure design and customized hydroponics system installation. The workflow includes controlled environment calibration, nutrient solution formulation, and integrated pest management planning. Subsequent activities involve AI-driven crop scheduling, staff training on automated systems, and compliance verification with local agricultural regulations. The final phases focus on establishing distribution logistics, continuous performance monitoring, and iterative optimization to maximize yield while minimizing resource consumption and environmental footprint in an urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Site_Analysis = Transition(label='Site Analysis')
Impact_Review = Transition(label='Impact Review')
Structure_Design = Transition(label='Structure Design')
Hydroponics_Install = Transition(label='Hydroponics Install')
Env_Calibration = Transition(label='Env Calibration')
Nutrient_Mixing = Transition(label='Nutrient Mixing')
Pest_Planning = Transition(label='Pest Planning')
Crop_Scheduling = Transition(label='Crop Scheduling')
Staff_Training = Transition(label='Staff Training')
Compliance_Check = Transition(label='Compliance Check')
Logistics_Setup = Transition(label='Logistics Setup')
Performance_Monitor = Transition(label='Performance Monitor')
Yield_Optimization = Transition(label='Yield Optimization')
Waste_Management = Transition(label='Waste Management')
Energy_Audit = Transition(label='Energy Audit')

# Construct the main partial order based on the described sequence

# Phase 1: Site analysis and impact review (sequential)
phase1 = StrictPartialOrder(nodes=[Site_Analysis, Impact_Review])
phase1.order.add_edge(Site_Analysis, Impact_Review)

# Phase 2: Modular structure design and hydroponics install (sequential)
phase2 = StrictPartialOrder(nodes=[Structure_Design, Hydroponics_Install])
phase2.order.add_edge(Structure_Design, Hydroponics_Install)

# Phase 3: Controlled environment calibration, nutrient mixing, pest planning (partial order)
phase3 = StrictPartialOrder(nodes=[Env_Calibration, Nutrient_Mixing, Pest_Planning])
# They seem consecutive, so link Env_Calibration -> Nutrient_Mixing -> Pest_Planning
phase3.order.add_edge(Env_Calibration, Nutrient_Mixing)
phase3.order.add_edge(Nutrient_Mixing, Pest_Planning)

# Phase 4: AI-driven crop scheduling, staff training, compliance check (sequential)
phase4 = StrictPartialOrder(nodes=[Crop_Scheduling, Staff_Training, Compliance_Check])
phase4.order.add_edge(Crop_Scheduling, Staff_Training)
phase4.order.add_edge(Staff_Training, Compliance_Check)

# Phase 5: Final phases focused on logistics, monitoring, optimization (some concurrency)
final_phase = StrictPartialOrder(nodes=[Logistics_Setup, Performance_Monitor, Yield_Optimization, Waste_Management, Energy_Audit])
# Logistics setup before performance monitoring and yield optimization
final_phase.order.add_edge(Logistics_Setup, Performance_Monitor)
final_phase.order.add_edge(Logistics_Setup, Yield_Optimization)
# Performance monitor and yield optimization happen concurrently (no order)
# Waste management and energy audit happen after yield optimization and performance monitor
final_phase.order.add_edge(Performance_Monitor, Waste_Management)
final_phase.order.add_edge(Yield_Optimization, Waste_Management)
final_phase.order.add_edge(Performance_Monitor, Energy_Audit)
final_phase.order.add_edge(Yield_Optimization, Energy_Audit)

# Now combine all phases sequentially:
# phase1 -> phase2 -> phase3 -> phase4 -> final_phase

root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, phase4, final_phase]
)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, final_phase)