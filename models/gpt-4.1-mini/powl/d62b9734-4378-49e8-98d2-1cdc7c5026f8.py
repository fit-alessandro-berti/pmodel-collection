# Generated from: d62b9734-4378-49e8-98d2-1cdc7c5026f8.json
# Description: This process involves the detailed verification and authentication of rare cultural artifacts acquired from diverse global sources. It begins with initial provenance research, followed by multi-spectral imaging and material composition analysis. Expert consultations and historical cross-referencing are conducted to confirm authenticity. Legal ownership is verified through international registries and customs documentation. The artifact then undergoes conservation status assessment before final certification is issued. Throughout the process, secure data logging and chain-of-custody protocols ensure integrity and traceability, essential for auction or museum acquisition purposes.

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
Expert_Review = Transition(label='Expert Review')
Historical_Cross = Transition(label='Historical Cross')
Legal_Verify = Transition(label='Legal Verify')
Registry_Search = Transition(label='Registry Search')
Customs_Clear = Transition(label='Customs Clear')
Condition_Assess = Transition(label='Condition Assess')
Data_Log = Transition(label='Data Log')
Chain_Custody = Transition(label='Chain Custody')
Report_Draft = Transition(label='Report Draft')
Certification = Transition(label='Certification')
Secure_Archive = Transition(label='Secure Archive')
Auction_Prep = Transition(label='Auction Prep')

# Build partial orders representing process structure

# Provenance research followed by imaging and material scan
po1 = StrictPartialOrder(nodes=[Provenance_Check, Image_Capture, Material_Scan])
po1.order.add_edge(Provenance_Check, Image_Capture)
po1.order.add_edge(Image_Capture, Material_Scan)

# Expert consultations and historical cross referencing (can be concurrent)
expert_hist = StrictPartialOrder(nodes=[Expert_Review, Historical_Cross])
# no order: concurrent

# Legal ownership verification details (3 steps in sequence)
legal_verification = StrictPartialOrder(nodes=[Legal_Verify, Registry_Search, Customs_Clear])
legal_verification.order.add_edge(Legal_Verify, Registry_Search)
legal_verification.order.add_edge(Registry_Search, Customs_Clear)

# Conservation assessment before final certification
certification_part = StrictPartialOrder(nodes=[Condition_Assess, Report_Draft, Certification])
certification_part.order.add_edge(Condition_Assess, Report_Draft)
certification_part.order.add_edge(Report_Draft, Certification)

# Secure data logging and chain-of-custody concurrent with main tasks
data_chain = StrictPartialOrder(nodes=[Data_Log, Chain_Custody])
# no order: concurrent

# Final preparation for auction or museum is last step after certification
final_prep = Auction_Prep

# Secure archive can follow certification and final prep (sequential after both)
archive_part = StrictPartialOrder(nodes=[Certification, final_prep, Secure_Archive])
archive_part.order.add_edge(Certification, final_prep)
archive_part.order.add_edge(final_prep, Secure_Archive)

# Combine expert_hist and legal_verification concurrently (no order between them)
expert_legal = StrictPartialOrder(nodes=[expert_hist, legal_verification])

# Combine above concurrent groups with provenance/imaging/material scan part
first_part = StrictPartialOrder(nodes=[po1, expert_legal, data_chain])
first_part.order.add_edge(po1, expert_legal)
first_part.order.add_edge(po1, data_chain)

# Combine certification part after legal and expert consultation
second_part = StrictPartialOrder(nodes=[first_part, certification_part])
second_part.order.add_edge(first_part, certification_part)

# Combine certification+final prep+secure archive after certification part
final_part = StrictPartialOrder(nodes=[second_part, archive_part])
final_part.order.add_edge(second_part, archive_part)

root = final_part