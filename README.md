LENR Literature Explorer
The LENR Literature Explorer is a Streamlit-based web application for interactively exploring a curated database of experimental and theoretical papers related to Low-Energy Nuclear Reactions (LENR).

🔍 Key Features
Faceted Search Interface: Users can filter papers using a rich set of criteria such as:

Document type (e.g. experimental, review, methods)

Materials used (e.g. Pd, Ti, Ni)

Sample geometries (e.g. foil, rod, thin film)

Hydrogen isotopes (H, D, none)

Loading methods, stimulation techniques, diagnostics, and claimed anomalies

Advanced Filter Logic: Each filter group supports logic options:

Any of (OR logic)

All of (AND logic)

Document type is handled as a single-choice category.

URL-Persistent Filters: Selected filters are reflected in the URL query string, making it easy to bookmark or share filtered views.

Matching Paper View: The center column shows all papers matching the active filters, with pagination and a publication histogram by year.

Details View: Selecting a paper shows a detailed summary in the right column:

Citation, link to the PDF, experimental justifications

Annotated checklist showing materials, methods, diagnostics, and anomalies

Embedded Google Form for corrections or additions

Reset Filters: A dedicated button resets all filters, selections, and URL state for a clean start.

📚 Data Sources
This app dynamically loads from three public Google Sheets:

metadata – citation and bibliographic data

checklist – binary flags for experimental variables

justifications – free-text reasoning for each classification

