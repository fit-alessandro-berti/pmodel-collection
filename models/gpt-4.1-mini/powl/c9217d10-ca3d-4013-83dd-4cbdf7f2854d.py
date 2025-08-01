# Generated from: c9217d10-ca3d-4013-83dd-4cbdf7f2854d.json
# Description: This process involves the complex orchestration of establishing an urban vertical farm within a repurposed industrial facility. It encompasses site analysis, environmental control system integration, crop selection based on microclimate data, automated nutrient delivery setup, and ongoing monitoring through IoT sensors. The process further includes workforce training for specialized hydroponic techniques, compliance with local agricultural regulations, marketing strategy alignment for direct-to-consumer sales, and continuous optimization of yield through data analytics. Each step demands coordination across engineering, agricultural science, logistics, and business development teams to ensure sustainable and profitable urban food production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Climate_Study = Transition(label='Climate Study')
Design_Layout = Transition(label='Design Layout')
System_Install = Transition(label='System Install')
Crop_Select = Transition(label='Crop Select')
Nutrient_Plan = Transition(label='Nutrient Plan')
Sensor_Setup = Transition(label='Sensor Setup')
Automation_Test = Transition(label='Automation Test')
Staff_Train = Transition(label='Staff Train')
Compliance_Check = Transition(label='Compliance Check')
Marketing_Sync = Transition(label='Marketing Sync')
Data_Monitor = Transition(label='Data Monitor')
Yield_Analyze = Transition(label='Yield Analyze')
Supply_Chain = Transition(label='Supply Chain')
Customer_Engage = Transition(label='Customer Engage')

# Partial order 1 (Engineering & Science orchestration):
# Site Survey --> Climate Study --> Design Layout --> System Install
# --> Crop Select --> Nutrient Plan --> Sensor Setup --> Automation Test
eng_sci_PO = StrictPartialOrder(
    nodes=[
        Site_Survey, Climate_Study, Design_Layout, System_Install,
        Crop_Select, Nutrient_Plan, Sensor_Setup, Automation_Test
    ]
)
eng_sci_PO.order.add_edge(Site_Survey, Climate_Study)
eng_sci_PO.order.add_edge(Climate_Study, Design_Layout)
eng_sci_PO.order.add_edge(Design_Layout, System_Install)
eng_sci_PO.order.add_edge(System_Install, Crop_Select)
eng_sci_PO.order.add_edge(Crop_Select, Nutrient_Plan)
eng_sci_PO.order.add_edge(Nutrient_Plan, Sensor_Setup)
eng_sci_PO.order.add_edge(Sensor_Setup, Automation_Test)

# Partial order 2 (Workforce training & compliance):
# Staff Train --> Compliance Check
train_compl_PO = StrictPartialOrder(
    nodes=[Staff_Train, Compliance_Check]
)
train_compl_PO.order.add_edge(Staff_Train, Compliance_Check)

# Partial order 3 (Marketing & Business orchestration):
# Marketing Sync --> Supply Chain --> Customer Engage
mkt_supply_PO = StrictPartialOrder(
    nodes=[Marketing_Sync, Supply_Chain, Customer_Engage]
)
mkt_supply_PO.order.add_edge(Marketing_Sync, Supply_Chain)
mkt_supply_PO.order.add_edge(Supply_Chain, Customer_Engage)

# Partial order 4 (Ongoing monitoring & optimization):
# Data Monitor --> Yield Analyze (looped continuously)
# Model loop: * (Data Monitor, Yield Analyze)
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Data_Monitor, Yield_Analyze]
)

# Combine all main parts concurrently (partial order without edges between groups)
root = StrictPartialOrder(
    nodes=[eng_sci_PO, train_compl_PO, mkt_supply_PO, monitor_loop]
)
# No edges connecting these four nodes: concurrent orchestration across teams