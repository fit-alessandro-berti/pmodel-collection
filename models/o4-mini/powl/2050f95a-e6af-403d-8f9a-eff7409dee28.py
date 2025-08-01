# Generated from: 2050f95a-e6af-403d-8f9a-eff7409dee28.json
# Description: This process outlines the steps required to establish an urban rooftop farm on a commercial building, integrating sustainable agriculture techniques with city infrastructure constraints. It involves initial site assessment, structural analysis, soil and water testing, system design for irrigation and crop placement, procurement of materials, installation of modular planters, setup of automated climate control, seed selection and planting, daily maintenance scheduling, pest monitoring using IoT sensors, periodic yield evaluation, community engagement for education, and final reporting to stakeholders. This atypical process requires coordination between agricultural experts, civil engineers, and urban planners to ensure a productive and environmentally friendly rooftop farm that enhances urban green space while complying with safety regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site        = Transition(label='Site Assess')
struct      = Transition(label='Structural Check')
soil        = Transition(label='Soil Testing')
water       = Transition(label='Water Quality')
design      = Transition(label='System Design')
buy         = Transition(label='Material Buy')
planter     = Transition(label='Planter Setup')
climate     = Transition(label='Climate Setup')
seed        = Transition(label='Seed Planting')
irrig       = Transition(label='Irrigation Start')
pest        = Transition(label='Pest Monitor')
yieldm      = Transition(label='Yield Measure')
maint       = Transition(label='Maintenance Plan')
community   = Transition(label='Community Meet')
final       = Transition(label='Final Report')

# Build the loop body: Maintenance → Pest Monitor → Yield Measure
loop_body = StrictPartialOrder(nodes=[maint, pest, yieldm])
loop_body.order.add_edge(maint, pest)
loop_body.order.add_edge(pest, yieldm)

# LOOP operator: do Maintenance (A), then either exit or do B (Pest+Yield) then A again
loop = OperatorPOWL(operator=Operator.LOOP, children=[maint, loop_body])

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site, struct, soil, water, design, buy,
        planter, climate, seed, irrig,
        loop, community, final
    ]
)

# Add control‐flow edges
root.order.add_edge(site, struct)
root.order.add_edge(struct, soil)
root.order.add_edge(struct, water)
root.order.add_edge(soil, design)
root.order.add_edge(water, design)
root.order.add_edge(design, buy)
root.order.add_edge(buy, planter)
root.order.add_edge(buy, climate)
root.order.add_edge(planter, seed)
root.order.add_edge(seed, irrig)
root.order.add_edge(climate, irrig)
root.order.add_edge(irrig, loop)
root.order.add_edge(loop, community)
root.order.add_edge(community, final)