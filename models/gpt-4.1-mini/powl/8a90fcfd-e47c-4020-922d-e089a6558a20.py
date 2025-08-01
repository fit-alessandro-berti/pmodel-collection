# Generated from: 8a90fcfd-e47c-4020-922d-e089a6558a20.json
# Description: This process outlines the setup of an urban vertical farming system within a constrained city environment. It involves selecting suitable building structures, integrating hydroponic and aeroponic technologies, optimizing energy consumption with renewable sources, and establishing automated monitoring for nutrient delivery and climate control. The process also includes compliance with local zoning laws, community engagement for sustainable practices, and iterative testing of crop yields under varying light and humidity conditions to maximize productivity while minimizing ecological footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Structure_Assess = Transition(label='Structure Assess')
Tech_Select = Transition(label='Tech Select')
Energy_Plan = Transition(label='Energy Plan')
Legal_Review = Transition(label='Legal Review')
Permit_Acquire = Transition(label='Permit Acquire')
System_Design = Transition(label='System Design')
Material_Order = Transition(label='Material Order')
Install_Framework = Transition(label='Install Framework')
Irrigation_Setup = Transition(label='Irrigation Setup')
Climate_Configure = Transition(label='Climate Configure')
Sensor_Deploy = Transition(label='Sensor Deploy')
Software_Integrate = Transition(label='Software Integrate')
Trial_Cultivation = Transition(label='Trial Cultivation')
Yield_Monitor = Transition(label='Yield Monitor')
Community_Meet = Transition(label='Community Meet')
Data_Analyze = Transition(label='Data Analyze')
Process_Adjust = Transition(label='Process Adjust')

# Model building and review:
# - Site Survey --> Structure Assess
# - Structure Assess --> Tech Select
# - Tech Select --> Energy Plan
# - Energy Plan --> (Legal Review XOR skip)
# - Legal Review --> Permit Acquire
# - Permit Acquire must happen if Legal Review was done
# (Permit Acquire depends on Legal Review)
# So model an XOR: choice to do Legal Review & Permit Acquire or skip both
legal_path = StrictPartialOrder(nodes=[Legal_Review, Permit_Acquire])
legal_path.order.add_edge(Legal_Review, Permit_Acquire)
legal_xor = OperatorPOWL(operator=Operator.XOR, children=[legal_path, SilentTransition()])

# After legal clearance or skipping it, proceed with system design etc.
# System Design follows tech select and legal permit chain
# Because legal_xor is after Energy_Plan, link Energy_Plan -> legal_xor
# Then legal_xor -> System Design

# Define system design sequence:
# System Design -> Material Order -> Install Framework -> Irrigation Setup -> Climate Configure
# -> Sensor Deploy -> Software Integrate
system_build_po = StrictPartialOrder(nodes=[
    System_Design, Material_Order, Install_Framework, Irrigation_Setup,
    Climate_Configure, Sensor_Deploy, Software_Integrate
])
system_build_po.order.add_edge(System_Design, Material_Order)
system_build_po.order.add_edge(Material_Order, Install_Framework)
system_build_po.order.add_edge(Install_Framework, Irrigation_Setup)
system_build_po.order.add_edge(Irrigation_Setup, Climate_Configure)
system_build_po.order.add_edge(Climate_Configure, Sensor_Deploy)
system_build_po.order.add_edge(Sensor_Deploy, Software_Integrate)

# Monitoring and community engagement run concurrently starting after system is integrated
# Activities: Trial Cultivation, Yield Monitor, Community Meet, Data Analyze, Process Adjust
# Trial Cultivation -> Yield Monitor -> Data Analyze -> Process Adjust (strict order)
# Community Meet runs concurrently with Trial Cultivation

trial_and_monitor_po = StrictPartialOrder(nodes=[Trial_Cultivation, Yield_Monitor, Data_Analyze, Process_Adjust, Community_Meet])
trial_and_monitor_po.order.add_edge(Trial_Cultivation, Yield_Monitor)
trial_and_monitor_po.order.add_edge(Yield_Monitor, Data_Analyze)
trial_and_monitor_po.order.add_edge(Data_Analyze, Process_Adjust)
# Community_Meet no edges connects it -> concurrent with all

# Now build the upper partial order integrating everything

root = StrictPartialOrder(nodes=[
    Site_Survey,
    Structure_Assess,
    Tech_Select,
    Energy_Plan,
    legal_xor,
    system_build_po,
    trial_and_monitor_po
])

# Add order dependencies:

root.order.add_edge(Site_Survey, Structure_Assess)
root.order.add_edge(Structure_Assess, Tech_Select)
root.order.add_edge(Tech_Select, Energy_Plan)
root.order.add_edge(Energy_Plan, legal_xor)
root.order.add_edge(legal_xor, system_build_po)
root.order.add_edge(system_build_po, trial_and_monitor_po)