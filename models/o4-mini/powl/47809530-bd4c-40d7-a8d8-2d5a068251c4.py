# Generated from: 47809530-bd4c-40d7-a8d8-2d5a068251c4.json
# Description: This process outlines the end-to-end setup of an urban vertical farming system within a repurposed industrial building. It begins with site evaluation and structural reinforcement, followed by installation of hydroponic racks, climate control units, and automated nutrient delivery systems. Subsequent activities include sensor calibration, seed selection, germination, and crop rotation planning. The process incorporates energy optimization, waste recycling, and integration of AI-driven growth monitoring to maximize yield. Finally, it covers staff training, compliance audits, and launch coordination to ensure sustainable, high-efficiency urban agriculture operations in a constrained environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
site_eval = Transition(label='Site Eval')
structure_check = Transition(label='Structure Check')
rack_install = Transition(label='Rack Install')
climate_setup = Transition(label='Climate Setup')
nutrient_config = Transition(label='Nutrient Config')
sensor_calibrate = Transition(label='Sensor Calibrate')
seed_select = Transition(label='Seed Select')
germination = Transition(label='Germination')
crop_plan = Transition(label='Crop Plan')
energy_audit = Transition(label='Energy Audit')
waste_setup = Transition(label='Waste Setup')
ai_integrate = Transition(label='AI Integrate')
staff_train = Transition(label='Staff Train')
compliance_review = Transition(label='Compliance Review')
launch_prep = Transition(label='Launch Prep')

# Create the partial‐order model
root = StrictPartialOrder(nodes=[
    site_eval, structure_check,
    rack_install, climate_setup, nutrient_config,
    sensor_calibrate, seed_select, germination,
    crop_plan, energy_audit, waste_setup, ai_integrate,
    staff_train, compliance_review, launch_prep
])

# Define the control‐flow dependencies

# 1. Site evaluation → structure check
root.order.add_edge(site_eval, structure_check)

# 2. After structure check, install racks, climate units, nutrient system in parallel
root.order.add_edge(structure_check, rack_install)
root.order.add_edge(structure_check, climate_setup)
root.order.add_edge(structure_check, nutrient_config)

# 3. Sensor calibration awaits all three installs
root.order.add_edge(rack_install, sensor_calibrate)
root.order.add_edge(climate_setup, sensor_calibrate)
root.order.add_edge(nutrient_config, sensor_calibrate)

# 4. Seed selection can start after structure check (independent of installs)
root.order.add_edge(structure_check, seed_select)

# 5. Germination requires both sensor calibrate and seed select
root.order.add_edge(sensor_calibrate, germination)
root.order.add_edge(seed_select, germination)

# 6. Crop rotation planning after germination
root.order.add_edge(germination, crop_plan)

# 7. Energy audit, waste setup, AI integration run in parallel after crop planning
root.order.add_edge(crop_plan, energy_audit)
root.order.add_edge(crop_plan, waste_setup)
root.order.add_edge(crop_plan, ai_integrate)

# 8. Staff training and compliance review both require completion of energy, waste, and AI tasks
for prep_task in (energy_audit, waste_setup, ai_integrate):
    root.order.add_edge(prep_task, staff_train)
    root.order.add_edge(prep_task, compliance_review)

# 9. Launch preparation after both staff training and compliance review
root.order.add_edge(staff_train, launch_prep)
root.order.add_edge(compliance_review, launch_prep)