def buyer_notification_agent(state):

    message = f"""
====== New Property Enquiry ======

Buyer Name : {state.get("buyer_name")}
Phone : {state.get("phone")}
Purpose : {state.get("purpose")}
"""

    print(message)

    state["notification"] = message

    return state