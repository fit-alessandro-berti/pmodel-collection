# Generated from: 6fde2d59-127e-4ac2-aaab-e85fd63875f4.json
# Description: This process outlines the comprehensive cycle of urban vertical farming in a controlled environment. It begins with site assessment and structural installation, followed by seed selection and nutrient solution preparation. Automated planting and environmental monitoring ensure optimal growth. Pest control and disease detection use AI-driven sensors. Harvesting is scheduled based on maturity data, after which post-harvest processing including cleaning, packaging, and quality inspection occurs. The produce is then distributed via smart logistics to urban markets. Maintenance of the farming units and data analytics for yield improvement complete the cycle, integrating sustainability and technology in an atypical agricultural business model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_assess       = Transition(label='Site Assess')
install_structure = Transition(label='Install Structure')
select_seeds      = Transition(label='Select Seeds')
prepare_nutrients = Transition(label='Prepare Nutrients')
automate_planting = Transition(label='Automate Planting')
monitor_climate   = Transition(label='Monitor Climate')
detect_pests      = Transition(label='Detect Pests')
control_disease   = Transition(label='Control Disease')
schedule_harvest  = Transition(label='Schedule Harvest')
harvest_crops     = Transition(label='Harvest Crops')
clean_produce     = Transition(label='Clean Produce')
package_goods     = Transition(label='Package Goods')
inspect_quality   = Transition(label='Inspect Quality')
distribute_goods  = Transition(label='Distribute Goods')
maintain_units    = Transition(label='Maintain Units')
analyze_data      = Transition(label='Analyze Data')

# A = initial one‐time setup: site assessment followed by structure installation
A = StrictPartialOrder(nodes=[site_assess, install_structure])
A.order.add_edge(site_assess, install_structure)

# B = the recurring cycle of farming tasks
B_nodes = [
    select_seeds,
    prepare_nutrients,
    automate_planting,
    monitor_climate,
    detect_pests,
    control_disease,
    schedule_harvest,
    harvest_crops,
    clean_produce,
    package_goods,
    inspect_quality,
    distribute_goods,
    maintain_units,
    analyze_data
]
B = StrictPartialOrder(nodes=B_nodes)

# seed selection and nutrient prep concur, both precede planting
B.order.add_edge(select_seeds, automate_planting)
B.order.add_edge(prepare_nutrients, automate_planting)

# after planting: monitor climate and detect pests in parallel
B.order.add_edge(automate_planting, monitor_climate)
B.order.add_edge(automate_planting, detect_pests)

# pest detection precedes disease control
B.order.add_edge(detect_pests, control_disease)

# both climate monitoring and disease control lead to harvest scheduling
B.order.add_edge(monitor_climate, schedule_harvest)
B.order.add_edge(control_disease, schedule_harvest)

# scheduling precedes actual harvest
B.order.add_edge(schedule_harvest, harvest_crops)

# post‐harvest processing in sequence: clean → package → inspect → distribute
B.order.add_edge(harvest_crops, clean_produce)
B.order.add_edge(clean_produce, package_goods)
B.order.add_edge(package_goods, inspect_quality)
B.order.add_edge(inspect_quality, distribute_goods)

# after distribution: maintenance and data analysis can run in parallel
B.order.add_edge(distribute_goods, maintain_units)
B.order.add_edge(distribute_goods, analyze_data)

# Wrap it all in a LOOP: do A once, then repeat B until exit
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])