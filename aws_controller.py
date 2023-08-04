import boto3

dynamo_client = boto3.resource('dynamodb')
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