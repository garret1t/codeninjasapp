import boto3

session = boto3.Session( aws_access_key_id='AKIAR5FKICKK3IMSNLW2', aws_secret_access_key='36X2mF+YfwcDu2TLp7XG6UigpZQAMuRtm0goC/iZ')
dynamo_client = session.resource('dynamodb',region_name='us-east-1')
table = dynamo_client.Table('YourTestTable')

def get_items():
    return table.scan()


def put_item(firstname,lastname,date,belt,level,activity):
    print("Put Item: " + firstname + " "+ lastname + " "+ belt + " "+ level + " "+ activity)
    return table.put_item(
        Item={
                                            "FirstName": firstname,
                                            "LastName": lastname,
                                            "Date": date,
                                            "Belt": belt,
                                            "Level": level,
                                            "Activity": activity,
        }
    )