import pandas as pd


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

def load_data():
    metadata_url = "https://docs.google.com/spreadsheets/d/1jIgF-NNQ2sug4ILxs-qFrp4JrewOfj2qEn3er9fh0BE/export?format=csv"
    checklist_url = "https://docs.google.com/spreadsheets/d/1PeIZKaXtn1gs7kSn3tb6NfMvSXoYxbwJBUwIRN0SotA/export?format=csv"
    metadata_df = pd.read_csv(metadata_url)
    checklist_df = pd.read_csv(checklist_url)
    checklist_df = checklist_df.apply(pd.to_numeric, errors="ignore").replace({'0': 0, '1': 1}).astype(int, errors="ignore")
    metadata_df.columns = metadata_df.columns.str.strip()
    checklist_df.columns = checklist_df.columns.str.strip()
    metadata_df.rename(columns={"filename": "Filename"}, inplace=True)
    checklist_df.rename(columns={"filename": "Filename"}, inplace=True)
    metadata_df = metadata_df[
        metadata_df["Filename"].notna() &
        (metadata_df["Filename"].str.strip() != "") &
        (metadata_df["Skip"] != 1) &
        metadata_df["Processed"].notna()
    ]
    checklist_df = checklist_df.merge(
        metadata_df[["Filename", "Publisher_Category"]],
        on="Filename",
        how="left"
    )
    checklist_df["Publisher_Category"] = checklist_df["Publisher_Category"].fillna("Other category or unknown")
    publisher_dummies = pd.get_dummies(checklist_df["Publisher_Category"], prefix="publishercategory")
    checklist_df = pd.concat([checklist_df, publisher_dummies], axis=1)
    publisher_counts = checklist_df["Publisher_Category"].value_counts().to_dict()
    for col in publisher_dummies.columns:
        raw_name = col.replace("publishercategory_", "")
        display_name = raw_name.replace("_", " ")
        count = publisher_counts.get(raw_name, 0)
        FILTER_LABELS[col] = f"{display_name} ({count})"
    return metadata_df, checklist_df

def parse_query_params(query_params):
    parsed = {}
    for key, value in query_params.items():
        for slug, group in GROUP_SLUGS.items():
            if key == f"{slug}_logic":
                parsed.setdefault(group, {})["logic"] = value[0] if isinstance(value, list) else value
            elif key == f"{slug}_fields":
                parsed.setdefault(group, {})["fields"] = value[0].split(",") if isinstance(value, list) else value.split(",")
    parsed["anomaly_reporting_mode"] = query_params.get("anomaly_reporting_mode", ["reported"])[0]
    return parsed

def apply_filters(df, filter_dict):
    mask = pd.Series([True] * len(df))
    doc_type_settings = filter_dict.get("Document Type", {})
    is_experimental = (
        doc_type_settings.get("fields") == ["documenttype_experimental"]
        if doc_type_settings else False
    )
    if is_experimental:
        mode = filter_dict.get("anomaly_reporting_mode", "reported")
        anomaly_cols = [col for col in df.columns if col.startswith("anomaliesclaimed_")]
        anomaly_sums = df[anomaly_cols].sum(axis=1)
        if mode == "reported":
            mask &= (anomaly_sums > 0)
        elif mode == "none":
            mask &= (anomaly_sums == 0)
    for group_name, settings in filter_dict.items():
        if group_name == "Anomaly Types" and mode == "none":
            continue
        fields = settings["fields"]
        logic = settings["logic"]
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

def build_selected_filters(query_params):
    selected_filters = {}
    for slug, group_name in GROUP_SLUGS.items():
        logic_key = f"{slug}_logic"
        fields_key = f"{slug}_fields"
        logic_val = query_params.get(logic_key, ["any of:"])[0] if isinstance(query_params.get(logic_key), list) else query_params.get(logic_key)
        fields_val = query_params.get(fields_key, [""])[0] if isinstance(query_params.get(fields_key), list) else query_params.get(fields_key)
        fields = fields_val.split(",") if fields_val else []
        if logic_val or fields:
            selected_filters[group_name] = {
                "logic": logic_val or "any of:",
                "fields": fields
            }
    return selected_filters
