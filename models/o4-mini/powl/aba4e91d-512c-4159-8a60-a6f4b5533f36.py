# Generated from: aba4e91d-512c-4159-8a60-a6f4b5533f36.json
# Description: This process outlines the comprehensive steps required to establish an urban rooftop farming system on a commercial building. It starts with assessing rooftop structural integrity and environmental factors, followed by designing modular planting units tailored for limited space. The process includes selecting optimal crop varieties for urban microclimates, acquiring sustainable soil and nutrient sources, and integrating automated irrigation and monitoring systems. Coordination with local authorities for permits and compliance with zoning laws is essential. The workflow also involves staff training on hydroponic techniques, pest management without chemicals, and harvest logistics to ensure fresh produce delivery. Finally, continuous performance evaluation and adaptation strategies are implemented to maintain crop yield and sustainability in an urban context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
roof_assess     = Transition(label="Roof Assess")
design_layout   = Transition(label="Design Layout")
crop_select     = Transition(label="Crop Select")
material_source = Transition(label="Material Sourcing")
unit_assembly   = Transition(label="Unit Assembly")
soil_prep       = Transition(label="Soil Prep")
irrigation_set  = Transition(label="Irrigation Setup")
system_integrate= Transition(label="System Integrate")
permit_filing   = Transition(label="Permit Filing")
compliance_chk  = Transition(label="Compliance Check")
staff_train     = Transition(label="Staff Train")
pest_control    = Transition(label="Pest Control")
harvest_plan    = Transition(label="Harvest Plan")
delivery_sched  = Transition(label="Delivery Schedule")
growth_monitor  = Transition(label="Growth Monitor")
yield_review    = Transition(label="Yield Review")
waste_manage    = Transition(label="Waste Manage")

# Silent transition for looping
skip = SilentTransition()

# Build the evaluation/adaptation cycle as a strict partial order
cycle = StrictPartialOrder(nodes=[growth_monitor, yield_review, waste_manage])
cycle.order.add_edge(growth_monitor, yield_review)
cycle.order.add_edge(yield_review, waste_manage)

# Wrap the cycle in a LOOP operator (execute cycle, then either exit or repeat)
loop_cycle = OperatorPOWL(operator=Operator.LOOP, children=[cycle, skip])

# Build the main workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    roof_assess,
    design_layout,
    crop_select,
    material_source,
    unit_assembly,
    soil_prep,
    irrigation_set,
    system_integrate,
    permit_filing,
    compliance_chk,
    staff_train,
    pest_control,
    harvest_plan,
    delivery_sched,
    loop_cycle
])

# Define the control-flow order
root.order.add_edge(roof_assess,    design_layout)
root.order.add_edge(design_layout,  crop_select)
root.order.add_edge(crop_select,    material_source)
root.order.add_edge(material_source,unit_assembly)
root.order.add_edge(unit_assembly,  soil_prep)
root.order.add_edge(soil_prep,      irrigation_set)
root.order.add_edge(irrigation_set, system_integrate)
root.order.add_edge(system_integrate, permit_filing)
root.order.add_edge(permit_filing,  compliance_chk)
root.order.add_edge(compliance_chk, staff_train)
root.order.add_edge(staff_train,    pest_control)
root.order.add_edge(pest_control,   harvest_plan)
root.order.add_edge(harvest_plan,   delivery_sched)
root.order.add_edge(delivery_sched, loop_cycle)