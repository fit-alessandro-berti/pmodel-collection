# Generated from: f2247c6d-b5f2-4c5a-86db-b9bb61f8bfee.json
# Description: This process involves managing the return and refurbishment of used electronic devices from customers to restore value and minimize waste. It starts with receiving returned items, followed by inspection, segregation based on condition, data wiping for privacy, component harvesting, repair or refurbishment, quality testing, and repackaging. Simultaneously, defective parts are recycled or disposed of responsibly. The process also includes updating inventory records, coordinating with resale channels, handling customer refunds or credits, and continuously analyzing return patterns to improve future product designs and reduce return rates. This atypical process integrates sustainability with profitability in a complex supply chain environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Receive_Returns = Transition(label='Receive Returns')
Inspect_Items = Transition(label='Inspect Items')
Segregate_Stock = Transition(label='Segregate Stock')
Wipe_Data = Transition(label='Wipe Data')
Harvest_Parts = Transition(label='Harvest Parts')
Refurbish_Units = Transition(label='Refurbish Units')
Test_Quality = Transition(label='Test Quality')
Recycle_Waste = Transition(label='Recycle Waste')
Dispose_Detects = Transition(label='Dispose Defects')
Update_Inventory = Transition(label='Update Inventory')
Coordinate_Resale = Transition(label='Coordinate Resale')
Process_Refunds = Transition(label='Process Refunds')
Analyze_Patterns = Transition(label='Analyze Patterns')
Improve_Design = Transition(label='Improve Design')
Report_Metrics = Transition(label='Report Metrics')

# Correct variable name typo Dispose_Detects -> Dispose_Defects
Dispose_Defects = Dispose_Detects
del Dispose_Detects

# Concurrent defect handling: Recycle_Waste and Dispose_Defects are concurrent
Recycling_Disposal_PO = StrictPartialOrder(nodes=[Recycle_Waste, Dispose_Defects])

# After Segregate_Stock, depending on condition, two branches:
# 1) refurbish branch: Wipe Data -> Harvest Parts -> Refurbish Units -> Test Quality -> Repackage (Repackage absent, so Test Quality ends refurb)
# 2) defective branch: Recycling_Disposal_PO concurrent activities

# Define refurbishment partial order (sequential)
Refurbish_PO = StrictPartialOrder(nodes=[Wipe_Data, Harvest_Parts, Refurbish_Units, Test_Quality])
Refurbish_PO.order.add_edge(Wipe_Data, Harvest_Parts)
Refurbish_PO.order.add_edge(Harvest_Parts, Refurbish_Units)
Refurbish_PO.order.add_edge(Refurbish_Units, Test_Quality)

# After refurb, continue with Update Inventory, Coordinate Resale, Process Refunds (these are sequential)
Post_Refurbish_PO = StrictPartialOrder(nodes=[Update_Inventory, Coordinate_Resale, Process_Refunds])
Post_Refurbish_PO.order.add_edge(Update_Inventory, Coordinate_Resale)
Post_Refurbish_PO.order.add_edge(Coordinate_Resale, Process_Refunds)

# Combine refurb branch and post refurb branch sequentially
Refurbish_Full_PO = StrictPartialOrder(nodes=[Refurbish_PO, Post_Refurbish_PO])
Refurbish_Full_PO.order.add_edge(Refurbish_PO, Post_Refurbish_PO)

# Choice after Segregate Stock: go refurbish path or defect handling path (concurrent recycle/dispose)
Segregate_Choice = OperatorPOWL(operator=Operator.XOR, children=[Refurbish_Full_PO, Recycling_Disposal_PO])

# Initial partial order: Receive Returns -> Inspect Items -> Segregate Stock -> Segregate_Choice
Main_PO1 = StrictPartialOrder(nodes=[Receive_Returns, Inspect_Items, Segregate_Stock, Segregate_Choice])
Main_PO1.order.add_edge(Receive_Returns, Inspect_Items)
Main_PO1.order.add_edge(Inspect_Items, Segregate_Stock)
Main_PO1.order.add_edge(Segregate_Stock, Segregate_Choice)

# Loop for continuous improve process
# Loop with body: Analyze Patterns -> Improve Design -> Report Metrics
# After Report Metrics, loop back to Analyze Patterns or exit
Analyze = Analyze_Patterns
Improve = Improve_Design
Report = Report_Metrics

Improve_PO = StrictPartialOrder(nodes=[Analyze, Improve, Report])
Improve_PO.order.add_edge(Analyze, Improve)
Improve_PO.order.add_edge(Improve, Report)

Loop_Improvement = OperatorPOWL(operator=Operator.LOOP, children=[Improve_PO, SilentTransition()])

# Final PO combining main process and improvement loop concurrently
root = StrictPartialOrder(nodes=[Main_PO1, Loop_Improvement])
# After main process complete, run loop (improve cycle runs concurrently, no order needed)

# Final result
# The loop node + main process run concurrently (no ordering)