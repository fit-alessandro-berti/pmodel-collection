# Generated from: 28460a01-c094-4150-9597-d3c565c3076c.json
# Description: This process describes a cyclical methodology for generating breakthrough innovations by integrating insights, technologies, and practices from multiple unrelated industries. It begins with environmental scanning and knowledge harvesting, followed by cross-sector ideation workshops that challenge conventional boundaries. Prototyping leverages rapid iteration with diverse teams, while validation incorporates feedback loops from pilot users across different market segments. Scaling involves tailored adaptation strategies per industry context, and continuous learning ensures the process evolves dynamically. This atypical approach fosters radical innovation by deliberately blending diverse domain expertise, avoiding siloed R&D, and embedding systemic feedback to sustain long-term competitive advantage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
scan_trends     = Transition(label='Scan Trends')
harvest_data    = Transition(label='Harvest Data')
map_insights    = Transition(label='Map Insights')
form_teams      = Transition(label='Form Teams')
ideate_cross    = Transition(label='Ideate Cross')
select_concepts = Transition(label='Select Concepts')
build_prototype = Transition(label='Build Prototype')
test_pilots     = Transition(label='Test Pilots')
gather_feedback = Transition(label='Gather Feedback')
refine_model    = Transition(label='Refine Model')
adapt_strategy  = Transition(label='Adapt Strategy')
launch_scaled   = Transition(label='Launch Scaled')
monitor_impact  = Transition(label='Monitor Impact')
capture_learn   = Transition(label='Capture Learn')
iterate_cycle   = Transition(label='Iterate Cycle')

# Main cycle without the explicit "Iterate Cycle" activity
main_cycle = StrictPartialOrder(nodes=[
    scan_trends,
    harvest_data,
    map_insights,
    form_teams,
    ideate_cross,
    select_concepts,
    build_prototype,
    test_pilots,
    gather_feedback,
    refine_model,
    adapt_strategy,
    launch_scaled,
    monitor_impact,
    capture_learn
])

# Define the sequential order of the main cycle
main_cycle.order.add_edge(scan_trends,     harvest_data)
main_cycle.order.add_edge(harvest_data,    map_insights)
main_cycle.order.add_edge(map_insights,    form_teams)
main_cycle.order.add_edge(form_teams,      ideate_cross)
main_cycle.order.add_edge(ideate_cross,    select_concepts)
main_cycle.order.add_edge(select_concepts, build_prototype)
main_cycle.order.add_edge(build_prototype, test_pilots)
main_cycle.order.add_edge(test_pilots,     gather_feedback)
main_cycle.order.add_edge(gather_feedback, refine_model)
main_cycle.order.add_edge(refine_model,    adapt_strategy)
main_cycle.order.add_edge(adapt_strategy,  launch_scaled)
main_cycle.order.add_edge(launch_scaled,   monitor_impact)
main_cycle.order.add_edge(monitor_impact,  capture_learn)

# Wrap the process into a LOOP: do main_cycle, then either exit or perform 'Iterate Cycle' and repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_cycle, iterate_cycle]
)