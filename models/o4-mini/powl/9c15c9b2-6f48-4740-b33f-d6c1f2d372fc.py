# Generated from: 9c15c9b2-6f48-4740-b33f-d6c1f2d372fc.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm within a densely populated city. It includes site analysis, structural assessment, soil and water testing, regulatory approvals, system design, installation of hydroponic or soil beds, irrigation setup, crop selection, pest management planning, community engagement, staff training, monitoring systems installation, initial seeding, growth tracking, and finally harvest scheduling. The process requires collaboration between engineers, agronomists, city officials, and local communities to ensure environmental compliance, optimize yield, and promote urban green spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
t_site_survey    = Transition(label='Site Survey')
t_load_test      = Transition(label='Load Test')
t_soil_sample    = Transition(label='Soil Sample')
t_water_check    = Transition(label='Water Check')
t_permit_apply   = Transition(label='Permit Apply')
t_design_plan    = Transition(label='Design Plan')
t_bed_install    = Transition(label='Bed Install')
t_irrigation     = Transition(label='Irrigation Setup')
t_crop_select    = Transition(label='Crop Select')
t_pest_control   = Transition(label='Pest Control')
t_community_meet = Transition(label='Community Meet')
t_staff_train    = Transition(label='Staff Train')
t_sensor_install = Transition(label='Sensor Install')
t_seed_plant     = Transition(label='Seed Plant')
t_growth_monitor = Transition(label='Growth Monitor')
t_harvest_plan   = Transition(label='Harvest Plan')

# Loop for repeated growth monitoring
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[t_growth_monitor, skip])

# Build the partially ordered workflow
root = StrictPartialOrder(nodes=[
    t_site_survey, t_load_test,
    t_soil_sample, t_water_check,
    t_permit_apply, t_design_plan,
    t_bed_install, t_irrigation,
    t_crop_select, t_pest_control,
    t_community_meet, t_staff_train,
    t_sensor_install, t_seed_plant,
    loop, t_harvest_plan
])

o = root.order
o.add_edge(t_site_survey,    t_load_test)
o.add_edge(t_load_test,      t_soil_sample)
o.add_edge(t_load_test,      t_water_check)
o.add_edge(t_soil_sample,    t_permit_apply)
o.add_edge(t_water_check,    t_permit_apply)
o.add_edge(t_permit_apply,   t_design_plan)
o.add_edge(t_design_plan,    t_bed_install)
o.add_edge(t_design_plan,    t_irrigation)
o.add_edge(t_bed_install,    t_crop_select)
o.add_edge(t_irrigation,     t_crop_select)
o.add_edge(t_crop_select,    t_pest_control)
o.add_edge(t_bed_install,    t_community_meet)
o.add_edge(t_irrigation,     t_community_meet)
o.add_edge(t_bed_install,    t_staff_train)
o.add_edge(t_irrigation,     t_staff_train)
o.add_edge(t_bed_install,    t_sensor_install)
o.add_edge(t_irrigation,     t_sensor_install)
o.add_edge(t_crop_select,    t_seed_plant)
o.add_edge(t_pest_control,   t_seed_plant)
o.add_edge(t_sensor_install, t_seed_plant)
o.add_edge(t_bed_install,    t_seed_plant)
o.add_edge(t_irrigation,     t_seed_plant)
o.add_edge(t_seed_plant,     loop)
o.add_edge(loop,             t_harvest_plan)