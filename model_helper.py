# -*- coding: utf-8 -*-
from einvoice.models import Terminal
from types import *

class Store():

    @staticmethod
    def getStoreTree(group1_id):

        stores = Terminal.objects.filter( group_1_id = group1_id )
        tree = {}

        for store in stores:

            # parent is group2
            if store.group_2_id:

                # key of group2 is existed, then add to 'child'
                if store.group_2.uuid in tree:
                    group2_uuid = store.group_2.uuid
                    tree[group2_uuid]['child'][store.uuid] = store

                # there is no attribure of group2
                else:
                    group2 = {
                                'uuid': store.group_2.uuid,
                                'type': 'group2',
                                'name': store.group_2.name,
                                'child': {},
                             }

                    group2['child'][store.uuid] = store

                    uuid = group2['uuid']
                    tree[uuid] = group2

            # parent is group1
            else:
                tree[store.uuid] = store

        return tree


