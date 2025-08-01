# Generated from: b2e25c2a-7584-4ceb-a58a-8ecc92a0c589.json
# Description: This process outlines the complex setup of an urban vertical farming system designed to optimize limited city space for high-yield crop production. It involves site analysis, modular structure assembly, environmental control calibration, nutrient solution preparation, and integration of IoT monitoring devices. Specialized activities include biosecurity protocol implementation to prevent contamination, adaptive lighting adjustment based on crop growth stages, and waste recycling for sustainability. The process concludes with trial harvests and data analysis to refine system parameters for commercial scalability and continuous improvement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Structure_Assemble = Transition(label='Structure Assemble')

Lighting_Setup = Transition(label='Lighting Setup')
Biosecurity_Check = Transition(label='Biosecurity Check')
Climate_Control = Transition(label='Climate Control')

Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Install = Transition(label='Sensor Install')

Irrigation_Test = Transition(label='Irrigation Test')
Seed_Planting = Transition(label='Seed Planting')

# Loop: Growth Monitor then choice (Waste Recycling or Data Logging) then System Tuning
Growth_Monitor = Transition(label='Growth Monitor')
Waste_Recycling = Transition(label='Waste Recycling')
Data_Logging = Transition(label='Data Logging')
System_Tuning = Transition(label='System Tuning')

# Trial Harvest then Safety Audit
Trial_Harvest = Transition(label='Trial Harvest')
Safety_Audit = Transition(label='Safety Audit')

# The adaptive lighting adjustment based on crop growth stages is presumably modeled in the loop,
# so we put Biosecurity_Check as prerequisite to lighting
# Order of initial setup: Site Survey -> Design Layout -> Structure Assemble

# Initial setup partial order
initial_setup = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, Structure_Assemble])
initial_setup.order.add_edge(Site_Survey, Design_Layout)
initial_setup.order.add_edge(Design_Layout, Structure_Assemble)

# Environment and biosecurity setup after structure assembled, partial order concurrent inside
env_setup = StrictPartialOrder(nodes=[Lighting_Setup, Biosecurity_Check, Climate_Control])
env_setup.order.add_edge(Biosecurity_Check, Lighting_Setup)  # Biosecurity precedes lighting adaptive adjustment

# Nutrient and sensor preparation after environment setup
nutrient_sensor = StrictPartialOrder(nodes=[Nutrient_Mix, Sensor_Install])
# They can be in parallel, no edges

# Irrigation Test and Seed Planting (after nutrient and sensor)
irrigation_seed = StrictPartialOrder(nodes=[Irrigation_Test, Seed_Planting])
irrigation_seed.order.add_edge(Irrigation_Test, Seed_Planting)

# Growth monitoring loop:
# * (Growth_Monitor, X(Waste_Recycling, Data_Logging))
monitor_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[Waste_Recycling, Data_Logging]
)
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Growth_Monitor, monitor_choice]
)

# After the loop, System Tuning
# Then Trial Harvest -> Safety Audit

final_sequence = StrictPartialOrder(
    nodes=[System_Tuning, Trial_Harvest, Safety_Audit]
)
final_sequence.order.add_edge(System_Tuning, Trial_Harvest)
final_sequence.order.add_edge(Trial_Harvest, Safety_Audit)

# Compose whole process partial order by ordering parts sequentially:
# initial_setup -> env_setup -> nutrient_sensor -> irrigation_seed -> growth_loop -> final_sequence

root = StrictPartialOrder(
    nodes=[
        initial_setup,
        env_setup,
        nutrient_sensor,
        irrigation_seed,
        growth_loop,
        final_sequence,
    ]
)
root.order.add_edge(initial_setup, env_setup)
root.order.add_edge(env_setup, nutrient_sensor)
root.order.add_edge(nutrient_sensor, irrigation_seed)
root.order.add_edge(irrigation_seed, growth_loop)
root.order.add_edge(growth_loop, final_sequence)