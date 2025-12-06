import mailbox
import random

mbox = mailbox.mbox('/Users/lzhao/Documents/Jobs-rejections!.mbox')

for i, message in enumerate(mbox):
    if i >= 20:  # only first 10
        break

    # If the message is multipart, walk through the parts
    if message.is_multipart():
        parts = []
        for part in message.walk():
            if part.get_content_type() == 'text/plain':
                parts.append(part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8', errors='ignore'))
        text = "\n".join(parts)
    else:
        text = message.get_payload(decode=True)
        if text:
            text = text.decode(message.get_content_charset() or 'utf-8', errors='ignore')

    print(f"----- Message {i+1} -----")
    print(text[:1000])  # print first 1000 chars to avoid huge output
    print()