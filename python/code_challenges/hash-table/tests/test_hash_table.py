from hash_table import __version__
from hash_table.hash_table import *
import pytest

def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def create_hashtable():
    hashtable= HashTable()
    hashtable.add("TOLAY",19-2-2018)
    hashtable.add("WATEEN",5-5-2019)
    hashtable.add("MY WORLD",-1-1991)

def test_hashTble_addition():
    hashtable= HashTable()
    hashtable.add("TOLAY",30)
    assert hashtable.contains("TOLAY") == True

def test_hashed_key():
    hashtable = HashTable()
    assert hashtable.hash("TOLAY") == 299

def test_hashtable_find(create_hashtable):
    hashtable = create_hashtable
    assert hashtable.find("TOLAY") == 40
    assert hashtable.find("WATEEN") == 55

def test_hashtable_not_find(create_hashtable):
    hashtable = create_hashtable
    assert hashtable.find("eslam") == None

def test_hashtable_contains(create_hashtable):
    ht=create_hashtable
    assert ht.contains("TOLAY")
    assert ht.contains("WATEEN")

def test_hashtable_collision():
    ht=HashTable(3)
    ht.add("eslam",11)
    ht.add("tw",1991)
    assert ht.find("tw")==1991

def test_hashtable_collision2(create_hashtable):
    ht=create_hashtable
    ht.add("40",44)
    ht.add("31",55)
    assert ht.find("31")==55


