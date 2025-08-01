# Generated from: 6ec63f82-ee19-4b5b-b81c-900cbb778f50.json
# Description: This process outlines the detailed steps involved in establishing an urban vertical farm within a repurposed industrial building. It begins with site analysis and environmental assessment, followed by modular system design and nutrient sourcing. The process includes installation of hydroponic towers, automated climate control calibration, and integration of renewable energy sources. Subsequent activities cover seed selection, germination monitoring, pest management without chemicals, and continuous growth optimization through AI analytics. Finally, the process addresses harvest scheduling, packaging automation, quality verification, and distribution logistics to local retailers, ensuring sustainability and minimal waste throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_analysis     = Transition(label='Site Analysis')
env_assessment    = Transition(label='Env Assessment')
modular_design    = Transition(label='Modular Design')
nutrient_sourcing = Transition(label='Nutrient Sourcing')
tower_install     = Transition(label='Tower Install')
climate_setup     = Transition(label='Climate Setup')
energy_integrate  = Transition(label='Energy Integrate')
seed_selection    = Transition(label='Seed Selection')
germination_check = Transition(label='Germination Check')
pest_control      = Transition(label='Pest Control')
growth_monitor    = Transition(label='Growth Monitor')
harvest_plan      = Transition(label='Harvest Plan')
packaging_auto    = Transition(label='Packaging Auto')
quality_check     = Transition(label='Quality Check')
distribution      = Transition(label='Distribution')

# Build the partial order (linear workflow)
root = StrictPartialOrder(nodes=[
    site_analysis, env_assessment, modular_design, nutrient_sourcing,
    tower_install, climate_setup, energy_integrate, seed_selection,
    germination_check, pest_control, growth_monitor, harvest_plan,
    packaging_auto, quality_check, distribution
])

# Define the sequence dependencies
edges = [
    (site_analysis,     env_assessment),
    (env_assessment,    modular_design),
    (modular_design,    nutrient_sourcing),
    (nutrient_sourcing, tower_install),
    (tower_install,     climate_setup),
    (climate_setup,     energy_integrate),
    (energy_integrate,  seed_selection),
    (seed_selection,    germination_check),
    (germination_check, pest_control),
    (pest_control,      growth_monitor),
    (growth_monitor,    harvest_plan),
    (harvest_plan,      packaging_auto),
    (packaging_auto,    quality_check),
    (quality_check,     distribution)
]

for src, tgt in edges:
    root.order.add_edge(src, tgt)