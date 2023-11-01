def open_tag_to_json(xml_string):
    result = {}

    tag_start = xml_string.find("<")
    tag_end = xml_string.find(">")

    if tag_start == -1 or tag_end == -1:
        return result

    tag = xml_string[tag_start + 1:tag_end]
    remaining_content = xml_string[tag_end + 1:]

    if "/" in tag:
        return result

    if " " in tag:
        tag, attributes = tag.split(" ", 1)
        attributes = attributes.strip()
        result['tag'] = tag
        result['attributes'] = parse_attributes(attributes)
    else:
        result['tag'] = tag

    remaining_content = remaining_content.strip()

    if remaining_content.startswith("<"):
        nested_tag = find_nested_tag(remaining_content)
        if nested_tag:
            nested_tag_start = remaining_content.find("<" + nested_tag)
            nested_tag_end = remaining_content.find(">", nested_tag_start)

            if nested_tag_start != -1 and nested_tag_end != -1:
                nested_tag_content = remaining_content[nested_tag_end + 1:]
                result['children'] = open_tag_to_json(nested_tag_content)

    return result


def parse_attributes(attributes_string):
    attributes = {}

    while attributes_string:
        attr_start = attributes_string.find(' ')
        if attr_start == -1:
            attr_start = len(attributes_string)

        attr = attributes_string[:attr_start]
        attr_end = attr.find('=')

        if attr_end != -1:
            attr_name = attr[:attr_end].strip()
            attr_value_start = attr.find('"', attr_end)
            attr_value_end = attr.find('"', attr_value_start + 1)

            if attr_value_start != -1 and attr_value_end != -1:
                attr_value = attr[attr_value_start + 1:attr_value_end]
                attributes[attr_name] = attr_value

        if attr_start == len(attributes_string):
            break

        attributes_string = attributes_string[attr_start + 1:]
        attributes_string = attributes_string.strip()

    return attributes


def find_nested_tag(xml_string):
    tag_start = xml_string.find("<")
    tag_end = xml_string.find(">")

    if tag_start != -1 and tag_end != -1:
        return xml_string[tag_start + 1:tag_end]

    return None


# Ví dụ:
xml_string = '<person id="1" name="John Doe">'
json_data = open_tag_to_json(xml_string)
print(json_data)