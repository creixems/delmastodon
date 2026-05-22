from mastodon import Mastodon
import datetime
import time

# Replace these with your information
CLIENT_ID = '[INSERT HERE]'
CLIENT_SECRET = '[INSERT HERE]'
ACCESS_TOKEN = '[INSERT HERE]'
INSTANCE_URL = 'https://mastodon.social'  # e.g., https://mastodon.social

# Initialize Mastodon instance
mastodon = Mastodon(
    api_base_url=INSTANCE_URL,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    access_token=ACCESS_TOKEN
)

def delete_own_posts_from_date(year, month, day):
    # Get the target date
    target_date = datetime.date(year, month, day)
    
    # Retrieve your own posts
    user_posts = mastodon.account_statuses(mastodon.me()['id'])  # Get your own posts
    delete_count = 0  # Counter for deleted posts

    for status in user_posts:
        # Parse the date of the post
        post_date = status['created_at'].date()
        
        # Check if the post's date matches the target date
        if post_date == target_date:
            # Delete the post
            print(f"Deleting post: {status['content']} (ID: {status['id']})")
            mastodon.status_delete(status['id'])
            delete_count += 1
            print(delete_count)
            print("waiting 1s…\n")
            time.sleep(1)
            
            # Wait 1 minutes after 20 deletes
            if delete_count % 20 == 0:
                print("Paused for 30 minutes...")
                time.sleep(1 * 60)  # Sleep for 30 minutes (30 minutes * 60 seconds)

            # Pause every 30 deletions
            if delete_count % 30 == 0:
                print("Paused for 30 minutes...")
                time.sleep(31 * 60)  # Sleep for 30 minutes (30 minutes * 60 seconds)

if __name__ == "__main__":
    # Set the date you want to delete posts from
    delete_year = 2024  # Example: 2024
    delete_month = 9    # Example: September
    delete_day = 23     # Example: 23rd

    delete_own_posts_from_date(delete_year, delete_month, delete_day)