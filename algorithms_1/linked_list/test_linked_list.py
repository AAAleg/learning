import unittest

from linked_list import Node, LinkedList

class TestLinkedListMethods(unittest.TestCase):

  def test_empty_list(self):
    l = LinkedList()

    self.assertEqual(l.head, None)
    self.assertEqual(l.tail, None)

  def test_list_with_one_node(self):
    l = LinkedList()
    n = Node(1)

    l.add_in_tail(n)

    self.assertEqual(l.head, n)
    self.assertEqual(l.tail, n)

  def test_list_length(self):
    l = LinkedList()
    n = Node(1)

    l.add_in_tail(n)

    self.assertEqual(l.len(), 1)
    self.assertEqual(l.head, n)
    self.assertEqual(l.tail, n)

  def test_list_length_with_few_elements(self):
    l = LinkedList()
    h = Node(1)
    t = Node(3)

    for node in [h, Node(2), t]:
      l.add_in_tail(node)

    self.assertEqual(l.len(), 3)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, t)

  def test_find(self):
    l = LinkedList()
    h = Node(1)
    t = Node(4)
    s = Node(3)

    for node in [h, Node(5), s, Node(6), t]:
      l.add_in_tail(node)

    self.assertEqual(l.find(3), s)

  def test_find_in_end(self):
    l = LinkedList()
    h = Node(1)
    s = Node(3)

    for node in [h, Node(5), s, Node(6), s]:
      l.add_in_tail(node)

    self.assertEqual(l.find(3), s)

  def test_find_in_beging(self):
    l = LinkedList()
    s = Node(3)

    l.add_in_tail(s)
    l.add_in_tail(Node(5))
    l.add_in_tail(Node(6))

    self.assertEqual(l.find(3), s)

  def test_find_all(self):
    l = LinkedList()
    s = Node(3)
    s2 = Node(3)
    s3 = Node(3)

    for node in [s, Node(5), s2, Node(6), s3]:
      l.add_in_tail(node)

    self.assertEqual(l.find_all(3), [s, s2, s3])

  def test_clean_list_with_one_element(self):
    l = LinkedList()
    h = Node(1)
    
    l.add_in_tail(h)

    self.assertEqual(l.len(), 1)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, h)

    l.clean()

    self.assertEqual(l.len(), 0)
    self.assertEqual(l.head, None)
    self.assertEqual(l.tail, None)

  def test_clean(self):
    l = LinkedList()
    h = Node(1)
    t = Node(4)

    for node in [h, Node(2), Node(3), t]:
      l.add_in_tail(node)

    self.assertEqual(l.len(), 4)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, t)

    l.clean()

    self.assertEqual(l.len(), 0)
    self.assertEqual(l.head, None)
    self.assertEqual(l.tail, None)

  def test_insert_after_node_is_none_in_empty_list(self):
    l = LinkedList()
    h = Node(1)
    
    l.insert(None, h)

    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, h)

  def test_insert_after_node_is_none_in_head_of_list(self):
    l = LinkedList()
    h = Node(1)
    t = Node(2)

    l.add_in_tail(t)
    l.insert(None, h)

    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, t)

  def test_insert_after_node_is_none_in_the_body_of_list(self):
    l = LinkedList()
    h = Node(1)
    a = Node(2)
    t = Node(4)

    l.add_in_tail(h)
    l.add_in_tail(a)
    l.add_in_tail(t)

    self.assertEqual(l.len(), 3)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, t)

    l.insert(a, Node(3))
    
    self.assertEqual(l.len(), 4)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, t)

  def test_insert_after_node_is_none_in_the_tail_of_list(self):
    l = LinkedList()
    h = Node(1)
    a = Node(2)
    t = Node(3)

    l.add_in_tail(h)
    l.add_in_tail(a)
    l.insert(a, t)
    
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, t)

  def test_delete_from_list_with_one_element(self):
    l = LinkedList()
    i = Node(1)

    l.add_in_tail(i)

    self.assertEqual(l.len(), 1)
    self.assertEqual(l.head, i)
    self.assertEqual(l.tail, i)

    l.delete(1)

    self.assertEqual(l.len(), 0)
    self.assertEqual(l.head, None)
    self.assertEqual(l.tail, None)


  def test_delete_from_head(self):
    l = LinkedList()
    h = Node(1)
    m = Node(2)
    t = Node(3)

    l.add_in_tail(h)
    l.add_in_tail(m)
    l.add_in_tail(t)

    self.assertEqual(l.len(), 3)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, t)

    l.delete(1)

    self.assertEqual(l.len(), 2)
    self.assertEqual(l.head, m)
    self.assertEqual(l.tail, t)

  def test_delete_from_body(self):
    l = LinkedList()
    h = Node(1)
    m = Node(2)
    t = Node(3)

    l.add_in_tail(h)
    l.add_in_tail(m)
    l.add_in_tail(t)

    self.assertEqual(l.len(), 3)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, t)

    l.delete(2)

    self.assertEqual(l.len(), 2)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, t)

  def test_delete_from_tail(self):
    l = LinkedList()
    h = Node(1)
    m = Node(2)
    t = Node(3)

    l.add_in_tail(h)
    l.add_in_tail(m)
    l.add_in_tail(t)

    self.assertEqual(l.len(), 3)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, t)

    l.delete(3)

    self.assertEqual(l.len(), 2)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, m)

  def test_delete_all_from_head(self):
    l = LinkedList()
    h = Node(1)
    m = Node(2)
    t = Node(3)

    for node in [h, Node(1), Node(1), m, t]:
      l.add_in_tail(node)

    self.assertEqual(l.len(), 5)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, t)

    l.delete(1, all=True)

    self.assertEqual(l.len(), 2)
    self.assertEqual(l.head, m)
    self.assertEqual(l.tail, t)

  def test_delete_all_from_body(self):
    l = LinkedList()
    h = Node(1)
    m = Node(2)
    t = Node(3)

    for node in [h, m, Node(2), Node(2), t]:
      l.add_in_tail(node)

    self.assertEqual(l.len(), 5)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, t)

    l.delete(2, all=True)

    self.assertEqual(l.len(), 2)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, t)

  def test_delete_all_from_tail(self):
    l = LinkedList()
    h = Node(1)
    m = Node(2)
    t = Node(3)

    for node in [h, m, Node(3), Node(3), t]:
      l.add_in_tail(node)

    self.assertEqual(l.len(), 5)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, t)

    l.delete(3, all=True)

    self.assertEqual(l.len(), 2)
    self.assertEqual(l.head, h)
    self.assertEqual(l.tail, m)


if __name__ == '__main__':
    unittest.main()