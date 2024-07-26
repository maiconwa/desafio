from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
import pandas as pd

from .models import FileApi
from .serializers import CheckCartaoSerializer
from .encrypt import load_key, encrypt_message, decrypt_message


dictionary = {"NOME": [],
              "DATA": [],
              "LOTE": [],
              "QTDREGISTRO": [],
              "NUMLOTE": [],
              "NUMCARTAO": []}


key_f = load_key()


class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def get_queryset(self):
        return FileApi.objects.all()

    def post(self, request, format=None):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'message': 'No file provided'}, status=400)
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
            last = FileApi.objects.all().last()
            if last is None:
                unique_l = str(i[1]) + str(i[2][4:]) + str(i[3]) + str(i[4])
                unique_l = unique_l.replace('-', '')
                FileApi.objects.create(nome=i[0],
                                       data=i[1],
                                       lote=i[2],
                                       quantidade_registro=i[3],
                                       numeracao_no_lote=i[4],
                                       numero_cartao=encrypt_message(i[5], key_f),
                                       unique=unique_l)
            else:
                unique_l = str(last.pk) + str(i[1]) + str(i[2][4:]) + str(i[3]) + str(i[4])
                unique_l = unique_l.replace('-', '')
                FileApi.objects.create(nome=i[0],
                                       data=i[1],
                                       lote=i[2],
                                       quantidade_registro=i[3],
                                       numeracao_no_lote=i[4],
                                       numero_cartao=encrypt_message(i[5], key_f),
                                       unique=unique_l)
        # closing the file
        file_obj.close()
        # Process the file here
        return Response({'message': 'File uploaded successfully'}, status=201)


class CheckCard(APIView):
    serializer_class = CheckCartaoSerializer

    def post(self, request, format=None):
        serializer = CheckCartaoSerializer(data=request.data, many=True)
        if serializer.is_valid():
            card_numbers = [item['numero_cartao'] for item in serializer.validated_data]
            decrypted_items = []
            all_cards = FileApi.objects.all()
            print(card_numbers[0])

            for card in all_cards:
                decrypted_card = str(decrypt_message((card.numero_cartao)[1:], load_key())).replace("b'", "").replace("'", "")
                if decrypted_card in card_numbers:
                    decrypted_items.append(card.unique)

            return Response(decrypted_items, status=200)
        else:
            return Response(serializer.errors, status=400)
