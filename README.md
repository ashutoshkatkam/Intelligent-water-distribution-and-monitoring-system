Intelligent Water Distribution and Monitoring System

Youtube link for demonstration video: https://youtu.be/y5hNoUl6csE

Project Idea

The project Intelligent water distribution system, as the name says it is all about management of water supply throughout the scale, right from small societies, townships to entire urban infrastructure and also for irrigation water supply management. The main task of the water distribution system is to maintain the water in the tank and also generate the water bills to the individual households which involve human efforts. This system can be automated using the Internet of things.

Solution Requirements:

The proposed system should continuously monitor the main tank water level and should automatically switch on/off the motors according to the tank water level and alert the admins.it should monitor the water flow of the individual houses and store the flow rate of each house in the DynamoDB to generate the water bills. The tank water level and the bills should be visualized in the Mobile App so that the Admin can monitor them. Alerts should be sent to Admin through SNS notification whenever the tank is full or empty.

Project Flow:

Main tank water level and water flow to individual houses are continuously published to AWS IoT core (Use Online simulator sensor for water flow and water level)

Create a rule and actions in AWS IoT core to store the data in Amazon DynamoDB.

Create a rule and action in AWS IoT to send SNS when the tank level is full or empty.

Create an API using Amazon API gateway and lambda function to retrieve the data from DynamoDB.

Create the mobile app to display tank water level

Retrieve the flowrate of individual houses, generate bills, and display them in mobile App
