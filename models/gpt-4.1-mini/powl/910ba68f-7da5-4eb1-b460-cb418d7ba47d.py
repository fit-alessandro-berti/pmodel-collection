# Generated from: 910ba68f-7da5-4eb1-b460-cb418d7ba47d.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a repurposed building. It requires coordination across multiple disciplines including structural assessment, environmental control integration, hydroponic system design, and supply chain logistics. The process begins with site selection and feasibility studies, followed by modular infrastructure installation, nutrient solution calibration, and automated monitoring setup. Concurrently, a multi-tier crop scheduling system is developed to optimize yield cycles. The process also incorporates community engagement initiatives and regulatory compliance checks to ensure sustainability and social acceptance. Continuous data analysis and system refinement are conducted post-launch to maximize efficiency and profitability in a confined urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
SiteSurvey = Transition(label='Site Survey')
FeasibilityCheck = Transition(label='Feasibility Check')

StructuralAudit = Transition(label='Structural Audit')

DesignLayout = Transition(label='Design Layout')
SystemInstall = Transition(label='System Install')

HydroponicsSetup = Transition(label='Hydroponics Setup')
NutrientMix = Transition(label='Nutrient Mix')

ClimateControl = Transition(label='Climate Control')
LightingConfig = Transition(label='Lighting Config')
SensorDeploy = Transition(label='Sensor Deploy')
AutomationLink = Transition(label='Automation Link')

CropPlanning = Transition(label='Crop Planning')

RegulatoryReview = Transition(label='Regulatory Review')
CommunityMeet = Transition(label='Community Meet')

DataAnalysis = Transition(label='Data Analysis')
SystemAdjust = Transition(label='System Adjust')

SupplyChain = Transition(label='Supply Chain')

# Site selection and feasibility studies: SiteSurvey -> FeasibilityCheck
site_feasibility = StrictPartialOrder(nodes=[SiteSurvey, FeasibilityCheck])
site_feasibility.order.add_edge(SiteSurvey, FeasibilityCheck)

# Modular infrastructure installation involves StructuralAudit, DesignLayout, SystemInstall with dependencies:
# StructuralAudit first, then DesignLayout, then SystemInstall
infra_install = StrictPartialOrder(nodes=[StructuralAudit, DesignLayout, SystemInstall])
infra_install.order.add_edge(StructuralAudit, DesignLayout)
infra_install.order.add_edge(DesignLayout, SystemInstall)

# Nutrient solution calibration: HydroponicsSetup -> NutrientMix
nutrient_calib = StrictPartialOrder(nodes=[HydroponicsSetup, NutrientMix])
nutrient_calib.order.add_edge(HydroponicsSetup, NutrientMix)

# Automated monitoring setup: ClimateControl, LightingConfig, SensorDeploy, AutomationLink
# All four activities must be done in this order to prepare the system:
auto_monitor_setup = StrictPartialOrder(nodes=[ClimateControl, LightingConfig, SensorDeploy, AutomationLink])
auto_monitor_setup.order.add_edge(ClimateControl, LightingConfig)
auto_monitor_setup.order.add_edge(LightingConfig, SensorDeploy)
auto_monitor_setup.order.add_edge(SensorDeploy, AutomationLink)

# Development of multi-tier crop scheduling system: CropPlanning alone
# It runs concurrently, so keep as a single node partial order
crop_scheduling = StrictPartialOrder(nodes=[CropPlanning])

# Community engagement and regulatory compliance - these two activities run concurrently
community_regulatory = StrictPartialOrder(nodes=[RegulatoryReview, CommunityMeet])

# Post-launch continuous loop of DataAnalysis followed by SystemAdjust, repeated
post_launch_loop = OperatorPOWL(operator=Operator.LOOP, children=[DataAnalysis, SystemAdjust])

# SupplyChain logistics (assumed independent)
supply_chain = StrictPartialOrder(nodes=[SupplyChain])

# Now connect these parts in correct partial order, based on description:

# Overall order relationships:
# site_feasibility -> infra_install -> nutrient_calib -> auto_monitor_setup
# crop_scheduling, community_regulatory, supply_chain run concurrently with above main chain (except post_launch_loop)
# post_launch_loop happens after all above are finished

root_nodes = [
    site_feasibility,
    infra_install,
    nutrient_calib,
    auto_monitor_setup,
    crop_scheduling,
    community_regulatory,
    supply_chain,
    post_launch_loop
]

root = StrictPartialOrder(nodes=root_nodes)

# Edges defining main linear workflow chain
root.order.add_edge(site_feasibility, infra_install)
root.order.add_edge(infra_install, nutrient_calib)
root.order.add_edge(nutrient_calib, auto_monitor_setup)

# Post launch loop after everything else
root.order.add_edge(crop_scheduling, post_launch_loop)
root.order.add_edge(community_regulatory, post_launch_loop)
root.order.add_edge(auto_monitor_setup, post_launch_loop)
root.order.add_edge(supply_chain, post_launch_loop)

# CropScheduling, CommunityRegulatory, SupplyChain run concurrently with main chain after auto_monitor_setup
# They have no ordering edges between each other or the earlier parts, except before post_launch_loop
# So no additional edges are needed beyond those to post_launch_loop
