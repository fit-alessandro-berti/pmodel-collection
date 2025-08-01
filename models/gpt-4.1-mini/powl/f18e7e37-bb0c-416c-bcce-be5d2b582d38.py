# Generated from: f18e7e37-bb0c-416c-bcce-be5d2b582d38.json
# Description: This process involves managing a highly personalized meal kit subscription service where customers select dietary preferences, delivery schedules, and recipe complexity. The system dynamically adjusts ingredient sourcing based on seasonal availability and regional supplier constraints. It incorporates real-time inventory tracking, quality inspections, and feedback loops to optimize future meal plans. Additionally, it integrates with third-party logistics for last-mile delivery efficiency and includes contingency planning for supply chain disruptions. The process concludes with customer satisfaction analysis to continuously refine meal offerings and service reliability, ensuring both freshness and variety while minimizing waste and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
User_Signup = Transition(label='User Signup')
Preference_Set = Transition(label='Preference Set')
Meal_Select = Transition(label='Meal Select')
Schedule_Delivery = Transition(label='Schedule Delivery')
Supplier_Match = Transition(label='Supplier Match')
Inventory_Check = Transition(label='Inventory Check')
Ingredient_Order = Transition(label='Ingredient Order')
Quality_Inspect = Transition(label='Quality Inspect')
Meal_Pack = Transition(label='Meal Pack')
Route_Plan = Transition(label='Route Plan')
Dispatch_Kit = Transition(label='Dispatch Kit')
Delivery_Track = Transition(label='Delivery Track')
Feedback_Collect = Transition(label='Feedback Collect')
Data_Analyze = Transition(label='Data Analyze')
Plan_Optimize = Transition(label='Plan Optimize')

# Silent transition (skip) for loop exit options
skip = SilentTransition()

# Loop: 
# Real-time inventory tracking, quality inspections, feedback loops to optimize future meal plans
# loop body: B = [Inventory_Check, Quality_Inspect, Feedback_Collect, Data_Analyze, Plan_Optimize]
# loop executes A first, here A = Ingredient_Order (ordering requires looping)
# so LOOP(Ingredient_Order, PO(Inventory,...,Plan_Optimize))
loop_body_nodes = [Inventory_Check, Quality_Inspect, Feedback_Collect, Data_Analyze, Plan_Optimize]
loop_body = StrictPartialOrder(nodes=loop_body_nodes)

# preserve partial order inside the loop_body
loop_body.order.add_edge(Inventory_Check, Quality_Inspect)
loop_body.order.add_edge(Quality_Inspect, Feedback_Collect)
loop_body.order.add_edge(Feedback_Collect, Data_Analyze)
loop_body.order.add_edge(Data_Analyze, Plan_Optimize)

loop = OperatorPOWL(operator=Operator.LOOP, children=[Ingredient_Order, loop_body])

# Partial orders for initial selection workflow: User Signup -> Preference Set -> Meal Select -> Schedule Delivery
initial_phase = StrictPartialOrder(nodes=[User_Signup, Preference_Set, Meal_Select, Schedule_Delivery])
initial_phase.order.add_edge(User_Signup, Preference_Set)
initial_phase.order.add_edge(Preference_Set, Meal_Select)
initial_phase.order.add_edge(Meal_Select, Schedule_Delivery)

# Partial order for supplier matching after scheduling delivery, but before ingredient order
supplier_phase = StrictPartialOrder(nodes=[Supplier_Match])
# No internal edges as single node

# Partial order for meal packaging and dispatch workflow
pack_dispatch_nodes = [Meal_Pack, Route_Plan, Dispatch_Kit, Delivery_Track]
pack_dispatch = StrictPartialOrder(nodes=pack_dispatch_nodes)
pack_dispatch.order.add_edge(Meal_Pack, Route_Plan)
pack_dispatch.order.add_edge(Route_Plan, Dispatch_Kit)
pack_dispatch.order.add_edge(Dispatch_Kit, Delivery_Track)

# Integrate phases using partial order:
# Initial phase -> supplier match -> loop(ingredient order + inventory feedback) -> pack & dispatch

# Collect all top-level nodes
nodes_top = [initial_phase, supplier_phase, loop, pack_dispatch]

root = StrictPartialOrder(nodes=nodes_top)

# Ordering between phases
root.order.add_edge(initial_phase, supplier_phase)
root.order.add_edge(supplier_phase, loop)
root.order.add_edge(loop, pack_dispatch)