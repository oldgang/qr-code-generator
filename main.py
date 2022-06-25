import qrcode
import cv2


class MainUI:
    def __init__(self):
        super().__init__()


class InfoUI:
    def __init__(self):
        super().__init__()


class QRcontroller():
    def generate(self, data, filename):
        # File name of the QR code Image
        QRCodefile = filename
        # Generating the QR code
        QRimage = qrcode.make(data)
        # Saving image into a file
        QRimage.save(QRCodefile)

    def read(self, filename):
        # read the QRCODE image
        image = cv2.imread(filename)
        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()
        # detect and decode
        data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
        # if there is a QR code
        # print the data
        if vertices_array is not None:
            print("QRCode data:")
            print(data)
        else:
            print("There was some error")


qr = QRcontroller()
qr.generate("https://ogloszenia.trojmiasto.pl", "ogloszenia3city.png")
qr.read("ogloszenia3city.png")
