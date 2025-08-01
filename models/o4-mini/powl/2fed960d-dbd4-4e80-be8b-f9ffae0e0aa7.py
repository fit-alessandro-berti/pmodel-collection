# Generated from: 2fed960d-dbd4-4e80-be8b-f9ffae0e0aa7.json
# Description: This process outlines the complex steps involved in establishing an urban beekeeping operation on a city rooftop. It covers site assessment, regulatory compliance, hive installation, bee colony acquisition, ongoing health monitoring, honey extraction, and community engagement activities. The process requires coordination with local authorities for permits, environmental impact evaluations, and integration with urban agriculture initiatives. It also involves managing seasonal changes, pest control without harmful chemicals, and educating neighbors about bee safety. Ultimately, the process aims to create a sustainable, productive beekeeping environment that supports pollination and local biodiversity while producing quality honey products.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey     = Transition(label='Site Survey')
permit_check    = Transition(label='Permit Check')
risk_assess     = Transition(label='Risk Assess')
hive_design     = Transition(label='Hive Design')
material_procure= Transition(label='Material Procure')
rooftop_prep    = Transition(label='Rooftop Prep')
hive_install    = Transition(label='Hive Install')
colony_order    = Transition(label='Colony Order')
bee_release     = Transition(label='Bee Release')

health_monitor  = Transition(label='Health Monitor')
pest_control    = Transition(label='Pest Control')
honey_harvest   = Transition(label='Honey Harvest')
wax_clean       = Transition(label='Wax Clean')
seasonal_adjust = Transition(label='Seasonal Adjust')
community_meet  = Transition(label='Community Meet')
education_plan  = Transition(label='Education Plan')
data_record     = Transition(label='Data Record')

# Initial setup partial order
init_po = StrictPartialOrder(nodes=[
    site_survey, permit_check, risk_assess,
    hive_design, material_procure, rooftop_prep,
    hive_install, colony_order, bee_release
])
init_po.order.add_edge(site_survey,    permit_check)
init_po.order.add_edge(permit_check,   risk_assess)
init_po.order.add_edge(risk_assess,    hive_design)
init_po.order.add_edge(hive_design,    material_procure)
init_po.order.add_edge(material_procure, rooftop_prep)
init_po.order.add_edge(rooftop_prep,   hive_install)
init_po.order.add_edge(hive_install,   colony_order)
init_po.order.add_edge(colony_order,   bee_release)

# Repeating seasonal activities partial order
rep_po = StrictPartialOrder(nodes=[
    health_monitor, pest_control, honey_harvest,
    wax_clean, seasonal_adjust, community_meet,
    education_plan, data_record
])
rep_po.order.add_edge(health_monitor,  pest_control)
rep_po.order.add_edge(health_monitor,  honey_harvest)
rep_po.order.add_edge(health_monitor,  wax_clean)
rep_po.order.add_edge(pest_control,    seasonal_adjust)
rep_po.order.add_edge(honey_harvest,   seasonal_adjust)
rep_po.order.add_edge(wax_clean,       seasonal_adjust)
rep_po.order.add_edge(seasonal_adjust, community_meet)
rep_po.order.add_edge(seasonal_adjust, education_plan)
rep_po.order.add_edge(community_meet,  data_record)
rep_po.order.add_edge(education_plan,  data_record)

# Loop: do initial setup once, then repeat seasonal activities until exit
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[init_po, rep_po]
)