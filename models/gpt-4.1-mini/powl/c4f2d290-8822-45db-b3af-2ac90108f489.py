# Generated from: c4f2d290-8822-45db-b3af-2ac90108f489.json
# Description: This process involves dynamically adjusting supply chain operations in response to real-time market disruptions and internal performance analytics. It starts with continuous data ingestion from multiple sources including supplier status, logistics conditions, and demand forecasts. Using predictive algorithms, the system identifies potential bottlenecks or opportunities for optimization. Next, automated scenario simulations evaluate alternative sourcing, routing, and inventory strategies. Decisions are then collaboratively reviewed by a cross-functional team who approve rapid reconfiguration plans. Implementation involves coordinated updates to procurement, warehousing, and transportation functions while monitoring key performance indicators to ensure resilience and cost efficiency. The process also integrates feedback loops to refine predictive models and operational protocols, enabling an agile, self-correcting supply network that adapts to unexpected changes without human intervention.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Data_Ingest = Transition(label='Data Ingest')
Status_Check = Transition(label='Status Check')
Forecast_Update = Transition(label='Forecast Update')
Risk_Assess = Transition(label='Risk Assess')
Scenario_Sim = Transition(label='Scenario Sim')
Model_Run = Transition(label='Model Run')
Option_Select = Transition(label='Option Select')
Team_Review = Transition(label='Team Review')
Plan_Approve = Transition(label='Plan Approve')
Procure_Adjust = Transition(label='Procure Adjust')
Route_Replan = Transition(label='Route Replan')
Inventory_Shift = Transition(label='Inventory Shift')
Execute_Updates = Transition(label='Execute Updates')
Monitor_KPIs = Transition(label='Monitor KPIs')
Feedback_Loop = Transition(label='Feedback Loop')

# First PO: concurrent ingestion activities
ingestion = StrictPartialOrder(nodes=[Data_Ingest, Status_Check, Forecast_Update])
# all concurrent: no order edges

# Second PO: after ingestion, sequential analysis: Risk_Assess -> Scenario_Sim -> Model_Run -> Option_Select
analysis = StrictPartialOrder(nodes=[Risk_Assess, Scenario_Sim, Model_Run, Option_Select])
analysis.order.add_edge(Risk_Assess, Scenario_Sim)
analysis.order.add_edge(Scenario_Sim, Model_Run)
analysis.order.add_edge(Model_Run, Option_Select)

# Third PO: collaborative review and approval, sequence
review_approve = StrictPartialOrder(nodes=[Team_Review, Plan_Approve])
review_approve.order.add_edge(Team_Review, Plan_Approve)

# Fourth PO: implementation updates and monitoring in parallel
updates = StrictPartialOrder(nodes=[Procure_Adjust, Route_Replan, Inventory_Shift])
# activities concurrent, no order edges

exec_monitor = StrictPartialOrder(nodes=[Execute_Updates, Monitor_KPIs])
exec_monitor.order.add_edge(Execute_Updates, Monitor_KPIs)  # execute then monitor

implementation = StrictPartialOrder(nodes=[updates, exec_monitor])
# add edges from updates and exec_monitor to a combined PO: concurrent

# Combine updates (3 concurrent) and exec_monitor (sequence) in overall implementation partial order
implementation = StrictPartialOrder(nodes=[Procure_Adjust, Route_Replan, Inventory_Shift, Execute_Updates, Monitor_KPIs])
implementation.order.add_edge(Execute_Updates, Monitor_KPIs)  # monitored after execution
# Procure_Adjust, Route_Replan, Inventory_Shift are concurrent with each other and with exec_monitor activities (no edges)

# Loop: feedback loop that refines predictive models and protocols - it modifies analysis and implementation repeatedly
# Loop body: B = Feedback_Loop, A = analysis + implementation combined
analysis_plus_impl = StrictPartialOrder(nodes=[Risk_Assess, Scenario_Sim, Model_Run, Option_Select,
                                              Procure_Adjust, Route_Replan, Inventory_Shift,
                                              Execute_Updates, Monitor_KPIs])
# add analysis order edges
analysis_plus_impl.order.add_edge(Risk_Assess, Scenario_Sim)
analysis_plus_impl.order.add_edge(Scenario_Sim, Model_Run)
analysis_plus_impl.order.add_edge(Model_Run, Option_Select)
# add implementation order edge
analysis_plus_impl.order.add_edge(Execute_Updates, Monitor_KPIs)

loop = OperatorPOWL(operator=Operator.LOOP, children=[analysis_plus_impl, Feedback_Loop])

# Now combine all parts in order: ingestion --> loop --> review/approve
root = StrictPartialOrder(nodes=[Data_Ingest, Status_Check, Forecast_Update, loop, Team_Review, Plan_Approve])

# ingestion concurrent - no edges among them
# ingestion all precede the loop
root.order.add_edge(Data_Ingest, loop)
root.order.add_edge(Status_Check, loop)
root.order.add_edge(Forecast_Update, loop)

# loop precedes review/approve
root.order.add_edge(loop, Team_Review)
root.order.add_edge(Team_Review, Plan_Approve)