# Generated from: d7737c35-e58b-4ba8-96bc-af94e425f158.json
# Description: This process ensures comprehensive traceability of artisan cheese production from raw milk sourcing through aging and packaging to final distribution. It involves meticulous documentation of milk origin, microbial cultures used, fermentation conditions, aging environments, and sensory evaluations. Quality checkpoints include microbial testing, texture analysis, and flavor profiling. The process integrates supplier audits, batch tracking, and regulatory compliance reviews. It also incorporates consumer feedback loops and sustainability assessments to optimize both product quality and environmental impact. Data is collected digitally at each stage to enable real-time analytics and to support recall procedures if necessary.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
milk_sourcing = Transition(label='Milk Sourcing')
supplier_audit = Transition(label='Supplier Audit')
culture_prep = Transition(label='Culture Prep')
milk_testing = Transition(label='Milk Testing')
fermentation_start = Transition(label='Fermentation Start')
ph_monitoring = Transition(label='pH Monitoring')
curd_cutting = Transition(label='Curd Cutting')
mold_inoculation = Transition(label='Mold Inoculation')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
texture_check = Transition(label='Texture Check')
flavor_profiling = Transition(label='Flavor Profiling')
batch_labeling = Transition(label='Batch Labeling')
packaging = Transition(label='Packaging')
distribution = Transition(label='Distribution')
feedback_review = Transition(label='Feedback Review')
sustainability_audit = Transition(label='Sustainability Audit')

# Define partial orders for major phases

# Phase 1: Milk sourcing and supplier audit and culture prep, then milk testing
phase1_nodes = [milk_sourcing, supplier_audit, culture_prep, milk_testing]
phase1 = StrictPartialOrder(nodes=phase1_nodes)
# Order dependencies:
# Milk sourcing --> Supplier Audit (supplier audit after sourcing)
phase1.order.add_edge(milk_sourcing, supplier_audit)
# Milk sourcing --> Culture Prep (culture prep can start after milk sourcing)
phase1.order.add_edge(milk_sourcing, culture_prep)
# Supplier Audit and Culture Prep precede Milk Testing (milk testing after both complete)
phase1.order.add_edge(supplier_audit, milk_testing)
phase1.order.add_edge(culture_prep, milk_testing)

# Phase 2: Fermentation and monitoring with loop on monitoring
# Loop consists of:
# A = Fermentation Start
# B = pH Monitoring
loop_fermentation = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_start, ph_monitoring])

# Phase 3: Curd cutting, mold inoculation, aging setup, humidity control, all partial order (some concurrency)
phase3_nodes = [curd_cutting, mold_inoculation, aging_setup, humidity_control]
phase3 = StrictPartialOrder(nodes=phase3_nodes)
# Enforce orders:
# Curd cutting --> Mold inoculation
phase3.order.add_edge(curd_cutting, mold_inoculation)
# Mold inoculation --> Aging Setup
phase3.order.add_edge(mold_inoculation, aging_setup)
# Aging Setup --> Humidity Control
phase3.order.add_edge(aging_setup, humidity_control)

# Phase 4: Quality checks texture check and flavor profiling, both after humidity control in partial order (concurrent)
phase4_nodes = [texture_check, flavor_profiling]
phase4 = StrictPartialOrder(nodes=phase4_nodes)
# Both after humidity control, will link externally

# Phase 5: Packaging, batch labeling, distribution partial order
phase5_nodes = [batch_labeling, packaging, distribution]
phase5 = StrictPartialOrder(nodes=phase5_nodes)
# Order dependencies:
# Batch labeling --> Packaging --> Distribution
phase5.order.add_edge(batch_labeling, packaging)
phase5.order.add_edge(packaging, distribution)

# Phase 6: Feedback review and sustainability audit, concurrent with distribution
phase6_nodes = [feedback_review, sustainability_audit]
phase6 = StrictPartialOrder(nodes=phase6_nodes)

# Now combine phases with partial orders and edges

# root nodes:
root_nodes = [
    phase1,
    loop_fermentation,
    phase3,
    phase4,
    phase5,
    phase6
]

root = StrictPartialOrder(nodes=root_nodes)

# Define partial order edges connecting phases:

# phase1 --> loop_fermentation
root.order.add_edge(phase1, loop_fermentation)

# loop_fermentation --> phase3
root.order.add_edge(loop_fermentation, phase3)

# phase3 --> phase4 (humidity control precedes texture and flavor check)
root.order.add_edge(phase3, phase4)

# phase4 --> phase5 (quality check precedes labeling/packaging)
root.order.add_edge(phase4, phase5)

# phase5 --> phase6 (distribution precedes feedback and sustainability audits)
root.order.add_edge(phase5, phase6)