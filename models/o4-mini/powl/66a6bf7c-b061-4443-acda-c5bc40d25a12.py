# Generated from: 66a6bf7c-b061-4443-acda-c5bc40d25a12.json
# Description: This process governs the end-to-end management of an urban vertical farm that integrates IoT monitoring, automated nutrient delivery, and AI-driven crop optimization. Starting from seed selection, the system adapts environmental controls dynamically based on sensor feedback to maximize yield while minimizing water and energy consumption. The workflow includes pest detection via image recognition, real-time growth analytics, and coordinated harvest scheduling. Post-harvest, produce undergoes automated quality grading and packaging before distribution to local markets and restaurants, ensuring freshness and traceability. The cycle concludes with system maintenance, data archiving, and continuous improvement through machine learning insights derived from operational data.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed           = Transition(label='Seed Selection')
iot            = Transition(label='IoT Setup')
nutrient       = Transition(label='Nutrient Mix')
sensor         = Transition(label='Sensor Check')
climate        = Transition(label='Climate Adjust')
water          = Transition(label='Water Control')
growth         = Transition(label='Growth Monitor')
ai             = Transition(label='AI Analysis')
pest           = Transition(label='Pest Detect')
harvest        = Transition(label='Harvest Plan')
quality        = Transition(label='Quality Scan')
package        = Transition(label='Auto Package')
dispatch       = Transition(label='Market Dispatch')
archive        = Transition(label='Data Archive')
maintain       = Transition(label='System Maintain')
feedback       = Transition(label='Feedback Loop')

# Build the adjustment sub-process (partial order)
adjustment = StrictPartialOrder(nodes=[water, climate, growth, ai, pest])
adjustment.order.add_edge(water,   growth)
adjustment.order.add_edge(climate, growth)
adjustment.order.add_edge(growth,  ai)
adjustment.order.add_edge(ai,      pest)

# Loop: sensor check then adjustment, repeating until exit
inner_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor, adjustment])

# Main workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    seed, iot, nutrient, inner_loop,
    harvest, quality, package, dispatch,
    archive, maintain, feedback
])

# Define the overall sequencing
root.order.add_edge(seed,     iot)
root.order.add_edge(iot,      nutrient)
root.order.add_edge(nutrient, inner_loop)
root.order.add_edge(inner_loop, harvest)
root.order.add_edge(harvest,  quality)
root.order.add_edge(quality,  package)
root.order.add_edge(package,  dispatch)
root.order.add_edge(dispatch, archive)
root.order.add_edge(archive,  maintain)
root.order.add_edge(maintain, feedback)