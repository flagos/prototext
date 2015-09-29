import os
import unittest

try:
    from addressbook_pb2 import AddressBook, Person
except:
    print "Please make sure your protobuf 2.6.x is properly installed."
    exit()

import ProtoText

TEST_ADDRESS_BOOK = os.path.dirname(__file__) + '/david.prototxt'


class TestProtoText(unittest.TestCase):
    def test_text_method(self):
        with open(TEST_ADDRESS_BOOK, 'r') as f:
            adr_book_text = f.read()
        adr_book_obj = AddressBook()
        adr_book_obj.ParseFromText(adr_book_text)
        self.assertEqual(str(adr_book_obj), adr_book_obj.SerializeToText())

    def test_dict_method(self):
        person_obj = Person(id=28)
        self.assertEqual(person_obj['id'], 28)
        # test __setitem__ for naive field
        person_obj['name'] = 'Nancy'
        # test __getitem__ for naive field
        self.assertEqual(person_obj['name'], 'Nancy')
        # test __setitem__ for naive repeated field set
        person_obj['phone'] = [Person.PhoneNumber(number="1234")]
        self.assertEqual(person_obj['phone'][0]['number'], "1234")
        # test __setitem__ for dict input repeated field set
        person_obj['phone'] = [{'number': 'dict123456'}]
        self.assertEqual(person_obj['phone'][0]['number'], "dict123456")
        # test __setitem__ for mixture input repeated field set
        person_obj['phone'] = [{'number': '4567'}, Person.PhoneNumber(number="1234")]
        self.assertEqual(person_obj['phone'][0]['number'], '4567')
        self.assertEqual(person_obj['phone'][1]['number'], '1234')
        # test update function
        person_obj.update({
            'name': 'Brown',
            'id': 15
        })
        self.assertEqual(person_obj['name'], 'Brown')
        self.assertEqual(person_obj['id'], 15)
