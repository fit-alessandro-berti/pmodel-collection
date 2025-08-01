# Generated from: 25a1da21-74b5-4446-b1d1-4019e8dfb741.json
# Description: This process involves the thorough authentication of historical artifacts intended for museum acquisition. It begins with preliminary provenance research, followed by multispectral imaging and material composition analysis. Specialist consultations are conducted to verify stylistic consistency. Trace element profiling and radiocarbon dating provide scientific validation. Parallelly, legal ownership checks and export compliance reviews ensure ethical acquisition. The workflow culminates in compiling a comprehensive authentication report and final approval by the acquisitions board, minimizing the risk of counterfeit or illegally sourced artifacts entering the collection.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Provenance_Check = Transition(label='Provenance Check')
Image_Capture = Transition(label='Image Capture')
Material_Scan = Transition(label='Material Scan')
Style_Review = Transition(label='Style Review')
Element_Analysis = Transition(label='Element Analysis')
Carbon_Dating = Transition(label='Carbon Dating')
Consult_Experts = Transition(label='Consult Experts')
Ownership_Verify = Transition(label='Ownership Verify')
Export_Review = Transition(label='Export Review')
Legal_Clearance = Transition(label='Legal Clearance')
Data_Integration = Transition(label='Data Integration')
Report_Draft = Transition(label='Report Draft')
Board_Review = Transition(label='Board Review')
Final_Approval = Transition(label='Final Approval')
Archive_Data = Transition(label='Archive Data')

# Specialist consultations (Style_Review followed by Consult_Experts)
specialist_consult = StrictPartialOrder(nodes=[Style_Review, Consult_Experts])
specialist_consult.order.add_edge(Style_Review, Consult_Experts)

# Scientific validation chain (Element_Analysis --> Carbon_Dating)
scientific_validation = StrictPartialOrder(nodes=[Element_Analysis, Carbon_Dating])
scientific_validation.order.add_edge(Element_Analysis, Carbon_Dating)

# First partial order: multispectral imaging and material composition analysis followed by specialist consults and scientific validation in sequence
multi_and_material = StrictPartialOrder(nodes=[Image_Capture, Material_Scan])
# Imaging and scanning concurrent (no edges)
# Then Style_Review -> Consult_Experts (specialist_consult)
# Then Element_Analysis -> Carbon_Dating (scientific_validation)

# Compose multi_and_material + specialist_consult + scientific_validation in sequence:
part1 = StrictPartialOrder(
    nodes=[multi_and_material, specialist_consult, scientific_validation]
)
part1.order.add_edge(multi_and_material, specialist_consult)
part1.order.add_edge(specialist_consult, scientific_validation)

# Legal checks: Ownership_Verify --> Export_Review --> Legal_Clearance
legal_checks = StrictPartialOrder(nodes=[Ownership_Verify, Export_Review, Legal_Clearance])
legal_checks.order.add_edge(Ownership_Verify, Export_Review)
legal_checks.order.add_edge(Export_Review, Legal_Clearance)

# Parallel block of part1 and legal_checks
parallel_block = StrictPartialOrder(nodes=[part1, legal_checks])
# no order edges between part1 and legal_checks => parallel

# Then Data_Integration after parallel block
after_parallel = StrictPartialOrder(nodes=[parallel_block, Data_Integration])
after_parallel.order.add_edge(parallel_block, Data_Integration)

# Then: Report Draft --> Board Review --> Final Approval
approval_sequence = StrictPartialOrder(
    nodes=[Report_Draft, Board_Review, Final_Approval]
)
approval_sequence.order.add_edge(Report_Draft, Board_Review)
approval_sequence.order.add_edge(Board_Review, Final_Approval)

# Then Archive_Data after final approval
final_sequence = StrictPartialOrder(nodes=[after_parallel, approval_sequence, Archive_Data])
final_sequence.order.add_edge(after_parallel, approval_sequence)
final_sequence.order.add_edge(approval_sequence, Archive_Data)

# Starting: Provenance Check must be before all above
root = StrictPartialOrder(nodes=[Provenance_Check, final_sequence])
root.order.add_edge(Provenance_Check, final_sequence)