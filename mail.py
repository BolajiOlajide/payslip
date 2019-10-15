import base64
import sys

from apiclient import errors


def get_messages(service, email):
    try:
        query = f"from:{email}"
        user_id = "me"
        response = service.users().messages().list(userId=user_id, q=query).execute()
        messages = []
        if "messages" in response:
            messages.extend(response["messages"])

        while "nextPageToken" in response:
            page_token = response["nextPageToken"]
            response = (
                service.users()
                .messages()
                .list(userId=user_id, q=query, pageToken=page_token)
                .execute()
            )
            messages.extend(response["messages"])

        return messages
    except errors.HttpError as error:
        print(f"An error occurred: {error}")


def get_message_detail(message_id, service):
    try:
        return service.users().messages().get(userId="me", id=message_id).execute()
    except errors.HttpError as error:
        print(f"An error occured {error}")


def download_attachments(messages, service):
    for message in messages:
        message_detail = get_message_detail(message["id"], service)

        internal_date = message_detail.get('internalDate')
        message_id = message_detail.get('id')

        for part in message_detail["payload"]["parts"]:
            print(f'Scraping email with message ID: {message_id}')
            filename = part.get("filename")
            print(filename, '<===')

            if filename:
                try:
                    # import pdb; pdb.set_trace()
                    file_data = base64.urlsafe_b64decode(
                        part["body"]["data"].encode("UTF-8")
                    )
                    path = f"attachments/{filename}"
                    with open('jue.txt', "w") as f:
                        f.write('One two threee!')

                    file = open(path, 'w')
                    file.write(file_data)
                    file.close()
                    print(f'Successfully saved to {path}')
                except KeyError:
                    print('Something funky! is missing...')


def scrape_email(service):
    email = input('Enter the Payer's email address you\'ll like to scrape: \n')
    print(f'Scraping payslips from: {email}\n')

    messages = get_messages(service, email)

    print(f'Got {len(messages)} emails from {email}. Will begin downloading the payslips shortly.')
    return download_attachments(messages, service)
