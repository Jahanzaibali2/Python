from odoo import models, fields

class Person(models.Model):
    _name = 'my_module.person'
    _description = 'Person Information'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    city = fields.Char(string="City")

# This defines a Person model that will create a table called my_module_person with columns: 
# name, age, and city.

# Create: To create a new record, you use the create() method.

self.env['my_module.person'].create({
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
})

# Read: To read records, you use the search(), browse(), or read() methods.

persons = self.env['my_module.person'].search([('age', '>', 18)])
for person in persons:
    print(person.name, person.age)


# Update: To update a record, you use the write() method.

person = self.env['my_module.person'].search([('name', '=', 'John Doe')])
person.write({'city': 'San Francisco'})

# Delete: To delete a record, you use the unlink() method.

person = self.env['my_module.person'].search([('name', '=', 'John Doe')])
person.unlink()