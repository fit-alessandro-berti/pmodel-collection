# Generated from: 42a65e0d-0566-45df-995d-633f85a9fe3c.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes initial site analysis, structural retrofitting, environmental system installation, crop selection based on microclimate data, automation setup for irrigation and lighting, nutrient solution calibration, pest control integration, workforce training for hydroponic techniques, and compliance with urban agricultural regulations. The process ensures sustainable resource use, optimized crop yields, and integration with local distribution networks, enabling fresh produce supply in dense metropolitan areas while minimizing ecological impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
SiteSurvey = Transition(label='Site Survey')
StructureAssess = Transition(label='Structure Assess')
RetrofitPlan = Transition(label='Retrofit Plan')
ClimateStudy = Transition(label='Climate Study')
SystemDesign = Transition(label='System Design')
InstallLighting = Transition(label='Install Lighting')
SetupIrrigation = Transition(label='Setup Irrigation')
NutrientMix = Transition(label='Nutrient Mix')
CropSelect = Transition(label='Crop Select')
AutomationConfig = Transition(label='Automation Config')
PestControl = Transition(label='Pest Control')
StaffTraining = Transition(label='Staff Training')
ComplianceCheck = Transition(label='Compliance Check')
YieldMonitor = Transition(label='Yield Monitor')
MarketLaunch = Transition(label='Market Launch')

# Structure:
# Initial site analysis: Site Survey --> Structure Assess --> Retrofit Plan
site_analysis = StrictPartialOrder(nodes=[SiteSurvey, StructureAssess, RetrofitPlan])
site_analysis.order.add_edge(SiteSurvey, StructureAssess)
site_analysis.order.add_edge(StructureAssess, RetrofitPlan)

# Environmental system installation: Climate Study --> System Design --> (Install Lighting and Setup Irrigation in parallel)
env_install = StrictPartialOrder(
    nodes=[ClimateStudy, SystemDesign, InstallLighting, SetupIrrigation]
)
env_install.order.add_edge(ClimateStudy, SystemDesign)
env_install.order.add_edge(SystemDesign, InstallLighting)
env_install.order.add_edge(SystemDesign, SetupIrrigation)

# Crop selection based on microclimate data: Crop Select after Climate Study
crop_selection = CropSelect  # single activity

# Automation setup for irrigation and lighting: Automation Config after Install Lighting and Setup Irrigation
automation = AutomationConfig  # single activity

automation_po = StrictPartialOrder(
    nodes=[automation, InstallLighting, SetupIrrigation]
)
automation_po.order.add_edge(InstallLighting, automation)
automation_po.order.add_edge(SetupIrrigation, automation)

# Nutrient solution calibration: Nutrient Mix
# Pest control integration: Pest Control
# Staff training for hydroponic techniques: Staff Training
# Compliance: Compliance Check

# Those four can be done in parallel after automation configuration & crop selection
post_setup_parallel = StrictPartialOrder(
    nodes=[NutrientMix, PestControl, StaffTraining, ComplianceCheck]
)
# no order among them - concurrent

# Yield Monitor after Nutrient Mix and Pest Control to check outcomes of nutrient and pest control
yield_monitor_po = StrictPartialOrder(
    nodes=[NutrientMix, PestControl, YieldMonitor]
)
yield_monitor_po.order.add_edge(NutrientMix, YieldMonitor)
yield_monitor_po.order.add_edge(PestControl, YieldMonitor)

# Market Launch last after Yield Monitor, Staff Training, Compliance Check
final_po = StrictPartialOrder(
    nodes=[YieldMonitor, StaffTraining, ComplianceCheck, MarketLaunch]
)
final_po.order.add_edge(YieldMonitor, MarketLaunch)
final_po.order.add_edge(StaffTraining, MarketLaunch)
final_po.order.add_edge(ComplianceCheck, MarketLaunch)

