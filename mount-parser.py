"""
mount_parser.py is used for parsing the string ourput of the `mount` command.
"""

#imports
import argparse

def convert_mount_enty_to_humnan_readable(mount_entry):
    """
    Converts a mount entry to a human-readable format.
    The fomrat of the mount entry is expected to be similar to: "[source] on [mount point] type [filesystem type] ([mount options])"
    Args:
        mount_entry (str): The mount entry string to convert.
        
    Returns:
        str: A human-readable representation of the mount entry.
    """
    if ("on" and "type") not in mount_entry:
        raise ValueError("Invalid mount entry format. Expected format: '[source] on [mount point] type [filesystem type] ([mount options])'")
    
    mount_entry_fields = mount_entry.split(" ")
    


    print(mount_entry)
    return mount_entry  # This should be replaced with actual conversion logic

def main():
    """
    The main function of the mount parser script.
    """
    convert_mount_enty_to_humnan_readable("/dev/mapper/s on / type ext4 (rw,relatime)") 

if __name__ == "__main__":
    main()
