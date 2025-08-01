# Generated from: f7af61c2-a8e6-4ba7-ab35-c489351b29ed.json
# Description: This process involves establishing a fully operational urban vertical farming system within a repurposed industrial building. It begins with site analysis and structural assessment, followed by modular farm design and environmental control installation. The process then moves to nutrient solution preparation, seed selection, and automated planting. Continuous monitoring of microclimate and plant health is conducted through IoT sensors, with adaptive lighting and irrigation adjustments. Waste recycling and energy optimization are integrated to ensure sustainability. Finally, the system undergoes rigorous quality assurance before commercial crop harvesting and distribution logistics are initiated, enabling efficient year-round urban agriculture production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Structure_Check = Transition(label='Structure Check')
Farm_Design = Transition(label='Farm Design')
Env_Control = Transition(label='Env Control')
Nutrient_Prep = Transition(label='Nutrient Prep')
Seed_Selection = Transition(label='Seed Selection')
Automated_Plant = Transition(label='Automated Plant')
Sensor_Setup = Transition(label='Sensor Setup')
Microclimate_Mon = Transition(label='Microclimate Mon')
Health_Monitor = Transition(label='Health Monitor')
Light_Adjust = Transition(label='Light Adjust')
Irrigation_Mod = Transition(label='Irrigation Mod')
Waste_Recycle = Transition(label='Waste Recycle')
Energy_Optimize = Transition(label='Energy Optimize')
Quality_Check = Transition(label='Quality Check')
Crop_Harvest = Transition(label='Crop Harvest')
Distribution_Plan = Transition(label='Distribution Plan')

# Build concurrent monitoring partial order:
# Sensor_Setup --> {Microclimate_Mon, Health_Monitor}, which run concurrently
monitoring = StrictPartialOrder(nodes=[Sensor_Setup, Microclimate_Mon, Health_Monitor])
monitoring.order.add_edge(Sensor_Setup, Microclimate_Mon)
monitoring.order.add_edge(Sensor_Setup, Health_Monitor)

# Build concurrent adjustment partial order:
# Microclimate_Mon, Health_Monitor --> concurrent Light_Adjust and Irrigation_Mod
adjust = StrictPartialOrder(nodes=[monitoring, Light_Adjust, Irrigation_Mod])
adjust.order.add_edge(monitoring, Light_Adjust)
adjust.order.add_edge(monitoring, Irrigation_Mod)

# Nutrient Prep, Seed Selection, Automated Plant in sequence
prep_seq = StrictPartialOrder(nodes=[Nutrient_Prep, Seed_Selection, Automated_Plant])
prep_seq.order.add_edge(Nutrient_Prep, Seed_Selection)
prep_seq.order.add_edge(Seed_Selection, Automated_Plant)

# Waste Recycle and Energy Optimize concurrent
waste_energy = StrictPartialOrder(nodes=[Waste_Recycle, Energy_Optimize])
# no order edges = concurrent

# Initial site and design sequence: Site Analysis --> Structure Check --> Farm Design --> Env Control
site_design = StrictPartialOrder(nodes=[Site_Analysis, Structure_Check, Farm_Design, Env_Control])
site_design.order.add_edge(Site_Analysis, Structure_Check)
site_design.order.add_edge(Structure_Check, Farm_Design)
site_design.order.add_edge(Farm_Design, Env_Control)

# Combine all preparation before monitoring: site_design --> prep_seq
prep_before_monitor = StrictPartialOrder(nodes=[site_design, prep_seq])
prep_before_monitor.order.add_edge(site_design, prep_seq)

# The monitoring and adjustment and waste/energy can run concurrently after prep
# combine (monitoring + adjustments) and waste_energy concurrently
monitoring_and_adjust = adjust
post_prep_concurrent1 = StrictPartialOrder(nodes=[monitoring_and_adjust, waste_energy])
# no order edges between them (concurrent)

# combine all after prep:
after_prep = StrictPartialOrder(nodes=[post_prep_concurrent1])
# No explicit order edge inside after_prep; to be linked with previous

# Overall before QA: prep_before_monitor --> after_prep
before_qa = StrictPartialOrder(nodes=[prep_before_monitor, post_prep_concurrent1])
before_qa.order.add_edge(prep_before_monitor, post_prep_concurrent1)

# Final QA followed by Crop Harvest and Distribution Plan sequence:
qa_and_harvest = StrictPartialOrder(nodes=[Quality_Check, Crop_Harvest, Distribution_Plan])
qa_and_harvest.order.add_edge(Quality_Check, Crop_Harvest)
qa_and_harvest.order.add_edge(Crop_Harvest, Distribution_Plan)

# Complete process: before_qa --> qa_and_harvest
root = StrictPartialOrder(nodes=[before_qa, qa_and_harvest])
root.order.add_edge(before_qa, qa_and_harvest)