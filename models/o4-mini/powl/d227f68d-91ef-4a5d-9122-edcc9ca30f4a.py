# Generated from: d227f68d-91ef-4a5d-9122-edcc9ca30f4a.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a metropolitan environment. It begins with site evaluation and proceeds through modular infrastructure assembly, hydroponic system installation, and climate control calibration. The process includes seed selection tailored to urban microclimates, nutrient solution formulation, and automated growth monitoring integration. It also involves compliance verification with local zoning laws, energy optimization for sustainability, pest management through biological controls, and logistics planning for distribution. Finally, the process concludes with staff training on advanced cultivation techniques and ongoing performance analysis to maximize yield and resource efficiency in a constrained urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the basic activities
site_survey    = Transition(label='Site Survey')
design_layout  = Transition(label='Design Layout')
permits_check  = Transition(label='Permits Check')
foundation_prep= Transition(label='Foundation Prep')
frame_assembly = Transition(label='Frame Assembly')
hydro_setup    = Transition(label='Hydro Setup')
climate_setup  = Transition(label='Climate Setup')
seed_selection = Transition(label='Seed Selection')
nutrient_mix   = Transition(label='Nutrient Mix')
system_calib   = Transition(label='System Calibration')
pest_control   = Transition(label='Pest Control')
automation_link= Transition(label='Automation Link')
distribution   = Transition(label='Distribution Plan')
staff_training = Transition(label='Staff Training')
yield_tracking = Transition(label='Yield Tracking')

# Build the strictly ordered workflow
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    permits_check,
    foundation_prep,
    frame_assembly,
    hydro_setup,
    climate_setup,
    seed_selection,
    nutrient_mix,
    system_calib,
    pest_control,
    automation_link,
    distribution,
    staff_training,
    yield_tracking
])

# Add the control-flow edges to enforce the sequence
root.order.add_edge(site_survey,    design_layout)
root.order.add_edge(design_layout,  permits_check)
root.order.add_edge(permits_check,  foundation_prep)
root.order.add_edge(foundation_prep, frame_assembly)
root.order.add_edge(frame_assembly,  hydro_setup)
root.order.add_edge(hydro_setup,     climate_setup)
root.order.add_edge(climate_setup,   seed_selection)
root.order.add_edge(seed_selection,  nutrient_mix)
root.order.add_edge(nutrient_mix,    system_calib)
root.order.add_edge(system_calib,    pest_control)
root.order.add_edge(pest_control,    automation_link)
root.order.add_edge(automation_link, distribution)
root.order.add_edge(distribution,    staff_training)
root.order.add_edge(staff_training,  yield_tracking)