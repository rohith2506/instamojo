'''
Yuji wordpress blog
vineetdhanawat.com imap google
Read mail from python script

Challanges/Advancements:-
1) Read/unread emails
2) remove spam
3) Generate statistics
4) Allow Email address form

@Author: Rohith
'''

import getpass, imaplib
import email
import email.header


def read_mail(username, password):
	'''
	get all unread messages from mail and parse the values and mark them as read 
	'''
	imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
	imap.login(username, password)
	imap.select('INBOX')

	status, response = imap.search(None, 'UNSEEN', 'FROM', 'rohithfortopcoder@gmail.com')
	unread_msg_nums = response[0].split()[::-1]
	print len(unread_msg_nums)

	messages = []
	for e_id in unread_msg_nums:
		_, response = imap.fetch(e_id, '(RFC822)')
		raw_email = response[0][1]
		email_message = email.message_from_string(raw_email)
		subject = email_message['subject']
		subject.strip()
		for part in email_message.walk():
			if part.get_content_type() == "text/plain":
				body = part.get_payload(decode=True)
				body = body.strip()
				break
		messages.append((subject, body))
	print messages

	for e_id in unread_msg_nums:
		imap.store(e_id, '+FLAGS', '\Seen')

	imap.close()
	imap.logout()
	return messages
