import xmlplain

with open("./input.xml", encoding='utf-8') as finput:
  root = xmlplain.xml_to_obj(finput, strip_space=True, fold_dict=True)

with open("output_with_libs.yaml", "w", encoding='utf-8') as foutput:
  xmlplain.obj_to_yaml(root, foutput)