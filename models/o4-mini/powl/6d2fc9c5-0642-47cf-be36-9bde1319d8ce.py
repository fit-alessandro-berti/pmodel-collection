# Generated from: 6d2fc9c5-0642-47cf-be36-9bde1319d8ce.json
# Description: This process outlines the establishment of an urban vertical farming system within a repurposed multi-story warehouse. It involves site evaluation, environmental system integration, hydroponic setup, crop selection based on urban climate, automated nutrient delivery design, and continuous monitoring via IoT sensors. The process also includes staff training for maintenance, regulatory compliance checks, and sustainability audits to ensure minimal energy consumption and waste. The goal is to create a self-sustaining, high-yield farm that leverages vertical space and technology to produce fresh produce efficiently in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey       = Transition(label='Site Survey')
structural_check  = Transition(label='Structural Check')
climate_study     = Transition(label='Climate Study')
design_layout     = Transition(label='Design Layout')
hydro_setup       = Transition(label='Hydro Setup')
lighting_install  = Transition(label='Lighting Install')
water_system      = Transition(label='Water System')
nutrient_mix      = Transition(label='Nutrient Mix')
sensor_deploy     = Transition(label='Sensor Deploy')
automation_config = Transition(label='Automation Config')
crop_choose       = Transition(label='Crop Choose')
staff_train       = Transition(label='Staff Train')
compliance_audit  = Transition(label='Compliance Audit')
trial_grow        = Transition(label='Trial Grow')
performance_review= Transition(label='Performance Review')
waste_manage      = Transition(label='Waste Manage')
energy_audit      = Transition(label='Energy Audit')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, structural_check, climate_study,
    design_layout,
    hydro_setup, lighting_install, water_system,
    nutrient_mix, sensor_deploy, automation_config,
    crop_choose, staff_train, compliance_audit,
    trial_grow, performance_review,
    waste_manage, energy_audit
])

# Phase 1: site evaluation → design
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(structural_check, design_layout)
root.order.add_edge(climate_study, design_layout)

# Phase 2: design → install systems (concurrent)
root.order.add_edge(design_layout, hydro_setup)
root.order.add_edge(design_layout, lighting_install)
root.order.add_edge(design_layout, water_system)

# Phase 3: system installs → setup monitoring and nutrient mixing
root.order.add_edge(hydro_setup, nutrient_mix)
root.order.add_edge(lighting_install, sensor_deploy)
root.order.add_edge(water_system, automation_config)

# Phase 4: compliance & crop selection after design/climate
root.order.add_edge(design_layout, compliance_audit)
root.order.add_edge(design_layout, crop_choose)
root.order.add_edge(climate_study, crop_choose)

# Phase 5: staff training after automation config
root.order.add_edge(automation_config, staff_train)

# Phase 6: trial grow after all preparations
root.order.add_edge(nutrient_mix,    trial_grow)
root.order.add_edge(sensor_deploy,   trial_grow)
root.order.add_edge(automation_config, trial_grow)
root.order.add_edge(crop_choose,     trial_grow)
root.order.add_edge(staff_train,     trial_grow)
root.order.add_edge(compliance_audit,trial_grow)

# Phase 7: review → waste & energy audits
root.order.add_edge(trial_grow,         performance_review)
root.order.add_edge(performance_review, waste_manage)
root.order.add_edge(performance_review, energy_audit)