# Generated from: a4e1efc0-519d-4794-a5d8-e4f1a96c01c2.json
# Description: This process outlines the complex and atypical steps involved in setting up an urban vertical farm in a densely populated city environment. It includes site assessment, modular structure design, hydroponic system integration, environmental control calibration, crop selection based on microclimate data, seed germination scheduling, nutrient solution formulation, pest monitoring with AI sensors, automated harvesting preparation, waste recycling workflows, market demand analysis, supply chain synchronization, energy consumption optimization, community engagement initiatives, and regulatory compliance verification to ensure sustainable and profitable urban agriculture operations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
sa  = Transition(label="Site Assessment")
sd  = Transition(label="Structure Design")
hs  = Transition(label="Hydroponic Setup")
ec  = Transition(label="Env Control")
cs  = Transition(label="Crop Selection")
ss  = Transition(label="Seed Scheduling")
nm  = Transition(label="Nutrient Mix")
pm_ = Transition(label="Pest Monitoring")
hp  = Transition(label="Harvest Prep")
wr  = Transition(label="Waste Recycling")
ma  = Transition(label="Market Analysis")
sync = Transition(label="Supply Sync")
eo  = Transition(label="Energy Optimize")
ce  = Transition(label="Community Engage")
cc  = Transition(label="Compliance Check")

# Loop around monitoring and harvest preparation:
#   * (Pest Monitoring, Harvest Prep)
loop_pm_hp = OperatorPOWL(operator=Operator.LOOP, children=[pm_, hp])

# Main operational sequence
main_seq = StrictPartialOrder(
    nodes=[sa, sd, hs, ec, cs, ss, nm, loop_pm_hp, wr]
)
main_seq.order.add_edge(sa, sd)
main_seq.order.add_edge(sd, hs)
main_seq.order.add_edge(hs, ec)
main_seq.order.add_edge(ec, cs)
main_seq.order.add_edge(cs, ss)
main_seq.order.add_edge(ss, nm)
main_seq.order.add_edge(nm, loop_pm_hp)
main_seq.order.add_edge(loop_pm_hp, wr)

# Business & regulatory sequence
biz_seq = StrictPartialOrder(
    nodes=[ma, sync, eo, ce, cc]
)
biz_seq.order.add_edge(ma, sync)
biz_seq.order.add_edge(sync, eo)
biz_seq.order.add_edge(eo, ce)
biz_seq.order.add_edge(ce, cc)

# Root: run both sequences concurrently
root = StrictPartialOrder(nodes=[main_seq, biz_seq])
# No edges between main_seq and biz_seq => they are parallel