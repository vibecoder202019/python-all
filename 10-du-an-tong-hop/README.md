# Module 10: Dự án Tổng hợp — ML API End-to-End

## Mục tiêu

Kết hợp tất cả kiến thức đã học vào một dự án hoàn chỉnh:
- Train ML model
- Xây dựng FastAPI serve model
- Viết tests
- Document API

---

## Dự án: House Price Predictor API

Xây dựng API dự đoán giá nhà dựa trên California Housing dataset.

### Yêu cầu chức năng

1. **Train model** — RandomForest trên California Housing
2. **API endpoints:**
   - `GET /health` — health check
   - `GET /model/info` — thông tin model
   - `POST /predict` — dự đoán giá 1 căn nhà
   - `POST /predict/batch` — dự đoán nhiều căn
   - `POST /model/retrain` — train lại model (optional)
3. **Validation** — Pydantic models cho input/output
4. **Tests** — pytest cho tất cả endpoints
5. **Documentation** — Swagger UI tự động

---

## Cấu trúc dự án

```
10-du-an-tong-hop/
├── README.md              ← bạn đang đọc
├── app/
│   ├── main.py
│   ├── models/schemas.py
│   ├── routers/predict.py
│   └── services/ml_service.py
├── scripts/
│   └── train_model.py
├── tests/
│   └── test_api.py
└── models/                ← model files (generated)
```

---

## Hướng dẫn thực hiện (tự làm)

### Bước 1: Train model
```bash
python scripts/train_model.py
```

### Bước 2: Implement API
- Copy cấu trúc từ Module 09
- Thay Iris → California Housing
- Input: 8 features (MedInc, HouseAge, AveRooms, ...)
- Output: predicted price

### Bước 3: Viết tests
```bash
pytest tests/ -v
```

### Bước 4: Chạy và test
```bash
uvicorn app.main:app --reload
open http://localhost:8000/docs
```

---

## Checklist hoàn thành

- [ ] Model train được với accuracy hợp lý (R² > 0.7)
- [ ] API chạy không lỗi
- [ ] Swagger UI hiển thị đúng
- [ ] POST /predict trả kết quả hợp lý
- [ ] Validation reject input sai
- [ ] Tests pass ≥ 80%
- [ ] Code có cấu trúc rõ ràng (routers, services, models)

---

## Mở rộng (optional)

Sau khi hoàn thành dự án cơ bản:

1. **Docker** — containerize API
2. **Database** — lưu prediction history (SQLite/PostgreSQL)
3. **Monitoring** — log predictions, track latency
4. **CI/CD** — GitHub Actions auto-test
5. **Deploy** — lên cloud (Railway, Render, AWS)

→ Tiếp tục với [MLOps Labs](../../labs/) để học deploy lên Kubernetes!

---

---

## Giải thích chi tiết (Tự học)

### Lệnh từng bước

```bash
python scripts/train_model.py
```
1. Load `fetch_california_housing()` — 8 features, target = giá nhà ($100k)
2. `train_test_split` → train RandomForestRegressor
3. Tính R², RMSE — đánh giá trên test set
4. `joblib.dump` → lưu model + scaler + metadata vào `models/`

```bash
uvicorn app.main:app --reload
```
- Server load model qua `MLService._load()` khi có request `/predict`

```bash
pytest tests/ -v
```
- `-v` verbose — hiện từng test pass/fail

---

### Giải thích code solution (tham khảo)

**`app/models/schemas.py`:**
```python
class HouseFeatures(BaseModel):
    med_inc: float = Field(..., ge=0)
    def to_features(self) -> list[float]:
        return [self.med_inc, self.house_age, ...]
```
- `to_features()` — chuyển Pydantic model → list số cho sklearn

**`app/services/ml_service.py`:**
```python
price = float(self._model.predict(scaled)[0])
return PricePrediction(
    predicted_price=round(price, 4),
    predicted_price_usd=round(price * 100_000, 2),
)
```
- Model predict giá đơn vị $100k → nhân 100_000 ra USD thực

**Luồng request POST /model/predict:**
```
Client JSON → Pydantic validate → to_features() → scaler.transform
→ model.predict → PricePrediction JSON → Client
```

---

### Checklist giải thích

| Mục | Cách kiểm tra |
|-----|---------------|
| R² > 0.7 | Xem output `train_model.py` |
| Validation | Gửi `med_inc: -1` → expect 422 |
| Tests | `pytest tests/ -v` → all passed |

---

## Gợi ý đáp án

Tham khảo implementation mẫu tại [solution/](solution/) — **chỉ xem sau khi đã tự làm**.
