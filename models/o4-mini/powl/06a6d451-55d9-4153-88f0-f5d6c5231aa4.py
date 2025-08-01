# Generated from: 06a6d451-55d9-4153-88f0-f5d6c5231aa4.json
# Description: This process outlines the detailed steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes site analysis, environmental impact assessment, modular system design, nutrient cycling setup, climate control calibration, and integration of IoT monitoring. Additionally, it covers workforce training, crop scheduling, pest management protocols, and supply chain coordination for distribution. The process ensures sustainable practices, energy efficiency, and maximized yield through innovative technology and precise resource management, accommodating urban space constraints while promoting local food production and reduced carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site        = Transition(label='Site Survey')
impact      = Transition(label='Impact Study')
design      = Transition(label='System Design')
build       = Transition(label='Module Build')
nutrient    = Transition(label='Nutrient Prep')
water       = Transition(label='Water Cycle')
climate     = Transition(label='Climate Setup')
sensor      = Transition(label='Sensor Install')
sync        = Transition(label='Data Sync')
plan        = Transition(label='Crop Planning')
workers     = Transition(label='Worker Train')
pest        = Transition(label='Pest Control')
audit       = Transition(label='Energy Audit')
harvest     = Transition(label='Harvest Plan')
distribution= Transition(label='Distribution')

# Setup phase: site survey through energy audit and IoT setup
setup_po = StrictPartialOrder(nodes=[
    site, impact, design, build, workers,
    nutrient, water, climate, sensor, sync, audit
])
setup_po.order.add_edge(site, impact)
setup_po.order.add_edge(impact, design)
# After system design we build modules and train workforce in parallel
setup_po.order.add_edge(design, build)
setup_po.order.add_edge(design, workers)
# Build → nutrient prep → water cycle → climate calibration
setup_po.order.add_edge(build, nutrient)
setup_po.order.add_edge(nutrient, water)
setup_po.order.add_edge(water, climate)
# Climate setup → sensor install → data synchronization
setup_po.order.add_edge(climate, sensor)
setup_po.order.add_edge(sensor, sync)
# Also climate calibration → energy audit
setup_po.order.add_edge(climate, audit)

# Define the recurring crop cycle: planning → harvest → distribution
cycle_body = StrictPartialOrder(nodes=[plan, harvest, distribution])
cycle_body.order.add_edge(plan, harvest)
cycle_body.order.add_edge(harvest, distribution)

# Loop: first do one crop cycle, then either exit or do pest control then another cycle
farming_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cycle_body, pest]
)

# Root model: setup followed by the looping crop cycles
root = StrictPartialOrder(nodes=[setup_po, farming_loop])
root.order.add_edge(setup_po, farming_loop)