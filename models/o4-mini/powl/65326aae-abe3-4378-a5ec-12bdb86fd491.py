# Generated from: 65326aae-abe3-4378-a5ec-12bdb86fd491.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm. It includes site evaluation, structural assessments, and soil testing to ensure safety and feasibility. The process continues with irrigation system design, nutrient sourcing, and crop selection tailored for microclimates. It integrates community engagement, permits acquisition, and installation of renewable energy sources to minimize environmental impact. Ongoing monitoring of plant health, pest control using organic methods, and data collection for yield optimization complete the cycle. This atypical business process blends agriculture, engineering, and urban planning to create productive green spaces in dense urban environments, contributing to food security and ecological benefits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey      = Transition(label="Site Survey")
structural_check = Transition(label="Structural Check")
soil_testing     = Transition(label="Soil Testing")
permit_filing    = Transition(label="Permit Filing")
system_design    = Transition(label="System Design")
nutrient_sourcing= Transition(label="Nutrient Sourcing")
crop_selection   = Transition(label="Crop Selection")
community_meet   = Transition(label="Community Meet")
solar_setup      = Transition(label="Solar Setup")
irrigation_install = Transition(label="Irrigation Install")
planting_seeds   = Transition(label="Planting Seeds")
pest_control     = Transition(label="Pest Control")
health_monitor   = Transition(label="Health Monitor")
yield_analyze    = Transition(label="Yield Analyze")
waste_manage     = Transition(label="Waste Manage")
data_logging     = Transition(label="Data Logging")

# Build the monitoring loop: Health Monitor, then Pest Control -> Data Logging -> Yield Analyze -> Waste Manage
monitoring_cycle = StrictPartialOrder(
    nodes=[pest_control, data_logging, yield_analyze, waste_manage]
)
monitoring_cycle.order.add_edge(pest_control, data_logging)
monitoring_cycle.order.add_edge(data_logging, yield_analyze)
monitoring_cycle.order.add_edge(yield_analyze, waste_manage)

loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[health_monitor, monitoring_cycle]
)

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        structural_check,
        soil_testing,
        system_design,
        nutrient_sourcing,
        crop_selection,
        community_meet,
        permit_filing,
        solar_setup,
        irrigation_install,
        planting_seeds,
        loop,
    ]
)

# Site evaluation sequence
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, soil_testing)

# After soil testing: three parallel design/prep tasks + community/permits/solar
for t in [system_design, nutrient_sourcing, crop_selection,
          community_meet, permit_filing, solar_setup]:
    root.order.add_edge(soil_testing, t)

# System Design leads to irrigation install
root.order.add_edge(system_design, irrigation_install)

# All three preparation tasks feed into planting seeds
for t in [nutrient_sourcing, crop_selection, irrigation_install]:
    root.order.add_edge(t, planting_seeds)

# After seeds planted, enter the monitoring loop
root.order.add_edge(planting_seeds, loop)