# Generated from: 5d382d21-f52c-4cb9-abc2-e1faf7a2c9a7.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming system within a repurposed industrial building. It includes initial site evaluation, environmental impact assessments, custom hydroponic system design, integration of AI-driven climate controls, procurement of specialized LED lighting, installation of modular growth racks, seed selection optimized for vertical growth, nutrient solution formulation, recruitment and training of agritech staff, continuous system calibration, pest management via biocontrol agents, data analytics for yield prediction, community engagement for local produce distribution, and ongoing sustainability audits to ensure minimal resource consumption and maximum crop output in a highly controlled urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities as POWL transitions
site_survey      = Transition(label="Site Survey")
impact_study     = Transition(label="Impact Study")
system_design    = Transition(label="System Design")
ai_integration   = Transition(label="AI Integration")
light_setup      = Transition(label="Light Setup")
rack_install     = Transition(label="Rack Install")
seed_select      = Transition(label="Seed Select")
nutrient_prep    = Transition(label="Nutrient Prep")
staff_hire       = Transition(label="Staff Hire")
staff_train      = Transition(label="Staff Train")
system_tune      = Transition(label="System Tune")
pest_control     = Transition(label="Pest Control")
data_review      = Transition(label="Data Review")
community_meet   = Transition(label="Community Meet")
sustain_audit    = Transition(label="Sustain Audit")

# Build a strictly ordered workflow (linear sequence)
root = StrictPartialOrder(nodes=[
    site_survey,
    impact_study,
    system_design,
    ai_integration,
    light_setup,
    rack_install,
    seed_select,
    nutrient_prep,
    staff_hire,
    staff_train,
    system_tune,
    pest_control,
    data_review,
    community_meet,
    sustain_audit
])

# Add the control‐flow edges (sequence)
root.order.add_edge(site_survey,    impact_study)
root.order.add_edge(impact_study,   system_design)
root.order.add_edge(system_design,  ai_integration)
root.order.add_edge(ai_integration, light_setup)
root.order.add_edge(light_setup,    rack_install)
root.order.add_edge(rack_install,   seed_select)
root.order.add_edge(seed_select,    nutrient_prep)
root.order.add_edge(nutrient_prep,  staff_hire)
root.order.add_edge(staff_hire,     staff_train)
root.order.add_edge(staff_train,    system_tune)
root.order.add_edge(system_tune,    pest_control)
root.order.add_edge(pest_control,   data_review)
root.order.add_edge(data_review,    community_meet)
root.order.add_edge(community_meet, sustain_audit)