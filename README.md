# TableGen

A simple generator made in python with the purpose of using JSON files as input and creating simple, random outputs.

### How to install

first, download the repository as a .zip file. Extract the contents into a folder then run the following commands to use python `pip` to install

`cd \DOWNLOAD PATH\`
`pip install .`

pip will collect and install requirements and tableGen

### Usage

tableGen has three modes (**NOTE:** all modes are under development and are subject to change.)

`gen` `create` `edit`

### Gen

to use TableGen's Generator, run

`tableGen gen TABLE...`

where `TABLE` is one or more tables you would like to generate. (**NOTE:** If the `TABLE` does not exist TableGen will ask if you would like to create the table)

EXAMPLE:
```
~ > tableGen gen npc
npc: A Young Male Human of Noble status. They are a Merchant. 
~ > tableGen gen human-name human shop
human-name: John Doe
human: 5' 6, Shaggy brown hair, simple blue pants, Extravagant Green tuxedo
shop: "of Wands and Wizzards" is a clean magic shop with various shelves aligned to face the counter. It contains wands and magical robes of various qualities.
```

OPTIONS:

| option | Name   | Description               | Default  |
| ------ | ------ | ------------------------- | -------- |
| -f     | FOLDER | Change desitnation folder | .\tables |

### Create

to use TableGen's table creator, run

`tableGen create TABLE`

where `TABLE` is the name of the table you'd like to create. (**NOTE:** this is also the name you will use to run through the generator)

TableGen will then ask you to create a scheme to use for the table. this is how tableGen will fill out information into the table.

EXAMPLE:

```
~ >tableGen create npc
npc/Scheme> A(n) {age} {race} {gender} of {socialstanding} status. They are a {porfession}
```

TableGen will use the words in `{}` as replacement text. these can also be used inside individual elements to create sub elements

TableGen will then go through each element and ask for items that it can replace.
Use a blank line to go onto the next item in the list. Any additional elements will be at the end of the list in order of creation

```
npc/age> Young
npc/age> Old
npc/age> Middle-aged
npc/age> 
npc/race> Human
npc/race> Orc
npc/race> Half-{subrace}
npc/race> 
npc/gender>
...
npc/subrace>
```

OPTIONS:

| option | Name   | Description               | Default  |
| ------ | ------ | ------------------------- | -------- |
| -f     | FOLDER | Change desitnation folder | .\tables |


### Edit

**UNDER CONSTRUCTION**