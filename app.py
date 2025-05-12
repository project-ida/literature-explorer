

# Human-readable labels for filter variables
FILTER_LABELS = {
    "documenttype_tooshort": "Too Short to Classify",
    "documenttype_experimental": "Experimental Paper",
    "documenttype_theoretical": "Theoretical Paper",
    "documenttype_methodsinstrument": "Methods/Instrument Paper",
    "documenttype_review": "Review Paper",
    "documenttype_slidedeck": "Slide Deck",
    "documenttype_other": "Other Document Type",

    "material_palladium": "Palladium (Pd)",
    "material_titanium": "Titanium (Ti)",
    "material_nickel": "Nickel (Ni)",
    "material_copper": "Copper (Cu)",
    "material_tungsten": "Tungsten (W)",
    "material_silver": "Silver (Ag)",
    "material_lithium": "Lithium (Li)",
    "material_lanthanum": "Lanthanum (La)",
    "material_vanadium": "Vanadium (V)",
    "material_rhodium": "Rhodium (Rh)",
    "material_tantalum": "Tantalum (Ta)",
    "material_boron": "Boron (B)",
    "material_iron": "Iron (Fe)",
    "material_zirconium": "Zirconium (Zr)",
    "material_other": "Other Material",
    "material_nolattice": "No Lattice Material",

    "shape_plate": "Plates/ingots",
    "shape_foil": "Foils",
    "shape_rod": "Rods",
    "shape_thinfilm": "Thin Film",
    "shape_wire": "Wires",
    "shape_tubes": "Tubes",
    "shape_dissolved": "Dissolved in Electrolyte",
    "shape_plated": "Plated on Cathode (Pre-experiment)",
    "shape_nanoparticles": "Nanoparticles",
    "shape_pressedpowder": "Pressed Powder",
    "shape_porousmesh": "Porous or Mesh",
    "shape_shavings": "Shavings",
    "shape_genericcathode": "Generic 'Cathode'",
    "shape_notclear": "Unclear Form",
    "shape_other": "Other Form",

    "fuel_d": "Deuterium Used",
    "fuel_h": "Hydrogen Used",
    "fuel_none": "No Hydrogen Isotopes",
    "fuel_notclear": "Fuel Not Clearly Specified",

    "loading_electrochemical": "Electrochemical Loading",
    "loading_co_deposition": "Co-deposition",
    "loading_gas": "Gas Loading",
    "loading_ionimplantation": "Ion Implantation",
    "loading_other": "Other Loading Method",

    "stimulation_thermal": "Thermal Stimulation",
    "stimulation_pressure": "Pressure Cycling",
    "stimulation_electrochemical": "Electrochemical Stimulation",
    "stimulation_ionbombardment": "Ion Bombardment",
    "stimulation_laser": "Laser Stimulation",
    "stimulation_currentpulsing": "Current Pulsing",
    "stimulation_ultrasound": "Ultrasound",
    "stimulation_cavitation": "Cavitation",
    "stimulation_other": "Other Stimulation",

    "diagnosticsused_calorimetry": "Calorimetry Used",
    "diagnosticsused_gascomposition": "Gas Composition Analysis",
    "diagnosticsused_tritium": "Tritium Detection",
    "diagnosticsused_surfacemorphology": "Surface Morphology Analysis",
    "diagnosticsused_elemental": "Elemental Analysis",
    "diagnosticsused_isotopic": "Isotopic Analysis",
    "diagnosticsused_neutronliquid": "Neutron Detection (Liquid Scintillator)",
    "diagnosticsused_neutronhe3": "Neutron Detection (He-3/BF3)",
    "diagnosticsused_neutronother": "Neutron Detection (Other)",
    "diagnosticsused_chargedparticlescr39": "Charged Particle Detection (CR-39)",
    "diagnosticsused_chargedparticleselectronic": "Charged Particle Detection (Electronic)",
    "diagnosticsused_gammaelectronic": "Gamma/X-ray Detection (Electronic)",
    "diagnosticsused_gammaradiography": "Gamma/X-ray Detection (Radiography)",
    "diagnosticsused_rf": "RF Emission",
    "diagnosticsused_resistance": "Resistance Measurement",
    "diagnosticsused_other": "Other Diagnostic",

    "anomaliesclaimed_calorimetry": "Calorimetric Anomaly",
    "anomaliesclaimed_gascomposition": "Gas Composition Anomaly",
    "anomaliesclaimed_tritium": "Tritium Anomaly",
    "anomaliesclaimed_surfacemorphology": "Surface Morphology Anomaly",
    "anomaliesclaimed_elemental": "Elemental Anomaly",
    "anomaliesclaimed_isotopic": "Isotopic Anomaly",
    "anomaliesclaimed_neutronliquid": "Neutron Anomaly (Liquid Scintillator)",
    "anomaliesclaimed_neutronhe3": "Neutron Anomaly (He-3/BF3)",
    "anomaliesclaimed_neutronother": "Neutron Anomaly (Other)",
    "anomaliesclaimed_chargedparticlescr39": "Charged Particle Anomaly (CR-39)",
    "anomaliesclaimed_chargedparticleselectronic": "Charged Particle Anomaly (Electronic)",
    "anomaliesclaimed_gammaelectronic": "Gamma/X-ray Anomaly (Electronic)",
    "anomaliesclaimed_gammaradiography": "Gamma/X-ray Anomaly (Radiographic)",
    "anomaliesclaimed_rf": "RF Emission Anomaly",
    "anomaliesclaimed_resistance": "Resistance Anomaly",
    "anomaliesclaimed_other": "Other Anomaly"
}


