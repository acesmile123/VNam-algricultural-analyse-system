# Hướng dẫn chạy Pipeline Dự đoán Năng suất / Sản lượng

## Cấu trúc

- `data/`: có X_train.csv (dùng để tạo preprocessor ở notebook 02_scaling_encoding.ipynb) và final_sau_missingvalues.csv (dùng để lấy lag_*).
- `src/`: Chứa mã nguồn xử lý dữ liệu, feature engineering, và pipeline.
- `models/`: Chứa các model máy học, preprocessor (02_scaling_encoding.ipynb).
- `predict.py`: Script chính để chạy dự đoán cho một mẫu dữ liệu mới.

## Những gì đã thực hiện

### Chạy 02_scaling_encoding.ipynb để lấy preprocessor.joblib

- `X_train.csv`: Dữ liệu huấn luyện (được tạo từ notebook 01) để fit Scaler.
- `02_scaling_encoding.ipynb`: thêm bước lưu, chạy lại và có được `models/preprocessor.joblib`

### Pipeline

1. Input gồm:
``` bash
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
    "yield_ta_per_ha": 0, # Placeholder, bỏ cũng được
    "area_thousand_ha": 227.8 # Diện tích năm 2024
```

2. Gộp df_input với df_final_sau_missingvalues và cho qua các bước trong file feature_engineering.py (clean, tạo features, ...)
- Output sau khi qua bước này chỉ còn df_input đã clean và thêm features (Xem ở hàm process_single_input trong file [`src/feature_engineering.py`](src/feature_engineering.py))

3. Tiếp tục cho df_input qua preprocessor.joblib (đã tạo từ [02_scaling_encoding.ipynb](02_scaling_encoding.ipynb))

4. Cho qua ensemble (Xem chi tiết [`src/ensemble.py`](src/ensemble.py))

5. output cuối cùng 
```bash
"yield_ton_per_ha": Năng suất tấn/ha
"production_tonnes": production_pred[0] * 1000 # Sản lượng theo tấn 
```
## Cách chạy để test

### 1. Tạo venv
```bash
python -m venv venv
venv/Scripts/activate
```

### 2. Chạy requirements.txt
```bash
pip install -r requirements.txt
```

### 3. Nấu cháo
```bash
python predict.py
```

Kết quả dự đoán (Năng suất và Sản lượng) sẽ được in ra màn hình. Có thể thay đổi input trong [predict.py](predict.py)

## Lưu ý quan trọng

- **Trọng số Ensemble**: Hiện tại tôi đang để ở [src/config.py](src/config.py), theo file evaluate_production.ipynb trong drive
