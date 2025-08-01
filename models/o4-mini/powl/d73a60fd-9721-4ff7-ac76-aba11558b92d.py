# Generated from: d73a60fd-9721-4ff7-ac76-aba11558b92d.json
# Description: This process outlines the establishment of an urban vertical farm integrating hydroponic and aeroponic systems within a multi-story building. It involves site analysis, structural adaptation, environmental control installation, nutrient cycling optimization, crop scheduling, energy management, pest monitoring, data analytics, waste recycling, and community engagement. The aim is to maximize crop yield in limited urban space while minimizing resource consumption and environmental impact, requiring coordination across engineering, agriculture, and sustainability teams.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
site_survey      = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
system_design    = Transition(label='System Design')
permit_filing    = Transition(label='Permit Filing')
foundation_prep  = Transition(label='Foundation Prep')
frame_build      = Transition(label='Frame Build')
irrigation_setup = Transition(label='Irrigation Setup')
lighting_install = Transition(label='Lighting Install')
climate_control  = Transition(label='Climate Control')
nutrient_mix     = Transition(label='Nutrient Mix')
crop_planting    = Transition(label='Crop Planting')
pest_scouting    = Transition(label='Pest Scouting')
data_monitoring  = Transition(label='Data Monitoring')
waste_sorting    = Transition(label='Waste Sorting')
energy_audit     = Transition(label='Energy Audit')
community_meet   = Transition(label='Community Meet')
yield_analysis   = Transition(label='Yield Analysis')

# Define the repeating (continuous) tasks as a concurrent block
continuous_tasks = StrictPartialOrder(
    nodes=[pest_scouting, data_monitoring, waste_sorting, energy_audit, community_meet]
)

# Loop operator: execute continuous_tasks at least once, then optionally repeat
skip = SilentTransition()
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[continuous_tasks, skip]
)

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        structural_audit,
        system_design,
        permit_filing,
        foundation_prep,
        frame_build,
        irrigation_setup,
        lighting_install,
        climate_control,
        nutrient_mix,
        crop_planting,
        loop,
        yield_analysis
    ]
)

# Sequential dependencies
o = root.order
o.add_edge(site_survey, structural_audit)
o.add_edge(structural_audit, system_design)
o.add_edge(system_design, permit_filing)
o.add_edge(permit_filing, foundation_prep)
o.add_edge(foundation_prep, frame_build)
o.add_edge(frame_build, irrigation_setup)
o.add_edge(irrigation_setup, lighting_install)
o.add_edge(lighting_install, climate_control)
o.add_edge(climate_control, nutrient_mix)
o.add_edge(nutrient_mix, crop_planting)
o.add_edge(crop_planting, loop)
o.add_edge(loop, yield_analysis)