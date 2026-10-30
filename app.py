
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Project Peacekeeper",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 PROJECT PEACEKEEPER")
st.subheader("Diplomatic Intelligence Centre")
st.caption("Version 0.1 | Built for humanity")

st.info(
    "An independent peace-support prototype. "
    "All proposals require human review. "
    "This application does not verify claims or make decisions for governments."
)

st.header("1. Conflict information")

with st.form("peace_analysis"):
    conflict = st.text_input(
        "Name or description of the disagreement"
    )

    st.subheader("Party A")
    party_a = st.text_input("Party A name")
    position_a = st.text_area(
        "What does Party A want?"
    )
    concerns_a = st.text_area(
        "What are Party A's concerns?"
    )

    st.divider()

    st.subheader("Party B")
    party_b = st.text_input("Party B name")
    position_b = st.text_area(
        "What does Party B want?"
    )
    concerns_b = st.text_area(
        "What are Party B's concerns?"
    )

    st.divider()

    st.subheader("2. Humanitarian considerations")

    shared = st.text_area(
        "What interests or priorities might both parties share?"
    )

    civilian_needs = st.text_area(
        "What do civilians urgently need protecting?"
    )

    evidence = st.text_area(
        "What evidence or sources support the information?"
    )

    submitted = st.form_submit_button(
        "🌍 Generate peace proposals",
        use_container_width=True
    )

if submitted:
    if not all([
        conflict, party_a, party_b,
        position_a, position_b
    ]):
        st.error("Please complete the conflict name, both parties and their positions.")
    else:
        st.header("3. Conflict analysis")

        st.write(f"**Conflict:** {conflict}")
        st.write(f"**Parties:** {party_a} and {party_b}")

        st.subheader("Party A's position")
        st.write(position_a)
        st.write("**Concerns:**", concerns_a or "Not supplied")

        st.subheader("Party B's position")
        st.write(position_b)
        st.write("**Concerns:**", concerns_b or "Not supplied")

        st.subheader("Potential common ground")
        st.write(shared or "No shared priorities have been identified yet.")

        st.subheader("Civilian protection")
        st.warning(
            civilian_needs or
            "Urgent civilian needs have not yet been documented."
        )

        st.header("4. Three diplomatic frameworks")

        proposals = [
            (
                "Proposal A: Humanitarian pause",
                "Explore a mutually agreed temporary cessation "
                "of hostilities, humanitarian access and civilian protection."
            ),
            (
                "Proposal B: Independent mediation",
                "Invite a mutually acceptable neutral mediator "
                "to facilitate structured negotiations."
            ),
            (
                "Proposal C: Phased peace agreement",
                "Explore a sequence of reciprocal, verifiable "
                "steps covering security concerns, humanitarian "
                "needs and longer-term political negotiations."
            )
        ]

        for title, description in proposals:
            with st.expander(title, expanded=True):
                st.write(description)
                st.caption(
                    "Illustrative framework, not an agreed settlement."
                )

        st.header("5. Evidence record")
        st.write(evidence or "No supporting evidence supplied.")
        st.caption(
            "Sources have not been independently verified."
        )

        st.success(
            "Initial diplomatic assessment generated. "
            "Human review is required."
        )

        st.download_button(
            "Download analysis",
            data=f"""
PROJECT PEACEKEEPER
Generated: {datetime.now().isoformat()}

Conflict: {conflict}

PARTY A: {party_a}
Position: {position_a}
Concerns: {concerns_a}

PARTY B: {party_b}
Position: {position_b}
Concerns: {concerns_b}

POTENTIAL COMMON GROUND:
{shared}

CIVILIAN NEEDS:
{civilian_needs}

EVIDENCE PROVIDED:
{evidence}

DIPLOMATIC FRAMEWORKS:
1. Humanitarian pause
2. Independent mediation
3. Phased peace agreement

All proposals require human review.
Claims have not been independently verified.
""",
            file_name="peacekeeper_analysis.txt"
        )

st.divider()
st.caption(
    "PROJECT PEACEKEEPER | Humanity before conflict."
)
