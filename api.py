from flask import Flask, request, jsonify
from utils import load_data, parse_query_params, build_selected_filters, apply_filters

app = Flask(__name__)

# Load data at startup
try:
    metadata_df, checklist_df = load_data()
except Exception as e:
    print(f"Error loading data: {e}")
    metadata_df, checklist_df = pd.DataFrame(), pd.DataFrame()  # Fallback to empty DataFrames

@app.route("/", methods=["GET"])
def get_filenames():
    try:
        query_params = request.args.to_dict(flat=False)
        selected_filters = build_selected_filters(query_params)
        matches = apply_filters(checklist_df, selected_filters)
        merged_df = matches.merge(metadata_df, on="Filename", how="left")
        
        # Apply search filter if provided
        search = query_params.get("search", [""])[0]
        if search:
            search_string_lower = search.strip().lower()
            merged_df = merged_df[
                merged_df["Matched Title"].str.lower().str.contains(search_string_lower, na=False) |
                merged_df["Matched All Authors"].str.lower().str.contains(search_string_lower, na=False)
            ]
        
        # Return filenames
        filenames = merged_df["Filename"].dropna().tolist()
        return jsonify({"filenames": filenames})
    except Exception as e:
        return jsonify({"error": f"Internal error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
