# Duck Typing: It is a concept where the type of an object is determined by its behaviour and not by its class 


class InkJetPrinter:
    def PrintDoc(self , document ):
        print("Ink jet printer printing: ",document)

class LaserPrinter:
    def PrintDoc(self , document ):
        print("Laser printer printing: ",document)

class PDFWritwe:
    def PrintDoc(self , document ):
        print(f"PDFWriter saving {document} as pdf ")


def StartPrinting(device):
    device.PrintDoc("Marvellous notes")

def main ():
   StartPrinting(InkJetPrinter())
   StartPrinting(LaserPrinter())
   StartPrinting(PDFWritwe()) 

main()