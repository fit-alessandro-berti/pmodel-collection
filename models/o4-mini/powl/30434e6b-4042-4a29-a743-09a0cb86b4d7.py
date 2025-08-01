# Generated from: 30434e6b-4042-4a29-a743-09a0cb86b4d7.json
# Description: This process involves establishing a fully functional urban vertical farming system within a repurposed industrial space. It includes site analysis, modular structure assembly, environmental system installation, crop selection based on local climate data, automated irrigation setup, nutrient solution calibration, integrated pest management, real-time monitoring system deployment, staff training, trial cultivation, data analytics for yield optimization, marketing strategy development, supply chain coordination, and continuous maintenance scheduling to ensure sustainable urban agriculture with minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site        = Transition(label='Site Survey')
design      = Transition(label='Design Layout')
structure   = Transition(label='Structure Build')
enviro      = Transition(label='Enviro Setup')
crop        = Transition(label='Crop Select')
irrigation  = Transition(label='Irrigation Config')
nutrient    = Transition(label='Nutrient Mix')
pest        = Transition(label='Pest Control')
sensor      = Transition(label='Sensor Install')
testing     = Transition(label='System Testing')
training    = Transition(label='Staff Training')
trial       = Transition(label='Trial Grow')
review      = Transition(label='Data Review')
market      = Transition(label='Market Plan')
supply      = Transition(label='Supply Sync')
maintenance = Transition(label='Maintenance Plan')

# A silent transition to use as the exit condition of the loop
skip = SilentTransition()

# Define the maintenance loop: do maintenance, then either exit or repeat
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[maintenance, skip]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site, design, structure, enviro, crop,
    irrigation, nutrient, pest, sensor,
    testing, training, trial, review,
    market, supply,
    maintenance_loop, skip
])

# Sequential backbone: Site Survey -> Design Layout -> Structure Build -> Enviro Setup -> Crop Select
root.order.add_edge(site, design)
root.order.add_edge(design, structure)
root.order.add_edge(structure, enviro)
root.order.add_edge(enviro, crop)

# After crop selection, configure four systems in parallel
for nxt in [irrigation, nutrient, pest, sensor]:
    root.order.add_edge(crop, nxt)

# All four must complete before system testing
for prev in [irrigation, nutrient, pest, sensor]:
    root.order.add_edge(prev, testing)

# System testing must finish before staff training
root.order.add_edge(testing, training)

# Both training and testing must finish before trial cultivation
root.order.add_edge(training, trial)
root.order.add_edge(testing, trial)

# Trial cultivation -> Data review
root.order.add_edge(trial, review)

# Data review -> Market plan and Supply sync in parallel
root.order.add_edge(review, market)
root.order.add_edge(review, supply)

# After market & supply preparations, enter continuous maintenance loop
root.order.add_edge(market, maintenance_loop)
root.order.add_edge(supply, maintenance_loop)