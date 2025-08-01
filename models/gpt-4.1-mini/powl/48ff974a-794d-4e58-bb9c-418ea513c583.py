# Generated from: 48ff974a-794d-4e58-bb9c-418ea513c583.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farm specializing in leafy greens and herbs. It begins with seed selection and preparation, followed by nutrient solution formulation and environmental calibration within stacked hydroponic layers. Continuous monitoring of plant health and growth metrics is conducted using IoT sensors and AI-driven analytics. Periodic pruning and pest control are integrated seamlessly to maintain optimal yield. Harvesting involves automated robotic arms to minimize damage, while post-harvest handling includes quality grading, packaging, and cold chain logistics. The process concludes with waste recycling and data feedback loops to improve subsequent cycles, ensuring sustainability and efficiency in an urban agriculture context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Seed_Prep = Transition(label='Seed Prep')
Nutrient_Mix = Transition(label='Nutrient Mix')
Env_Calibration = Transition(label='Env Calibration')
Planting_Setup = Transition(label='Planting Setup')

Growth_Monitor = Transition(label='Growth Monitor')
Health_Check = Transition(label='Health Check')
Pest_Control = Transition(label='Pest Control')
Pruning_Task = Transition(label='Pruning Task')

Automated_Harvest = Transition(label='Automated Harvest')
Quality_Grade = Transition(label='Quality Grade')
Packaging_Line = Transition(label='Packaging Line')
Cold_Storage = Transition(label='Cold Storage')

Waste_Recycle = Transition(label='Waste Recycle')
Data_Analysis = Transition(label='Data Analysis')
Cycle_Review = Transition(label='Cycle Review')

# First partial order (seed prep to planting setup)
initial_phase = StrictPartialOrder(nodes=[Seed_Prep, Nutrient_Mix, Env_Calibration, Planting_Setup])
initial_phase.order.add_edge(Seed_Prep, Nutrient_Mix)
initial_phase.order.add_edge(Nutrient_Mix, Env_Calibration)
initial_phase.order.add_edge(Env_Calibration, Planting_Setup)

# Loop body: during growing period, monitor/grow + pest control/pruning intertwined
# Model the maintenance tasks as choice followed by re-monitoring the growth

# Maintenance choice: Pest Control or Pruning Task
maintenance_choice = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, Pruning_Task])

# Loop: Growth monitoring + Health Check then choice(maintenance) and back to growth monitoring again or exit
growth_health = StrictPartialOrder(nodes=[Growth_Monitor, Health_Check])
growth_health.order.add_edge(Growth_Monitor, Health_Check)

loop_body = StrictPartialOrder(nodes=[maintenance_choice, growth_health])
loop_body.order.add_edge(maintenance_choice, growth_health)

growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_health, maintenance_choice])

# Harvest and post-harvest process partial order
harvest_phase = StrictPartialOrder(nodes=[Automated_Harvest, Quality_Grade, Packaging_Line, Cold_Storage])
harvest_phase.order.add_edge(Automated_Harvest, Quality_Grade)
harvest_phase.order.add_edge(Quality_Grade, Packaging_Line)
harvest_phase.order.add_edge(Packaging_Line, Cold_Storage)

# Final phase: waste recycle and data feedback
final_phase = StrictPartialOrder(nodes=[Waste_Recycle, Data_Analysis, Cycle_Review])
final_phase.order.add_edge(Waste_Recycle, Data_Analysis)
final_phase.order.add_edge(Data_Analysis, Cycle_Review)

# Compose the full process partial order with all phases in sequence
root = StrictPartialOrder(
    nodes=[initial_phase, growth_loop, harvest_phase, final_phase]
)
root.order.add_edge(initial_phase, growth_loop)
root.order.add_edge(growth_loop, harvest_phase)
root.order.add_edge(harvest_phase, final_phase)