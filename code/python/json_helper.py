#!/usr/bin/python
import json
import requests

def check_json_field(value, key):                                                                                                
    if not value.has_key(key):
        print("Invalid json missing key %s" % key)
        return False
    
    if not isinstance(value[key], dict):
        print("Invalid json invalid key %s" % key)
        return False

    return True

def json_loads(data):
    text = json.loads(data)
    print("json loads: %s" % text)
    if check_json_field(text, "test") is True:
        test = text.get("test")
        print("a=%d, b=%d, c=%d, d=%s, e=%s" % \
                (test.get("a"), test.get("b"), test.get("c"), test.get("d"), test.get("e")))
    return text

def json_dumps(data):
    data_dump = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    print("json dumps: %s" % data_dump)

def json_request():
    url = 'https://github.com/timeline.json'
    r = requests.get(url)
    data = r.json()
    print("json request:%s" % data)
    for key, value in data.items():
        print("%s=%s" % (key, value))

def main():
    jsonData = '{"test":{"a":1,"b":2.0,"c":false,"d":null,"e":"string"}}';
    text = json_loads(jsonData)
    json_dumps(text)
    json_request()


if __name__ == "__main__":
    main()
