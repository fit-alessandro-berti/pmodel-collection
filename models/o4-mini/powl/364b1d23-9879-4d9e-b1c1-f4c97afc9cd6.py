# Generated from: 364b1d23-9879-4d9e-b1c1-f4c97afc9cd6.json
# Description: This process outlines the complex and innovative steps involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It includes site assessment, climate control system design, modular planting structure assembly, nutrient recycling setup, automation integration for irrigation and lighting, pest management protocols, and real-time data analytics deployment. The workflow ensures sustainability through energy efficiency, waste minimization, and crop yield optimization, while addressing urban zoning regulations and community engagement for local produce distribution. This atypical but realistic process requires multidisciplinary coordination among architects, agronomists, engineers, and IT specialists to successfully create a scalable vertical farming ecosystem in a constrained urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
zoning_check     = Transition(label='Zoning Check')
design_layout    = Transition(label='Design Layout')
climate_setup    = Transition(label='Climate Setup')
structure_build  = Transition(label='Structure Build')
irrigation_install = Transition(label='Irrigation Install')
lighting_setup   = Transition(label='Lighting Setup')
automation_config = Transition(label='Automation Config')
nutrient_mix     = Transition(label='Nutrient Mix')
pest_control     = Transition(label='Pest Control')
data_analytics   = Transition(label='Data Analytics')
energy_audit     = Transition(label='Energy Audit')
waste_manage     = Transition(label='Waste Manage')
staff_training   = Transition(label='Staff Training')
launch_crop      = Transition(label='Launch Crop')
market_setup     = Transition(label='Market Setup')
community_meet   = Transition(label='Community Meet')

# Define loop for continuous management: analytics then mix & pest before analytics again
loop_body = StrictPartialOrder(nodes=[nutrient_mix, pest_control])
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analytics, loop_body])

# Assemble the root partial order
root = StrictPartialOrder(nodes=[
    site_survey, zoning_check, design_layout, climate_setup, structure_build,
    irrigation_install, lighting_setup, automation_config, loop,
    energy_audit, waste_manage, staff_training, launch_crop,
    market_setup, community_meet
])

# Define ordering constraints
o = root.order
o.add_edge(site_survey, zoning_check)
o.add_edge(zoning_check, design_layout)
o.add_edge(design_layout, climate_setup)
o.add_edge(design_layout, structure_build)
o.add_edge(structure_build, irrigation_install)
o.add_edge(structure_build, lighting_setup)
o.add_edge(irrigation_install, automation_config)
o.add_edge(lighting_setup, automation_config)
o.add_edge(automation_config, loop)
o.add_edge(loop, energy_audit)
o.add_edge(energy_audit, waste_manage)
o.add_edge(waste_manage, staff_training)
o.add_edge(staff_training, launch_crop)
o.add_edge(launch_crop, market_setup)
o.add_edge(launch_crop, community_meet)