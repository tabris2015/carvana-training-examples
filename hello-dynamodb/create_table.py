import boto3


def create_devices_table(dynamodb=None):
    dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")
    # Table defination
    table = dynamodb.create_table(
        TableName="Students",
        KeySchema=[
            {
                "AttributeName": "CI",
                "KeyType": "HASH"  # Partition key
            },
            {
                "AttributeName": "Name",
                "KeyType": "RANGE"  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "CI",
                # AttributeType defines the data type. "S" is string type and "N" is number type
                "AttributeType": "N"
            },
            {
                "AttributeName": "Name",
                "AttributeType": "S"
            },
        ],
        ProvisionedThroughput={
            # ReadCapacityUnits set to 10 strongly consistent reads per second
            "ReadCapacityUnits": 10,
            "WriteCapacityUnits": 10  # WriteCapacityUnits set to 10 writes per second
        }
    )
    return table


if __name__ == "__main__":
    device_table = create_devices_table()
    # Print table status
    print("Status:", device_table.table_status)
