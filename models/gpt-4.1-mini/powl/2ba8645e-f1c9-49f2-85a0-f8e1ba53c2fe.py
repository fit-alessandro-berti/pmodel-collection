# Generated from: 2ba8645e-f1c9-49f2-85a0-f8e1ba53c2fe.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a repurposed commercial building. It includes site analysis, structural modifications, installation of hydroponic and aeroponic systems, climate control programming, and integration of IoT sensors for real-time monitoring. The workflow also covers sourcing specialized LED lighting, nutrient solution formulation, recruitment of agronomists, and development of a supply chain for local distribution. Continuous optimization and data analysis ensure sustainability and yield maximization in a constrained urban environment, blending advanced technology with agricultural expertise to meet growing local food demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
site_survey = Transition(label='Site Survey')
structural_scan = Transition(label='Structural Scan')
permit_acquire = Transition(label='Permit Acquire')
system_design = Transition(label='System Design')
hydroponic_setup = Transition(label='Hydroponic Setup')
aeroponic_install = Transition(label='Aeroponic Install')
led_mounting = Transition(label='LED Mounting')
climate_config = Transition(label='Climate Config')
sensor_deploy = Transition(label='Sensor Deploy')
nutrient_mix = Transition(label='Nutrient Mix')
agronomist_hire = Transition(label='Agronomist Hire')
data_integration = Transition(label='Data Integration')
trial_growth = Transition(label='Trial Growth')
supply_chain = Transition(label='Supply Chain')
yield_review = Transition(label='Yield Review')
optimization_plan = Transition(label='Optimization Plan')

# Pre-construction phase: site survey, structural scan, permit acquire (in order)
pre_construction = StrictPartialOrder(nodes=[site_survey, structural_scan, permit_acquire])
pre_construction.order.add_edge(site_survey, structural_scan)
pre_construction.order.add_edge(structural_scan, permit_acquire)

# System design after permits acquired
system_design_stage = StrictPartialOrder(nodes=[permit_acquire, system_design])
system_design_stage.order.add_edge(permit_acquire, system_design)

# Setup of hydroponic and aeroponic systems (can be concurrent after system design)
systems_setup = StrictPartialOrder(nodes=[hydroponic_setup, aeroponic_install])
# no order edges = concurrent setup

# Lighting setup after system design
led_stage = StrictPartialOrder(nodes=[system_design, led_mounting])
led_stage.order.add_edge(system_design, led_mounting)

# Climate config and sensor deploy after LED mounting (can be concurrent)
climate_sensor = StrictPartialOrder(nodes=[climate_config, sensor_deploy])
# no order edges = concurrent

# Both climate_config and sensor_deploy depend on led_mounting
climate_sensor_full = StrictPartialOrder(nodes=[led_mounting, climate_config, sensor_deploy])
climate_sensor_full.order.add_edge(led_mounting, climate_config)
climate_sensor_full.order.add_edge(led_mounting, sensor_deploy)

# Nutrient Mix and Agronomist Hire can be concurrent, both after climate/sensor setup
nutrient_agronomist = StrictPartialOrder(nodes=[nutrient_mix, agronomist_hire])
# no order edges = concurrent

nutrient_agronomist_full = StrictPartialOrder(
    nodes=[climate_config, sensor_deploy, nutrient_mix, agronomist_hire]
)
nutrient_agronomist_full.order.add_edge(climate_config, nutrient_mix)
nutrient_agronomist_full.order.add_edge(sensor_deploy, nutrient_mix)
nutrient_agronomist_full.order.add_edge(climate_config, agronomist_hire)
nutrient_agronomist_full.order.add_edge(sensor_deploy, agronomist_hire)

# Data integration depends on nutrient_mix and agronomist_hire
data_integration_stage = StrictPartialOrder(
    nodes=[nutrient_mix, agronomist_hire, data_integration]
)
data_integration_stage.order.add_edge(nutrient_mix, data_integration)
data_integration_stage.order.add_edge(agronomist_hire, data_integration)

# Trial growth after data integration
trial_growth_stage = StrictPartialOrder(nodes=[data_integration, trial_growth])
trial_growth_stage.order.add_edge(data_integration, trial_growth)

# Supply chain and yield review after trial growth (can be concurrent)
supply_yield = StrictPartialOrder(nodes=[supply_chain, yield_review])
# no order edges = concurrent

supply_yield_full = StrictPartialOrder(nodes=[trial_growth, supply_chain, yield_review])
supply_yield_full.order.add_edge(trial_growth, supply_chain)
supply_yield_full.order.add_edge(trial_growth, yield_review)

# Optimization plan after yield review
optimization_stage = StrictPartialOrder(nodes=[yield_review, optimization_plan])
optimization_stage.order.add_edge(yield_review, optimization_plan)

# Combine the system setup (hydroponic + aeroponic) with LED/climate/sensor chain after system design
system_and_led = StrictPartialOrder(
    nodes=[system_design, hydroponic_setup, aeroponic_install, led_mounting, climate_config, sensor_deploy]
)
system_and_led.order.add_edge(system_design, hydroponic_setup)
system_and_led.order.add_edge(system_design, aeroponic_install)
system_and_led.order.add_edge(system_design, led_mounting)
system_and_led.order.add_edge(led_mounting, climate_config)
system_and_led.order.add_edge(led_mounting, sensor_deploy)

# Now assemble full process partial order nodes including all activities and sub-processes
nodes_all = [
    site_survey, structural_scan, permit_acquire,
    system_design,
    hydroponic_setup, aeroponic_install,
    led_mounting, climate_config, sensor_deploy,
    nutrient_mix, agronomist_hire,
    data_integration,
    trial_growth,
    supply_chain, yield_review,
    optimization_plan
]

root = StrictPartialOrder(nodes=nodes_all)

# Add edges representing ordering constraints:
# Pre-construction sequence
root.order.add_edge(site_survey, structural_scan)
root.order.add_edge(structural_scan, permit_acquire)

# System design after permits
root.order.add_edge(permit_acquire, system_design)

# System setups (hydroponic, aeroponic) start after system design
root.order.add_edge(system_design, hydroponic_setup)
root.order.add_edge(system_design, aeroponic_install)

# LED mounting after system design
root.order.add_edge(system_design, led_mounting)

# Climate config and sensor deploy after LED mounting
root.order.add_edge(led_mounting, climate_config)
root.order.add_edge(led_mounting, sensor_deploy)

# Nutrient mix and agronomist hire after climate config and sensor deploy (both)
root.order.add_edge(climate_config, nutrient_mix)
root.order.add_edge(sensor_deploy, nutrient_mix)
root.order.add_edge(climate_config, agronomist_hire)
root.order.add_edge(sensor_deploy, agronomist_hire)

# Data integration after nutrient mix and agronomist hire
root.order.add_edge(nutrient_mix, data_integration)
root.order.add_edge(agronomist_hire, data_integration)

# Trial growth after data integration
root.order.add_edge(data_integration, trial_growth)

# Supply chain and yield review after trial growth
root.order.add_edge(trial_growth, supply_chain)
root.order.add_edge(trial_growth, yield_review)

# Optimization plan after yield review
root.order.add_edge(yield_review, optimization_plan)