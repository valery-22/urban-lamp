from services.chat_service import ChatService

# Initialize the chat service
chat_service = ChatService()

# Simulate a user ID
user_id = "user123"

# Create a new chat session
chat_id = chat_service.create_chat(user_id)
print(f"Chat session created with ID: {chat_id}")

# Define a user message
user_message = "How can I contact your company by email?"
print(f"User Message: {user_message}")

try:
    ai_response = chat_service.process_message(user_id, chat_id, user_message)
    print(f"AI Response: {ai_response}")
except Exception as e:
    print(f"Error: {e}")

# TODO: Define and print a follow-up question
# TODO: Send the follow-up question to test context retention
# TODO: Print the AI's response to the follow-up questionç

follow_up_question = "Can you give en email address?"
print(f"Follow-up Question: {follow_up_question}")

try:
    follow_up_response = chat_service.process_message(user_id, chat_id, follow_up_question)
    print(f"AI Follow-up Response: {follow_up_response}")
except Exception as e:
    print(f"Error during follow-up: {e}")