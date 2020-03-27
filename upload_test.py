import boto3

ddb = boto3.resource('dynamodb', aws_access_key_id='A#KIA#JMS6#MK2ED#RKO#3DUQ#', aws_secret_access_key='Ny#aaT/y#Z1YJ83WO#gHO4gk2#TSD0x4#jA7YvlM#dNsgR', region_name='us-east-2')
table = ddb.Table('listings')


def put_listing():
    table.put_item(
        Item={
            'listing_id': '1234',
            'title': 'Margiela GATs',
            'designer': 'Maison Margiela',
            'category': 'Shoes',
            'size': '12',
            'price': 150
        }
    )

put_listing()