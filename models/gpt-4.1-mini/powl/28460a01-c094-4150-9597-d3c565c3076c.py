# Generated from: 28460a01-c094-4150-9597-d3c565c3076c.json
# Description: This process describes a cyclical methodology for generating breakthrough innovations by integrating insights, technologies, and practices from multiple unrelated industries. It begins with environmental scanning and knowledge harvesting, followed by cross-sector ideation workshops that challenge conventional boundaries. Prototyping leverages rapid iteration with diverse teams, while validation incorporates feedback loops from pilot users across different market segments. Scaling involves tailored adaptation strategies per industry context, and continuous learning ensures the process evolves dynamically. This atypical approach fosters radical innovation by deliberately blending diverse domain expertise, avoiding siloed R&D, and embedding systemic feedback to sustain long-term competitive advantage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Scan_Trends = Transition(label='Scan Trends')
Harvest_Data = Transition(label='Harvest Data')
Map_Insights = Transition(label='Map Insights')

Form_Teams = Transition(label='Form Teams')
Ideate_Cross = Transition(label='Ideate Cross')
Select_Concepts = Transition(label='Select Concepts')

Build_Prototype = Transition(label='Build Prototype')
Test_Pilots = Transition(label='Test Pilots')
Gather_Feedback = Transition(label='Gather Feedback')

Refine_Model = Transition(label='Refine Model')
Adapt_Strategy = Transition(label='Adapt Strategy')
Launch_Scaled = Transition(label='Launch Scaled')

Monitor_Impact = Transition(label='Monitor Impact')
Capture_Learn = Transition(label='Capture Learn')

Iterate_Cycle = Transition(label='Iterate Cycle')

# First partial order: environmental scanning and knowledge harvesting
# Scan Trends --> Harvest Data --> Map Insights, which precedes team formation & ideation
env_scan_po = StrictPartialOrder(nodes=[Scan_Trends, Harvest_Data, Map_Insights])
env_scan_po.order.add_edge(Scan_Trends, Harvest_Data)
env_scan_po.order.add_edge(Harvest_Data, Map_Insights)

# Team formation and ideation partial order
team_ideate_po = StrictPartialOrder(nodes=[Form_Teams, Ideate_Cross, Select_Concepts])
team_ideate_po.order.add_edge(Form_Teams, Ideate_Cross)
team_ideate_po.order.add_edge(Ideate_Cross, Select_Concepts)

# Prototyping and validation partial order
proto_valid_po = StrictPartialOrder(nodes=[Build_Prototype, Test_Pilots, Gather_Feedback])
proto_valid_po.order.add_edge(Build_Prototype, Test_Pilots)
proto_valid_po.order.add_edge(Test_Pilots, Gather_Feedback)

# Refinement and scaling partial order
refine_scale_po = StrictPartialOrder(nodes=[Refine_Model, Adapt_Strategy, Launch_Scaled])
refine_scale_po.order.add_edge(Refine_Model, Adapt_Strategy)
refine_scale_po.order.add_edge(Adapt_Strategy, Launch_Scaled)

# Monitoring and learning partial order
monitor_learn_po = StrictPartialOrder(nodes=[Monitor_Impact, Capture_Learn])
monitor_learn_po.order.add_edge(Monitor_Impact, Capture_Learn)

# Define loop body partial order: 
# This includes prototyping+validation, then refinement+scaling, then monitoring+learning, then iterate cycle
loop_body_po = StrictPartialOrder(
    nodes=[proto_valid_po, refine_scale_po, monitor_learn_po, Iterate_Cycle]
)
loop_body_po.order.add_edge(proto_valid_po, refine_scale_po)
loop_body_po.order.add_edge(refine_scale_po, monitor_learn_po)
loop_body_po.order.add_edge(monitor_learn_po, Iterate_Cycle)

# Loop: execute prototyping-validation-refinement-scaling-monitoring-learning and iteration cycle repeatedly 
# * (loop_body, tau)
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body_po, Iterate_Cycle])

# Assemble top level partial order combining:
# 1) env scanning (Scan Trends->Harvest Data->Map Insights)
# 2) team formation + ideation (Form Teams -> Ideate Cross -> Select Concepts)
# 3) loop (prototyping + refinement + learning cycled)
# Partial order: env_scan_po -> team_ideate_po -> loop
root = StrictPartialOrder(nodes=[env_scan_po, team_ideate_po, loop])
root.order.add_edge(env_scan_po, team_ideate_po)
root.order.add_edge(team_ideate_po, loop)