# Generated from: 3fe5e06f-9b5f-4a35-9e1f-81848aa44b12.json
# Description: This process outlines the integration of urban vertical farming systems within existing city infrastructure to optimize local food production, reduce transportation emissions, and promote sustainable agriculture. It involves site assessment, modular farm installation, IoT sensor deployment for environment monitoring, nutrient recycling, energy management, crop scheduling, automated harvesting, quality assurance, data analytics, community engagement, and regulatory compliance. The process ensures seamless coordination between technology providers, municipal authorities, and local communities, fostering innovation while addressing urban food security and ecological impact through continuous improvement and scalability planning.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permit_review = Transition(label='Permit Review')
modular_install = Transition(label='Modular Install')
sensor_setup = Transition(label='Sensor Setup')
nutrient_mix = Transition(label='Nutrient Mix')
energy_sync = Transition(label='Energy Sync')
crop_plan = Transition(label='Crop Plan')
irrigation_tune = Transition(label='Irrigation Tune')
harvest_automate = Transition(label='Harvest Automate')
quality_check = Transition(label='Quality Check')
data_analysis = Transition(label='Data Analysis')
waste_recycle = Transition(label='Waste Recycle')
community_meet = Transition(label='Community Meet')
compliance_audit = Transition(label='Compliance Audit')
scale_strategy = Transition(label='Scale Strategy')

# Model:
# Logical sequence with some concurrency and control structures:
# 1) Site Survey --> Design Layout --> Permit Review
# 2) Then Modular Install and Sensor Setup can be concurrent
# 3) After that Nutrient Mix, Energy Sync in parallel (concurrent)
# 4) Crop Plan comes after Nutrient Mix and Energy Sync
# 5) Irrigation Tune after Crop Plan
# 6) Harvest Automate after Irrigation Tune
# 7) Quality Check and Data Analysis can be concurrent after Harvest Automate
# 8) Waste Recycle runs concurrently with Quality Check and Data Analysis (all three parallel)
# 9) Community Meet after Quality Check
# 10) Compliance Audit after Community Meet and Data Analysis
# 11) Scale Strategy as a loop node: run Scale Strategy, then either exit or go back (continuous improvement)

# Create partial order for initial sequence and concurrency
init_po = StrictPartialOrder(nodes=[
    site_survey, design_layout, permit_review,
    modular_install, sensor_setup,
    nutrient_mix, energy_sync,
    crop_plan, irrigation_tune, harvest_automate,
    quality_check, data_analysis, waste_recycle,
    community_meet, compliance_audit
])

# Add order edges for initial sequence
init_po.order.add_edge(site_survey, design_layout)
init_po.order.add_edge(design_layout, permit_review)

# permit_review --> modular_install and sensor_setup (concurrent)
init_po.order.add_edge(permit_review, modular_install)
init_po.order.add_edge(permit_review, sensor_setup)

# modular_install and sensor_setup --> nutrient_mix and energy_sync (concurrent)
init_po.order.add_edge(modular_install, nutrient_mix)
init_po.order.add_edge(sensor_setup, nutrient_mix)
init_po.order.add_edge(modular_install, energy_sync)
init_po.order.add_edge(sensor_setup, energy_sync)

# nutrient_mix and energy_sync --> crop_plan
init_po.order.add_edge(nutrient_mix, crop_plan)
init_po.order.add_edge(energy_sync, crop_plan)

# crop_plan --> irrigation_tune --> harvest_automate
init_po.order.add_edge(crop_plan, irrigation_tune)
init_po.order.add_edge(irrigation_tune, harvest_automate)

# harvest_automate --> quality_check, data_analysis, waste_recycle (concurrent)
init_po.order.add_edge(harvest_automate, quality_check)
init_po.order.add_edge(harvest_automate, data_analysis)
init_po.order.add_edge(harvest_automate, waste_recycle)

# quality_check --> community_meet
init_po.order.add_edge(quality_check, community_meet)

# community_meet and data_analysis --> compliance_audit
init_po.order.add_edge(community_meet, compliance_audit)
init_po.order.add_edge(data_analysis, compliance_audit)

# Loop on scale_strategy after compliance_audit
loop = OperatorPOWL(operator=Operator.LOOP, children=[scale_strategy, SilentTransition()])

# compliance_audit --> loop (scale strategy)
root = StrictPartialOrder(nodes=[init_po, loop])
root.order.add_edge(init_po, loop)