from services.email_services import send_email


def notification_agent(state):

    print("\n===== Sending Emails =====\n")

    for buyer in state["recommended_buyers"]:

        body = f"""
🏠 NEW PROPERTY RECOMMENDATION

Location : {state['location']}

Price : ₹{state['price']:,.0f}

Bedrooms : {state['features']['bedroom']}

Bathrooms : {state['features']['bathroom']}

Owner Name : {state['owner_name']}

Phone : {state['phone']}

Status : {state['status']}

AI Recommendation:
{buyer['analysis']}
"""

        try:

            send_email(
                buyer["email"],
                "Property Recommendation",
                body
            )

            print(
                f"Successfully sent to {buyer['email']}"
            )

        except Exception as e:

            print(
                f"Failed for {buyer['email']}"
            )

            print(e)

    return state