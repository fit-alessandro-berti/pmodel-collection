# Generated from: 828b9e2b-5f4d-409d-a7da-7f89c31e5952.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming system within a metropolitan environment. It involves site assessment, modular structure design, hydroponic system installation, climate control calibration, seed selection, nutrient solution preparation, automated monitoring setup, pest management strategy, energy optimization, yield prediction modeling, staff training, compliance auditing, marketing launch, and continuous performance evaluation. The process ensures sustainable food production with minimal environmental impact and maximizes space efficiency in urban settings, integrating advanced technology with agricultural best practices to promote local food security and economic growth.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
site_survey         = Transition(label='Site Survey')
design_layout       = Transition(label='Design Layout')
structure_build     = Transition(label='Structure Build')
install_hydroponics = Transition(label='Install Hydroponics')
calibrate_climate   = Transition(label='Calibrate Climate')
seed_selection      = Transition(label='Seed Selection')
prepare_nutrients   = Transition(label='Prepare Nutrients')
setup_automation    = Transition(label='Setup Automation')
pest_control        = Transition(label='Pest Control')
optimize_energy     = Transition(label='Optimize Energy')
yield_modeling      = Transition(label='Yield Modeling')
train_staff         = Transition(label='Train Staff')
audit_compliance    = Transition(label='Audit Compliance')
launch_marketing    = Transition(label='Launch Marketing')
evaluate_performance= Transition(label='Evaluate Performance')

# Build the strictly ordered workflow
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    structure_build,
    install_hydroponics,
    calibrate_climate,
    seed_selection,
    prepare_nutrients,
    setup_automation,
    pest_control,
    optimize_energy,
    yield_modeling,
    train_staff,
    audit_compliance,
    launch_marketing,
    evaluate_performance
])

# Add the sequential dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, structure_build)
root.order.add_edge(structure_build, install_hydroponics)
root.order.add_edge(install_hydroponics, calibrate_climate)
root.order.add_edge(calibrate_climate, seed_selection)
root.order.add_edge(seed_selection, prepare_nutrients)
root.order.add_edge(prepare_nutrients, setup_automation)
root.order.add_edge(setup_automation, pest_control)
root.order.add_edge(pest_control, optimize_energy)
root.order.add_edge(optimize_energy, yield_modeling)
root.order.add_edge(yield_modeling, train_staff)
root.order.add_edge(train_staff, audit_compliance)
root.order.add_edge(audit_compliance, launch_marketing)
root.order.add_edge(launch_marketing, evaluate_performance)