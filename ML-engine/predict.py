import sys
from pathlib import Path

# Add src to path so we can import from it
# This assumes predict.py is in d:\agri-app-cs331\machine_learning\
sys.path.append(str(Path(__file__).parent))

from src import pipeline

# Example Input (Matches the image provided by user)
input_data = {
    "province_name": "An Giang",
    "year": 2025,
    "commodity": "rice",
    "season": "winter_spring",
    "avg_temperature": 27.74333333333332,
    "min_temperature": 17.65233333333335,
    "max_temperature": 40.10466666666666,
    "surface_temperature": 28.337846153846158,
    "wet_bulb_temperature": 25.367282051282054,
    "precipitation": 4.424846153846153,
    "solar_radiation": 18.406230769230767,
    "relative_humidity": 78.1953076923077,
    "wind_speed": 2.378,
    "surface_pressure": 100.83476923076923,
    "surface_elevation": 4,
    "avg_ndvi": 0.5651,
    "soil_ph_level": 5.7,
    "soil_organic_carbon": 1.93,
    "soil_nitrogen_content": 0.2296,
    "soil_sand_ratio": 21.1,
    "soil_clay_ratio": 42.3,
    # Additional required fields
    "yield_ta_per_ha": 0, # Placeholder
    "area_thousand_ha": 227.8 # Example area
}

if __name__ == "__main__":
    print("=== Agri-App Yield Prediction Pipeline ===")
    try:
        result = pipeline.run_pipeline(input_data)
        if result:
            print("\nPrediction Success!")
            print(f"Predicted Yield: {result['yield_ton_per_ha']:.4f} ton/ha")
            print(f"Predicted Production: {result['production_tonnes']:.4f} tonnes")
        else:
            print("\nPrediction returned no result.")
    except Exception as e:
        print(f"\nError: {e}")
        print("\nTroubleshooting:")
        print("1. Ensure 'data/raw/final_sau_missingvalues.csv' exists.")
        print("2. Ensure 'models/preprocessor.joblib' exists (Run notebook 02).")
        print("3. Ensure models are in 'models/' directory.")
