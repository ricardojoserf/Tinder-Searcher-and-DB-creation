# Tinder-Searcher-and-DB-creation
Tinder Searcher and DB creation - Proof of concept for Tinder security team


## Usage

### Database creation

```
python tinderbase.py -m {min age} -M {max age} -d {max distance}
```

### Searching by name
```
python tindersearcher.py -n {name} -m {min age} -M {max age} -d {max distance}
```


## Examples

### Database creation
```
python tinderbase.py -m 29 -M 29 -d 3
```

### Searching by name
```
python tindersearcher.py -n "Ana" -m 25 -M 29 -d 3
```


## Requirements

```
sudo pip install pynder robobrowser regex lxml

sudo pip install --upgrade html5lib beautifulsoup4
```

Comment line 27 in /usr/local/lib/python2.7/dist-packages/pynder/models/user.py file (part of Pynder library):

```
#self.schools_id.extend([school["id"] for school in data['schools']])
```