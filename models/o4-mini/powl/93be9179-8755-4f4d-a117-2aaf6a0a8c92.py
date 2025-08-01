# Generated from: 93be9179-8755-4f4d-a117-2aaf6a0a8c92.json
# Description: This process outlines the complex and atypical steps involved in establishing a vertical farm within an urban environment. It begins with site evaluation focusing on structural integrity and sunlight availability, followed by modular design planning tailored to limited urban space. The process integrates hydroponic system installation, climate control calibration, and IoT sensor deployment for real-time monitoring. It includes nutrient solution preparation, seed selection based on urban crop suitability, and automated planting schedules. Additionally, energy optimization through renewable sources is implemented alongside waste recycling protocols. The final stages involve staff training on specialized equipment, compliance checks with urban agricultural regulations, and community engagement for local food distribution, ensuring a sustainable and efficient vertical farming operation within city limits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define all activities as POWL transitions
site_eval = Transition(label='Site Eval')
design_plan = Transition(label='Design Plan')
hydro_install = Transition(label='Hydroponic Install')
climate_setup = Transition(label='Climate Setup')
sensor_deploy = Transition(label='Sensor Deploy')
nutrient_prep = Transition(label='Nutrient Prep')
seed_select = Transition(label='Seed Select')
automate_plant = Transition(label='Automate Plant')
energy_opt = Transition(label='Energy Optimize')
waste_recycle = Transition(label='Waste Recycle')
staff_train = Transition(label='Staff Train')
compliance_check = Transition(label='Compliance Check')
community_meet = Transition(label='Community Meet')
harvest_plan = Transition(label='Harvest Plan')
data_analyze = Transition(label='Data Analyze')

# Create the root partial order with all nodes
root = StrictPartialOrder(nodes=[
    site_eval, design_plan,
    hydro_install, climate_setup, sensor_deploy,
    nutrient_prep, seed_select, automate_plant,
    energy_opt, waste_recycle,
    staff_train, compliance_check, community_meet,
    harvest_plan, data_analyze
])

# 1) Site Eval -> Design Plan
root.order.add_edge(site_eval, design_plan)

# 2) After design, install, climate setup, and sensor deploy can run in parallel
for nxt in (hydro_install, climate_setup, sensor_deploy):
    root.order.add_edge(design_plan, nxt)

# 3) Once infrastructure is in place, prepare nutrients, select seeds, and automate planting
for pre in (hydro_install, climate_setup, sensor_deploy):
    for nxt in (nutrient_prep, seed_select, automate_plant):
        root.order.add_edge(pre, nxt)

# 4) After those three, optimize energy and recycle waste (can run in parallel)
for pre in (nutrient_prep, seed_select, automate_plant):
    for nxt in (energy_opt, waste_recycle):
        root.order.add_edge(pre, nxt)

# 5) Once energy & waste protocols are set, train staff, check compliance, and meet community
for pre in (energy_opt, waste_recycle):
    for nxt in (staff_train, compliance_check, community_meet):
        root.order.add_edge(pre, nxt)

# 6) Final planning and analysis after training, compliance checks, and community engagement
for pre in (staff_train, compliance_check, community_meet):
    for nxt in (harvest_plan, data_analyze):
        root.order.add_edge(pre, nxt)