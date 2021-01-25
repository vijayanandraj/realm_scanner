def dot_get(_dict, path, default=None):
  for key in path.split('.'):
    try:
      _dict = _dict[key]
    except KeyError:
      return default
  return _dict


ref_dict = {"clientSDKIn" : {"clientArgs" :
                                      {"app_info" : {"app_number" : 787912, "app_name": "TestApp"}},
                                        "cloud_info" : {"cloud_id" : "TestCloud", "cloud_provider" : "AZURE"}},
                                        "templateName" :  "Storage",
                            "methodArgs" : {"arg1" : "value1", "arg2" : "value2"}}


print(ref_dict)

print(dot_get(ref_dict, 'clientSDKIn.clientArgs.app_info.app_number'))


