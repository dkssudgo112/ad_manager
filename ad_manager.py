# -*- coding: utf-8 -*-

import ldap3

def connect():
    # Connect to the AD server as a super user
    server = ldap3.Server("your_ad_server", port=389, use_ssl=False)
    return ldap3.Connection(server, user="super_user_dn", password="super_user_password", auto_bind=True)

def add_user():
    # Create a new user
    conn = connect()
    user_dn = "cn=new_user_name,ou=Users,dc=your_domain,dc=com"
    user_attributes = {
        "objectClass": ["top", "person", "organizationalPerson", "user"],
        "cn": "new_user_name",
        "givenName": "New",
        "sn": "User",
        "displayName": "New User",
        "userPrincipalName": "new_user_name@your_domain.com",
        "unicodePwd": ldap3.utils.encode_password("password"),
        "userAccountControl": 512
    }
    conn.add(user_dn, attributes=user_attributes)

    # Unbind from the AD
    conn.unbind()

def delete_user():
    conn = connect()
    user_dn = "cn=new_user_name,ou=Users,dc=your_domain,dc=com"
    # Delete the user
    conn.delete(user_dn)

    # Unbind from the AD
    conn.unbind()

def make_group():
# Create a new group
    conn = connect()
    group_dn = "cn=new_group_name,ou=Groups,dc=your_domain,dc=com"
    group_attributes = {
        "objectClass": ["top", "group"],
        "cn": "new_group_name",
        "groupType": -2147483646,
        "sAMAccountName": "new_group_name",
        "description": "New Group"
    }
    conn.add(group_dn, attributes=group_attributes)

    # Unbind from the AD
    conn.unbind()

def delete_group():
    conn = connect()
    group_dn = "cn=new_group_name,ou=Groups,dc=your_domain,dc=com"
    # Delete the group
    conn.delete(group_dn)

    # Unbind from the AD
    conn.unbind()

def add_user_in_group():    
    # Add a user to a group
    conn = connect()
    user_dn = "cn=existing_user_name,ou=Users,dc=your_domain,dc=com"
    group_dn = "cn=existing_group_name,ou=Groups,dc=your_domain,dc=com"
    conn.modify(group_dn, {"member": [(ldap3.MODIFY_ADD, [user_dn])]})

    # Unbind from the AD
    conn.unbind()

def delete_user_in_group():
    # Add a user to a group
    conn = connect()
    user_dn = "cn=existing_user_name,ou=Users,dc=your_domain,dc=com"
    group_dn = "cn=existing_group_name,ou=Groups,dc=your_domain,dc=com"
    # Remove a user from a group
    conn.modify(group_dn, {"member": [(ldap3.MODIFY_DELETE, [user_dn])]})

    # Unbind from the AD
    conn.unbind()