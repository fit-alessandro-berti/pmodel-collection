# Generated from: 30e98119-5be6-4fdf-8c1c-c8ed808a7719.json
# Description: This process involves establishing a sustainable urban beekeeping operation within a metropolitan area. It begins with site scouting to identify suitable rooftop or community garden locations, followed by local regulation assessment to ensure compliance with city ordinances. Next, hive selection and acquisition are conducted, choosing appropriate hive designs for urban environments. Installation requires careful placement and securing of hives, considering environmental factors and accessibility. Regular hive inspections and health monitoring are performed to detect pests or diseases early. Pollination tracking is integrated by mapping nearby flora and bee activity patterns. Honey extraction employs specialized urban-friendly equipment and methods to minimize disturbance. Packaging and labeling comply with local food safety standards. Community engagement includes educational workshops and collaboration with local farmers for crop pollination enhancement. Finally, waste management and equipment sterilization ensure sustainability and hive longevity in the urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site = Transition(label="Site Scouting")
reg = Transition(label="Regulation Check")
select = Transition(label="Hive Selection")
purchase = Transition(label="Hive Purchase")
install = Transition(label="Hive Installation")
inspect = Transition(label="Health Inspection")
pest = Transition(label="Pest Control")
flora = Transition(label="Flora Mapping")
track = Transition(label="Pollination Track")
extract = Transition(label="Honey Extraction")
package = Transition(label="Honey Packaging")
label = Transition(label="Label Compliance")
workshop = Transition(label="Community Workshop")
liaison = Transition(label="Farmer Liaison")
waste = Transition(label="Waste Disposal")
clean = Transition(label="Equipment Clean")

# Loop: perform Health Inspection, then either exit or do Pest Control and repeat
inspection_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[inspect, pest]
)

# Build the partial order
root = StrictPartialOrder(
    nodes=[
        site,
        reg,
        select,
        purchase,
        install,
        inspection_loop,
        flora,
        track,
        extract,
        package,
        label,
        workshop,
        liaison,
        waste,
        clean
    ]
)

# Add the sequence and concurrency relations
o = root.order
o.add_edge(site, reg)
o.add_edge(reg, select)
o.add_edge(select, purchase)
o.add_edge(purchase, install)
o.add_edge(install, inspection_loop)
o.add_edge(inspection_loop, flora)
o.add_edge(flora, track)
o.add_edge(track, extract)
o.add_edge(extract, package)
o.add_edge(package, label)
# After labeling, run both community activities in parallel
o.add_edge(label, workshop)
o.add_edge(label, liaison)
# Both community activities must finish before waste disposal
o.add_edge(workshop, waste)
o.add_edge(liaison, waste)
# Finally, equipment cleaning follows waste disposal
o.add_edge(waste, clean)