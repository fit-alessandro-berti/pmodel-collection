# Generated from: 6d2fc9c5-0642-47cf-be36-9bde1319d8ce.json
# Description: This process outlines the establishment of an urban vertical farming system within a repurposed multi-story warehouse. It involves site evaluation, environmental system integration, hydroponic setup, crop selection based on urban climate, automated nutrient delivery design, and continuous monitoring via IoT sensors. The process also includes staff training for maintenance, regulatory compliance checks, and sustainability audits to ensure minimal energy consumption and waste. The goal is to create a self-sustaining, high-yield farm that leverages vertical space and technology to produce fresh produce efficiently in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
site_survey = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
climate_study = Transition(label='Climate Study')
design_layout = Transition(label='Design Layout')
hydro_setup = Transition(label='Hydro Setup')
lighting_install = Transition(label='Lighting Install')
water_system = Transition(label='Water System')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_deploy = Transition(label='Sensor Deploy')
automation_config = Transition(label='Automation Config')
crop_choose = Transition(label='Crop Choose')
staff_train = Transition(label='Staff Train')
compliance_audit = Transition(label='Compliance Audit')
trial_grow = Transition(label='Trial Grow')
performance_review = Transition(label='Performance Review')
waste_manage = Transition(label='Waste Manage')
energy_audit = Transition(label='Energy Audit')

# Model understanding and assumptions:
# - Site Survey, Structural Check, Climate Study must happen early and can be concurrent (site evaluation)
# - Then Design Layout (require results from previous)
# - Hydro Setup includes Hydro Setup, Lighting Install, Water System, Nutrient Mix
# - Sensor Deploy and Automation Config form environmental system integration and automated nutrient delivery design
# - Crop Choose depends on Climate Study (select crop by urban climate)
# - Staff Train, Compliance Audit, Sustainability audits (Waste Manage, Energy Audit) run towards the end with Trial Grow and Performance Review
# We'll do some partial orders with concurrency:

# Site evaluation partial order (site survey and structural check concurrent, then climate study)
site_eval = StrictPartialOrder(nodes=[site_survey, structural_check, climate_study])
site_eval.order.add_edge(site_survey, climate_study)
site_eval.order.add_edge(structural_check, climate_study)

# Hydroponic and lighting/water/nutrient setup partial order (can run in parallel)
hydro_setup_po = StrictPartialOrder(
    nodes=[hydro_setup, lighting_install, water_system, nutrient_mix]
)
# No order edges, they are concurrent tasks in setup

# Environmental integration partial order
env_integration = StrictPartialOrder(nodes=[sensor_deploy, automation_config])
# Concurrent

# Crop Choice depends on climate study (which is in site_eval)
# We will link climate_study --> crop_choose in final order

# Staff train, compliance audit, waste manage, energy audit form sustainability and regulatory checks
# These can be concurrent but all before trial_grow and performance_review

sustain_checks = StrictPartialOrder(
    nodes=[staff_train, compliance_audit, waste_manage, energy_audit]
)
# No edges => concurrent

# Trial grow and performance review happen after others
trial_phase = StrictPartialOrder(nodes=[trial_grow, performance_review])
trial_phase.order.add_edge(trial_grow, performance_review)

# Now combine partial orders and add cross edges to reflect dependencies

# Create a root strict partial order with all main groups as nodes
root = StrictPartialOrder(
    nodes=[
        site_eval,           # site evaluation partial order
        design_layout,
        hydro_setup_po,      # hydroponic setup concurrent activities
        env_integration,     # sensor deploy, automation config concurrent
        crop_choose,
        sustain_checks,      # staff train, compliance audit, waste manage, energy audit concurrent
        trial_phase
    ]
)

# Add dependency edges according to process flow

# site_eval --> design_layout
root.order.add_edge(site_eval, design_layout)

# design_layout --> hydro_setup_po
root.order.add_edge(design_layout, hydro_setup_po)

# hydro_setup_po --> env_integration (integration after setup)
root.order.add_edge(hydro_setup_po, env_integration)

# climate_study (inside site_eval) --> crop_choose
# To add this, add edge from site_eval to crop_choose to ensure crop_choose after climate_study
# But crop_choose should be after climate_study in site_eval anyway.
# Since site_eval to crop_choose means after all site_eval tasks; it's safe here.
root.order.add_edge(site_eval, crop_choose)

# env_integration --> sustain_checks (sustainability and compliance after env setup)
root.order.add_edge(env_integration, sustain_checks)

# crop_choose --> sustain_checks (staff need to train after crop choice)
root.order.add_edge(crop_choose, sustain_checks)

# sustain_checks --> trial_phase (test and review after training and compliance)
root.order.add_edge(sustain_checks, trial_phase)