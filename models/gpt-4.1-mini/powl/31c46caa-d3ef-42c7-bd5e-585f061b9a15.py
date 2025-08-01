# Generated from: 31c46caa-d3ef-42c7-bd5e-585f061b9a15.json
# Description: This process outlines the intricate steps involved in establishing a scalable urban vertical farming operation within a repurposed industrial building. It includes site evaluation, environmental control design, multi-tier crop selection, and integrated pest management strategies. The workflow further covers automation system installation, nutrient delivery calibration, energy optimization, data analytics deployment, and community engagement initiatives to ensure sustainable food production in dense metropolitan areas. Each activity focuses on balancing technological innovation with ecological considerations and regulatory compliance to create a self-sustaining urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
SiteSurvey = Transition(label='Site Survey')
StructuralAudit = Transition(label='Structural Audit')
LayoutDesign = Transition(label='Layout Design')
ClimateSetup = Transition(label='Climate Setup')
LightingInstall = Transition(label='Lighting Install')
IrrigationPlan = Transition(label='Irrigation Plan')
CropSelection = Transition(label='Crop Selection')
SeedSowing = Transition(label='Seed Sowing')
PestControl = Transition(label='Pest Control')
NutrientMix = Transition(label='Nutrient Mix')
AutomationConfig = Transition(label='Automation Config')
EnergyAudit = Transition(label='Energy Audit')
DataIntegration = Transition(label='Data Integration')
HarvestSchedule = Transition(label='Harvest Schedule')
WasteRecycling = Transition(label='Waste Recycling')
CommunityOutreach = Transition(label='Community Outreach')
RegulationCheck = Transition(label='Regulation Check')

# Phase 1: Site evaluation: Site Survey -> Structural Audit -> Layout Design
site_evaluation = StrictPartialOrder(nodes=[SiteSurvey, StructuralAudit, LayoutDesign])
site_evaluation.order.add_edge(SiteSurvey, StructuralAudit)
site_evaluation.order.add_edge(StructuralAudit, LayoutDesign)

# Phase 2: Environmental control design: Climate Setup -> Lighting Install + Irrigation Plan in parallel
env_control = StrictPartialOrder(nodes=[ClimateSetup, LightingInstall, IrrigationPlan])
env_control.order.add_edge(ClimateSetup, LightingInstall)
env_control.order.add_edge(ClimateSetup, IrrigationPlan)

# Phase 3: Crop selection & preparation: Crop Selection -> Seed Sowing
crop_prep = StrictPartialOrder(nodes=[CropSelection, SeedSowing])
crop_prep.order.add_edge(CropSelection, SeedSowing)

# Phase 4: Pest control and nutrient delivery (parallel)
# Pest Control and Nutrient Mix are parallel, but both after Seed Sowing
pest_nutrient = StrictPartialOrder(nodes=[PestControl, NutrientMix])
# seed_sowing must happen before both pest control and nutrient mix
# We'll create a PO that combines SeedSowing then pest/nutrient parallel
seed_pest_nutrient = StrictPartialOrder(nodes=[SeedSowing, PestControl, NutrientMix])
seed_pest_nutrient.order.add_edge(SeedSowing, PestControl)
seed_pest_nutrient.order.add_edge(SeedSowing, NutrientMix)
# pest control and nutrient mix concurrent (no order between them)

# Phase 5: Automation system installation & energy audit: Automation Config -> Energy Audit
automation_energy = StrictPartialOrder(nodes=[AutomationConfig, EnergyAudit])
automation_energy.order.add_edge(AutomationConfig, EnergyAudit)

# Phase 6: Data analytics deployment & harvest schedule (in parallel)
data_harvest = StrictPartialOrder(nodes=[DataIntegration, HarvestSchedule])
# concurrent, no order edges

# Phase 7: Waste recycling and community outreach (in parallel)
waste_community = StrictPartialOrder(nodes=[WasteRecycling, CommunityOutreach])
# concurrent, no order edges

# Phase 8: Regulation check (last, after everything)
# So regulation check depends on all previous major phases

# Combine the major phases in order reflecting process logical flow:

# Step 1 to 3 sequential:
step1to3 = StrictPartialOrder(nodes=[site_evaluation, env_control, crop_prep])
step1to3.order.add_edge(site_evaluation, env_control)
step1to3.order.add_edge(env_control, crop_prep)

# Step 4 depends on crop prep (specifically on Seed Sowing inside crop_prep)
# So step4 depends on crop_prep node
step1to4 = StrictPartialOrder(nodes=[step1to3, pest_nutrient])
step1to4.order.add_edge(step1to3, pest_nutrient)

# Step 5 depends on step4 (or at least on Seed Sowing? 
# More logical to come after pest control and nutrient mix.)
step1to5 = StrictPartialOrder(nodes=[step1to4, automation_energy])
step1to5.order.add_edge(step1to4, automation_energy)

# Step 6 can run after automation and energy audit
step1to6 = StrictPartialOrder(nodes=[step1to5, data_harvest])
step1to6.order.add_edge(step1to5, data_harvest)

# Step 7 depends on step 6 (waste recycling & community outreach after data and harvest scheduling)
step1to7 = StrictPartialOrder(nodes=[step1to6, waste_community])
step1to7.order.add_edge(step1to6, waste_community)

# Step 8 regulation check last
root = StrictPartialOrder(nodes=[step1to7, RegulationCheck])
root.order.add_edge(step1to7, RegulationCheck)