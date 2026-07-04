#!/usr/bin/python3
"""Module for serializing and deserializing data using XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file.

    Args:
        dictionary: A Python dictionary to serialize.
        filename: The filename of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="    ")
    tree.write(filename, encoding="unicode", xml_declaration=False)


def deserialize_from_xml(filename):
    """Deserialize a Python dictionary from an XML file.

    Args:
        filename: The filename of the input XML file.

    Returns:
        A Python dictionary reconstructed from the XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    return {child.tag: child.text for child in root}
