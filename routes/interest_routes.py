from agents.buyer_notification_agent import buyer_notification_agent
'''
router = APIRouter(
    prefix="/interest",
    tags=["Interest"]
)

@router.post("/")
def send_interest(data: dict):

    print("\n========== BUYER REQUEST ==========")
    print("Property ID:", data["property_id"])
    print("Buyer Name:", data["buyer_name"])
    print("Phone:", data["phone"])
    print("Purpose:", data["purpose"])

    notification = buyer_notification_agent({
        "name": data["buyer_name"],
        "phone": data["phone"],
        "purpose": data["purpose"]
    })

    return {
        "message": "Owner notified successfully",
        "notification": notification
    }
'''

from fastapi import APIRouter

router = APIRouter()

@router.post("/interest")
def send_interest(data: dict):

    print("\n====== New Property Enquiry ======")
    print("Buyer Name:", data["buyer_name"])
    print("Phone:", data["phone"])
    print("Purpose:", data["purpose"])

    return {
        "message": "Interest sent"
    }