# Generated from: 177afcd8-21b2-46ac-b9a7-7849076acae8.json
# Description: This process involves the intricate planning and establishment of a vertical farming system within an urban environment, integrating advanced hydroponic techniques, renewable energy sources, and smart automation. It begins with site analysis and zoning compliance, followed by modular unit design and nutrient solution formulation. The process includes climate control calibration, seed selection, and planting schedules tailored for maximum yield in limited space. Continuous monitoring through IoT sensors ensures optimal growth conditions, while waste recycling loops convert organic residues into biofertilizers. Post-harvest procedures encompass automated picking, quality grading, and packaging for local distribution. Stakeholder coordination and periodic system audits guarantee sustainable operation and scalability in dense city landscapes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# define all activities
site_analysis     = Transition(label='Site Analysis')
zoning_check      = Transition(label='Zoning Check')
unit_design       = Transition(label='Unit Design')
nutrient_prep     = Transition(label='Nutrient Prep')
climate_setup     = Transition(label='Climate Setup')
seed_selection    = Transition(label='Seed Selection')
planting_plan     = Transition(label='Planting Plan')
sensor_install    = Transition(label='Sensor Install')
growth_monitor    = Transition(label='Growth Monitor')
waste_recycle     = Transition(label='Waste Recycle')
biofertilizer_make= Transition(label='Biofertilizer Make')
automated_harvest = Transition(label='Automated Harvest')
quality_grade     = Transition(label='Quality Grade')
packaging_prep    = Transition(label='Packaging Prep')
local_dispatch    = Transition(label='Local Dispatch')
stakeholder_meet  = Transition(label='Stakeholder Meet')
system_audit      = Transition(label='System Audit')

# define loops
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle, biofertilizer_make])
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_meet, system_audit])

# build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis, zoning_check, unit_design, nutrient_prep,
    climate_setup, seed_selection, planting_plan,
    sensor_install, growth_monitor,
    waste_loop,
    automated_harvest, quality_grade, packaging_prep,
    audit_loop,
    local_dispatch
])

# add control-flow dependencies
o = root.order
o.add_edge(site_analysis, zoning_check)
o.add_edge(zoning_check, unit_design)
o.add_edge(unit_design, nutrient_prep)
o.add_edge(nutrient_prep, climate_setup)
o.add_edge(climate_setup, seed_selection)
o.add_edge(seed_selection, planting_plan)

o.add_edge(planting_plan, sensor_install)
o.add_edge(planting_plan, waste_loop)

o.add_edge(sensor_install, growth_monitor)
o.add_edge(growth_monitor, automated_harvest)
o.add_edge(waste_loop, automated_harvest)

o.add_edge(automated_harvest, quality_grade)
o.add_edge(quality_grade, packaging_prep)

o.add_edge(packaging_prep, audit_loop)
o.add_edge(audit_loop, local_dispatch)