import matplotlib.pyplot as plt
import re
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

reset_triggered = st.session_state.pop("reset_triggered", False)


st.set_page_config(layout="wide")

# --- Reduce default Streamlit padding ---
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    ul {
        margin-top: 0.25rem;
        margin-bottom: 0.25rem;
        padding-left: 1.2rem;
    }
    li {
        margin-bottom: 0.1rem;
    }    
    .custom-filename {
        color: #FF4B4B; /* Same as default Streamlit body text color */
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }  
    label[data-testid="stWidgetLabel"] {
        min-height: 0px !important;
        padding: 0 !important;
        margin: 0 !important;
        line-height: 0 !important;
    }

/* Target the text inside buttons */
button[data-testid="stBaseButton-secondary"] p {
    font-size: 0.8rem !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* Optionally reduce padding around the button too */
button[data-testid="stBaseButton-secondary"] {
    padding: 0.2rem 0.5rem !important;
    margin-bottom: 0.1rem !important;
}

    </style>
""", unsafe_allow_html=True)

#st.cache_data.clear()

# --- LOAD DATA FROM PUBLIC GOOGLE SHEETS WITH CACHING ---
@st.cache_data
def load_csv(url):
    return pd.read_csv(url)

# --- LOAD DATA ---
metadata_url = "https://docs.google.com/spreadsheets/d/1jIgF-NNQ2sug4ILxs-qFrp4JrewOfj2qEn3er9fh0BE/export?format=csv"
checklist_url = "https://docs.google.com/spreadsheets/d/1PeIZKaXtn1gs7kSn3tb6NfMvSXoYxbwJBUwIRN0SotA/export?format=csv"
justifications_url = "https://docs.google.com/spreadsheets/d/1TFZYM6sYoQNN3BQ1v_EAdAS9U2p3EJaVQlQyejocsBU/export?format=csv"

metadata_df = load_csv(metadata_url)
checklist_df = load_csv(checklist_url)
justifications_df = load_csv(justifications_url)

# --- Standardize column names ---
metadata_df.columns = metadata_df.columns.str.strip()
checklist_df.columns = checklist_df.columns.str.strip()
justifications_df.columns = justifications_df.columns.str.strip()

metadata_df.rename(columns={"filename": "Filename"}, inplace=True)
checklist_df.rename(columns={"filename": "Filename"}, inplace=True)
justifications_df.rename(columns={"filename": "Filename"}, inplace=True)

metadata_df = metadata_df[metadata_df["Filename"].notna() & (metadata_df["Filename"].str.strip() != "")]

# --- GROUP CHECKBOXES ---
def get_checkbox_groups(headers):
    groups = {
        "Document Type": [],
        "Sample materials": [],
        "Sample shapes (initial)": [],
        "Hydrogen isotopes": [],
        "Hydrogen loading": [],
        "Stimulation": [],
        "Diagnostics Used": [],
        "Anomalies Claimed": []
    }
    for h in headers:
        if h.startswith("documenttype_"):
            groups["Document Type"].append(h)
        elif h.startswith("material_"):
            groups["Sample materials"].append(h)
        elif h.startswith("shape_"):
            groups["Sample shapes (initial)"].append(h)
        elif h.startswith("fuel_"):
            groups["Hydrogen isotopes"].append(h)
        elif h.startswith("loading_"):
            groups["Hydrogen loading"].append(h)
        elif h.startswith("stimulation_"):
            groups["Stimulation"].append(h)
        elif h.startswith("diagnosticsused_"):
            groups["Diagnostics Used"].append(h)
        elif h.startswith("anomaliesclaimed_"):
            groups["Anomalies Claimed"].append(h)
    return groups

def clean_citation(raw_citation):
    """Remove URLs and trim content after 'First Author:' or 'Keywords:'."""
    if not isinstance(raw_citation, str):
        return ""
    # Remove URLs
    citation = re.sub(r"http\S+", "", raw_citation)
    # Cut at First Author: or Keywords:
    citation = re.split(r"First Author:|Keywords:", citation)[0]
    return citation.strip()

# --- UI ---
st.title("LENR Literature Explorer")

col1, col2, col3 = st.columns([2, 3, 4], gap="medium")

# --- LEFT COLUMN (COL1) FILTERS WITH ALL/ANY LOGIC ---
# --- LEFT COLUMN (COL1) FILTERS WITH ALL/ANY LOGIC ---
# --- LEFT COLUMN (COL1) FILTERS WITH ALL/ANY LOGIC ---
with col1:
    with st.container(border=True, height=800):
        st.subheader("Filter Papers:")
        st.markdown("Refresh page to reset filters")

        checklist_headers = checklist_df.columns.tolist()[1:]
        checkbox_groups = get_checkbox_groups(checklist_headers)
        selected_filters = {}  # dict with logic and field list per group
        group_items = list(checkbox_groups.items())

        # --- Step 1: Always show Document Type first ---
        group_name, fields = group_items[0]  # This should be "Document Type"
        with st.expander(group_name, expanded=True):
            options = ["All Document Types"] + [FILTER_LABELS.get(f, f) for f in fields]
            selected_label = st.radio("", options, key="doc_type_radio", index=0)

            selected_field = None
            if selected_label != "All Document Types":
                selected_field = next((f for f in fields if FILTER_LABELS.get(f) == selected_label), None)
                #if selected_field:
                selected_filters[group_name] = {"logic": "Only one", "fields": [selected_field]}

            show_experiment_filters = selected_field == "documenttype_experimental"

        # --- Step 2: Show other filters only if "Experimental Paper" is selected ---
        if show_experiment_filters:
            for i, (group_name, fields) in enumerate(group_items[1:]):  # Skip Document Type
                with st.expander(group_name, expanded=True):
                    logic = st.radio(
                        "", ["any of:", "all of:"],
                        index=0,
                        key=f"{group_name}_logic",
                        horizontal=True,
                        format_func=lambda x: f"**{x}**"
                    )

                    # --- Select All / None Buttons ---
                    if st.button("Select All", key=f"{group_name}_select_all"):
                        for field in fields:
                            st.session_state[field] = True

                    if st.button("Select None", key=f"{group_name}_select_none"):
                        for field in fields:
                            st.session_state[field] = False

                    # --- Checkboxes ---
                    selected_fields = []
                    for field in fields:
                        label = FILTER_LABELS.get(field, field.replace("_", " ").title())
                        default = True if field not in st.session_state else st.session_state[field]
                        checked = st.checkbox(label, key=field, value=default)
                        if checked:
                            selected_fields.append(field)

                    # --- Add to filters only if relevant ---
                    #if selected_fields or logic == "all of:":
                    selected_filters[group_name] = {"logic": logic, "fields": selected_fields}

                if i < len(group_items[1:]) - 1:
                    st.markdown("**and**")




# Middle Column: Matching Papers
with col2:
    with st.container(border=True, height=800):
        st.subheader("Matching Papers:")
        st.markdown("<a name='top'></a>", unsafe_allow_html=True)
 
        #st.markdown("### 🔍 Debug: Filter Dict")
        #st.json(selected_filters)


        def apply_filters(df, filter_dict):
            mask = pd.Series([True] * len(df))

            for group_name, settings in filter_dict.items():
                fields = settings["fields"]
                logic = settings["logic"]

                # If no fields selected, exclude all
                if not fields:
                    return df.iloc[0:0]

                submask = df[fields].astype(bool)

                if group_name == "Document Type":
                    field = fields[0]
                    mask &= df[field] == 1
                else:
                    if logic == "all of:":
                        mask &= submask.all(axis=1)
                    elif logic == "any of:":
                        # Avoid fallback to unfiltered if all unchecked
                        if submask.shape[1] == 0:
                            return df.iloc[0:0]
                        mask &= submask.any(axis=1)

            return df[mask]



        matches = apply_filters(checklist_df, selected_filters)


        merged_df = matches.merge(metadata_df, on="Filename", how="left")
        merged_df = merged_df.sort_values(by="Year", ascending=False)

        total = metadata_df.shape[0]
        showing = merged_df.shape[0]

        if merged_df.empty:
            st.markdown("**No papers matching the selected criteria.**")
        else:
            st.markdown(f"**Matching {showing} of {total} total papers.**")

            # Histogram: Papers per year
            if showing > 0:

                # Determine year range
                min_year = int(merged_df["Year"].min())
                max_year = int(merged_df["Year"].max())
                year_span = max_year - min_year + 1

                if year_span > 40:
                    # Use 5-year bins
                    bin_size = 5
                    bins = range(min_year - (min_year % bin_size), max_year + bin_size, bin_size)
                    merged_df["Year_Bin"] = pd.cut(merged_df["Year"], bins=bins, right=False)
                    year_counts = merged_df["Year_Bin"].value_counts().sort_index()
                    labels = [f"{int(interval.left)}–{int(interval.right - 1)}" for interval in year_counts.index]
                else:
                    year_counts = merged_df["Year"].value_counts().sort_index()
                    labels = [int(y) for y in year_counts.index]

                # Plot
                fig, ax = plt.subplots(figsize=(8, 3))
                ax.bar(labels, year_counts.values, color="skyblue")
                ax.set_xlabel("Year")
                ax.set_ylabel("Number of Papers")
                ax.yaxis.get_major_locator().set_params(integer=True)
                ax.tick_params(axis='x', labelrotation=45)
                st.pyplot(fig)

            st.markdown("---")

            # Top pagination (assign once to session state)
            # Pagination: TOP
            page_size = 20
            total_pages = (showing + page_size - 1) // page_size

            top_left, middle, top_right = st.columns([1, 3, 5])
            with top_left:
                st.markdown(
                    f"<div style='text-align: left; padding-top: 0.6rem;'>"
                    f"Page"
                    f"</div>",
                    unsafe_allow_html=True
                )
            with middle:
                page = st.number_input("", min_value=1, max_value=total_pages, value=1, step=1, key="page_number")            
            start = (page - 1) * page_size
            end = start + page_size
            with top_right:
                st.markdown(
                    f"<div style='text-align: right; padding-top: 0.6rem;'>"
                    f"Showing papers {start + 1}–{min(end, showing)} out of {showing}"
                    f"</div>",
                    unsafe_allow_html=True
                )

            st.markdown("---")


            # Paper list
            if "selected_filename" not in st.session_state:
                st.session_state.selected_filename = None

            for idx, row in merged_df.iloc[start:end].iterrows():
                year = int(row["Year"]) if not pd.isna(row["Year"]) else "Unknown"
                if st.button(f"{year}: {row['Filename']}", key=f"btn_{start + idx}"):
                    st.session_state.selected_filename = row['Filename']
                    st.rerun()
                st.caption(clean_citation(row['Citation']))

            st.markdown("---")

            # BOTTOM pagination block
            # Pagination: BOTTOM (just visual mirror)
            bottom_left, bottom_right = st.columns([1, 2])
            with bottom_left:
                st.markdown(f"**Page:** {page}")
            with bottom_right:
                st.markdown(
                    f"<div style='text-align: right;'>"
                    f"Showing papers {start + 1}–{min(end, showing)} out of {showing}"
                    f"</div>",
                    unsafe_allow_html=True
                )

            # Back to Top button
            st.markdown("[⬆ Back to Top](#top)")




# Right Column: Justifications + Checklist summary
# Right Column: Justifications + Checklist summary
with col3:
    with st.container(border=True, height=800):
        st.subheader("Details:")
        if st.session_state.get("selected_filename"):
            filename = st.session_state.selected_filename

            # Show citation and PDF link at the top
            meta_row = metadata_df[metadata_df["Filename"] == filename]
            if not meta_row.empty:
                citation = clean_citation(meta_row.iloc[0].get("Citation", ""))
                url = meta_row.iloc[0].get("URL", "")
                year = meta_row.iloc[0].get("Year", "")
                display_name = f"{int(year)}: {filename}" if pd.notna(year) else filename
                st.markdown(f"<div class='custom-filename'>{display_name}</div>", unsafe_allow_html=True)
                if isinstance(citation, str) and citation.strip():
                    st.markdown(citation.strip())
                if isinstance(url, str) and url.strip():
                    st.markdown(f"[📄 View PDF]({url})")

            just_row = justifications_df[justifications_df['Filename'] == filename]
            just_check = checklist_df[checklist_df['Filename'] == filename]

            if not just_row.empty and not just_check.empty:
                # Add pages_long if available
                pages_long = just_row.iloc[0].get("pages_long")
                if pd.notna(pages_long):
                    st.markdown(f"**Length**: {int(pages_long)} page(s)")

                sections = {
                    "Document Type": "documenttype_",
                    "Sample materials": "material_",
                    "Sample shapes (initial)": "shape_",
                    "Hydrogen isotopes": "fuel_",
                    "Hydrogen loading": "loading_",
                    "Stimulation": "stimulation_",
                    "Diagnostics Used": "diagnosticsused_",
                    "Anomalies Claimed": "anomaliesclaimed_"
                }

                justification_fields = {
                    "Document Type": "documenttype_justification",
                    "Sample materials": "material_justifications",
                    "Sample shapes (initial)": "shape_justifications",
                    "Hydrogen isotopes": "fuel_justifications",
                    "Hydrogen loading": "loading_justifications",
                    "Stimulation": "stimulation_justifications",
                    "Diagnostics Used": "diagnosticsused_justifications",
                    "Anomalies Claimed": "anomaliesclaimed_justifications"
                }

                for section_title, prefix in sections.items():
                    st.markdown(f"##### {section_title}")

                    # Add shape_summary above the checklist entries in Forms section
                    if section_title == "Forms":
                        shape_summary = just_row.iloc[0].get("shape_summary")
                        if isinstance(shape_summary, str) and shape_summary.strip():
                            st.markdown(f"<i>{shape_summary.strip()}</i>", unsafe_allow_html=True)

                    # Checklist variables
                    for col in just_check.columns:
                        if col.startswith(prefix) and just_check.iloc[0][col] == 1:
                            label = FILTER_LABELS.get(col, col)
                            st.markdown(f"- **{label}**")

                    # Justification paragraph
                    just_col = justification_fields.get(section_title)
                    if just_col in just_row.columns:
                        justification = just_row.iloc[0][just_col]
                        if isinstance(justification, str) and justification.strip():
                            # Insert line breaks where a new justification starts
                            formatted = justification.replace('" "', '"<br>"')
                            st.markdown(f"<span style='color:gray'>{formatted}</span>", unsafe_allow_html=True)

                # Add controls_summary if available
                controls = just_row.iloc[0].get("controls_summary")
                if isinstance(controls, str) and controls.strip():
                    st.markdown("##### Control Experiments")
                    st.markdown(f"<span style='color:gray'>{controls.strip()}</span>", unsafe_allow_html=True)

                # Corrections submission via embedded Google Form
                if filename:
                    with st.expander("Submit a Correction"):
                        url = f"https://docs.google.com/forms/d/e/1FAIpQLSfF2xt7APZP0Q57QhODjkfxRYDOYiUSp5jTVo_8N68-2FCnww/viewform?embedded=true&entry.1418398831={filename}&hl=en"
                        st.markdown(
                            f"""<iframe src="{url}" width="100%" height="750" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>""",
                            unsafe_allow_html=True
                        )

            else:
                st.warning("No details found for selected file.")        

