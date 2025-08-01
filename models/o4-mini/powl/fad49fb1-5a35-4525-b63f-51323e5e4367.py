# Generated from: fad49fb1-5a35-4525-b63f-51323e5e4367.json
# Description: This process describes the complex orchestration involved in establishing a fully operational urban vertical farm within a repurposed high-rise building. It involves site assessment, modular system design, resource sourcing, automation integration, environmental calibration, crop selection tailored to microclimates, iterative growth monitoring, pest management without chemicals, waste recycling, community engagement for local distribution, and compliance with urban agriculture regulations. The process ensures sustainable production with minimal environmental impact while optimizing yield and energy efficiency through advanced IoT and AI-driven controls.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey      = Transition(label="Site Survey")
design_modules   = Transition(label="Design Modules")
source_materials = Transition(label="Source Materials")
install_frame    = Transition(label="Install Framework")
setup_irrigation = Transition(label="Setup Irrigation")
integrate_sens   = Transition(label="Integrate Sensors")
configure_ai     = Transition(label="Configure AI")
calibrate_clm    = Transition(label="Calibrate Climate")
ensure_compl     = Transition(label="Ensure Compliance")
select_crops     = Transition(label="Select Crops")
plant_seeds      = Transition(label="Plant Seeds")
monitor_growth   = Transition(label="Monitor Growth")
manage_pests     = Transition(label="Manage Pests")
recycle_waste    = Transition(label="Recycle Waste")
distribute_prod  = Transition(label="Distribute Produce")
engage_comm      = Transition(label="Engage Community")

# Initial setup sequence: site survey through planting seeds
init_nodes = [
    site_survey, design_modules, source_materials, install_frame,
    setup_irrigation, integrate_sens, configure_ai, calibrate_clm,
    ensure_compl, select_crops, plant_seeds
]
init_seq = StrictPartialOrder(nodes=init_nodes)
# enforce the sequential order
edges = list(zip(init_nodes, init_nodes[1:]))
for src, tgt in edges:
    init_seq.order.add_edge(src, tgt)

# Loop for iterative monitoring, pest management, waste recycling
# Body of loop: monitor growth
body = monitor_growth
# Redo branch: pest management and waste recycling can happen concurrently
redo = StrictPartialOrder(nodes=[manage_pests, recycle_waste])
# Define the loop operator
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[body, redo])

# After the loop, distribute produce and engage the community
# These two may proceed in parallel once the loop completes
root = StrictPartialOrder(nodes=[init_seq, growth_loop, distribute_prod, engage_comm])
root.order.add_edge(init_seq, growth_loop)
root.order.add_edge(growth_loop, distribute_prod)
root.order.add_edge(growth_loop, engage_comm)