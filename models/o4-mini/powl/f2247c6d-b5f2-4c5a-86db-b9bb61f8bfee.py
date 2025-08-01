# Generated from: f2247c6d-b5f2-4c5a-86db-b9bb61f8bfee.json
# Description: This process involves managing the return and refurbishment of used electronic devices from customers to restore value and minimize waste. It starts with receiving returned items, followed by inspection, segregation based on condition, data wiping for privacy, component harvesting, repair or refurbishment, quality testing, and repackaging. Simultaneously, defective parts are recycled or disposed of responsibly. The process also includes updating inventory records, coordinating with resale channels, handling customer refunds or credits, and continuously analyzing return patterns to improve future product designs and reduce return rates. This atypical process integrates sustainability with profitability in a complex supply chain environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
t_receive     = Transition(label="Receive Returns")
t_inspect     = Transition(label="Inspect Items")
t_segregate   = Transition(label="Segregate Stock")
t_wipe        = Transition(label="Wipe Data")
t_harvest     = Transition(label="Harvest Parts")
t_refurbish   = Transition(label="Refurbish Units")
t_test        = Transition(label="Test Quality")
t_recycle     = Transition(label="Recycle Waste")
t_dispose     = Transition(label="Dispose Defects")
t_update      = Transition(label="Update Inventory")
t_coord       = Transition(label="Coordinate Resale")
t_refund      = Transition(label="Process Refunds")
t_analyze     = Transition(label="Analyze Patterns")
t_improve     = Transition(label="Improve Design")
t_report      = Transition(label="Report Metrics")

# --- Good‐item branch: either harvest or (refurbish then test) ---
# Sequence: refurbish -> test
seq_refurbish = StrictPartialOrder(nodes=[t_refurbish, t_test])
seq_refurbish.order.add_edge(t_refurbish, t_test)

# XOR choice between harvesting parts or refurbish+test
xor_good = OperatorPOWL(operator=Operator.XOR, children=[t_harvest, seq_refurbish])

# --- Defective‐item branch: recycle or dispose ---
xor_defect = OperatorPOWL(operator=Operator.XOR, children=[t_recycle, t_dispose])

# --- Continuous improvement loop: analyze+report then optionally improve then repeat ---
# Body of loop: analyze -> report
body_loop = StrictPartialOrder(nodes=[t_analyze, t_report])
body_loop.order.add_edge(t_analyze, t_report)

# LOOP operator: execute body_loop, then optionally do improve then body_loop again
loop_ci = OperatorPOWL(operator=Operator.LOOP, children=[body_loop, t_improve])

# --- Build the top‐level partial order ---
root = StrictPartialOrder(
    nodes=[
        t_receive,
        t_inspect,
        t_segregate,
        t_wipe,
        xor_good,
        xor_defect,
        t_update,
        t_coord,
        t_refund,
        loop_ci
    ]
)

# Add the main control‐flow edges
root.order.add_edge(t_receive,   t_inspect)
root.order.add_edge(t_inspect,   t_segregate)

# After segregation, two branches in parallel
root.order.add_edge(t_segregate, t_wipe)        # good‐item branch starts
root.order.add_edge(t_segregate, xor_defect)   # defect branch starts

# Good‐item branch sequencing
root.order.add_edge(t_wipe,      xor_good)

# Both branches must complete before updating inventory
root.order.add_edge(xor_good,    t_update)
root.order.add_edge(xor_defect,  t_update)

# Final straight‐through steps
root.order.add_edge(t_update,    t_coord)
root.order.add_edge(t_coord,     t_refund)
root.order.add_edge(t_refund,    loop_ci)

# 'root' now holds the complete POWL model