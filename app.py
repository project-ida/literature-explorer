BASE_URL = "https://literature-explorer.streamlit.app/"
#BASE_URL = "http://localhost:8501/"

SUPPRESS_CACHING = 0

# Human-readable labels for filter variables
FILTER_LABELS = {
    "documenttype_tooshort": "⚠️ Too Short to Classify",
    "documenttype_experimental": "🔬 Experimental Paper",
    "documenttype_theoretical": "🧠 Theoretical Paper",
    "documenttype_methodsinstrument": "🛠️ Methods/Instrument Paper",
    "documenttype_review": "📖 Review Paper",
    "documenttype_slidedeck": "📊 Slide Deck",
    "documenttype_other": "❓ Other Document Type",

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

GROUP_SLUGS = {
    "document_type": "Document Type",
    "sample_materials": "Sample Materials",
    "sample_shapes": "Sample Shapes",
    "hydrogen_isotopes": "Hydrogen Isotopes",
    "hydrogen_loading": "Hydrogen Loading",
    "stimulation": "Stimulation",
    "diagnostics_used": "Diagnostics Used",
    "anomalies_claimed": "Anomaly Types",
    "publisher_category": "Publisher Category" 
}

# Define the desired order for Publisher Categories
PUBLISHER_ORDER = {
    "ICCF conference": 1,
    "LENR workshop": 2,
    "Other conference": 3,
    "J. Condensed Matter Nucl. Sci.": 4,
    "Fusion Technol.": 5,   
    "Phys. Rev. family": 6,
    "J. Electroanal. Chem.": 7,
    "J. Fusion Energy": 8,
    "Nuovo Cimento": 9, 
    "J. Alloys and Compounds": 10,
    "Curr. Sci.": 11,
    "J. Less-Common Met.": 12,
    "Int. J. Hydrogen Energy": 13,
    "J. New Energy": 14,
    "Electrochim. Acta": 15,
    "Nature": 16,    
    "Trans. Fusion Technol.": 17,        
    "Other journal": 18,   
    "LENR Sourcebook": 19,
    "LENR-CANR.org": 20,
    "Book": 21,
    "EPRI": 22,
    "Technical report": 23,    
    "Magazine/newspaper": 24,    
    "Infinite Energy": 25,    
    "Other category or unknown": 26,
    "Unknown": 99  # fallback
}


import matplotlib.pyplot as plt
import re
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

from urllib.parse import urlencode

@st.cache_data
def load_url_mappings():
    df = pd.read_csv("url-mappings.csv")
    return dict(zip(df["slug"], df["query_string"]))


debug_mode = st.query_params.get("debug") == "1"

query_params = st.query_params
short_slug = query_params.get("link", None)


if short_slug:
    mappings = load_url_mappings()
    if short_slug in mappings:
        raw_query_string = mappings[short_slug].split("#")[0]  # remove fragment if any
        sep = "&" if "?" in raw_query_string else "?"
        full_url = f"{BASE_URL}{raw_query_string}{sep}processedlink={short_slug}"

        st.markdown(f"""
            <div style="background-color: #eef2f5; border-left: 4px solid #2c91f0; padding: 1rem; margin-bottom: 1rem; border-radius: 0.25rem;">
                ✅ Found filter configuration for <strong>{short_slug}</strong>.<br><br>
                👉 <a href="{full_url}"><strong>Click here to load this filter configuration</strong></a>
            </div>
        """, unsafe_allow_html=True)

        st.stop()
    else:
        st.error(f"No preset found for `{short_slug}`.")
        st.stop()


# Only set the search_string once from URL
if "search_string" not in st.session_state:
    query_search = st.query_params.get("search", "")
    if isinstance(query_search, list):
        query_search = query_search[0]
    st.session_state["search_string"] = query_search


def slugify_group_name(name):
    return name.replace(" ", "_").lower()

def parse_query_params():
    parsed = {}
    for key, value in st.query_params.items():
        for slug, group in GROUP_SLUGS.items():
            if key == f"{slug}_logic":
                parsed.setdefault(group, {})["logic"] = value
            elif key == f"{slug}_fields":
                parsed.setdefault(group, {})["fields"] = value.split(",") if value else []

    # only set anomaly checkboxes if not already set by user interaction
    if "anomaly_reporting_mode" not in st.session_state:
        st.session_state["anomaly_reporting_mode"] = st.query_params.get("anomaly_reporting_mode", "reported")

    return parsed



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
    hr {
        margin-block-start: 0.1em !important;
        margin-block-end: 0.1em !important;
    }
    .custom-details1 {
        color: #FF4B4B; /* Same as default Streamlit body text color */
        font-size: 1.25rem;
        font-weight: 400;
        margin-bottom: 0.5rem;
    }  
    .custom-details2 {
        color: #000000; 
        font-size: 1.25rem;
        font-weight: 400;
        margin-bottom: 0.5rem;
    }     
    .custom-details3 {
        color: #CCCCCC; 
        font-size: 1.25rem;
        font-weight: 400;
        margin-bottom: 0.5rem;
    } 
    .custom-matches1 {
        color: #FF4B4B; /* Same as default Streamlit body text color */
        font-weight: 400;
        margin-bottom: 0.5rem;
    }  
    .custom-matches2 {
        color: #000000; 
        font-weight: 400;
        margin-bottom: 0.5rem;
    }     
    .custom-matches3 {
        color: #CCCCCC; 
        font-weight: 400;
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

if SUPPRESS_CACHING:
    st.cache_data.clear()

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

checklist_df = checklist_df.apply(pd.to_numeric, errors="ignore").replace({'0': 0, '1': 1}).astype(int, errors="ignore")

# --- Standardize column names ---
metadata_df.columns = metadata_df.columns.str.strip()
checklist_df.columns = checklist_df.columns.str.strip()
justifications_df.columns = justifications_df.columns.str.strip()

metadata_df.rename(columns={"filename": "Filename"}, inplace=True)
checklist_df.rename(columns={"filename": "Filename"}, inplace=True)
justifications_df.rename(columns={"filename": "Filename"}, inplace=True)

metadata_df = metadata_df[
    metadata_df["Filename"].notna() &
    (metadata_df["Filename"].str.strip() != "") &
    (metadata_df["Skip"] != 1) &
    metadata_df["Processed"].notna()    
]

# Merge Publisher_Category from metadata into checklist
checklist_df = checklist_df.merge(
    metadata_df[["Filename", "Publisher_Category"]],
    on="Filename",
    how="left"
)

# One-hot encode Publisher_Category (e.g., publishercategory_elsevier = 1)
checklist_df["Publisher_Category"] = checklist_df["Publisher_Category"].fillna("Other category or unknown")
publisher_dummies = pd.get_dummies(checklist_df["Publisher_Category"], prefix="publishercategory")
checklist_df = pd.concat([checklist_df, publisher_dummies], axis=1)

# Count number of rows for each Publisher Category (for display)
publisher_counts = checklist_df["Publisher_Category"].value_counts().to_dict()

for col in publisher_dummies.columns:
    # Extract original category name (e.g., "Elsevier")
    raw_name = col.replace("publishercategory_", "")
    display_name = raw_name.replace("_", " ")  # No .title()
    count = publisher_counts.get(raw_name, 0)
    FILTER_LABELS[col] = f"{display_name} ({count})"

# Parse filenames from URL
custom_filenames = st.query_params.get("filenames", "")
if isinstance(custom_filenames, list):
    custom_filenames = custom_filenames[0]  # Handle list input
custom_filenames = [f.strip() for f in custom_filenames.split(",") if f.strip()] if custom_filenames else []
# Validate filenames against metadata_df
valid_filenames = [f for f in custom_filenames if f in metadata_df["Filename"].values]
is_custom_list = len(valid_filenames) > 0


# --- GROUP CHECKBOXES ---
def get_checkbox_groups(headers):
    groups = {
        "Document Type": [],
        "Sample Materials": [],
        "Sample Shapes": [],
        "Hydrogen Isotopes": [],
        "Hydrogen Loading": [],
        "Stimulation": [],
        "Diagnostics Used": [],
        "Anomaly Types": [],
        "Publisher Category": []
    }
    for h in headers:
        if h.startswith("documenttype_"):
            groups["Document Type"].append(h)
        elif h.startswith("material_"):
            groups["Sample Materials"].append(h)
        elif h.startswith("shape_"):
            groups["Sample Shapes"].append(h)
        elif h.startswith("fuel_"):
            groups["Hydrogen Isotopes"].append(h)
        elif h.startswith("loading_"):
            groups["Hydrogen Loading"].append(h)
        elif h.startswith("stimulation_"):
            groups["Stimulation"].append(h)
        elif h.startswith("diagnosticsused_"):
            groups["Diagnostics Used"].append(h)
        elif h.startswith("anomaliesclaimed_"):
            groups["Anomaly Types"].append(h)
        elif h.startswith("publishercategory_"):
            groups["Publisher Category"].append(h)

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

def should_expand_group(group_name, fields, prefilled_filters):
    selected_fields = prefilled_filters.get(group_name, {}).get("fields", [])
    
    # If no fields are prefilled (i.e. changing document type), fallback to session_state
    if not selected_fields:
        return not all(st.session_state.get(field, True) for field in fields)

    return set(selected_fields) != set(fields)


# --- UI ---
#st.title("LENR Literature Explorer")


def build_selected_filters():
    selected_filters = {}

    for slug, group_name in GROUP_SLUGS.items():
        logic_key = f"{slug}_logic"
        fields_key = f"{slug}_fields"

        logic_val = st.query_params.get(logic_key)
        fields_val = st.query_params.get(fields_key)

        if fields_val:
            # Handle potential list input from multiple query params
            if isinstance(fields_val, list):
                fields = []
                for entry in fields_val:
                    fields += entry.split(",")
            else:
                fields = fields_val.split(",")
        else:
            fields = []

        if logic_val or fields:
            selected_filters[group_name] = {
                "logic": logic_val or "any of:",
                "fields": fields
            }

    return selected_filters

def apply_filters(df, filter_dict):
    mask = pd.Series([True] * len(df))

    # Check if we're filtering for experimental papers
    doc_type_settings = filter_dict.get("Document Type", {})
    is_experimental = (
        doc_type_settings.get("fields") == ["documenttype_experimental"]
        if doc_type_settings else False
    )

    # Only apply this filter if experimental
    if is_experimental:
        mode = st.session_state.get("anomaly_reporting_mode", "reported")
        anomaly_cols = [col for col in df.columns if col.startswith("anomaliesclaimed_")]
        anomaly_sums = df[anomaly_cols].sum(axis=1)

        if mode == "reported":
            mask &= (anomaly_sums > 0)
        elif mode == "none":
            mask &= (anomaly_sums == 0)

    # --- Now process all field-specific filters ---
    for group_name, settings in filter_dict.items():
        # Skip anomaly fields entirely if no anomalies reported is selected
        if group_name == "Anomaly Types" and mode == "none":
            continue  # skip specific anomaly filters

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
                mask &= submask.any(axis=1)

    return df[mask]


if debug_mode: 
    built_selected_filters = build_selected_filters()
    st.json(built_selected_filters)

    built_matches = apply_filters(checklist_df, built_selected_filters)
    st.markdown(built_matches)
    
    merged_df = built_matches.merge(metadata_df, on="Filename", how="left")
    st.json(merged_df["Filename"].dropna().tolist())


st.markdown("""
<style>
/* Hide the checkbox */
#popup-toggle {
  display: none;
}

/* Style the label like a link */
.popup-label {
  font-size: 0.8rem;
  color: #888;
  margin-left: 1rem;
  text-decoration: underline;
  cursor: pointer;
}

/* The popup overlay (initially hidden) */
.popup-overlay {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: rgba(0,0,0,0.6);
  display: none;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

/* Show when checkbox is checked */
#popup-toggle:checked ~ .popup-overlay {
  display: flex;
}

/* The popup content box */
.popup-box {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  max-width: 500px;
  font-size: 0.9rem;
  box-shadow: 0 2px 12px rgba(0,0,0,0.3);
  position: relative;
}

/* Close button inside popup */
.popup-box .close-label {
  position: absolute;
  top: 8px;
  right: 12px;
  font-size: 1.5rem;
  cursor: pointer;
}
</style>

<!-- Hidden checkbox toggle -->
<input type="checkbox" id="popup-toggle">

<div style='display: flex; justify-content: space-between; align-items: baseline; width: 100%;'>
  <h1 style='margin-bottom: 0.5rem;'>LENR Literature Explorer</h1>
  <div style='display: flex; justify-content: flex-end;'>
    <label for="popup-toggle" class="popup-label" style="margin-left: 1rem; margin-bottom: 0.5rem;">Acknowledgments</label>
    <a href="#" class="popup-label" onclick="event.preventDefault(); document.getElementById('saved-config-toggle').checked = true;" style="margin-left: 1rem; margin-bottom: 0.5rem;">Saved filter configurations</a>
  </div>
</div>

<!-- Popup content for Acknowledgments (shows when checkbox is checked) -->
<div class="popup-overlay">
  <div class="popup-box">
    <label for="popup-toggle" class="close-label">×</label>
    <h4>Acknowledgments</h4>
    <p>We would like to thank <strong>Jed Rothwell</strong> of <a href="https://www.lenr-canr.org" target="_blank">lenr-canr.org</a> for collecting a publicly accessible library of LENR papers, which this project draws on.</p>
    <p>Support from the <strong>Anthropocene Institute</strong> and <strong>ARPA-E</strong> is also gratefully acknowledged.</p>
  </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 3, 4], gap="medium")

# --- LEFT COLUMN (COL1) FILTERS WITH ALL/ANY LOGIC ---
with col1:
    with st.container(border=True, height=800):
        st.subheader("Filter Papers:")

        if is_custom_list:
            # Display custom list message with reset link
            st.markdown("""
                <div style="background-color: #eef2f5; border-left: 4px solid #2c91f0; padding: 0.75rem; margin-bottom: 1rem; border-radius: 0.25rem;">
                    A custom list of papers has been provided and filter settings do not apply. 
                    <a href="?"><strong>Click here to reset and return to filtering.</strong></a>
                </div>
            """, unsafe_allow_html=True)
        else:
            # Existing filter controls
            if "processedlink" in st.query_params:
                processedlink = st.query_params["processedlink"]
                st.markdown(f"""
                    <div style="background-color: #eef2f5; border-left: 4px solid #2c91f0; padding: 0.75rem; margin-bottom: 1rem; border-radius: 0.25rem;">
                        Filter configuration '<strong>{processedlink}</strong>' has been loaded.
                    </div>
                """, unsafe_allow_html=True)

            if st.button("🔄 Reset All Filters"):
                # Clear query params
                st.query_params.clear()
                # Clear document type radio
                st.session_state.pop("doc_type_radio", None)
                # Clear logic radios and checkboxes
                for group_name in GROUP_SLUGS.values():
                    st.session_state.pop(f"{group_name}_logic", None)
                for key in FILTER_LABELS:
                    st.session_state.pop(key, None)
                # Clear filename selection
                st.session_state.pop("selected_filename", None)
                st.session_state.pop("anomaly_reporting_reported", None)
                st.session_state.pop("anomaly_reporting_none", None)
                st.session_state["anomaly_reporting_reported"] = True
                st.session_state["anomaly_reporting_none"] = True
                # Rerun the app
                st.rerun()

            st.markdown("**Filter papers by**")

            checklist_headers = checklist_df.columns.tolist()[1:]
            checkbox_groups = get_checkbox_groups(checklist_headers)
            
            # Ensure defaults are set
            if "anomaly_reporting_reported" not in st.session_state:
                st.session_state["anomaly_reporting_reported"] = True
            if "anomaly_reporting_none" not in st.session_state:
                st.session_state["anomaly_reporting_none"] = True

            prefilled_filters = parse_query_params()
            selected_filters = {}  # dict with logic and field list per group
            group_items = list(checkbox_groups.items())

            # Publisher Category checkboxes
            publisher_fields = checkbox_groups.get("Publisher Category", [])
            publisher_fields.sort(key=lambda x: PUBLISHER_ORDER.get(
                x.replace("publishercategory_", "").replace("_", " "), 999
            ))

            with st.expander("Publisher Category", expanded=should_expand_group("Publisher Category", publisher_fields, prefilled_filters)):
                logic_key = "Publisher Category_logic"
                prefill = prefilled_filters.get("Publisher Category", {})
                if logic_key not in st.session_state:
                    st.session_state[logic_key] = prefill.get("logic", "any of:")
                logic = st.radio(
                    "Filter logic",
                    ["any of:"],
                    index=0 if st.session_state[logic_key] == "any of:" else 1,
                    key=logic_key,
                    horizontal=True,
                    format_func=lambda x: f"**{x}**",
                    label_visibility="collapsed"
                )
                if st.button("Select All", key="publisher_select_all"):
                    for field in publisher_fields:
                        st.session_state[field] = True
                if st.button("Select None", key="publisher_select_none"):
                    for field in publisher_fields:
                        st.session_state[field] = False
                selected_fields = []
                for field in publisher_fields:
                    label = FILTER_LABELS.get(field, field)
                    pre_fields = set(prefill.get("fields", []))
                    if field not in st.session_state:
                        st.session_state[field] = field in pre_fields if pre_fields else True
                    checked = st.checkbox(label, key=field)
                    if checked:
                        selected_fields.append(field)
                selected_filters["Publisher Category"] = {
                    "logic": st.session_state[logic_key],
                    "fields": selected_fields
                }

            st.markdown("**and**")

            # Document Type (always first)
            group_name, fields = group_items[0]
            with st.expander(group_name, expanded=True):
                options = ["All Document Types"] + [FILTER_LABELS.get(f, f) for f in fields]
                pre_selected_field = None
                doc_prefill = prefilled_filters.get(group_name, {})
                doc_fields = doc_prefill.get("fields", [])
                if doc_fields:
                    pre_selected_field = FILTER_LABELS.get(doc_fields[0])
                if "doc_type_radio" not in st.session_state:
                    st.session_state["doc_type_radio"] = pre_selected_field or "All Document Types"
                st.radio(
                    "Document Type",
                    options,
                    key="doc_type_radio",
                    label_visibility="collapsed"
                )
                if st.session_state.get("selected_filename") and pre_selected_field and st.session_state.doc_type_radio != pre_selected_field:
                    st.session_state.selected_filename = None
                selected_field = None
                if st.session_state.doc_type_radio != "All Document Types":
                    selected_field = next((f for f in fields if FILTER_LABELS.get(f) == st.session_state.doc_type_radio), None)
                    selected_filters[group_name] = {"logic": "Only one", "fields": [selected_field]}
                show_experiment_filters = selected_field == "documenttype_experimental"

            if show_experiment_filters:
                st.markdown("**and**")
                for i, (group_name, fields) in enumerate(group_items[1:]):
                    if group_name in ["Publisher Category"]:
                        continue
                    if group_name == "Anomaly Types":
                        with st.expander("Anomalies Claimed", expanded=True):
                            if "anomaly_reporting_mode" not in st.session_state:
                                st.session_state["anomaly_reporting_mode"] = "reported"
                            mode = st.radio(
                                "",
                                ["reported", "none"],
                                format_func=lambda x: "Yes" if x == "reported" else "No",
                                key="anomaly_reporting_mode",
                                horizontal=True
                            )
                        if st.session_state["anomaly_reporting_mode"] == "none":
                            continue
                        else:
                            st.markdown("**and**")
                    with st.expander(group_name, expanded=should_expand_group(group_name, fields, prefilled_filters)):
                        prefill = prefilled_filters.get(group_name, {})
                        pre_logic = prefill.get("logic", "any of:")
                        pre_fields = set(prefill.get("fields", []))
                        logic_key = f"{group_name}_logic"
                        if logic_key not in st.session_state:
                            st.session_state[logic_key] = pre_logic if pre_logic in ["any of:", "all of:"] else "any of:"
                        logic = st.radio(
                            "Filter logic",
                            ["any of:", "all of:"],
                            index=0 if st.session_state[logic_key] == "any of:" else 1,
                            key=logic_key,
                            horizontal=True,
                            format_func=lambda x: f"**{x}**",
                            label_visibility="collapsed"
                        )
                        if st.button("Select All", key=f"{group_name}_select_all"):
                            for field in fields:
                                st.session_state[field] = True
                        if st.button("Select None", key=f"{group_name}_select_none"):
                            for field in fields:
                                st.session_state[field] = False
                        selected_fields = []
                        for field in fields:
                            label = FILTER_LABELS.get(field, field)
                            if field not in st.session_state:
                                st.session_state[field] = field in pre_fields if pre_fields else True
                            checked = st.checkbox(label, key=field)
                            if checked:
                                selected_fields.append(field)
                        selected_filters[group_name] = {"logic": st.session_state[logic_key], "fields": selected_fields}
                    if i < len(group_items[1:]) - 2:
                        st.markdown("**and**")

            # Update URL with current filters (only if not using custom filenames)
            query_params = {}
            for slug, group_name in GROUP_SLUGS.items():
                if group_name in selected_filters:
                    settings = selected_filters[group_name]
                    query_params[f"{slug}_logic"] = settings["logic"]
                    query_params[f"{slug}_fields"] = ",".join(settings["fields"])
            if "selected_filename" in st.session_state:
                filters_changed = False
                for group_name, current in selected_filters.items():
                    prefill = prefilled_filters.get(group_name, {})
                    if prefill.get("logic") != current.get("logic") or set(prefill.get("fields", [])) != set(current.get("fields", [])):
                        filters_changed = True
                        break
                if filters_changed:
                    st.session_state.selected_filename = None
            query_params["anomaly_reporting_mode"] = st.session_state.get("anomaly_reporting_mode", "reported")
            if debug_mode:
                st.json(selected_filters)
            if not is_custom_list:
                st.query_params.clear()
                st.query_params.update(query_params)

# Middle Column: Matching Papers
with col2:
    with st.container(border=True, height=800):
        st.subheader("Matching Papers:")
        st.markdown("<a name='top'></a>", unsafe_allow_html=True)

        if is_custom_list:
            # Filter by provided filenames
            matches = checklist_df[checklist_df["Filename"].isin(valid_filenames)]
            if matches.empty:
                st.markdown("**No valid papers found for the provided identifiers.**")
        else:
            # Apply normal filter logic
            matches = apply_filters(checklist_df, selected_filters)

        st.markdown("---")

        query_params = st.query_params
        default_search = query_params.get("search", "")
        if isinstance(default_search, list):
            default_search = default_search[0]
        search_col1, search_col2 = st.columns([1, 8])
        with search_col1:
            st.markdown(
                f"<div style='text-align: left; padding-top: 0.45rem;'>Filter by</div>",
                unsafe_allow_html=True
            )
        with search_col2:
            search_string = st.text_input("", value=st.session_state["search_string"], key="search_string_inline_col2")

        st.markdown("---")

        merged_df = matches.merge(metadata_df, on="Filename", how="left")
        merged_df = merged_df.sort_values(by="Year", ascending=False)

        if search_string != st.query_params.get("search", ""):
            st.query_params.update(search=search_string)
            st.session_state["search_string"] = search_string

        if search_string.strip():
            search_string_lower = search_string.strip().lower()
            merged_df = merged_df[
                merged_df["Matched Title"].str.lower().str.contains(search_string_lower, na=False) |
                merged_df["Matched All Authors"].str.lower().str.contains(search_string_lower, na=False)
            ]

        total = metadata_df.shape[0]
        showing = merged_df.shape[0]

        if debug_mode:
            missing_filenames = set(metadata_df["Filename"]) - set(merged_df["Filename"])
            if missing_filenames:
                st.markdown("### ⚠️ Files excluded by current filters:")
                for fname in sorted(missing_filenames):
                    st.code(fname)

        if merged_df.empty:
            st.markdown("**No papers matching the selected criteria.**")
        else:
            st.markdown(f"**Matching {showing} of {total} total papers.**")
            # Histogram: Papers per year
            if showing > 0:
                min_year = int(merged_df["Year"].min())
                max_year = int(merged_df["Year"].max())
                min_year = 1985
                max_year = 2025
                year_span = max_year - min_year + 1
                if year_span > 41:
                    bin_size = 5
                    bins = range(min_year - (min_year % bin_size), max_year + bin_size, bin_size)
                    merged_df["Year_Bin"] = pd.cut(merged_df["Year"], bins=bins, right=False)
                    year_counts = merged_df["Year_Bin"].value_counts().sort_index()
                    labels = [f"{int(interval.left)}–{int(interval.right - 1)}" for interval in year_counts.index]
                else:
                    year_counts = merged_df["Year"].value_counts().sort_index()
                    labels = [int(y) for y in year_counts.index]
            zoom_enabled = st.checkbox("Zoom to Fit Y-Axis", value=False)
            fig, ax = plt.subplots(figsize=(8, 3))
            ax.bar(labels, year_counts.values, color="skyblue")
            ax.set_xlim(1985, 2025)
            if zoom_enabled:
                y_max = max(year_counts.values) if len(year_counts) > 0 else 1
                ax.set_ylim(0, int(y_max * 1.1))
            else:
                ax.set_ylim(0, 200)
            ax.set_xlabel("Year")
            ax.set_ylabel("Number of Papers")
            ax.tick_params(axis='x', labelrotation=45)
            st.pyplot(fig)
            st.markdown("---")
            # Pagination: TOP
            page_size = 20
            total_pages = (showing + page_size - 1) // page_size
            top_left, middle, top_right = st.columns([1, 3, 5])
            with top_left:
                st.markdown(
                    f"<div style='text-align: left; padding-top: 0.6rem;'>Page</div>",
                    unsafe_allow_html=True
                )
            with middle:
                page = st.number_input(
                    "Page Number",
                    min_value=1,
                    max_value=total_pages,
                    value=1,
                    step=1,
                    key="page_number",
                    label_visibility="collapsed"
                )
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
            if "selected_filename" not in st.session_state:
                st.session_state.selected_filename = None

            for idx, row in merged_df.iloc[start:end].iterrows():
                filename = row["Filename"]
                year = int(row["Year"]) if not pd.isna(row["Year"]) else "Unknown"
                matched_authors = row.get("Matched All Authors", "")
                matched_title = row.get("Matched Title", "")
                matched_publisher = row.get("Matched Publisher", "")
                publisher_category = row.get("Publisher_Category", "")
                matched_publisher = str(matched_publisher) if pd.notna(matched_publisher) else ""
                publisher_category = str(publisher_category) if pd.notna(publisher_category) else ""
                if matched_publisher and publisher_category and matched_publisher.strip() != publisher_category.strip():
                    matched_publisher_display = f"{matched_publisher} (category: {publisher_category})"
                else:
                    matched_publisher_display = matched_publisher
                display_name = f"<b>{year}</b>: {matched_authors}"
                st.markdown(f"""
                <div style="border: 0px solid #ddd; padding: 0rem; border-radius: 0.5rem; margin-bottom: 1rem;">
                    <div class="custom-matches1">{display_name}</div>
                    <div class="custom-matches2">{matched_title}</div>
                    <div class="custom-matches3">{matched_publisher_display}</div>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"🔍 View Details", key=f"btn_{start + idx}"):
                    st.session_state.selected_filename = filename
                    st.rerun()
                st.markdown("---")
            # Pagination: BOTTOM
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
            st.markdown("[⬆ Back to Top](#top)")
            if not merged_df.empty:
                matched_filenames = "\n".join(merged_df["Filename"].dropna().astype(str).tolist())
                st.markdown("###### All Matched Identifiers (for further processing):")
                st.text_area("", matched_filenames, height=100)      



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

                # --- NEW: Show matched metadata fields with conditional bracket logic ---
                matched_title = meta_row.iloc[0].get("Matched Title", "")
                matched_authors = meta_row.iloc[0].get("Matched All Authors", "")
                matched_publisher = meta_row.iloc[0].get("Matched Publisher", "")
                publisher_category = meta_row.iloc[0].get("Publisher_Category", "")
                citation = clean_citation(meta_row.iloc[0].get("Citation", ""))
                url = meta_row.iloc[0].get("URL", "")
                year = meta_row.iloc[0].get("Year", "")
                display_name = f"<b>{int(year)}</b>: {matched_authors}" if pd.notna(year) else matched_authors

                if matched_publisher and publisher_category and matched_publisher.strip() != publisher_category.strip():
                    matched_publisher_display = f"{matched_publisher} (category: {publisher_category})"
                else:
                    matched_publisher_display = matched_publisher

                st.markdown(f"<div class='custom-details1'>{display_name}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='custom-details2'>{matched_title}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='custom-details3'>{matched_publisher_display}</div>", unsafe_allow_html=True)

                if isinstance(url, str) and url.strip():
                    st.markdown(f"[📄 View PDF]({url})")

            just_row = justifications_df[justifications_df['Filename'] == filename]
            just_check = checklist_df[checklist_df['Filename'] == filename]

            if not just_row.empty and not just_check.empty:
                # Add pages_long if available
                pages_long = just_row.iloc[0].get("pages_long")
                if pd.notna(pages_long):
                    st.markdown(f"{int(pages_long)} page(s)")

                sections = {
                    "Document Type": "documenttype_",
                    "Sample Materials": "material_",
                    "Sample Shapes": "shape_",
                    "Hydrogen Isotopes": "fuel_",
                    "Hydrogen Loading": "loading_",
                    "Stimulation": "stimulation_",
                    "Diagnostics Used": "diagnosticsused_",
                    "Anomalies Claimed": "anomaliesclaimed_"
                }

                justification_fields = {
                    "Document Type": "documenttype_justification",
                    "Sample Materials": "material_justifications",
                    "Sample Shapes": "shape_justifications",
                    "Hydrogen Isotopes": "fuel_justifications",
                    "Hydrogen Loading": "loading_justifications",
                    "Stimulation": "stimulation_justifications",
                    "Diagnostics Used": "diagnosticsused_justifications",
                    "Anomalies Claimed": "anomaliesclaimed_justifications"
                }

                is_experimental = bool(just_check.iloc[0].get("documenttype_experimental") == 1)

                for section_title, prefix in sections.items():

                    if section_title == "Document Type":
                        # Compose the label + justification together in one Markdown block
                        document_type_block = ""

                        # Checklist label
                        for col in just_check.columns:
                            if col.startswith(prefix) and just_check.iloc[0][col] == 1:
                                label = FILTER_LABELS.get(col, col)
                                document_type_block += f"<p><strong>{label}</strong></p>"

                        # Justification text
                        just_col = justification_fields.get(section_title)
                        if just_col in just_row.columns:
                            justification = just_row.iloc[0][just_col]
                            if isinstance(justification, str) and justification.strip():
                                formatted = re.sub(r'\s*-\s*', ' ', justification).replace('" "', '"<br>"')
                                document_type_block += f"<p style='color:gray'>{formatted}</p>"

                        # Wrap in a styled div
                        st.markdown(f"""
                            <div style="background-color: #f5f5f5; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
                                {document_type_block}
                            </div>
                        """, unsafe_allow_html=True)

                    if section_title != "Document Type" and not is_experimental:
                        continue  # Show only Document Type unless paper is experimental

                    if section_title != "Document Type":
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
                                if section_title == "Document Type":
                                    st.markdown(f"**{label}**")  # No bullet
                                else:
                                    st.markdown(f"- **{label}**")  # Bullet for other sections

                        # Justification paragraph
                        just_col = justification_fields.get(section_title)
                        if just_col in just_row.columns:
                            justification = just_row.iloc[0][just_col]
                            if isinstance(justification, str) and justification.strip():
                                # Insert line breaks where a new justification starts
                                formatted = re.sub(r'\s*-\s*', ' ', justification).replace('" "', '"<br>"')

                                st.markdown(f"<span style='color:gray'>{formatted}</span>", unsafe_allow_html=True)

                # Add controls_summary if available
                controls = just_row.iloc[0].get("controls_summary")
                if is_experimental and isinstance(controls, str) and controls.strip():
                    st.markdown("##### Control Experiments")
                    st.markdown(f"<span style='color:gray'>{controls.strip()}</span>", unsafe_allow_html=True)

                with st.expander("Citation & Identifier"):
                    
                    if isinstance(citation, str) and citation.strip():
                        st.markdown(f"**Full Citation:** {citation.strip()}")                  
                    #st.markdown(f"**Internal filename:** {filename}")                        
                    google_file_id = meta_row.iloc[0].get("Google_FileID", "")
                    if isinstance(google_file_id, str) and google_file_id.strip():
                        #drive_url = f"https://drive.google.com/uc?export=download&id={google_file_id.strip()}"
                        drive_url = f"https://drive.google.com/file/d/{google_file_id.strip()}/view"
                        st.markdown(f"**Internal Identifier:** {filename} ([📄]({drive_url}))")
                    else:
                        st.markdown(f"**Internal Identifier:** {filename}")


                # Corrections submission via embedded Google Form
                if filename:
                    with st.expander("Submit a Comment"):
                        url = f"https://docs.google.com/forms/d/e/1FAIpQLSfF2xt7APZP0Q57QhODjkfxRYDOYiUSp5jTVo_8N68-2FCnww/viewform?embedded=true&entry.1418398831={filename}&hl=en"
                        st.markdown(
                            f"""<iframe src="{url}" width="100%" height="900" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>""",
                            unsafe_allow_html=True
                        )

            else:
                st.warning("No details found for selected file.")        

