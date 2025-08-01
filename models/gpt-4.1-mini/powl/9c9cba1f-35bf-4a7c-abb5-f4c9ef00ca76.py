# Generated from: 9c9cba1f-35bf-4a7c-abb5-f4c9ef00ca76.json
# Description: This process outlines the establishment of an urban vertical farming system that integrates hydroponics, renewable energy, and AI-driven environmental controls to optimize crop yield in limited city spaces. It involves site analysis, modular assembly, nutrient calibration, system integration, continuous monitoring, predictive maintenance, and adaptive harvesting schedules to ensure sustainable, high-efficiency food production within urban environments. The process also includes community engagement and regulatory compliance to align with local policies and promote urban agricultural awareness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Module_Fabrication = Transition(label='Module Fabrication')
Hydro_Setup = Transition(label='Hydro Setup')
Energy_Install = Transition(label='Energy Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
AI_Configuration = Transition(label='AI Configuration')
Nutrient_Mix = Transition(label='Nutrient Mix')
Water_Testing = Transition(label='Water Testing')
Lighting_Adjust = Transition(label='Lighting Adjust')
Crop_Planting = Transition(label='Crop Planting')
Growth_Monitor = Transition(label='Growth Monitor')
Data_Analysis = Transition(label='Data Analysis')
Maintenance_Check = Transition(label='Maintenance Check')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Manage = Transition(label='Waste Manage')
Community_Meet = Transition(label='Community Meet')
Compliance_Audit = Transition(label='Compliance Audit')

# Stage 1: Initial site survey and design (sequential)
initial_seq = StrictPartialOrder(nodes=[Site_Survey, Design_Layout])
initial_seq.order.add_edge(Site_Survey, Design_Layout)

# Stage 2: Modular assembly (3 tasks can be done in parallel)
mod_assembly = StrictPartialOrder(nodes=[Module_Fabrication, Hydro_Setup, Energy_Install])
# No order edges, concurrent

# Stage 3: System integration (Sensor deploy then AI config)
sys_integration = StrictPartialOrder(nodes=[Sensor_Deploy, AI_Configuration])
sys_integration.order.add_edge(Sensor_Deploy, AI_Configuration)

# Stage 4: Nutrient and environment adjustment (sequential)
nutrient_env = StrictPartialOrder(nodes=[Nutrient_Mix, Water_Testing, Lighting_Adjust])
nutrient_env.order.add_edge(Nutrient_Mix, Water_Testing)
nutrient_env.order.add_edge(Water_Testing, Lighting_Adjust)

# Stage 5: Crop planting (single)
crop_plant = Crop_Planting

# Stage 6: Growth monitoring and data analysis loop
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Growth_Monitor,  # A: monitor
        Data_Analysis    # B: analyze (then back to monitor)
    ]
)

# Stage 7: Maintenance checks (periodic)
maintenance = Maintenance_Check

# Stage 8: Harvest planning and waste management (sequence)
harvest_waste = StrictPartialOrder(nodes=[Harvest_Plan, Waste_Manage])
harvest_waste.order.add_edge(Harvest_Plan, Waste_Manage)

# Stage 9: Community engagement & compliance (can happen concurrently with harvest & waste)
community_compliance = StrictPartialOrder(nodes=[Community_Meet, Compliance_Audit])
# No order edges, concurrent

# Combine harvest & waste with community & compliance in partial order to run concurrently
final_stage = StrictPartialOrder(
    nodes=[harvest_waste, community_compliance]
)
# no order edges -> they run concurrently

# Combine monitoring loop with maintenance in partial order - assume maintenance runs after some monitoring (seq)
monitor_maint = StrictPartialOrder(nodes=[monitor_loop, maintenance])
monitor_maint.order.add_edge(monitor_loop, maintenance)

# Combine system integration and nutrient env adjustments (seq)
sys_nutrient = StrictPartialOrder(nodes=[sys_integration, nutrient_env])
sys_nutrient.order.add_edge(sys_integration, nutrient_env)

# Combine modular assembly then system integration + nutrient env (seq)
mod_sys_nutrient = StrictPartialOrder(nodes=[mod_assembly, sys_nutrient])
mod_sys_nutrient.order.add_edge(mod_assembly, sys_nutrient)

# Combine planting with monitor+maint (seq)
plant_monitor_maint = StrictPartialOrder(nodes=[crop_plant, monitor_maint])
plant_monitor_maint.order.add_edge(crop_plant, monitor_maint)

# Combine above sequences in order:
# initial_seq -> mod_sys_nutrient -> plant_monitor_maint -> final_stage
root = StrictPartialOrder(
    nodes=[initial_seq, mod_sys_nutrient, plant_monitor_maint, final_stage]
)
root.order.add_edge(initial_seq, mod_sys_nutrient)
root.order.add_edge(mod_sys_nutrient, plant_monitor_maint)
root.order.add_edge(plant_monitor_maint, final_stage)