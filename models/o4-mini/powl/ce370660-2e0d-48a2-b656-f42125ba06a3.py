# Generated from: ce370660-2e0d-48a2-b656-f42125ba06a3.json
# Description: This process outlines the establishment of a sustainable urban rooftop farm on a commercial building. It involves initial structural assessments to ensure load capacity, followed by modular soil bed installation adapted for limited space. Specialized irrigation systems are integrated to optimize water usage, alongside solar-powered sensors for real-time monitoring of crop health. The process also includes obtaining necessary permits, community engagement for local support, and coordinated logistics for seed and nutrient delivery. Finally, staff training on hydroponic techniques and ongoing maintenance schedules ensure the farm’s productivity and environmental benefits are maximized throughout the year.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# define transitions
structural = Transition(label='Structural Check')
permit = Transition(label='Permit Apply')
design = Transition(label='Design Layout')
soil = Transition(label='Soil Prep')
bed = Transition(label='Bed Install')
irrig = Transition(label='Irrigation Setup')
sensor = Transition(label='Sensor Mount')
solar = Transition(label='Solar Connect')
seed_order = Transition(label='Seed Order')
nutrient_mix = Transition(label='Nutrient Mix')
community_meet = Transition(label='Community Meet')
staff_train = Transition(label='Staff Train')
plant_crop = Transition(label='Plant Crop')
maintenance_plan = Transition(label='Maintenance Plan')
harvest_schedule = Transition(label='Harvest Schedule')
waste_manage = Transition(label='Waste Manage')

# build partial order
root = StrictPartialOrder(nodes=[
    structural, permit, design, soil, bed, irrig, sensor, solar,
    seed_order, nutrient_mix, community_meet, staff_train,
    plant_crop, maintenance_plan, harvest_schedule, waste_manage
])

# initial planning
root.order.add_edge(structural, permit)
root.order.add_edge(structural, design)
# site preparation
root.order.add_edge(permit, soil)
root.order.add_edge(design, soil)
root.order.add_edge(soil, bed)
# system installations
root.order.add_edge(bed, irrig)
root.order.add_edge(bed, sensor)
root.order.add_edge(sensor, solar)
# procurement & logistics
root.order.add_edge(permit, seed_order)
root.order.add_edge(design, seed_order)
root.order.add_edge(seed_order, nutrient_mix)
# community engagement & training
root.order.add_edge(permit, community_meet)
root.order.add_edge(design, community_meet)
root.order.add_edge(community_meet, staff_train)
# planting prerequisites
root.order.add_edge(bed, plant_crop)
root.order.add_edge(irrig, plant_crop)
root.order.add_edge(solar, plant_crop)
root.order.add_edge(seed_order, plant_crop)
root.order.add_edge(nutrient_mix, plant_crop)
root.order.add_edge(staff_train, plant_crop)
# ongoing care and wrap-up
root.order.add_edge(plant_crop, maintenance_plan)
root.order.add_edge(maintenance_plan, harvest_schedule)
root.order.add_edge(harvest_schedule, waste_manage)