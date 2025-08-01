# Generated from: f18e7e37-bb0c-416c-bcce-be5d2b582d38.json
# Description: This process involves managing a highly personalized meal kit subscription service where customers select dietary preferences, delivery schedules, and recipe complexity. The system dynamically adjusts ingredient sourcing based on seasonal availability and regional supplier constraints. It incorporates real-time inventory tracking, quality inspections, and feedback loops to optimize future meal plans. Additionally, it integrates with third-party logistics for last-mile delivery efficiency and includes contingency planning for supply chain disruptions. The process concludes with customer satisfaction analysis to continuously refine meal offerings and service reliability, ensuring both freshness and variety while minimizing waste and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
signup       = Transition(label="User Signup")
pref         = Transition(label="Preference Set")
select       = Transition(label="Meal Select")
sched        = Transition(label="Schedule Delivery")
supplier     = Transition(label="Supplier Match")
inv_check    = Transition(label="Inventory Check")
ing_order    = Transition(label="Ingredient Order")
quality      = Transition(label="Quality Inspect")
pack         = Transition(label="Meal Pack")
route        = Transition(label="Route Plan")
dispatch     = Transition(label="Dispatch Kit")
track        = Transition(label="Delivery Track")
feedback     = Transition(label="Feedback Collect")
analyze      = Transition(label="Data Analyze")
optimize     = Transition(label="Plan Optimize")

# Loop for replenishing inventory: check → order → (back to check)
inv_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[inv_check, ing_order]
)

# Initial one‐time part: signup then set preferences
init = StrictPartialOrder(nodes=[signup, pref])
init.order.add_edge(signup, pref)

# Main body of the subscription cycle
body_nodes = [
    pref,
    select,
    sched,
    supplier,
    inv_loop,
    quality,
    pack,
    route,
    dispatch,
    track,
    feedback,
    analyze,
    optimize
]
body = StrictPartialOrder(nodes=body_nodes)
body.order.add_edge(pref, select)
body.order.add_edge(select, sched)
body.order.add_edge(sched, supplier)
body.order.add_edge(supplier, inv_loop)
body.order.add_edge(inv_loop, quality)
body.order.add_edge(quality, pack)
body.order.add_edge(pack, route)
body.order.add_edge(route, dispatch)
body.order.add_edge(dispatch, track)
body.order.add_edge(track, feedback)
body.order.add_edge(feedback, analyze)
body.order.add_edge(analyze, optimize)

# Top‐level loop: after signup, repeat the meal‐kit cycle (preferences → ... → optimization)
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[init, body]
)