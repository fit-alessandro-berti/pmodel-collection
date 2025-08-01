# Generated from: 4e8bf7dc-cc2e-47c4-9aaf-94efaad021bf.json
# Description: This process outlines the intricate steps required to establish a fully operational urban vertical farm within a repurposed industrial building. It begins with site analysis and environmental impact assessment, followed by modular structure design and customized hydroponics system installation. The workflow includes controlled environment calibration, nutrient solution formulation, and integrated pest management planning. Subsequent activities involve AI-driven crop scheduling, staff training on automated systems, and compliance verification with local agricultural regulations. The final phases focus on establishing distribution logistics, continuous performance monitoring, and iterative optimization to maximize yield while minimizing resource consumption and environmental footprint in an urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site = Transition(label='Site Analysis')
impact = Transition(label='Impact Review')
structure = Transition(label='Structure Design')
hydro = Transition(label='Hydroponics Install')
calibration = Transition(label='Env Calibration')
nutrient = Transition(label='Nutrient Mixing')
pest = Transition(label='Pest Planning')
crop = Transition(label='Crop Scheduling')
staff = Transition(label='Staff Training')
compliance = Transition(label='Compliance Check')
logistics = Transition(label='Logistics Setup')
perf = Transition(label='Performance Monitor')
yield_opt = Transition(label='Yield Optimization')
waste = Transition(label='Waste Management')
energy = Transition(label='Energy Audit')

# Build the loop body for iterative optimization (one iteration)
body_loop = StrictPartialOrder(nodes=[perf, yield_opt, waste, energy])
body_loop.order.add_edge(perf, yield_opt)
body_loop.order.add_edge(yield_opt, waste)
body_loop.order.add_edge(waste, energy)

# A silent transition to enable loop exit
skip = SilentTransition()

# Define the LOOP operator: perform one iteration, then optionally repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[body_loop, skip])

# Root partial order: integrates all phases
root = StrictPartialOrder(
    nodes=[
        site, impact,
        structure, hydro,
        calibration, nutrient, pest,
        crop, staff, compliance,
        logistics,
        loop
    ]
)

# Phase 1: Site Analysis and Impact Review in parallel, then Design & Install
root.order.add_edge(site, structure)
root.order.add_edge(impact, structure)
root.order.add_edge(site, hydro)
root.order.add_edge(impact, hydro)

# Phase 2: Structure & Hydroponics complete before Calibration, Mixing, Pest Planning
for prev in (structure, hydro):
    root.order.add_edge(prev, calibration)
    root.order.add_edge(prev, nutrient)
    root.order.add_edge(prev, pest)

# Phase 3: Calibration, Mixing, Pest Planning complete before Scheduling, Training, Compliance
for prev in (calibration, nutrient, pest):
    root.order.add_edge(prev, crop)
    root.order.add_edge(prev, staff)
    root.order.add_edge(prev, compliance)

# Phase 4: Once scheduling, training, and compliance are done, set up logistics
for prev in (crop, staff, compliance):
    root.order.add_edge(prev, logistics)

# Final Phase: Logistics → iterative monitoring & optimization loop
root.order.add_edge(logistics, loop)