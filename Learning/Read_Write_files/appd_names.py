import json


# file = open('formatted-alerts.json')
# alerts = json.load(file)
#
# rules = alerts['healthRuleMembers']
#
# for rule in rules:
#     print(rule['model']['name'] + ',')


with open('formatted-alerts.json', 'r') as read_file:
    alert_data = json.load(read_file)
    health_rule_members = alert_data['healthRuleMembers']

print(type(health_rule_members))