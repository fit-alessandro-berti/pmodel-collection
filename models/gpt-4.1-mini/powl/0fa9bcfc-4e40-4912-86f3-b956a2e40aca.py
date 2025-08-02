# Generated from: 0fa9bcfc-4e40-4912-86f3-b956a2e40aca.json
# Description: This process outlines the comprehensive setup of an urban vertical farm, integrating advanced hydroponic systems, IoT-based environmental controls, and renewable energy sources. It involves initial site analysis in dense city environments, modular infrastructure assembly, nutrient solution formulation, and continuous monitoring to optimize crop yield. The process also includes community engagement for local sourcing, regulatory compliance with urban agricultural policies, and integration with local distribution networks to ensure fresh produce delivery. This atypical business process requires coordination across agriculture, technology, and urban planning domains to create a sustainable food production model within metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
PermittingCheck = Transition(label='Permitting Check')
ModularBuild = Transition(label='Modular Build')
SystemInstall = Transition(label='System Install')
NutrientPrep = Transition(label='Nutrient Prep')
SeedPlanting = Transition(label='Seed Planting')
ClimateSetup = Transition(label='Climate Setup')
IoTConfig = Transition(label='IoT Config')
WaterTesting = Transition(label='Water Testing')
GrowthMonitor = Transition(label='Growth Monitor')
EnergyAudit = Transition(label='Energy Audit')
HarvestPlan = Transition(label='Harvest Plan')
CommunityMeet = Transition(label='Community Meet')
RegulationReview = Transition(label='Regulation Review')
DistributionLink = Transition(label='Distribution Link')
WasteManage = Transition(label='Waste Manage')

# Build partial orders for site setup
site_setup = StrictPartialOrder(nodes=[SiteSurvey, DesignLayout, PermittingCheck])
site_setup.order.add_edge(SiteSurvey, DesignLayout)
site_setup.order.add_edge(DesignLayout, PermittingCheck)

# Build partial orders for physical construction and system installation
construction = StrictPartialOrder(nodes=[ModularBuild, SystemInstall])
construction.order.add_edge(ModularBuild, SystemInstall)

# Nutrient preparation, seed planting and climate preparation flow
prep_and_planting = StrictPartialOrder(nodes=[NutrientPrep, SeedPlanting, ClimateSetup])
prep_and_planting.order.add_edge(NutrientPrep, SeedPlanting)
prep_and_planting.order.add_edge(SeedPlanting, ClimateSetup)

# IoT configuration and water testing (can be concurrent with Energy Audit)
iot_water = StrictPartialOrder(nodes=[IoTConfig, WaterTesting])
iot_water.order.add_edge(IoTConfig, WaterTesting)

# Growth monitoring and harvest planning (growth monitor loops continuously before harvest)
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[GrowthMonitor, SilentTransition()])
growth_and_harvest = StrictPartialOrder(nodes=[monitor_loop, HarvestPlan])
growth_and_harvest.order.add_edge(monitor_loop, HarvestPlan)

# Community and regulation related activities can happen in parallel, combined via choice then partial order
community_regulation = StrictPartialOrder(nodes=[CommunityMeet, RegulationReview])
# No order between CommunityMeet and RegulationReview (concurrent)

# Distribution and waste management in sequence after harvest
distribution_flow = StrictPartialOrder(nodes=[DistributionLink, WasteManage])
distribution_flow.order.add_edge(DistributionLink, WasteManage)

# Now combine segments with partial orders respecting dependencies

# First big partial order: site setup -> construction -> system prep & planting
phase1 = StrictPartialOrder(nodes=[site_setup, construction, prep_and_planting])
phase1.order.add_edge(site_setup, construction)
phase1.order.add_edge(construction, prep_and_planting)

# Combine iot_water and energy audit concurrently
energy_audit = EnergyAudit  # single node

iot_energy = StrictPartialOrder(nodes=[iot_water, energy_audit])
iot_energy.order.add_edge(iot_water, energy_audit)  # IoT chain before energy audit
# No edge from energy_audit to others, so energy audit happens after iot_water

# Combine growth & harvest with distribution
post_harvest = StrictPartialOrder(nodes=[growth_and_harvest, distribution_flow])
post_harvest.order.add_edge(growth_and_harvest, distribution_flow)

# Community & regulation parallel and before distribution
community_and_reg = community_regulation

# Combine community/regulation and distribution flow, placing community/regulation before distribution flow
comm_reg_dist = StrictPartialOrder(nodes=[community_and_reg, distribution_flow])
comm_reg_dist.order.add_edge(community_and_reg, distribution_flow)

# Now final root combining everything respecting overall flow:
# phase1 -> (iot_water+energy_audit) -> growth_and_harvest -> community/regulation -> distribution/waste

step1 = phase1
step2 = iot_energy
step3 = growth_and_harvest
step4 = community_and_reg
step5 = distribution_flow

root = StrictPartialOrder(nodes=[step1, step2, step3, step4, step5])
root.order.add_edge(step1, step2)
root.order.add_edge(step2, step3)
root.order.add_edge(step3, step4)
root.order.add_edge(step4, step5)