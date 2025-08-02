# Generated from: 4e108019-8ece-46f6-91df-f2625b676313.json
# Description: This process involves dynamically adjusting supply chain operations based on real-time data inputs from multiple sources including weather forecasts, geopolitical events, and market demand fluctuations. It coordinates procurement, production scheduling, logistics, and inventory management by continuously evaluating risk factors and optimizing resource allocation. The process employs predictive analytics to anticipate disruptions and initiate contingency protocols, ensuring minimal downtime and cost efficiency. Cross-functional teams collaborate to validate adjustments, confirm supplier capabilities, and realign distribution strategies to maintain service levels while adapting to evolving external conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
Data_Ingestion = Transition(label='Data Ingestion')
Risk_Assessment = Transition(label='Risk Assessment')
Demand_Forecast = Transition(label='Demand Forecast')
Supplier_Audit = Transition(label='Supplier Audit')
Inventory_Check = Transition(label='Inventory Check')
Capacity_Plan = Transition(label='Capacity Plan')
Schedule_Update = Transition(label='Schedule Update')
Logistics_Review = Transition(label='Logistics Review')
Contingency_Setup = Transition(label='Contingency Setup')
Resource_Align = Transition(label='Resource Align')
Cross_team_Sync = Transition(label='Cross-team Sync')
Order_Prioritize = Transition(label='Order Prioritize')
Cost_Analysis = Transition(label='Cost Analysis')
Performance_Track = Transition(label='Performance Track')
Compliance_Verify = Transition(label='Compliance Verify')
Feedback_Loop = Transition(label='Feedback Loop')

# Loop to represent continuous evaluation and adjustment: loop over Risk Assessment that
# chooses to exit or perform Contingency Setup and Resource Align then again Risk Assessment
loop = OperatorPOWL(operator=Operator.LOOP, children=[Risk_Assessment, OperatorPOWL(operator=Operator.XOR, children=[Contingency_Setup, Resource_Align])])

# Choice among input data activities that feed the Risk Assessment
data_choice = OperatorPOWL(operator=Operator.XOR, children=[Data_Ingestion, Demand_Forecast])

# Partial order modeling the supply chain operations with concurrency:
# - data_choice feeds Risk Assessment (loop)
# - Supplier Audit and Inventory Check can proceed concurrently
# - Capacity Plan and Schedule Update proceed after Supplier Audit and Inventory Check
# - Logistics Review follows Schedule Update
# - Order Prioritize and Cost Analysis proceed concurrently after Logistics Review
# - Performance Track and Compliance Verify proceed after Order Prioritize and Cost Analysis
# - Cross_team_Sync coordinates before Feedback Loop

root = StrictPartialOrder(
    nodes=[
        data_choice,
        loop,
        Supplier_Audit,
        Inventory_Check,
        Capacity_Plan,
        Schedule_Update,
        Logistics_Review,
        Order_Prioritize,
        Cost_Analysis,
        Performance_Track,
        Compliance_Verify,
        Cross_team_Sync,
        Feedback_Loop
    ]
)

o = root.order
# Ordering edges according to the described flows
o.add_edge(data_choice, loop)                      # Input data precedes Risk Assessment loop
o.add_edge(Supplier_Audit, Capacity_Plan)          # Supplier Audit precedes Capacity Plan
o.add_edge(Inventory_Check, Capacity_Plan)          # Inventory Check precedes Capacity Plan
o.add_edge(Capacity_Plan, Schedule_Update)          # Capacity Plan precedes Schedule Update
o.add_edge(Schedule_Update, Logistics_Review)       # Schedule Update precedes Logistics Review
o.add_edge(Logistics_Review, Order_Prioritize)      # Logistics Review precedes Order Prioritize
o.add_edge(Logistics_Review, Cost_Analysis)         # Logistics Review precedes Cost Analysis
o.add_edge(Order_Prioritize, Performance_Track)     # Order Prioritize precedes Performance Track
o.add_edge(Order_Prioritize, Compliance_Verify)     # Order Prioritize precedes Compliance Verify
o.add_edge(Cost_Analysis, Performance_Track)        # Cost Analysis precedes Performance Track
o.add_edge(Cost_Analysis, Compliance_Verify)        # Cost Analysis precedes Compliance Verify
o.add_edge(Performance_Track, Cross_team_Sync)      # Performance Track precedes Cross-team Sync
o.add_edge(Compliance_Verify, Cross_team_Sync)      # Compliance Verify precedes Cross-team Sync
o.add_edge(Cross_team_Sync, Feedback_Loop)          # Cross-team Sync precedes Feedback Loop

# Allow Supplier Audit and Inventory Check concurrent start (no edges between them)
# Also Data choice and Supplier Audit, Inventory Check are unordered (concurrent)
# Feedback_Loop finalizes process
