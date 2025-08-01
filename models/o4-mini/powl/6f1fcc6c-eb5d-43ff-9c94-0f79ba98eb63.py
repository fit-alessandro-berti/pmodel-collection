# Generated from: 6f1fcc6c-eb5d-43ff-9c94-0f79ba98eb63.json
# Description: This process involves establishing a multi-tiered urban vertical farm within a repurposed industrial building. It encompasses site analysis, environmental control system installation, hydroponic infrastructure setup, nutrient formulation, automated monitoring deployment, crop seeding, growth cycle management, pest control using integrated biological agents, harvesting, post-harvest processing, quality assurance, packaging, logistics coordination, and sustainable waste recycling. The complexity arises from integrating cutting-edge agricultural technology with urban architectural constraints, regulatory compliance, and real-time data analytics to maximize yield and minimize environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
install_hvac = Transition(label='Install HVAC')
setup_hydro = Transition(label='Setup Hydroponics')
formulate_nutrients = Transition(label='Formulate Nutrients')
deploy_sensors = Transition(label='Deploy Sensors')
seed_crops = Transition(label='Seed Crops')
monitor_growth = Transition(label='Monitor Growth')
apply_biocontrol = Transition(label='Apply Biocontrol')
harvest_crops = Transition(label='Harvest Crops')
process_yield = Transition(label='Process Yield')
quality_check = Transition(label='Quality Check')
package_produce = Transition(label='Package Produce')
arrange_transport = Transition(label='Arrange Transport')
recycle_waste = Transition(label='Recycle Waste')

# Silent transition for loop exit
skip = SilentTransition()

# Define growth-cycle subprocess: monitor -> biocontrol
growth_seq = StrictPartialOrder(nodes=[monitor_growth, apply_biocontrol])
growth_seq.order.add_edge(monitor_growth, apply_biocontrol)

# Loop: repeat the growth sequence until exit
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_seq, skip])

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        design_layout,
        install_hvac,
        setup_hydro,
        formulate_nutrients,
        deploy_sensors,
        seed_crops,
        growth_loop,
        harvest_crops,
        process_yield,
        quality_check,
        package_produce,
        arrange_transport,
        recycle_waste
    ]
)

# Control‐flow edges
# 1. Site survey → design layout
root.order.add_edge(site_survey, design_layout)
# 2. Design → {HVAC, Hydroponics} in parallel
root.order.add_edge(design_layout, install_hvac)
root.order.add_edge(design_layout, setup_hydro)
# 3. After both infrastructure tasks: {Nutrients, Sensors} in parallel
root.order.add_edge(install_hvac, formulate_nutrients)
root.order.add_edge(setup_hydro, formulate_nutrients)
root.order.add_edge(install_hvac, deploy_sensors)
root.order.add_edge(setup_hydro, deploy_sensors)
# 4. Nutrients & Sensors → Seed crops
root.order.add_edge(formulate_nutrients, seed_crops)
root.order.add_edge(deploy_sensors, seed_crops)
# 5. Seeding → start growth loop
root.order.add_edge(seed_crops, growth_loop)
# 6. After exiting loop → harvest → process → QA → package → transport → recycle
root.order.add_edge(growth_loop, harvest_crops)
root.order.add_edge(harvest_crops, process_yield)
root.order.add_edge(process_yield, quality_check)
root.order.add_edge(quality_check, package_produce)
root.order.add_edge(package_produce, arrange_transport)
root.order.add_edge(arrange_transport, recycle_waste)