# Combine post_setup_parallel with yield_monitor_po and final_po carefully:
# NutrientMix and PestControl are in both post_setup_parallel and yield_monitor_po -> unify by using all nodes once in a bigger PO:
post_setup_with_yield = StrictPartialOrder(
    nodes=[NutrientMix, PestControl, StaffTraining, ComplianceCheck, YieldMonitor]
)
# Add edges from post_setup_parallel: none because concurrent except those nodes themselves
# Add yield_monitor edges
post_setup_with_yield.order.add_edge(NutrientMix, YieldMonitor)
post_setup_with_yield.order.add_edge(PestControl, YieldMonitor)
# StaffTraining and ComplianceCheck concurrent with NutrientMix, PestControl, YieldMonitor (except final edges)
# They all must precede MarketLaunch (final_po edges)
post_setup_with_yield_final = StrictPartialOrder(
    nodes=[NutrientMix, PestControl, StaffTraining, ComplianceCheck, YieldMonitor, MarketLaunch]
)
post_setup_with_yield_final.order.add_edge(NutrientMix, YieldMonitor)
post_setup_with_yield_final.order.add_edge(PestControl, YieldMonitor)
post_setup_with_yield_final.order.add_edge(YieldMonitor, MarketLaunch)
post_setup_with_yield_final.order.add_edge(StaffTraining, MarketLaunch)
post_setup_with_yield_final.order.add_edge(ComplianceCheck, MarketLaunch)

# Now unify all nodes and orders:
# Start with site_analysis --> retrofit plan --> environmental installation --> automation & crop select --> post setup with yield and launch
# Crop Select depends on Climate Study (part of env_install), so Crop Select after Climate Study and probably after System Design
# For safety, put CropSelect after ClimateStudy, parallel with SystemDesign + Installations

# Combine ClimateStudy, SystemDesign, InstallLighting, SetupIrrigation, CropSelect, AutomationConfig
env_plus_crop = StrictPartialOrder(
    nodes=[ClimateStudy, SystemDesign, InstallLighting, SetupIrrigation, CropSelect, AutomationConfig]
)
env_plus_crop.order.add_edge(ClimateStudy, SystemDesign)
env_plus_crop.order.add_edge(SystemDesign, InstallLighting)
env_plus_crop.order.add_edge(SystemDesign, SetupIrrigation)
env_plus_crop.order.add_edge(ClimateStudy, CropSelect)
env_plus_crop.order.add_edge(InstallLighting, AutomationConfig)
env_plus_crop.order.add_edge(SetupIrrigation, AutomationConfig)

# Now fully: site_analysis --> env_plus_crop --> post_setup_with_yield_final
root = StrictPartialOrder(
    nodes=[
        SiteSurvey,
        StructureAssess,
        RetrofitPlan,
        ClimateStudy,
        SystemDesign,
        InstallLighting,
        SetupIrrigation,
        CropSelect,
        AutomationConfig,
        NutrientMix,
        PestControl,
        StaffTraining,
        ComplianceCheck,
        YieldMonitor,
        MarketLaunch,
    ]
)

# Add site_analysis edges
root.order.add_edge(SiteSurvey, StructureAssess)
root.order.add_edge(StructureAssess, RetrofitPlan)

# From retrofit plan to env_plus_crop: RetrofitPlan --> ClimateStudy
root.order.add_edge(RetrofitPlan, ClimateStudy)

# env_plus_crop edges
root.order.add_edge(ClimateStudy, SystemDesign)
root.order.add_edge(SystemDesign, InstallLighting)
root.order.add_edge(SystemDesign, SetupIrrigation)
root.order.add_edge(ClimateStudy, CropSelect)
root.order.add_edge(InstallLighting, AutomationConfig)
root.order.add_edge(SetupIrrigation, AutomationConfig)

# From env_plus_crop to post_setup_with_yield_final: AutomationConfig --> NutrientMix, PestControl, StaffTraining, ComplianceCheck
root.order.add_edge(AutomationConfig, NutrientMix)
root.order.add_edge(AutomationConfig, PestControl)
root.order.add_edge(AutomationConfig, StaffTraining)
root.order.add_edge(AutomationConfig, ComplianceCheck)

# post_setup_with_yield_final edges
root.order.add_edge(NutrientMix, YieldMonitor)
root.order.add_edge(PestControl, YieldMonitor)
root.order.add_edge(YieldMonitor, MarketLaunch)
root.order.add_edge(StaffTraining, MarketLaunch)
root.order.add_edge(ComplianceCheck, MarketLaunch)