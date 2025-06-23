from controllers.chat_controller import ChatController

# TODO: Initialize the ChatController
chat_controller = ChatController()

# TODO: Ensure a user session for testing and print the user ID
user_id = chat_controller.ensure_user_session()
print(user_id)