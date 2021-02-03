#!/usr/bin/env python3
"""

"""

import sys
import os
import mimetypes
import tempfile

# Import the email modules we'll need
from email import policy
from email.parser import Parser

from subprocess import run

PRINTER = 'Officejet-Pro-8600'


def main(msg_stream):
    msg = Parser(policy=policy.default).parse(msg_stream)

    print(msg.keys())

    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Temp dir is: {temp_dir}")

        for attachment in msg.iter_attachments():
            fn = attachment.get_filename()
            extension = (os.path.splitext(attachment.get_filename())[1] if fn else
                         mimetypes.guess_extension(attachment.get_content_type()))

            data = attachment.get_content()

            # Write attachment
            with tempfile.NamedTemporaryFile(suffix=extension) as outfile:
                print(f'Attachment filename is {outfile.name}, extension is {extension}')
                outfile.write(data.encode('utf-8') if isinstance(data, str) else data)

                # Print attachment
                print_attachment(outfile.name, extension)


def print_attachment(path, extension):
    """"""
    if extension == '.pdf':
        # Print directly using lp
        print(f"Printing: {path}")
        run(["/usr/bin/lp", "-d", PRINTER, path])
    else:
        # Try to convert to pdf using libreoffice
        with tempfile.NamedTemporaryFile(suffix=".pdf") as outfile:
            print(f"Converting: {path} to {outfile.name}")
            run(["/usr/bin/python3", "/usr/bin/unoconv", "-o", outfile.name, path])
            print_attachment(outfile.name, ".pdf")


if __name__ == '__main__':
    main(sys.stdin)
