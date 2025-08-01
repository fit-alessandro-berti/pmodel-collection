# Generated from: 4e290359-723a-4e31-8ea0-fd83591a47f4.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farm within a dense metropolitan area. It involves site analysis, environmental impact assessments, modular system design, multi-layer crop planning, automated nutrient delivery setup, energy optimization strategies, integration with local supply chains, community engagement, regulatory compliance, and ongoing maintenance protocols. The process demands coordination between agricultural experts, engineers, urban planners, and marketing teams to ensure sustainable production of fresh produce while minimizing ecological footprints and maximizing yield within limited urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
impact_study    = Transition(label='Impact Study')
modular_design  = Transition(label='Modular Design')
crop_mapping    = Transition(label='Crop Mapping')
sensor_install  = Transition(label='Sensor Install')
irrigation_setup= Transition(label='Irrigation Setup')
nutrient_mix    = Transition(label='Nutrient Mix')
energy_audit    = Transition(label='Energy Audit')
waste_plan      = Transition(label='Waste Plan')
permit_filing   = Transition(label='Permit Filing')
supplier_vetting= Transition(label='Supplier Vetting')
community_meet  = Transition(label='Community Meet')
tech_integration= Transition(label='Tech Integration')
trial_harvest   = Transition(label='Trial Harvest')
market_launch   = Transition(label='Market Launch')
system_tuning   = Transition(label='System Tuning')
maintenance_chk = Transition(label='Maintenance Check')

# Define the maintenance loop: do maintenance check, then choose to exit or tune & repeat
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[maintenance_chk, system_tuning]
)

# Build the overall partial‐order workflow
root = StrictPartialOrder(
    nodes=[
        site_survey, impact_study,
        modular_design, crop_mapping,
        sensor_install, irrigation_setup, nutrient_mix,
        energy_audit, waste_plan,
        permit_filing, supplier_vetting,
        community_meet, tech_integration,
        trial_harvest, market_launch,
        maintenance_loop
    ]
)

# Define the control‐flow dependencies
po = root.order
po.add_edge(site_survey,    impact_study)

po.add_edge(impact_study,   modular_design)
po.add_edge(impact_study,   crop_mapping)

po.add_edge(modular_design, sensor_install)
po.add_edge(crop_mapping,   sensor_install)

po.add_edge(sensor_install, irrigation_setup)
po.add_edge(irrigation_setup, nutrient_mix)

po.add_edge(nutrient_mix,   energy_audit)
po.add_edge(nutrient_mix,   waste_plan)

po.add_edge(energy_audit,   permit_filing)
po.add_edge(waste_plan,     permit_filing)
po.add_edge(energy_audit,   supplier_vetting)
po.add_edge(waste_plan,     supplier_vetting)

po.add_edge(permit_filing,  community_meet)
po.add_edge(supplier_vetting, community_meet)

po.add_edge(community_meet,  tech_integration)
po.add_edge(tech_integration, trial_harvest)
po.add_edge(trial_harvest,   market_launch)

po.add_edge(market_launch,   maintenance_loop)