# Generated from: 197f8a0b-7bfd-43fe-9af7-de1d1ffb6e98.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farm within a repurposed industrial building. It covers initial site assessment, environmental impact analysis, structural modifications, hydroponic system design, nutrient cycle planning, automation integration, staff training, regulatory compliance, and market launch strategies. The approach uniquely combines architectural retrofitting with advanced agricultural technology to maximize yield in limited urban spaces, addressing sustainability and fresh local produce demand while navigating complex zoning laws and community engagement requirements.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey      = Transition(label='Site Survey')
impact_study     = Transition(label='Impact Study')
design_layout    = Transition(label='Design Layout')
permit_filing    = Transition(label='Permit Filing')
structure_mod    = Transition(label='Structure Mod')
system_install   = Transition(label='System Install')
nutrient_plan    = Transition(label='Nutrient Plan')
water_setup      = Transition(label='Water Setup')
lighting_config  = Transition(label='Lighting Config')
automation_test  = Transition(label='Automation Test')
staff_onboard    = Transition(label='Staff Onboard')
compliance_check = Transition(label='Compliance Check')
trial_grow       = Transition(label='Trial Grow')
harvest_eval     = Transition(label='Harvest Eval')
market_launch    = Transition(label='Market Launch')

# Hydroponic sub‐process: these four steps can proceed in parallel
hydro = StrictPartialOrder(
    nodes=[system_install, nutrient_plan, water_setup, lighting_config]
)

# Root partial order: the overall process
root = StrictPartialOrder(
    nodes=[
        site_survey,
        impact_study,
        design_layout,
        permit_filing,
        structure_mod,
        hydro,
        automation_test,
        staff_onboard,
        compliance_check,
        trial_grow,
        harvest_eval,
        market_launch
    ]
)

# Define the control flow (dependencies)
root.order.add_edge(site_survey, impact_study)
root.order.add_edge(impact_study, design_layout)
root.order.add_edge(design_layout, permit_filing)
root.order.add_edge(permit_filing, structure_mod)
root.order.add_edge(structure_mod, hydro)             # enter hydroponic parallel block
root.order.add_edge(hydro, automation_test)            # after all hydro steps complete
root.order.add_edge(automation_test, staff_onboard)
root.order.add_edge(staff_onboard, compliance_check)
root.order.add_edge(compliance_check, trial_grow)
root.order.add_edge(trial_grow, harvest_eval)
root.order.add_edge(harvest_eval, market_launch)