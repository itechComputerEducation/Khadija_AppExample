import json

def chatbot_response(message):

    message = message.lower()

    # ✅ Check booking first (more specific)
    if "book goa" in message:
        return {"reply": "✅ Booking Goa... Done!", "book": {"place": "Goa", "price": 5000}}

    elif "book manali" in message:
        return {"reply": "✅ Booking Manali... Done!", "book": {"place": "Manali", "price": 7000}}

    # ✅ Then check general queries
    elif "goa" in message:
        return {"reply": "Goa trip costs ₹5000. Type 'book goa' to confirm", "place": "Goa", "price": 5000}

    elif "manali" in message:
        return {"reply": "Manali trip costs ₹7000. Type 'book manali' to confirm", "place": "Manali", "price": 7000}

    elif "show" in message:
        return {"reply": "Showing your bookings..."}

    else:
        return {"reply": "I can help you book trips (Goa/Manali). Try typing 'Goa' or 'Manali'"}