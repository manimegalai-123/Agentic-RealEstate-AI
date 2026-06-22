from fastapi import APIRouter

from schemas.price_schema import PriceInput
from services.price_predictor import predict_price
from typing import List
from fastapi import APIRouter, UploadFile, File


router = APIRouter(
    prefix="/price",
    tags=["Price Prediction"]
)


@router.post("/")
def get_price(data: PriceInput):

    feature_dict = data.dict()

    price = predict_price(feature_dict)

    return {
        "predicted_price": float(price)
    }
