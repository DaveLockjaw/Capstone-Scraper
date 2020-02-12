import boto3

dynamodb = boto3.resource('dynamodb',aws_access_key_id='AKIAIOQISPXCU4ZTULGA', aws_secret_access_key='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', region_name='us-east-2')
table = dynamodb.Table('listings')


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