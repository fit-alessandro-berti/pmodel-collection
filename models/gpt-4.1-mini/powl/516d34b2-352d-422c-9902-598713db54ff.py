# Generated from: 516d34b2-352d-422c-9902-598713db54ff.json
# Description: This process outlines the deployment of a custom drone fleet for environmental monitoring in remote areas. It involves initial site analysis, drone customization to adapt to varying weather conditions, regulatory compliance checks with local authorities, pilot training on specialized equipment, iterative testing of flight patterns, real-time data integration with satellite feeds, maintenance scheduling based on predictive analytics, emergency response protocols setup, community engagement for awareness, and final deployment with continuous performance monitoring and adaptive mission updates. The process ensures optimized data collection while maintaining safety and regulatory standards in complex terrains.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Drone_Customization = Transition(label='Drone Customization')
Regulatory_Check = Transition(label='Regulatory Check')
Pilot_Training = Transition(label='Pilot Training')
Flight_Testing = Transition(label='Flight Testing')
Data_Integration = Transition(label='Data Integration')
Maintenance_Plan = Transition(label='Maintenance Plan')
Emergency_Setup = Transition(label='Emergency Setup')
Community_Outreach = Transition(label='Community Outreach')
Mission_Planning = Transition(label='Mission Planning')
Performance_Review = Transition(label='Performance Review')
Pattern_Adjustment = Transition(label='Pattern Adjustment')
Battery_Swap = Transition(label='Battery Swap')
Signal_Calibration = Transition(label='Signal Calibration')
Report_Generation = Transition(label='Report Generation')

# Loop for iterative Flight Testing and Pattern Adjustment with Battery Swap and Signal Calibration as part of the testing cycle
# Represent the inner loop body as partial order of Battery Swap and Signal Calibration concurrent (no order)
battery_signal = StrictPartialOrder(nodes=[Battery_Swap, Signal_Calibration])

# Flight testing cycle partial order: battery_signal --> Pattern_Adjustment (Pattern_Adjustment after battery_signal)
testing_cycle = StrictPartialOrder(nodes=[battery_signal, Pattern_Adjustment])
testing_cycle.order.add_edge(battery_signal, Pattern_Adjustment)

# Loop structure: body = Flight_Testing followed by testing_cycle
# Flight_Testing --> testing_cycle nodes

# Compose nodes for loop body sequence: Flight_Testing then testing_cycle (partial order)
ft_cycle_nodes = [Flight_Testing, testing_cycle]
ft_cycle_po = StrictPartialOrder(nodes=ft_cycle_nodes)
ft_cycle_po.order.add_edge(Flight_Testing, testing_cycle)

# Define the loop: 
# Loop body A = Flight_Testing + testing_cycle (ft_cycle_po)
# Loop redo B = battery_signal (allow repairing) - but semantically battery_signal and Pattern_Adjustment are repeated inside testing_cycle
# For simplicity, consider the loop on ft_cycle_po and the redo is empty loop, use silent transition
skip = SilentTransition()
loop_testing = OperatorPOWL(operator=Operator.LOOP, children=[ft_cycle_po, skip])

# Core flow partial order:
# Site Analysis --> Drone Customization --> Regulatory Check --> Pilot Training --> loop_testing --> Data Integration --> Maintenance Plan --> Emergency Setup --> Community Outreach --> Mission Planning --> Performance Review --> Report Generation

nodes = [
    Site_Analysis,
    Drone_Customization,
    Regulatory_Check,
    Pilot_Training,
    loop_testing,
    Data_Integration,
    Maintenance_Plan,
    Emergency_Setup,
    Community_Outreach,
    Mission_Planning,
    Performance_Review,
    Report_Generation
]

root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(Site_Analysis, Drone_Customization)
root.order.add_edge(Drone_Customization, Regulatory_Check)
root.order.add_edge(Regulatory_Check, Pilot_Training)
root.order.add_edge(Pilot_Training, loop_testing)
root.order.add_edge(loop_testing, Data_Integration)
root.order.add_edge(Data_Integration, Maintenance_Plan)
root.order.add_edge(Maintenance_Plan, Emergency_Setup)
root.order.add_edge(Emergency_Setup, Community_Outreach)
root.order.add_edge(Community_Outreach, Mission_Planning)
root.order.add_edge(Mission_Planning, Performance_Review)
root.order.add_edge(Performance_Review, Report_Generation)