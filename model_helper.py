# -*- coding: utf-8 -*-
from einvoice.models import Terminal, Group_1
from types import *

class Store():

    @staticmethod
    def getStoreTree(group1_id):

        stores = Terminal.objects.filter( group_1_id = group1_id )
        group1 = Group_1.objects.get( pk= group1_id )

        g1_tree = { 'name': group1.name }
        sub_tree = {}

        for store in stores:

            # parent is group2
            if store.group_2_id:

                # key of group2 is existed, then add to 'child'
                if store.group_2.uuid in sub_tree:
                    group2_uuid = store.group_2.uuid
                    sub_tree[group2_uuid]['child'][store.uuid] = { 'name': store.name }

                # there is no attribure of group2
                else:
                    group2 = {
                                'uuid':  store.group_2.uuid,
                                'type': 'group2',
                                'name': store.group_2.name,
                                'child': {},
                             }

                    group2['child'][store.uuid] = { 'name': store.name }

                    uuid = group2['uuid']
                    sub_tree[uuid] = group2

            # parent is group1
            else:
                sub_tree[store.uuid] = { 'name': store.name }

        g1_tree['child'] = sub_tree

#        g1_tree = { 'name':'tree', 'child':{ 'name': 'child' } }
#        print g1_tree
        return g1_tree


