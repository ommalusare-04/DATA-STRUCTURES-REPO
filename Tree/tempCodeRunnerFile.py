    succ=self.get_successor(rt)
            rt.data=succ.data
            rt.right = self.deleteNode(rt.right,succ.data)
            r