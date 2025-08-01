# Generated from: fad49fb1-5a35-4525-b63f-51323e5e4367.json
# Description: This process describes the complex orchestration involved in establishing a fully operational urban vertical farm within a repurposed high-rise building. It involves site assessment, modular system design, resource sourcing, automation integration, environmental calibration, crop selection tailored to microclimates, iterative growth monitoring, pest management without chemicals, waste recycling, community engagement for local distribution, and compliance with urban agriculture regulations. The process ensures sustainable production with minimal environmental impact while optimizing yield and energy efficiency through advanced IoT and AI-driven controls.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Modules = Transition(label='Design Modules')
Source_Materials = Transition(label='Source Materials')
Install_Framework = Transition(label='Install Framework')
Setup_Irrigation = Transition(label='Setup Irrigation')
Integrate_Sensors = Transition(label='Integrate Sensors')
Configure_AI = Transition(label='Configure AI')
Select_Crops = Transition(label='Select Crops')
Calibrate_Climate = Transition(label='Calibrate Climate')
Plant_Seeds = Transition(label='Plant Seeds')
Monitor_Growth = Transition(label='Monitor Growth')
Manage_Pests = Transition(label='Manage Pests')
Recycle_Waste = Transition(label='Recycle Waste')
Engage_Community = Transition(label='Engage Community')
Ensure_Compliance = Transition(label='Ensure Compliance')
Distribute_Produce = Transition(label='Distribute Produce')

# Model iterative growth monitoring and pest management as a loop:
# LOOP(Monitor Growth, Manage Pests)
growth_pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[Monitor_Growth, Manage_Pests])

# After planting seeds, the loop of monitoring growth and managing pests occurs repeatedly
plant_and_monitor = StrictPartialOrder(nodes=[Plant_Seeds, growth_pest_loop])
plant_and_monitor.order.add_edge(Plant_Seeds, growth_pest_loop)

# After Integrate Sensors comes Configure AI and Calibrate Climate (likely parallel, both depend on sensors)
# Partial order with Configure_AI and Calibrate_Climate concurrent after Integrate_Sensors
sensors_ai_calibration = StrictPartialOrder(nodes=[Integrate_Sensors, Configure_AI, Calibrate_Climate])
sensors_ai_calibration.order.add_edge(Integrate_Sensors, Configure_AI)
sensors_ai_calibration.order.add_edge(Integrate_Sensors, Calibrate_Climate)

# Crop selection depends on Calibrate Climate (tailoring crops to microclimates)
select_crops_after_calibration = StrictPartialOrder(nodes=[Calibrate_Climate, Select_Crops])
select_crops_after_calibration.order.add_edge(Calibrate_Climate, Select_Crops)

# The Design, Source, Install, and Setup represent core modular system design and installation:
design_source_install = StrictPartialOrder(
    nodes=[Design_Modules, Source_Materials, Install_Framework, Setup_Irrigation]
)
design_source_install.order.add_edge(Design_Modules, Source_Materials)
design_source_install.order.add_edge(Source_Materials, Install_Framework)
design_source_install.order.add_edge(Install_Framework, Setup_Irrigation)

# Community engagement and compliance and distribution are final steps, likely parallel:
community_compliance_distribution = StrictPartialOrder(
    nodes=[Engage_Community, Ensure_Compliance, Distribute_Produce]
)
# Engage_Community must precede Distribute_Produce
community_compliance_distribution.order.add_edge(Engage_Community, Distribute_Produce)
# Ensure_Compliance must precede Distribute_Produce
community_compliance_distribution.order.add_edge(Ensure_Compliance, Distribute_Produce)

# Waste recycling can be concurrent with community engagement or compliance, no strict order needed
# Let's add Recycle Waste concurrent with community and compliance activities:
final_activities = StrictPartialOrder(
    nodes=[Recycle_Waste, community_compliance_distribution]
)
# The StrictPartialOrder nodes here include another StrictPartialOrder (community_compliance_distribution),
# so to avoid nesting issues, we flatten those nodes:

# Flatten nodes for final_activities manually
final_nodes = [Recycle_Waste, Engage_Community, Ensure_Compliance, Distribute_Produce]
final_order = StrictPartialOrder(nodes=final_nodes)
final_order.order.add_edge(Engage_Community, Distribute_Produce)
final_order.order.add_edge(Ensure_Compliance, Distribute_Produce)

# Top-level partial order:
# Site Survey -> Design_Source_Install_Setup -> sensors_ai_calibration -> select_crops_after_calibration
# -> plant_and_monitor -> final_order

root = StrictPartialOrder(
    nodes=[
        Site_Survey,
        design_source_install,
        sensors_ai_calibration,
        select_crops_after_calibration,
        plant_and_monitor,
        final_order
    ]
)

# Add edges to reflect order
root.order.add_edge(Site_Survey, design_source_install)
root.order.add_edge(design_source_install, sensors_ai_calibration)
root.order.add_edge(sensors_ai_calibration, select_crops_after_calibration)
root.order.add_edge(select_crops_after_calibration, plant_and_monitor)
root.order.add_edge(plant_and_monitor, final_order)