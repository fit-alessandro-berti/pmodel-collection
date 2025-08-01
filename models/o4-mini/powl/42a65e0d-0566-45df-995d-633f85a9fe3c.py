# Generated from: 42a65e0d-0566-45df-995d-633f85a9fe3c.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes initial site analysis, structural retrofitting, environmental system installation, crop selection based on microclimate data, automation setup for irrigation and lighting, nutrient solution calibration, pest control integration, workforce training for hydroponic techniques, and compliance with urban agricultural regulations. The process ensures sustainable resource use, optimized crop yields, and integration with local distribution networks, enabling fresh produce supply in dense metropolitan areas while minimizing ecological impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# define activities
site_survey      = Transition(label='Site Survey')
structure_assess = Transition(label='Structure Assess')
retrofit_plan    = Transition(label='Retrofit Plan')
climate_study    = Transition(label='Climate Study')
system_design    = Transition(label='System Design')
install_lighting = Transition(label='Install Lighting')
setup_irrigation = Transition(label='Setup Irrigation')
nutrient_mix     = Transition(label='Nutrient Mix')
crop_select      = Transition(label='Crop Select')
automation_config= Transition(label='Automation Config')
pest_control     = Transition(label='Pest Control')
staff_training   = Transition(label='Staff Training')
compliance_check = Transition(label='Compliance Check')
yield_monitor    = Transition(label='Yield Monitor')
market_launch    = Transition(label='Market Launch')

# assemble the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey,
    structure_assess,
    retrofit_plan,
    climate_study,
    system_design,
    install_lighting,
    setup_irrigation,
    nutrient_mix,
    crop_select,
    automation_config,
    pest_control,
    staff_training,
    compliance_check,
    yield_monitor,
    market_launch
])

# define the ordering relations
o = root.order
o.add_edge(site_survey,      structure_assess)
o.add_edge(site_survey,      climate_study)
o.add_edge(structure_assess, retrofit_plan)
o.add_edge(retrofit_plan,    system_design)
o.add_edge(climate_study,    system_design)
o.add_edge(system_design,    install_lighting)
o.add_edge(system_design,    setup_irrigation)
o.add_edge(system_design,    pest_control)
o.add_edge(install_lighting, automation_config)
o.add_edge(setup_irrigation, automation_config)
o.add_edge(automation_config,nutrient_mix)
o.add_edge(climate_study,    crop_select)
o.add_edge(crop_select,      nutrient_mix)
o.add_edge(crop_select,      pest_control)
o.add_edge(pest_control,     staff_training)
o.add_edge(automation_config,staff_training)
o.add_edge(staff_training,   compliance_check)
o.add_edge(pest_control,     compliance_check)
o.add_edge(compliance_check, yield_monitor)
o.add_edge(nutrient_mix,     yield_monitor)
o.add_edge(yield_monitor,    market_launch)