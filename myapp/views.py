from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
import pandas as pd
from cryptography.fernet import Fernet

from .models import FileApi
from .serializers import CheckCartaoSerializer


dictionary = {"NOME": [],
              "DATA": [],
              "LOTE": [],
              "QTDREGISTRO": [],
              "NUMLOTE": [],
              "NUMCARTAO": []}


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def laod_key():
    try:
        open("secret.key", "rb").read()
    except:
        generate_key()
    return open("secret.key", "rb").read()


def encrypt_message(message, key):
    encoded_message = message.encode()
    f = Fernet(key)
    encrypt_message = f.encrypt(encoded_message)
    return encrypt_message


def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypt_message_message = f.decrypt(encrypted_message)
    return decrypt_message_message


key_f = laod_key()


class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def get_queryset(self):
        return FileApi.objects.all()

    def post(self, request, format=None):
        file_obj = request.FILES['file']
        fileContent = "None"
        new_file = []
        init = True
        mid = False
        while fileContent:
            if init is False:
                mid = True

            fileContent = file_obj.readline()
            fileContent = fileContent.strip()
            if init:
                nome = fileContent[0:29]
                data = fileContent[29:37]
                lote = fileContent[37:45]
                qtdregistro = fileContent[45:51]
                new_file.extend((nome, data, lote, qtdregistro))
                init = False
            if mid:
                numeracao_no_lote = fileContent[0:7]
                numero_cartao = fileContent[7:26]
                new_file.extend((numeracao_no_lote, numero_cartao))
        data = list()
        for i in new_file:
            clean = str(i)
            clean = clean.replace(" ", "").replace("b'", "").replace("'", "")
            data.append(clean)
        for i in range(len(data)):
            if i >= 4 and i < (len(data) - 4):
                if i % 2 == 0:
                    dictionary["NOME"].append(data[0])
                    dictionary["DATA"].append(data[1])
                    dictionary["LOTE"].append(data[2])
                    dictionary["QTDREGISTRO"].append(data[3])
                    dictionary["NUMLOTE"].append(data[i])
                    dictionary["NUMCARTAO"].append(data[i+1])
        data = pd.DataFrame.from_dict(dictionary)

        for i in data.values:
            unique_l = str(i[1]) + str(i[2][4:]) + str(i[3]) + str(i[4])
            unique_l = unique_l.replace('-', '')
            FileApi.objects.create(nome=i[0], data=i[1], lote=i[2],
                                   quantidade_registro=i[3],
                                   numeracao_no_lote=i[4],
                                   numero_cartao=encrypt_message(i[5], key_f),
                                   unique=unique_l)
        # closing the file
        file_obj.close()
        # Process the file here
        return Response({'message': 'File uploaded successfully'})


class CheckCartaoView2(APIView):
    serializer_class = CheckCartaoSerializer

    def post(self, request, format=None, many=True):
        serializer = CheckCartaoSerializer(data=request.data, many=True)
        if serializer.is_valid():
            itens = []
            all_products = FileApi.objects.all()
            myValues = all_products.values_list()
            for i in request.data:
                card = str(i.get('numero_cartao'))
                for i in myValues:
                    new = str(decrypt_message(i[6][1:], key_f))
                    new = new[1:].replace("'", "")
                    if new == card:
                        itens.append(i[7])
        return Response(itens)
