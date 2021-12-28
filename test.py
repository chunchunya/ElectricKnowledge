import requests, json
url = 'http://localhost:8088/Change'
js = json.dumps('{"nodes":{"210":{"labels": "变电站","attrs":{"transformerSubstation_type": "变电站","elevation": "","name": "###沙岭变###","DC_voltage_level": "","highest_voltage_level": 500,"region": "沈阳"}}},'
                '"links":{"114": {"labels": "变电站", "attrs":{"name": "白浑#2线","length": "39.33","voltage_level": "220"}}}}', ensure_ascii=False)
data = {'cha_data': '{"nodes":{"210":{"labels": "变电站","attrs":{"transformerSubstation_type": "变电站","elevation": "","name": "###沙岭变###","DC_voltage_level": "","highest_voltage_level": 500,"region": "沈阳"}}},'
                '"links":{"114": {"labels": "变电站", "attrs":{"name": "白浑#2线","length": "39.33","voltage_level": "220"}}}}'}
r = requests.post(url, data)
print(r)

