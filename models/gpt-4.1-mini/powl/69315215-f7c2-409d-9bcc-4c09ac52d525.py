# Generated from: 69315215-f7c2-409d-9bcc-4c09ac52d525.json
# Description: This process outlines the establishment of a vertical farming system within an urban environment, integrating advanced hydroponics, AI-driven climate control, and renewable energy sources. The workflow begins with site assessment and structural analysis, followed by modular rack installation and sensor network deployment. Nutrient solution calibration and seed selection are conducted simultaneously to optimize growth cycles. Continuous monitoring and adaptive lighting adjustments ensure maximum yield. Waste recycling and water reclamation are embedded to maintain sustainability. The process concludes with harvest scheduling and distribution logistics, emphasizing traceability and minimal carbon footprint throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Assess = Transition(label='Site Assess')
Structure_Scan = Transition(label='Structure Scan')
Rack_Install = Transition(label='Rack Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Choose = Transition(label='Seed Choose')
Water_Cycle = Transition(label='Water Cycle')
Light_Adjust = Transition(label='Light Adjust')
Climate_Tune = Transition(label='Climate Tune')
Growth_Monitor = Transition(label='Growth Monitor')
Waste_Recycle = Transition(label='Waste Recycle')
Energy_Sync = Transition(label='Energy Sync')
Harvest_Plan = Transition(label='Harvest Plan')
Data_Log = Transition(label='Data Log')
Distribute_Crop = Transition(label='Distribute Crop')
Trace_Verify = Transition(label='Trace Verify')

# First phase: Site Assess and Structure Scan sequential
first_phase = StrictPartialOrder(nodes=[Site_Assess, Structure_Scan])
first_phase.order.add_edge(Site_Assess, Structure_Scan)

# Second phase: Rack Install and Sensor Deploy sequential after first phase
second_phase = StrictPartialOrder(nodes=[Rack_Install, Sensor_Deploy])
second_phase.order.add_edge(Rack_Install, Sensor_Deploy)

# Connect first_phase to second_phase
prep_phase = StrictPartialOrder(nodes=[first_phase, second_phase])
prep_phase.order.add_edge(first_phase, second_phase)

# Nutrient Mix and Seed Choose concurrent (simultaneous)
nutrient_seed = StrictPartialOrder(nodes=[Nutrient_Mix, Seed_Choose])

# Monitoring phase partial order with adaptive lighting and climate tuning around growth monitoring
monitoring_phase = StrictPartialOrder(nodes=[Growth_Monitor, Light_Adjust, Climate_Tune])
monitoring_phase.order.add_edge(Light_Adjust, Growth_Monitor)
monitoring_phase.order.add_edge(Climate_Tune, Growth_Monitor)

# Sustainability phase: Waste Recycle, Water Cycle, Energy Sync concurrent
sustainability_phase = StrictPartialOrder(nodes=[Waste_Recycle, Water_Cycle, Energy_Sync])

# Ending phase partial order: Harvest Plan followed by Data Log and Distribute Crop in parallel, then Trace Verify last
end_phase = StrictPartialOrder(nodes=[Harvest_Plan, Data_Log, Distribute_Crop, Trace_Verify])
end_phase.order.add_edge(Harvest_Plan, Data_Log)
end_phase.order.add_edge(Harvest_Plan, Distribute_Crop)
end_phase.order.add_edge(Data_Log, Trace_Verify)
end_phase.order.add_edge(Distribute_Crop, Trace_Verify)

# Assemble the entire workflow partial order
root = StrictPartialOrder(
    nodes=[prep_phase, nutrient_seed, monitoring_phase, sustainability_phase, end_phase]
)

# Edges to enforce partial order for entire process:
# prep_phase -> nutrient_seed
root.order.add_edge(prep_phase, nutrient_seed)
# nutrient_seed -> monitoring_phase
root.order.add_edge(nutrient_seed, monitoring_phase)
# monitoring_phase -> sustainability_phase
root.order.add_edge(monitoring_phase, sustainability_phase)
# sustainability_phase -> end_phase
root.order.add_edge(sustainability_phase, end_phase)