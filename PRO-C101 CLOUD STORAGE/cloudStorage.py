import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BIjB0iuW3jf8dEH1LWfWiRU1k5K7DQD2wGT2y1NHYMB89HYl4U3GlqG8NOu0_n-cjAxKwvmCWrKVCNRlMVteBwtPNWAszVj0n_UZWn3MtxehT2EaDEhIkzYCDZ7MAcxkm0hSwLA'
    transferData = TransferData(access_token)

    file_from = input("ENTER FILE PATH TO TRANSFER")

    file_to = input("ENTER THE FULL PATH TO UPLOAD TO DROPBOX")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)


main()