# Generated from: 31290ce0-bfbf-4d50-89e3-fb8e47d955fc.json
# Description: This process outlines the complex steps involved in establishing a fully operational urban vertical farm within a constrained city environment. Starting with site assessment and zoning approval, it includes innovative modular design, integrating IoT-based climate control, and hydroponic system installation. The workflow addresses energy optimization through renewable sources, advanced nutrient delivery calibration, and pest management without chemicals. The process also incorporates community engagement for educational tours, continuous data monitoring, and adaptive crop scheduling based on market trends. Final stages involve certification for organic produce and launching a subscription-based delivery service, ensuring sustainability and profitability in urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Assess = Transition(label='Site Assess')
Zoning_Approve = Transition(label='Zoning Approve')
Modular_Design = Transition(label='Modular Design')
IoT_Setup = Transition(label='IoT Setup')
Climate_Config = Transition(label='Climate Config')
Hydroponic_Install = Transition(label='Hydroponic Install')
Energy_Audit = Transition(label='Energy Audit')
Renewables_Integrate = Transition(label='Renewables Integrate')
Nutrient_Calibrate = Transition(label='Nutrient Calibrate')
Pest_Control = Transition(label='Pest Control')
Community_Engage = Transition(label='Community Engage')
Data_Monitor = Transition(label='Data Monitor')
Crop_Schedule = Transition(label='Crop Schedule')
Organic_Certify = Transition(label='Organic Certify')
Launch_Delivery = Transition(label='Launch Delivery')

# We model the process roughly as follows:
# Sequential start: Site Assess -> Zoning Approve
# Then Modular Design
# Then a partial order of IoT and Hydroponic Install with Climate Config ordered after IoT Setup
# Then Energy Audit -> Renewables Integrate
# Nutrient Calibrate and Pest Control concurrent
# Community Engage concurrent with a loop of (Data Monitor and Crop Schedule)
# Finally Organic Certify -> Launch Delivery

# Construct partial order for IoT and Hydroponic Install with Climate Config depending on IoT
iot_hydro_po = StrictPartialOrder(nodes=[IoT_Setup, Climate_Config, Hydroponic_Install])
iot_hydro_po.order.add_edge(IoT_Setup, Climate_Config)  # Climate Config depends on IoT Setup

# Nutrient Calibrate and Pest Control concurrent
nutr_pest_po = StrictPartialOrder(nodes=[Nutrient_Calibrate, Pest_Control])

# Loop node: monitor and schedule repeatedly until decided to exit
monitor_schedule_seq = StrictPartialOrder(nodes=[Data_Monitor, Crop_Schedule])
loop_monitor_schedule = OperatorPOWL(operator=Operator.LOOP, children=[monitor_schedule_seq, SilentTransition()])

# Community Engage concurrent with the loop of monitoring and scheduling
community_monitor_po = StrictPartialOrder(nodes=[Community_Engage, loop_monitor_schedule])

# Then Organic Certify and Launch Delivery sequential
final_po = StrictPartialOrder(nodes=[Organic_Certify, Launch_Delivery])
final_po.order.add_edge(Organic_Certify, Launch_Delivery)

# Compose main PO stepwise

# 1) Start sequence: Site Assess -> Zoning Approve -> Modular Design
start_seq = StrictPartialOrder(nodes=[Site_Assess, Zoning_Approve, Modular_Design])
start_seq.order.add_edge(Site_Assess, Zoning_Approve)
start_seq.order.add_edge(Zoning_Approve, Modular_Design)

# 2) After Modular Design: iot_hydro_po partial order
# We create a PO connecting Modular Design to iot_hydro_po
step2 = StrictPartialOrder(nodes=[start_seq, iot_hydro_po])
step2.order.add_edge(start_seq, iot_hydro_po)

# 3) Energy Audit and Renewables Integrate sequential
energy_seq = StrictPartialOrder(nodes=[Energy_Audit, Renewables_Integrate])
energy_seq.order.add_edge(Energy_Audit, Renewables_Integrate)

# Combine step2 with energy_seq sequentially
step3 = StrictPartialOrder(nodes=[step2, energy_seq])
step3.order.add_edge(step2, energy_seq)

# 4) Nutrient Calibrate and Pest Control concurrent
# Add to the flow after energy_seq
step4 = StrictPartialOrder(nodes=[step3, nutr_pest_po])
step4.order.add_edge(step3, nutr_pest_po)

# 5) Then community_monitor_po concurrent after step4
step5 = StrictPartialOrder(nodes=[step4, community_monitor_po])
step5.order.add_edge(step4, community_monitor_po)

# 6) Finally add final_po sequentially
root = StrictPartialOrder(nodes=[step5, final_po])
root.order.add_edge(step5, final_po)